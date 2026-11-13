---
id: TASK-137
title: 'fold column shows lines'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - folds
dependencies: []
ordinal: 137000
---

## Description

folds: the fold column draws the vertical line at every depth, no digits and no triangles.
Commits: config 588bd08.

## Acceptance Criteria

- [x] #1 `lua/genja/opt-listchars.lua`: `foldopen` and `foldclose` are `│` like `foldsep` (▼ and ▶ before)
- [x] #2 `after/ftplugin/markdown.lua`: `foldcolumn = 'auto:9'`, so nested headings get a wide enough column
  (nvim shows a digit once a fold nests deeper than the column is wide; no option turns that off)
- [x] #3 leftover: the comment on the html comment groups in `after/ftplugin/markdown.lua` said "gray
  background"

## Verify

- [x] test: markdown file with H1 to H6 nested: the fold column grows and shows `│` at every depth, no digits
- [x] test: open and closed folds both show `│`, no ▼ or ▶
- [ ] test: a code file with folds deeper than 3 (indent or syntax) can still show digits: fixed width 3

## Notes

- To avoid digits everywhere without widening: a custom `foldexpr` that caps the level at 3.
