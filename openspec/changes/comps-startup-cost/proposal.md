# cut genja-completion011 startup cost

Status: To Do (backlog TASK-213)

## Why

On 2026-11-27 the config got startup profiling (`Makefile.startup.mk`: `make startup`,
`startup-cold`, `startup-jitprof-plugins N=5`, per-plugin trees). After the treesitter and Defender
fixes, genja-completion011 is the largest single item in a start:

- warm: ~74 ms of its own code, ~138 ms with what it loads (lazy profile)
- cold, Defender exclusions in place: ~114 ms own, ~361 ms total; ~480 ms in a later cold run
- before the `nvim-data` exclusion: 1.58 s cold, since every module it pulls in was scanned

It loads at VeryLazy and on `BufReadPre`/`BufNewFile`, so it runs after the first screen but before
nvim takes input. On an empty start it sets up all of LSP and Mason just so the command line has
completion. Two fixes are already in (2026-11-27): nvim-lint no longer loads it at setup for a WSL
distro lookup, and the installed servers are enabled in one `vim.lsp.enable(list)` call instead of
one per server (each call re-ran FileType on every buffer, ~15 ms).

The goal: an empty start pays only for completion, a start with a file pays for the LSP of that
file's filetype, and neither notices Mason unless something is missing.

## What the profiles showed

Measured, single runs unless noted:

- mason-lspconfig's `get_installed_package_names()` and its name map: ~17 ms warm. They run at
  setup because `ensure_installed` and the enable step need the installed list
- the mason modules themselves (`mason-core.functional`, `mason-registry`, installers): ~165 ms cold
  in total, before the Defender fix; still the largest group cold
- `require mason-lspconfig.lsp.autotools_ls`: 21 ms cold for one module, the `make` language
- blink.cmp: 40-60 ms cold; `blink.cmp.fuzzy.download.files` alone ~22 ms cold, the prebuilt matcher
  check
- `[string]:spawn` was 6% of one start's samples in plain jit.p; something starts a process during
  startup. Not yet traced to its caller

Suspected, not measured:

- `load_lang()` and `load_config()` call `nvim_get_runtime_file()` for every enabled language and
  for `local.lua`: a runtimepath scan each, about 20 per start. `pcall(require, ...)` searches the
  same path and could replace the check
- `install_tools()` and mason-lspconfig's `setup()` both call `registry.refresh()` at start; on a
  machine with everything installed that is work for nothing, and possibly the `spawn`
- the ~114 ms (cold) of genja-completion011's own code is not yet split by line; the `self` column
  of `make startup-jitprof-plugins` now does that

## The idea

Split the plugin's start into what the first keypress needs and what the first file needs.

1. Completion first, LSP later. blink.cmp and the command line sources load at VeryLazy (or
   `CmdlineEnter`, `InsertEnter`); servers, Mason and mason-lspconfig load on the first `FileType`
   that has an enabled server. An empty start then sets up no LSP at all.
2. Mason only when needed. Read the installed servers once from `mason/packages/` (a directory
   listing) and enable them; call `registry.refresh()`, `ensure_installed` and `install_tools()`
   only when a wanted package is missing, and then after a delay (`vim.defer_fn`), so installs never
   compete with the first screen. `:Mason`, `:MasonInstall` and `:checkhealth` still load the full
   thing.
3. Per-language work on demand. Language modules are loaded when collecting servers; anything heavier
   in them (WSL lookups, project detection) moves into `root_dir`, `before_init` or the server's
   first attach. The mason-lspconfig overrides (`mason-lspconfig.lsp.<name>`) are required only for
   the servers being enabled, on their filetype.
4. Fewer runtimepath scans. Replace `nvim_get_runtime_file()` checks before `require` with the
   `require` itself, keeping the warning for a missing language file.
5. Find the `spawn`. Trace it with `make startup-jitprof-full` (it shows nvim's own frames) and move
   it out of startup or drop it.

Each step is measured before and after with `make startup-jitprof-plugins N=5` (median, self
column) and `make startup-cold`, and noted in the task.

## Impact

- genja-completion011: `comps/init.lua` (order and triggers), `lsp/init.lua` (installed list,
  refresh and installs deferred, overrides per server), `lang/*.lua` where a module does work at
  load, CLAUDE.md
- config: `lua/lazyp/new/genja-completion011.lua` triggers (VeryLazy for completion, FileType for
  LSP), maybe split into two specs
- tests: the config's `tests/comps011` groups `lsp`, `ready`, `mason` and `cmp` must pass as before;
  `ready` covers the first-file attach, which the split moves
- risk: a server must still attach to the first file opened from the command line
  (`nvim foo.php`); FileType for that buffer can fire before the LSP part is set up, so setup has to
  enable for the buffers already open (as `vim.lsp.enable()` does after `vim_did_enter`)
