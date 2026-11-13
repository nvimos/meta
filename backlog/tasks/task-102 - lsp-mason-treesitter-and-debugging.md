---
id: TASK-102
title: 'lsp, mason, treesitter and debugging'
status: Needs Test
assignee: []
created_date: '2026-10-25'
labels:
  - nvim-config
  - languages
  - from-config
dependencies: []
ordinal: 102000
---

## Description

Finished work on languages, 2026-10-25 .. 2026-11-06: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-52 - guide-behat.md`: Behat runner (2026-11-05)
  - `backlog/docs/doc-53 - guide-c-navigate.md`: C projects without a build (2026-11-05)
  - `backlog/docs/doc-54 - guide-css-html-lsp.md`: CSS and HTML language servers (2026-11-05)
  - `backlog/docs/doc-55 - guide-drupal.md`: Drupal projects (2026-11-05)
  - `backlog/docs/doc-58 - guide-neotest-golang.md`: Go tests through neotest (2026-11-05)
  - `backlog/docs/doc-59 - guide-parsers-web-go.md`: Treesitter parsers for PHP-project web files and Go (2026-11-05)
  - `backlog/docs/doc-62 - guide-go-parsers.md`: Go: treesitter parsers templ and proto (2026-11-10)
  - `backlog/docs/doc-63 - guide-js-tests.md`: JS/TS tests in neotest: vitest or jest (2026-11-10)
  - `backlog/docs/doc-66 - guide-typescript.md`: TypeScript projects out of the box (2026-11-10)

## Acceptance Criteria

- [x] #1 mason: `make mason-luals` reinstalls lua-language-server headless (2026-10-25; `solved-26.10.25-07.40-mason-luals.md`)
- [x] #2 mason: make target to reinstall autotools_ls after Python moved (2026-10-26; `solved-26.10.26-23.48-mason-make.md`)
- [x] #3 lsp: rename typed in a float over the word instead of the cmdline prompt (2026-10-28; `solved-26.10.28-22.34-rename-inline.md`)
- [x] #4 lsp: powershell_es asked the rename disclaimer every session (2026-10-28; `solved-26.10.28-22.42-pses-rename.md`)
- [x] #5 lsp: :EnableLang turns a language on or off for the session (2026-10-28; `solved-26.10.28-23.12-enable-lang.md`)
- [x] #6 lsp: :CheckHealthLspSimple renamed to :CheckHealthSimpleLsp (2026-10-31; `solved-26.10.31-10.23-lsp-check-rename.md`)
- [x] #7 ecolog: "Spawning process with cmd: { "ecolog-lsp" } failed" on .sh files (2026-10-31; `solved-26.10.31-12.14-ecolog-cond.md`)
- [x] #8 Makefile.lazy.mk: `update` / `sync` run `update-treesitter` again (2026-11-03; `solved-26.11.03-14.02-make-treesitter.md`)
- [x] #9 mason: lua-language-server cut off by its own running server (2026-11-03; `solved-26.11.03-14.02-mason-receipt.md`)
- [x] #10 plug in a new language (e.g. Flutter/Dart later) without shipping every language (2026-11-05; `ideas-60-add-a-language.md`)
- [x] #11 dap-view: lighter debug UI next to dap-ui (2026-11-05; `solved-26.11.05-20.22-dap-view.md`)
- [x] #12 textobjects: function body / whole function objects, next and last (2026-11-06; `solved-26.11.06-15.10-textobjects.md`)
- [x] #13 treesitter: incremental selection from vermadens config (2026-11-06; `solved-26.11.06-15.10-ts-node-select.md`)
- [x] #14 migrate treesitter config (undated; `2026-migrate-treesitter.md`)
- [x] #15 lsp binds: close hover window with <esc> (undated; `ideas-04-lsp-hover-esc.md`)
- [x] #16 lsp binds: scroll in hover window / buffer (undated; `ideas-05-lsp-hover-scroll.md`)
- [x] #17 treesitter: add a gui-trigger key that lists further actions (maybe g.) (undated; `ideas-17-action-menu.md`)
- [x] #18 Go: gopls local import groups from go.work/go.mod, code lenses, <leader>cl runs the lens (e3c61d5, 4a917a0) (undated; `ideas-21-go-gopls.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: `make mason-luals`, then `make mason` (`solved-26.10.25-07.40-mason-luals.md`)
- [ ] test: grn on a variable, type a name, <CR>; rename applied (`solved-26.10.28-22.34-rename-inline.md`)
- [ ] test: menu open, <C-j> inserts the item and the float stays; <CR> then renames (`solved-26.10.28-22.34-rename-inline.md`)
- [ ] test: <Esc> <Esc> leaves the name unchanged (`solved-26.10.28-22.34-rename-inline.md`)
- [ ] powershell_es: settings.powershell.renameSymbol.acceptRenameDisclaimer = true in genja-completion011 lang/powershell.lua (setting name unverified) (`solved-26.10.28-22.34-rename-inline.md`)
- [ ] test: restart nvim, grn on a variable in a .ps1 file; no disclaimer prompt, rename applied (`solved-26.10.28-22.42-pses-rename.md`)
- [ ] test: :EnableLang python in a .py buffer attaches pyright; -off stops it (`solved-26.10.28-23.12-enable-lang.md`)
- [ ] test: :EnableLang -save typescript writes lua/genja/lsp/local.lua, comments kept (`solved-26.10.28-23.12-enable-lang.md`)
- [ ] test: <F2> in a buffer of an off language lists the item (`solved-26.10.28-23.12-enable-lang.md`)
- [ ] test: `make -n -f Makefile.lazy.mk sync` lists two nvim lines (`solved-26.11.03-14.02-make-treesitter.md`)
- [ ] test: `make test D=comps011 G=receipts` (`solved-26.11.03-14.02-mason-receipt.md`)
- [ ] test: `make mason-luals` with nvim open on a lua file (`solved-26.11.03-14.02-mason-receipt.md`)
- [ ] test: <leader>dv opens right of the code, not below (`solved-26.11.05-20.22-dap-view.md`)
