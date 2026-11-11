---
id: TASK-3
title: 'extras outside the idea list, Oct-Nov 2026'
status: Done
assignee: []
created_date: '2026-11-05'
labels:
  - nvim-config
  - todo-ideas
  - ideas-november
dependencies: []
ordinal: 3000
---

## Description

Batches of work done beside the idea list, one per day; the original notes are in
`legacy/todo-ideas.md`, section "ideas october".

## Acceptance Criteria

- [x] 2026-11-05: batch (was TASK-3)
    - [x] oil: ]c [c jump to changed entries, ggC commits the entry (f5ce192); ~ checkbox cycle x . ~ n (0862b18)
    - [x] plug-wip plugins are their own repos (tox2ik/<name>); specs load the local checkout, else clone it (2492965, 43c806f, 90814fb)
    - [x] tests/startup: a clean clone starts cleanly, startup below 1 s (f1951ca)
    - [x] lint: checkmake off, its config and parser kept (fdbf5e3)
    - [x] docs: readme.add-a-language.md checklist (7b69862); guide for C without a build (cbb8df5)
    - [x] aerial: test that the sidebar follows :edit (ed46209)
- [x] 2026-11-06: visual `<C-s>`/`<BS>` grow and shrink by node (3bed5be); tested (was TASK-4)
    - [x] textobjects: mini.ai with treesitter f c o, next/last on aN iN / aL iL (09eb281);
    - [x] abbrev: ymdd! weekday and date (c6143cd); tested
    - [x] tests: cmdline shellcmd menu opens on a typed char (53d9252); which-key buffer-local groups (aa538e9)
- [x] 2026-11-07: visual `<leader>pC` pastes from a buffer without a file (plugin ea2d156); tested (was TASK-5)
    - [x] claudefterm: session markers removed, /rename still names the terminal (54ffee2; plugin ff46a75);
- [x] 2026-10-23: builtins under `<leader>jb` (6aa5a7b); which-key groups `<leader>j`. and `<leader>j`/ (73c4c3b) (was TASK-6)
    - [x] winbar: quickfix windows show w:quickfix_title, no duplicate %q (6f29b37)
    - [x] map-telescope: helpers in fn.lua; `<leader>jj1`/jj2 quickfix/loclist, genja grep/find on jjJ/jjj,
    - [x] focus.nvim: vim.g.focus_disable, so `<C-w>`= sticks; `<leader>tPf` can turn it on (28c80c0)
    - [x] every vim.notify names its file through a SRC prefix (2aadf61)
    - [x] mylunsj lists Telescope mydirs first (1151dfb)
    - [x] cmdline completion: `<Tab>`/`<S-Tab>` next/previous, `<Up>`/`<Down>` pick while the menu is open (b5173ad)
- [x] 2026-10-24: one shared state per Gui* function; neovim-gui-shim on again; tested (3580a06, ad94a79); :Mydirs reset deletes the usage file; tested (1132d6b) (was TASK-7)
    - [x] cmdline: `<C-j>`/`<C-k>` pick items, `<Up>`/`<Down>` back to history (0de4d52)
    - [x] map-lsp: descs for nvim 0.11 gr* defaults, references on gR, [d ]d go the way their descs say (5e788aa)
    - [x] markdown: `<F2>` glow preview in a new pwsh window, Windows only (21cfe96)
    - [x] intro: eob ~ drawn in column 0 like vanilla (81a4659)
    - [x] gui: nvim-qt toggles on `<leader>mQ`…, GuiFuncs picker (`<F3>`, `<F2>` gui), right-click frameless,
    - [x] edit: visual `<leader>w`, wraps lines as "line",; title case on `<leader>wsT`, sort paragraph `<leader>wsp` (8f25155)
    - [x] f2 git: `<M-a>` git adds the file, picker stays open (e6c04ac)
    - [x] hilite: darker Search/IncSearch/CurSearch background (a1b0857)
    - [x] startdirs: `<M-1>`…`<M-4>` jump by rank and don't count a use; :Mydirs picker,
- [x] 2026-10-25: comps011 lsp/cmp/lint with groups and timings (9f5f014); tests/Makefile runs every dir (was TASK-8)
    - [x] telescope keymaps: `<M-r>` after `<M-f>`/`<M-x>` cycles the groups of the refined list; tested (2debb3b)
    - [x] tests: map-plugin miss log and health (af13aed), claudefterm per project (63800da),
    - [x] aerial: nav float 5% see-through (cbe6c13)
    - [x] gitsigns: `<leader>mGs` attaches skipped buffers again (e9e50f7)
    - [x] f2: groups of at most 6 chars, main list `group  label` in one column (5edddfa)
    - [x] floaterm: :PwshFterm (50e4b8a)
    - [x] mason: make mason-luals reinstalls lua-language-server headless (19d67f5)
    - [x] :ToggleDiagnostics for the current buffer (38e3d2d)
    - [x] f2 diag: hide excess undoes show all (620545d); pickers: matched chars in Visual fg, bold (00b05e5)
    - [x] genja-finder: `<M-Up>` rescans in the parent dir (93a8b69); `<C-]>` opens the entry, a dir entry itself (7bc4759, 31b74cd)
    - [x] statusline: [Nameless] for unnamed buffers (eddb6e5); telescope key footer dropped, key help kept (5c6e9a7)
    - [x] md: substitutions wrap vim key notation in backticks (c4d6b26)
    - [x] commit popup also on `<leader>gcm` and `<leader>C` (39dab59); `<leader>ei` tab-local from stdpath (7b05312)
    - [x] nvim-qt: nvim-qt.qss stylesheet, dark title bar note in ginit.vim (41e5bb6)
- [x] 2026-10-26: and `<C-/>` descs (2f85171), claudefterm marker toggle and !! markers (a5ae869), f2 git staged picker (5e81cdf) (was TASK-9)
    - [x] tests: pwsh Makefile, per-name groups, timings for every case, make gather/failed/plan/slow/status (8d2d86c)
    - [x] lua_ls: GENJA_LUA_NO_LIB=1 skips libraries, set by tests/Makefile (53642d0)
    - [x] :checkhealth genja.lsp: servers not installed, broken Python venvs, mason launchers (96b7910)
    - [x] bashls: mason's shellcheck.exe path on Windows (0bdc719); claudefterm kill() crash (0b46cfa)
    - [x] auto-todo round: shared checkmake.ini (9152813), `<M-CR>`/`<C-s>` submit popups (776f78a), telescope default keys
    - [x] statusline: plain separators in terminals, icons in GUI (487aec2); :Ct for :ClaudeFterm (9073fcb)
    - [x] guifont JetBrainsMono NFM 12 (ac41882); make mason-make reinstalls autotools_ls (170ba57)
- [x] 2026-10-27: tests/completion: sources, keys, cmdline, `<CR>` (191c6cf, 55c1296) (was TASK-10)
    - [x] blink.cmp replaces nvim-cmp, own sources on one source builder, blade-nav source (2d6b4bd, 00268c4);
    - [x] genja-util: shared centred float and text helpers; plug-wip plugins tidied (b34a1a8, f16695b)
    - [x] gen.nvim: ollama qwen3.5:0.8b prompt menu on `<leader>ai` (2bd7b6f)
- [x] 2026-10-28: batch (was TASK-11)
    - [x] LSP rename typed in a float over the word: grn, `<leader>c2`, right-click (527755d)
    - [x] :EnableLang turns a language on/off for the session, -save writes lsp/local.lua, `<F2>` offers it (03ce43e)
    - [x] completion menu colours from StatusLine (e45657e); cmdline `<Down>`/`<Up>` walk the menu, history without one (dbd3c64)
    - [x] terminal windows: scrolloff 0 (db72fa3); :help you page (b7337e9); `<leader>ts` toggles spelling (fda9e2e)
    - [x] colorscheme set in init.vim, Gui* settings grouped (6adb2ed); markdownlint MD012 off (ce73378)
- [x] 2026-10-29: :Google / :Perplexity / :Xty, `<F2>` lookup, web and ai providers (80b9277, 5e70490, f9854f3); dim underline on markdown links (42d9f18) (was TASK-12)
    - [x] ccc.nvim colour picker and highlighter: `<leader>ic`, `<leader>tc` (e26d31e)
    - [x] paste search: right-click on a selection (cbeef81); genja-paste-ai.nvim: :PasteSearch, :Wot,
    - [x] terminal keys, `` <C-`> `` floaterm toggle, sessions keep shells (f4675f6)
    - [x] md-fix: expand tabs, backtick vim keys, `<leader>tm` (420d58c; Lua port 893ff63); formatlistpat for checkboxes, footnotes (d69e644)
    - [x] diag-align: virtual text in one column per paragraph (5b579f9); diagnostic colours per severity (d778534);
    - [x] legendary: 0king fork, `<leader>jl`, in mylunsj (14a73da), bigger dropdown (b366920)
    - [x] :ClaudeFterm -ax passes --ax-screen-reader (0db2b57)
    - [x] which-key: helix preset, left-centred, fixed height (da8581b, 5eb0576, a143fca); test groups vs mappings (f7a9970)
    - [x] unsaved buffers picker before :qa, jj, s: (58316bd)
- [x] 2026-10-30: batch (was TASK-13)
    - [x] unsaved picker: layout, E13 overwrite prompt, :q and :x, tests (4ccf5bc)
    - [x] telescope: per-picker prompt hint via b:telescope_hint (bb164fe); :Messages -yank copies :messages (1270b29)
    - [x] abbrev: g quits via a `<CR>` map, :g/pat/ stays :global (a3e07a3)
- [x] 2026-10-31: wrapper saved in sessions (140ed09); `<S-Insert>` sends `<C-v>` to pwsh terminals (df0a668); `<M-j>`/`<M-k>` walk the menu (aa7cdc5); `<M-f>` previous, `<M-w>` first, `<M-s>` 3 down (9693171);; no men (was TASK-14)
    - [x] netrw.nvim icons (c30c591); ghost text: minuet-ai.nvim and llm.nvim on ollama (d7d084f); both in todo-done/
    - [x] terminal: bare :terminal opens pwsh on Windows, bash on Linux (80c8fa1); idle shells under a 'shell'
    - [x] cmdline: `<Up>`/`<Down>` history until a menu walk, no preselect (fc6cd99); `<C-BS>` deletes a word (8351d8f);
    - [x] minuet: answers only `<M-y>` unless blink auto-complete is on (6dead7f); qwen2.5-coder, all providers,
    - [x] :HiInspect shows highlight groups under the cursor (17dceca); :CheckHealthLspSimple renamed
    - [x] completion doc window: menu colours, rounded frame, padding (29e8c26, 08a6f5c, 7390836)
    - [x] lint: runs cancelled by nvim-lint no longer reported as exit code 1 (cd4a0ab)
    - [x] tests: gopls go-list warmup (a3f049a), make timings slowest last (cd57bdf), mason linters installed (ef9867a),
    - [x] ecolog: ecolog2 with ecolog-lsp, else ecolog.nvim v1 (d7842a2, ca842c0)
    - [x] copilot.vim and llm.nvim shelved, keys commented out (18ed193, 1185287)
    - [x] oil: :Lexplore works again (e7b8ece); telescope key help in insert mode without n maps (48936c2)
    - [x] markdown: gq wraps checkbox items under the text (58538ea); md-fix follows editorconfig sections (aeab075)
    - [x] diag-align toggle on `<leader>tta` and in `<F2>` (27648c7); right-click paste search with a picked provider (fa42e84);
- [x] 2026-11-02: batch (was TASK-15)
    - [x] lint: `<leader>cx` turns the markdownlint/vale rule under the cursor off (01f7cda)
    - [x] tests: copilot case skips without copilot.vim in lazy (9244bc1)
- [x] 2026-11-03: batch (was TASK-16)
    - [x] :Ct starts claude in the current window (3911a0b)
    - [x] ~ cycles markdown checkbox states blank x n . ~ (c773959); ]j [j / ]y [y jump to open checkboxes (70a20a1)
    - [x] tests: yellow NOTE lines, shorter case path (9bebc59)
    - [x] Makefile.lazy.mk: update-treesitter a prerequisite of update/sync again (3480b0d)
    - [x] mason: cut-off installs repair themselves on open, make kills lua_ls first, lua_ls logs to stdpath('log') (eef2590)
    - [x] hilite: muted diagnostic underline and virtual text (65812bb); `<leader>`' opens oldfiles (5c637f8)
