---
id: TASK-132
title: 'folds: z1/z2 change the fold level, foldnestmax 5'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - folds
dependencies: []
ordinal: 132000
---

## Description

folds: `z1` lowers and `z2` raises 'foldlevel' by one. Commits: config 24e73e2.

## Acceptance Criteria

- [x] #1 `lua/genja/map-zero.lua`: `z1` runs `zm`, `z2` runs `zr` (both take a count)
- [x] #2 `lua/genja/opt.lua`: `foldnestmax = 5` in the ui fold; only for foldmethod indent and syntax, not
  expr (markdown)

## Verify

- [ ] test: `z1` closes one more fold level, `z2` opens one more, `3z2` opens three
- [ ] test: `z10<CR>` still sets the window height to 10 (it waits for `timeoutlen` after `z1`)

## Notes

- `foldnestmax` does nothing for markdown folds (treesitter expression). A custom `foldexpr` would cap the
  depth.
