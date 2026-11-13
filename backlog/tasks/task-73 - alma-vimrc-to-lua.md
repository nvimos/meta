---
id: TASK-73
title: 'alma vimrc to lua'
status: To Do
assignee: []
created_date: '2026-11-10'
labels:
  - nvim-config
  - todo-2027
  - new-setup-2027
dependencies: []
ordinal: 73000
---

## Description

almavimrc

- incorporate / rewrite to lua
  - set up a tracker readme
  - maybe annotate / comment functions in vim9 and say where their nvim counterparts are
  - consider dropping long-term support idea
  - just copy what you need back to nvim, and leave it as is
- put submodules lua/genja/alma -> nvim/alma
  - split in modules/parts and set up a concat script
  - keep as a stable-fallback for nvim or vim9 setup
    - try linking vim9 .vimrc to .config/neovim/init.vim
- or not

From `todo-2027.md`, section "new setup 2027".

## Original notes

```markdown
- [ ] almavimrc:
  - incorporate / rewrite to lua
    - set up a tracker readme
    - maybe annotate / comment functions in vim9 and say where their nvim counterparts are
    - consider dropping long-term support idea
    - just copy what you need back to nvim, and leave it as is
  - put submodules lua/genja/alma -> nvim/alma
    - split in modules/parts and set up a concat script
    - keep as a stable-fallback for nvim or vim9 setup
      - try linking vim9 .vimrc to .config/neovim/init.vim
  - or not
```
