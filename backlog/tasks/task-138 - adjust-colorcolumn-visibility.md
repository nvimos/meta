---
id: TASK-138
title: 'adjust colorcolumn visibility'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - colors
dependencies: []
ordinal: 138000
---

## Description

colors: the textwidth/colorcolumn stripe is barely visible. Commits: config dc8b9a8.

## Acceptance Criteria

- [x] #1 `lua/genja/hilite.lua`: `color_column` blends the `Normal` background 25% towards the colorscheme's
  gray `#303030` (result `#0c0c0c`), at startup and on `ColorScheme`

## Verify

- [ ] test: markdown file (`colorcolumn=+1`): the stripe is faint but visible
- [ ] test: `:ReloadLuaGenja` twice: the stripe does not change

## Notes

- `COLORCOLUMN_BLEND` 15 makes it nearly invisible, 40 a faint stripe.
