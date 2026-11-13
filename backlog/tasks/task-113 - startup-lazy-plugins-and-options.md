---
id: TASK-113
title: 'startup, lazy, plugins and options'
status: Needs Test
assignee: []
created_date: '2026-10-24'
labels:
  - nvim-config
  - config
  - from-config
dependencies: []
ordinal: 113000
---

## Description

Finished work on config, 2026-10-24 .. 2026-11-09: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

## Acceptance Criteria

- [x] #1 make: gitea targets moved to the setup-2026-cut project (2026-10-24; `solved-26.10.24-06.42-gitea-to-setup.md`)
- [x] #2 fu: `:ToggleDiagnostics` for the current buffer (2026-10-25; `solved-26.10.25-07.40-toggle-diagnostics.md`)
- [x] #3 init: enable ui2 only on new enough nvim (2026-10-25; `solved-26.10.25-12.41-ui2-guard.md`)
- [x] #4 init.vim: guifont JetBrainsMono NFM 12 (2026-10-26; `solved-26.10.26-23.48-guifont.md`)
- [x] #5 opt: listchars variants commented, eol marker off (2026-10-26; `solved-26.10.26-23.48-listchars.md`)
- [x] #6 autoresource: reload ext/ modules, skip the alma vimrc (2026-10-28; `solved-26.10.28-23.12-autoresource-ext.md`)
- [x] #7 plugins: ccc.nvim colour picker and highlighter (2026-10-29; `solved-26.10.29-20.56-ccc-colour-picker.md`)
- [x] #8 plugins: legendary.nvim from the 0king fork, in mylunsj (2026-10-29; `solved-26.10.29-22.26-legendary.md`)
- [x] #9 secrets: API keys in a gitignored local file (2026-10-31; `solved-26.10.31-10.23-local-secrets.md`)
- [x] #10 ext: reload a Lua module without restarting nvim (2026-11-08; `solved-26.11.08-20.58-reload-lua.md`)
- [x] #11 ext: user command modules grouped in a subfolder (2026-11-08; `solved-26.11.08-20.58-user-command-dir.md`)
- [x] #12 ext: reload every genja module without restarting nvim (2026-11-09; `solved-26.11.09-23.43-reload-genja.md`)
- [x] #13 branch out as nvim09-2023 (undated; `2026-branch-nvim09-2023.md`)
- [x] #14 F1:       Live Grep (ripgrep) (undated; `2026-check-features.md`)
- [x] #15 describe file names and their purpose in lua/genja (undated; `2026-describe-lua-genja-files.md`)
- [x] #16 find backup on usb or external drive (undated; `2026-find-backup.md`)
- [x] #17 freeze 2023 branch, push (undated; `2026-freeze-2023-branch.md`)
- [x] #18 import solid vimscript config (undated; `2026-import-vimscript-config.md`)
- [x] #19 refactor lazy nvim setup (undated; `2026-refactor-lazy-setup.md`)
- [x] #20 figure out the runtimepath issue (undated; `2026-runtimepath-issue.md`)
- [x] #21 quickfix list close with x (undated; `ideas-02-quickfix-close-x.md`)
- [x] #22 nvim: remove charity nag. keep plain startup message (undated; `ideas-03-remove-charity-nag.md`)
- [x] #23 genja-splitpad.nvim: padding column next to the separator in unfocused splits (4956074, 0bb1d95); spec disabled in lua/lazyp/no/ (6fdd7e3) (undated; `ideas-24-genja-splitpad.md`)
- [x] #24 almavimrc. clone in lua the behaviors (undated; `ideas-29-alma-behaviours.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: `<F2>` make targets in nvim lists the main and `lazy: …` targets only; `make` in setup-2026-cut has the gitea targets (`solved-26.10.24-06.42-gitea-to-setup.md`)
- [ ] test: `:ToggleDiagnostics` twice in a lua file with warnings (`solved-26.10.25-07.40-toggle-diagnostics.md`)
- [ ] the comment says 0.12, the check 0.13; `else if` must be `elseif` before uncommenting (`solved-26.10.25-12.41-ui2-guard.md`)
- [ ] test: start nvim 0.11 / 0.12: no require error (`solved-26.10.25-12.41-ui2-guard.md`)
- [ ] the commented listchars lines are indented with spaces; the repo uses tabs (`solved-26.10.26-23.48-listchars.md`)
- [ ] test: :w on lua/genja/ext/tilde.lua reloads it; :w on the alma vimrc does not (`solved-26.10.28-23.12-autoresource-ext.md`)
- [ ] test: <leader>ic on a hex colour edits it, elsewhere inserts; <leader>tc in a markdown file (`solved-26.10.29-20.56-ccc-colour-picker.md`)
- [ ] test: `:ReloadLua genja-statusline.winbar` completes with Tab and redraws the winbar (`solved-26.11.08-20.58-reload-lua.md`)
- [ ] test: restart nvim, `:WrapFold`, visual `zf`, `<leader>wwf` and `:SortLen` still work (`solved-26.11.08-20.58-user-command-dir.md`)
- [ ] open: `doc-wip/squash-ideas-oct-17.details.md` still names the old wrapfold path (history record, left alone) (`solved-26.11.08-20.58-user-command-dir.md`)
- [ ] test: `:ReloadLuaGenja` prints `reloaded N modules in M ms`, the cwd stays (`solved-26.11.09-23.43-reload-genja.md`)
- [ ] test: a module with a syntax error is reported and the old one stays loaded (`solved-26.11.09-23.43-reload-genja.md`)
