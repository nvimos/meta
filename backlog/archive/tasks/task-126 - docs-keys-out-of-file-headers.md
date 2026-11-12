---
id: TASK-126
title: 'docs: keys out of file headers'
status: Done
assignee: []
created_date: '2026-11-12'
labels:
  - docs
  - issue
  - nvim-config
dependencies: []
ordinal: 126000
---

## Description

docs: file headers listed keys, some stale; keys belong in the cheatsheet. Commits: config b13f809.

## Acceptance Criteria

- [x] #1 30 headers (plugin/, lua/genja/ext/, map-plugin/, specs) point to the file that sets the keys
- [x] #2 cheatsheet: undotree `<leader>mu` (header said `<leader>u`), unsaved picker mouse clicks
- [x] #3 CLAUDE.md `## Keymaps` and `## Adding a plugin`: headers name no keys
