---
id: TASK-101
title: 'lint and diagnostics: finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-25'
labels:
  - nvim-config
  - lint
  - from-config
dependencies: []
ordinal: 101000
---

## Description

Finished work on lint and diagnostics, 2026-10-25 .. 2026-11-07: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-13 - guide-lint-first-wave.md`: nvim-lint first wave (#14e)
  - `backlog/docs/doc-27 - guide-diag-limit.md`: Diagnostics: first 3 per severity
  - `backlog/docs/doc-30 - guide-lint-second-wave.md`: nvim-lint second wave (idea 14e)
  - `backlog/docs/doc-31 - guide-lint-vale-gitleaks.md`: nvim-lint: gitleaks and vale (idea 14e, third wave)
  - `backlog/docs/doc-38 - guide-checkmake-config.md`: checkmake: no warnings about missing all / clean / test targets
  - `backlog/docs/doc-57 - guide-lint-go-js-css.md`: golangci-lint, eslint, stylelint (2026-11-05)

## Acceptance Criteria

- [x] #1 lint: checkmake never reported on Windows (2026-10-25; `solved-26.10.25-00.07-checkmake-windows.md`)
- [x] #2 diagnostics: only the first 3 per severity are drawn (2026-10-25; `solved-26.10.25-00.07-diag-limit.md`)
- [x] #3 lint: gitleaks and vale (14e still later) (2026-10-25; `solved-26.10.25-00.07-lint-vale-gitleaks.md`)
- [x] #4 lint: vint crashes on Windows; editorconfig test needed indent_style (2026-10-25; `solved-26.10.25-00.07-lint-vint-off.md`)
- [x] #5 lint: "Linter command `cmd.exe` exited with code: 1" doesnt name the linter (2026-10-25; `solved-26.10.25-07.26-lint-linter-name.md`)
- [x] #6 lint: selene allows one-line `if` (2026-10-25; `solved-26.10.25-12.41-selene-one-line-if.md`)
- [x] #7 lint: markdownlint allows several blank lines in a row (2026-10-28; `solved-26.10.28-23.12-markdownlint-md012.md`)
- [x] #8 diagnostics: virtual text in one column per paragraph (2026-10-29; `solved-26.10.29-20.56-diag-align.md`)
- [x] #9 lint: "linter gitleaks exited with code: 1" at startup (2026-10-31; `solved-26.10.31-12.14-lint-relint.md`)
- [x] #10 diagnostics: switch the one-column alignment (2026-10-31; `solved-26.10.31-20.02-diag-align.md`)
- [x] #11 lint: vale and gitleaks checked by hand (2026-10-31; `solved-26.10.31-20.02-lint-notes.md`)
- [x] #12 lint: checkmake off by choice, first-wave linters checked (2026-11-05; `solved-26.11.05-20.22-checkmake-off.md`)
- [x] #13 diag: toggle all diagnostics next to the 3-per-severity limit (2026-11-06; `solved-26.11.06-15.13-diag-toggle.md`)
- [x] #14 diag: limit of 3 per severity is on at startup again (2026-11-07; `solved-26.11.07-02.10-diag-limit-startup.md`)
- [x] #15 nvim-lint: further linters (not covered by an LSP) (undated; `ideas-14e-nvim-lint-linters.md`)
- [x] #16 diagnostics (undated; `ideas-43-diagnostics-limit.md`)
- [x] #17 linter for makefile: disable "required" target all and clean (undated; `ideas-49-makefile-lint.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] report upstream (mfussenegger/nvim-lint; no issue found) (`solved-26.10.25-00.07-checkmake-windows.md`)
- [ ] test: `<F2>` show all, `<F2>` hide excess: back to 3 (`solved-26.10.25-00.07-diag-limit.md`)
- [ ] test: `:MasonToolsInstall`, `:ValeSync`, then the guide's samples (`solved-26.10.25-00.07-lint-vale-gitleaks.md`)
- [ ] revisit vint on Linux/WSL or a fork for heavy vimscript editing (`solved-26.10.25-00.07-lint-vint-off.md`)
- [ ] test: restart nvim, open the buffer that gave the warning, check `:messages` names the linter (`solved-26.10.25-07.26-lint-linter-name.md`)
- [ ] find which file makes the named linter fail and fix it (`solved-26.10.25-07.26-lint-linter-name.md`)
- [ ] report upstream (mfussenegger/nvim-lint): exit-code warning should use `linter.name` (`solved-26.10.25-07.26-lint-linter-name.md`)
- [ ] test: lint `lua/genja/init.lua`: no multiple_statements warning (`solved-26.10.25-12.41-selene-one-line-if.md`)
- [ ] test: a paragraph with several diagnostics shows them in one column; vim.g.diag_align = false (`solved-26.10.29-20.56-diag-align.md`)
- [ ] :MasonUninstall checkmake (still installed) (`solved-26.11.05-20.22-checkmake-off.md`)
- [ ] test: <leader>ttt in a file with diagnostics, twice (`solved-26.11.06-15.13-diag-toggle.md`)
