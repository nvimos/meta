---
id: TASK-25
title: 'control WSL instances and Docker containers from nvim'
status: Needs Test
assignee: []
created_date: '2026-11-05'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
  - todo-2026-neovim011
  - release-v2026
dependencies: []
ordinal: 25000
---

## Description

control WSL instances and Docker containers from nvim

- today: only phpactor's wsl.exe calls (lang/php.lua); nothing for listing/starting/stopping distros or containers
- ideas: picker for `wsl -l -v` (start, terminate, shell into, set default with confirmation);
  picker for docker ps/images/compose (logs, exec shell, restart); check existing plugins first

From `todo-ideas.md`, section "ideas october".
- v2026 release checklist item 16 (was TASK-56): WSL and Docker control from nvim

## Branch

Built 2026-11-05 and 2026-11-10 on `PR-wsl-docker` in the config repo (fb2113e .. db842e3), not merged yet:
:Wsl and :Docker pickers, :WslFterm, F2 compose; docker defaults to the phpactor distro.

## Verify

- [ ] the test session in the branch's `todo-test/wsl-docker.md` (guided, one step per question)
- [ ] merge the branch into the working branch

## Original notes

```markdown
- [ ] control WSL instances and Docker containers from nvim (2026-11-05)
  - today: only phpactor's wsl.exe calls (lang/php.lua); nothing for listing/starting/stopping distros or containers
  - ideas: picker for `wsl -l -v` (start, terminate, shell into, set default with confirmation);
    picker for docker ps/images/compose (logs, exec shell, restart); check existing plugins first
```
