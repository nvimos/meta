---
id: TASK-124
title: 'markdown: conceal toggle and cycle'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - markdown
  - issue
  - nvim-config
dependencies: []
ordinal: 124000
---

## Description

markdown: show or hide markup through conceallevel; fix on save moved to a longer key. Commits: config 82cbc5d.

## Acceptance Criteria

- [x] #1 lua/genja/ext/md-conceal.lua: `<leader>tmc` toggles 0 and ON (2), F2 task `conceal cycle` 0 1 2 3
- [x] #2 plugin/md-fix.lua: `<leader>tm` -> `<leader>tmm`
- [x] #3 which-key group `<leader>tm`, cheatsheet, lua/genja/readme.md

## Verify

- [ ] test: markdown file, `<leader>tmc` twice: markup shown, then hidden
- [ ] test: `<F2>` > conceal cycle steps 0 1 2 3
- [ ] test: `<leader>tmm` switches fix on save
