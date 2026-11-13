---
id: TASK-123
title: 'winbar: names for plugin windows'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - statusline
  - issue
  - nvim-config
dependencies: []
ordinal: 123000
---

## Description

winbar: plugin windows showed [Scratch] or internal buffer names. Commits: genja-statusline.nvim 8a797ad.

## Acceptance Criteria

- [x] #1 FT_LABELS in plug-wip/genja-statusline.nvim/lua/genja-statusline/winbar.lua: aerial, undotree, neotest, overseer, dap-ui, dap-view
- [x] #2 aerial shows `Outline: <file>` from b:source_buffer
- [x] #3 README.md winbar bullet

## Verify

- [ ] test: `:AerialToggle`, switch files: winbar reads `Outline: <file>`
- [ ] test: open undotree, a dap-ui session, the neotest summary: plain names
