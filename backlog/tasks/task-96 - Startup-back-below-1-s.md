---
id: TASK-96
title: 'startup back below 1 s'
status: To Do
assignee: []
created_date: '2026-11-10'
labels:
  - performance
dependencies: []
ordinal: 96000
---

## Description

The startup test (`make test D=startup`, a Lua file) failed at 01:15 on 2026-11-10: 1.04-1.47 s, limit 1 s.
It passed at 00:50. `nvim --startuptime`: lazy-plug-spec ~300 ms self, opening buffers ~380 ms.
The new svelte/astro/angular parsers cost at most ~50 ms in a quick comparison; the rest is noise or older.

## Acceptance Criteria

- [ ] #1 find what grew (lazy spec count, treesitter install list, FileType handlers)
- [ ] #2 `make test D=startup` passes three times in a row
