---
id: TASK-100
title: 'blink.cmp, cmdline and abbreviation completion'
status: Done
assignee: []
created_date: '2026-10-24'
labels:
  - nvim-config
  - completion
  - from-config
dependencies: []
ordinal: 100000
---

## Description

Finished work on completion, 2026-10-24 .. 2026-11-06: Solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-21 - guide-tilde-dial.md`: `~` toggles and dial.nvim (idea 29a)
  - `backlog/docs/doc-26 - guide-comps011-tests.md`: comps011 integration tests: LSP, cmp, linters; groups and slowness
  - `backlog/docs/doc-44 - guide-blink-manual-test.md`: blink.cmp: manual test guide

## Acceptance Criteria

- [x] #1 cmdline: `<C-j>`/`<C-k>` pick menu items, `<Up>`/`<Down>` always recall history (2026-10-24; `solved-26.10.24-06.42-cmdline-keys.md`)
- [x] #2 comps011: integration tests for LSP, cmp and linters (2026-10-25; `solved-26.10.25-00.07-comps011-tests.md`)
- [x] #3 comp011: bashls gave no shellcheck diagnostics on Windows (2026-10-26; `solved-26.10.26-22.30-bashls-shellcheck.md`)
- [x] #4 comp011: detect servers and mason tools that silently never start (2026-10-26; `solved-26.10.26-22.30-lsp-health.md`)
- [x] #5 comp011: lua_ls needs 5-7 s to index its libraries before it completes; tests dont need them (2026-10-26; `solved-26.10.26-22.30-lua-no-lib.md`)
- [x] #6 completion: menu colours from StatusLine, no selection bar (2026-10-28; `solved-26.10.28-23.12-blink-colours.md`)
- [x] #7 completion: `<Down>`/`<Up>` walk the cmdline menu, history without one (2026-10-28; `solved-26.10.28-23.12-cmdline-updown.md`)
- [x] #8 comps011: spec turns on php, python, gitconfig, sshconfig (2026-10-28; `solved-26.10.28-23.12-comps-spec.md`)
- [x] #9 abbrev: g alone quits through :Unsaved; :g/pat/, :g! and :let g:x work again (2026-10-30; `solved-26.10.30-01.56-g-quit.md`)
- [x] #10 completion: cmdline `<Up>`/`<Down>` are history as in plain Vim; no preselect (2026-10-31; `solved-26.10.31-06.53-cmdline-history.md`)
- [x] #11 completion: minuet answers only `<M-y>`, not every manual trigger (2026-10-31; `solved-26.10.31-06.53-minuet-manual.md`)
- [x] #12 completion: cmdline menu walks on `<M-j>`/`<M-k>`, not `<C-j>`/`<C-k>` (2026-10-31; `solved-26.10.31-10.23-cmdline-meta-keys.md`)
- [x] #13 completion: more cmdline menu keys (2026-10-31; `solved-26.10.31-12.14-cmdline-more-keys.md`)
- [x] #14 completion: cmdline menu stays shut on one-char commands (2026-10-31; `solved-26.10.31-12.14-cmdline-one-char.md`)
- [x] #15 completion: "appearance.lua:57: Buffer is not modifiable" on blinks doc window (2026-10-31; `solved-26.10.31-13.30-doc-padding-fix.md`)
- [x] #16 completion: explain the doc windows winblend and border (2026-10-31; `solved-26.10.31-14.42-blink-doc-border.md`)
- [x] #17 completion: doc window comment and docs for the shadow border (2026-10-31; `solved-26.10.31-14.45-doc-shadow-comment.md`)
- [x] #18 completion: `!` and `:terminal` names come from a disk cache (2026-11-02; `solved-26.11.02-18.49-completion-shell-cache.md`)
- [x] #19 tilde: `~` cycles markdown checkbox states (2026-11-03; `solved-26.11.03-14.02-tilde-checkbox.md`)
- [x] #20 abbrev: weekday with the date (2026-11-06; `solved-26.11.06-15.13-abbrev-ymdd.md`)
- [x] #21 disable old completion setup (undated; `2026-disable-old-completion.md`)
- [x] #22 cmp: delay popup by 500 ms if it starts with :w (undated; `ideas-10-cmp-write-popup.md`)
- [x] #23 comps011 (undated; `ideas-47-comps011-tests.md`)
- [x] #24 comps011 (undated; `tested-2026-10-31.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [x] test: `:e <Tab>`, then `<C-j>`/`<C-k>` move in the menu; `<Up>` closes it and shows the previous command (`solved-26.10.24-06.42-cmdline-keys.md`)
- [x] reinstall lua-language-server (half-installed, mason/staging left) and autotools-language-server (gone Python) (`solved-26.10.25-00.07-comps011-tests.md`)
- [x] bashls and gopls: attach without diagnostics; check `go` on PATH (`solved-26.10.25-00.07-comps011-tests.md`)
- [x] test: `make test D=comps011 G=gather`, then `make timings` (`solved-26.10.25-00.07-comps011-tests.md`)
- [x] test: open a .sh with `if [ -n $1 ]`: shellcheck warnings show (`solved-26.10.26-22.30-bashls-shellcheck.md`)
- [x] `:MasonInstall --force css-lsp eslint-lsp html-lsp json-lsp` to drop the full-path launchers (warnings) (`solved-26.10.26-22.30-lsp-health.md`)
- [x] test: `pwsh -File tests/manual/measure-lua-ls.ps1 -Runs 3` and `-NoLib`: compare ready times (`solved-26.10.26-22.30-lua-no-lib.md`)
- [x] test: `make test D=comps011 G=lua_ls V=1`: ready/cmp pass well under 10 s (`solved-26.10.26-22.30-lua-no-lib.md`)
- [x] lower the lua_ls ready/cmp timeouts once the -NoLib numbers are known (`solved-26.10.26-22.30-lua-no-lib.md`)
- [x] test: menu in two colorschemes, :colorscheme switch keeps it (`solved-26.10.28-23.12-blink-colours.md`)
- [x] test: :e`<Up>` with the menu closed recalls filtered history (`solved-26.10.28-23.12-cmdline-updown.md`)
- [x] spec is indented with spaces; config uses tabs (`solved-26.10.28-23.12-comps-spec.md`)
- [x] test: :term`<Tab>` gives :terminal; :ec`<Up>` recalls history with the menu open; `<C-j>` then `<Down>` walks the menu (`solved-26.10.31-06.53-cmdline-history.md`)
- [x] test: `make test D=completion` in tests/ (`solved-26.10.31-06.53-cmdline-history.md`)
- [x] lua_ls warns inject-field on config.cmdline and blink.cmp.CmdlineConfigPartial undefined (no blink library in this workspace) (`solved-26.10.31-06.53-cmdline-history.md`)
- [x] test: `<Tab>` in insert mode shows no minuet items; `<M-y>` does (needs ollama serve) (`solved-26.10.31-06.53-minuet-manual.md`)
- [x] test: :Minuet blink toggle, then minuet items appear while typing (`solved-26.10.31-06.53-minuet-manual.md`)
- [x] test: the doc window of an item with documentation opens framed, padded, without the error (`solved-26.10.31-13.30-doc-padding-fix.md`)
- [x] BlinkCmpDocBorder and the FloatBorder mapping are unused with shadow: drop or keep for 'rounded' (`solved-26.10.31-14.45-doc-shadow-comment.md`)
- [x] test: `:ResetPathCache` twice: deletes, then "no path cache to delete" (`solved-26.11.02-18.49-completion-shell-cache.md`)
- [x] test: the list rebuilds after 3 h (age check, not covered by a test) (`solved-26.11.02-18.49-completion-shell-cache.md`)
- [x] test: first `!n` after a rebuild shows the menu (`solved-26.11.02-18.49-completion-shell-cache.md`)
- [x] test: `~` five times on a `- [ ] item` line, cursor on the text (`solved-26.11.03-14.02-tilde-checkbox.md`)
- [x] `~` on the `-` list marker turns it into `+`; skip that swap on checkbox lines? (`solved-26.11.03-14.02-tilde-checkbox.md`)
- [x] test: type ymdd! in insert mode (`solved-26.11.06-15.13-abbrev-ymdd.md`)
