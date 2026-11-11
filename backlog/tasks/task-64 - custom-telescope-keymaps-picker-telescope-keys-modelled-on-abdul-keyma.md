---
id: TASK-64
title: 'custom telescope keymaps picker (telescope-keys), modelled on abdul-keymaps'
status: To Do
assignee: []
created_date: '2026-11-10'
labels:
  - nvim-config
  - todo-2027
  - new-setup-2027
dependencies: []
ordinal: 64000
---

## Description

custom telescope keymaps picker (telescope-keys), modelled on abdul-keymaps

- plug-wip/abdul-keymaps.nvim (fork), spec lua/lazyp/new/abdul-keymaps.lua
- reproduce its behavior
  - filters: builtin_patterns, include_builtins_with_desc, exclude_patterns
  - categories: category_patterns + category_order
  - keys: t cycles the mode filter (n, i, v, x, then the rest, then all), T all modes,
        / search (empty resets), r refresh, h key hints
- search key, desc and category; mode letters instead of icons

From `todo-2027.md`, section "new setup 2027".

## Original notes

```markdown
- [ ] custom telescope keymaps picker (telescope-keys), modelled on abdul-keymaps
  - plug-wip/abdul-keymaps.nvim (fork), spec lua/lazyp/new/abdul-keymaps.lua
  - reproduce its behavior
    - filters: builtin_patterns, include_builtins_with_desc, exclude_patterns
    - categories: category_patterns + category_order
    - keys: t cycles the mode filter (n, i, v, x, then the rest, then all), T all modes,
          / search (empty resets), r refresh, h key hints
  - search key, desc and category; mode letters instead of icons
```
