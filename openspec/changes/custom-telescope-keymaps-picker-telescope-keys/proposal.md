# custom telescope keymaps picker (telescope-keys), modelled on abdul-keymaps

Status: To Do (backlog TASK-64)

## Why

custom telescope keymaps picker (telescope-keys), modelled on abdul-keymaps

- plug-wip/abdul-keymaps.nvim (fork), spec lua/lazyp/new/abdul-keymaps.lua
- reproduce its behavior
  - filters: builtin_patterns, include_builtins_with_desc, exclude_patterns
  - categories: category_patterns + category_order
  - keys: t cycles the mode filter (n, i, v, x, then the rest, then all), T all modes,
        / search (empty resets), r refresh, h key hints
- search key, desc and category; mode letters instead of icons

## What Changes

- (to be worked out)

## Impact

- Source: `todo-2027.md`, section "new setup 2027"

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
