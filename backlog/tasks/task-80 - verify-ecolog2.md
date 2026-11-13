---
id: TASK-80
title: 'verify ecolog2'
status: To Do
assignee: []
created_date: '2026-11-10'
labels:
  - nvim-config
  - todo-2027
  - git-add-improvement
dependencies: []
ordinal: 80000
---

## Description

verify ecolog2 (with rust) (lua/lazyp/ui-telescope/ecolog.lua; from...

- `cargo install ecolog-lsp` by hand; ~/.cargo/bin is on PATH (lua/genja/env.lua)
- test: `<leader>gE`, `<leader>gEs`, `<leader>gEv` do something with ecolog2 loaded
- test: with cargo or ecolog-lsp on PATH :Lazy lists ecolog2.nvim loaded and ecolog.nvim disabled

From `todo-2027.md`, section "git add improvement".

## Original notes

```markdown
- [ ] verify ecolog2 (with rust) (lua/lazyp/ui-telescope/ecolog.lua; from todo-issue/solved-26.10.31-12.14-ecolog-cond.md)
  - `cargo install ecolog-lsp` by hand; ~/.cargo/bin is on PATH (lua/genja/env.lua)
  - test: `<leader>gE`, `<leader>gEs`, `<leader>gEv` do something with ecolog2 loaded
  - test: with cargo or ecolog-lsp on PATH :Lazy lists ecolog2.nvim loaded and ecolog.nvim disabled
```
