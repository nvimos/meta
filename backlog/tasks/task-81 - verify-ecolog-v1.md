---
id: TASK-81
title: 'verify ecolog v1'
status: To Do
assignee: []
created_date: '2026-11-10'
labels:
  - nvim-config
  - todo-2027
  - git-add-improvement
dependencies: []
ordinal: 81000
---

## Description

verify ecolog v1 (without rust)

- test: without cargo and ecolog-lsp on PATH :Lazy lists ecolog.nvim loaded and ecolog2.nvim disabled
- test: `<leader>gE`, `<leader>gEp`, `<leader>gEs`, `<leader>gEv` do something with ecolog v1 loaded
- note: ecolog2's cond also takes cargo alone; with cargo on PATH and no ecolog-lsp, ecolog2 loads and .sh files log a spawn error

From `todo-2027.md`, section "git add improvement".

## Original notes

```markdown
- [ ] verify ecolog v1 (without rust)
  - test: without cargo and ecolog-lsp on PATH :Lazy lists ecolog.nvim loaded and ecolog2.nvim disabled
  - test: `<leader>gE`, `<leader>gEp`, `<leader>gEs`, `<leader>gEv` do something with ecolog v1 loaded
  - note: ecolog2's cond also takes cargo alone; with cargo on PATH and no ecolog-lsp, ecolog2 loads and .sh files log a spawn error
```
