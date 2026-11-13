---
id: TASK-135
title: 'step ccc slider by 10 with shift-arrows'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - colors
dependencies: []
ordinal: 135000
---

## Description

ccc: in the colour picker `<S-Left>` and `<S-Right>` move the slider by 10, ten times the 1 of `<Left>` and
`<Right>`. Commits: config 9a71f59.

## Acceptance Criteria

- [x] #1 `lua/lazyp/new/ccc.lua`: `<S-Left>` is `decrease10`, `<S-Right>` is `increase10`
- [x] #2 the `?` help popup and `readme.cheatsheet.md` list the keys

## Verify

- [ ] test: `<leader>ic`, `<Left>`/`<Right>` change the slider by 1, `<S-Left>`/`<S-Right>` by 10
- [ ] test: `?` in the picker lists the Shift keys
