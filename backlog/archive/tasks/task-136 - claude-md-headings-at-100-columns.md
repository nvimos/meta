---
id: TASK-136
title: 'claude.md headings at 100 columns'
status: Done
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - docs
dependencies: []
ordinal: 136000
---

## Description

docs: `CLAUDE.md` tightened, restructured into headings (to level 3), wrapped at 100 columns, with a new
`## Color design` section. Commits: config 9011592, config a18b779.

## Acceptance Criteria

- [x] #1 repeated bullets merged, filler cut (9011592)
- [x] #2 long list items turned into paragraphs under `##` and `###` headings; lists only for short, real
  lists
- [x] #3 prose wrapped at 100 columns; `## Formatting CLAUDE.md` records the rules
- [x] #4 `## Color design`: measure, derive, hierarchy, surfaces, scope and fallback, with contrast targets
- [x] #5 the "Lua files use tabs" line dropped (contradicted the 4-space rule)
