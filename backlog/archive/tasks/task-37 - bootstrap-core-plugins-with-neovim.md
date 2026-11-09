---
id: TASK-37
title: 'bootstrap core plugins with neovim'
status: Dropped
assignee: []
created_date: '2026-11-10'
labels:
  - todo-2026-neovim011
  - new-setup-2026
dependencies: []
ordinal: 37000
---

## Description

bootstrap core plugins with neovim

- ~/.local/share/nvim/site/pack/core/opt/ (Linux/macOS) (or under $XDG_DATA_HOME/nvim)
- %LOCALAPPDATA%\nvim-data\site\pack\core\opt\ (Windows)

From `todo-2026-neovim011.md`, section "new setup 2026".

## Acceptance Criteria

- [x] #1 lazy disables pack/ loading (vim.pkg.add)
- [x] #2 plugin manager: stick with lazy
- [x] #3 move bootstrap to lua/lazy-boot.vim

## Original notes

```markdown
-[n] bootstrap core plugins with neovim
    -[x] lazy disables pack/ loading (vim.pkg.add)
        - ~/.local/share/nvim/site/pack/core/opt/ (Linux/macOS) (or under $XDG_DATA_HOME/nvim)
        - %LOCALAPPDATA%\nvim-data\site\pack\core\opt\ (Windows)
    -[x] plugin manager: stick with lazy
    -[x] move bootstrap to lua/lazy-boot.vim
```
