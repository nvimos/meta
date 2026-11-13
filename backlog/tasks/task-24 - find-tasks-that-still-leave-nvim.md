---
id: TASK-24
title: 'find tasks that still leave nvim'
status: Needs Test
assignee: []
created_date: '2026-11-05'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 24000
---

## Description

nvim as the interface to the OS for coding work: shell, terminal, pwsh, Git Bash, git

- today: floaterm commands (:PwshFterm, :BashFterm, :LazygitFterm), toggleterm, :terminal pwsh/bash, Neogit, mini.git
- open: which simple tasks still make you leave nvim?

From `todo-ideas.md`, section "ideas october".

## Branch

Built 2026-11-05 and 2026-11-10 on `PR-tasks-detach` in the config repo (56be3ca .. 0bda9dd), not merged yet:
long processes on overseer: output buffer, statusline count, detach with log/pid or psmux, :Tasks, :Unsaved.

## Verify

- [ ] the test session in the branch's `todo-test/tasks-long-processes.md` (guided, one step per question)
- [ ] merge the branch into the working branch

## Original notes

```markdown
- [ ] nvim as the interface to the OS for coding work: shell, terminal, pwsh, Git Bash, git (2026-11-05)
  - today: floaterm commands (:PwshFterm, :BashFterm, :LazygitFterm), toggleterm, :terminal pwsh/bash, Neogit, mini.git
  - open: which simple tasks still make you leave nvim?
```
