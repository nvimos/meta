# bootstrap core plugins with neovim

Status: Dropped (backlog TASK-37)

## Why

bootstrap core plugins with neovim

- ~/.local/share/nvim/site/pack/core/opt/ (Linux/macOS) (or under $XDG_DATA_HOME/nvim)
- %LOCALAPPDATA%\nvim-data\site\pack\core\opt\ (Windows)

## What Changes

- lazy disables pack/ loading (vim.pkg.add)
- plugin manager: stick with lazy
- move bootstrap to lua/lazy-boot.vim

## Impact

- Source: `todo-2026-neovim011.md`, section "new setup 2026"

## Original notes

```markdown
-[n] bootstrap core plugins with neovim
    -[x] lazy disables pack/ loading (vim.pkg.add)
        - ~/.local/share/nvim/site/pack/core/opt/ (Linux/macOS) (or under $XDG_DATA_HOME/nvim)
        - %LOCALAPPDATA%\nvim-data\site\pack\core\opt\ (Windows)
    -[x] plugin manager: stick with lazy
    -[x] move bootstrap to lua/lazy-boot.vim
```
