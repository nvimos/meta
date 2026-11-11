---
id: TASK-107
title: 'F2 context menu: finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-24'
labels:
  - f2
  - from-config
dependencies: []
ordinal: 107000
---

## Description

Finished work on F2 context menu, 2026-10-24 .. 2026-11-09: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

## Acceptance Criteria

- [x] #1 f2: git add one file and keep the picker open (2026-10-24; `solved-26.10.24-17.31-f2-git-add.md`)
- [x] #2 f2: item names less noisy (2026-10-25; `solved-26.10.25-00.07-f2-item-names.md`)
- [x] #3 f2: sources move into `lua/genja/f2/collect/` (2026-10-25; `solved-26.10.25-12.41-f2-collect.md`)
- [x] #4 f2: group names as symbols, a pwsh item for .ps1 files (2026-11-09; `solved-26.11.09-23.43-f2-groups.md`)
- [x] #5 f2 item names (undated; `ideas-42-f2-item-names.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: oil in a repo, <F2> > git add, <M-a> on a modified and an untracked file (`solved-26.10.24-17.31-f2-git-add.md`)
- [ ] test: `<F2>` in a markdown file: labels start in one column (`solved-26.10.25-00.07-f2-item-names.md`)
- [ ] test: `<F2>` in a lua file, in oil, in markdown; `:DevReloadF2`, then `<F2>` (`solved-26.10.25-12.41-f2-collect.md`)
- [ ] test: `make test D=f2` in `tests/` (`solved-26.10.25-12.41-f2-collect.md`)
- [ ] test: `make` in tests/f2 (`solved-26.11.09-23.43-f2-groups.md`)
- [ ] test: `<F2>` in a .ps1 buffer runs it; `<F2>` in markdown shows `markdown  glow preview` (`solved-26.11.09-23.43-f2-groups.md`)
- [ ] open: let callers add their own groups (todo in groups.lua) (`solved-26.11.09-23.43-f2-groups.md`)
