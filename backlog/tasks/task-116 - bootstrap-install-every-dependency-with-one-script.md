---
id: TASK-116
title: 'bootstrap: install every dependency with one script'
status: To Do
assignee: []
created_date: '2026-11-08'
labels:
  - nvim-config
  - install
  - release
dependencies: []
ordinal: 116000
---

## Description

A serious install needs Neovim 0.11+, Git, curl, ripgrep, fd, Node, Python, PowerShell 7, GNU Make, Go, PHP,
a C compiler, Nerd Fonts, WSL, Docker and optional AI tools. Fine for the author's workstation, not a
portable "clone this and forget it" distro (outside review, `backlog/docs/doc-1 - cleanup-release-2026.md`).

Change: `openspec/changes/bootstrap-and-ci/`.

## Acceptance Criteria

- [ ] #1 write a bootstrap.sh
- [ ] #2 write a bootstrap.ps1

## Original notes

```markdown
- What worries me (manus im)
  - The main problem is maturity, not taste.
  - The GitHub repository appears to have been created on November 7, 2026, has zero stars, zero forks, no releases, no
    license listed, and its default branch is unusually named enterprise. Its latest commits are effectively the initial
    author’s ongoing development work. Repository metadata
  - The dependency surface is also large. A serious installation may involve Neovim 0.11+, Git, curl, ripgrep, fd, Node,
    Python, PowerShell 7, GNU Make, Go, PHP, a C compiler, Nerd Fonts, WSL, Docker, and several optional AI tools. That
    is perfectly reasonable for the author’s Windows workstation, but it is not a portable “clone this and forget it”
    distro.
  - install all deps automagically
    - [ ] write a bootstrap.sh
    - [ ] write a bootstrap.ps1
  - manual testink
    - [ ] test on a real lumix
    - [ ] test on a termux
    - [ ] test on a vps / free shell
    - [ ] try it in an isolated NVIM_APPNAME profile

  - [ ] set up github actiones para tests
    - [ ] do a install-and-enable everything test
    - [ ] add some ci bling to the readme
```

From `legacy/nvim-config/todo-2026.md`.
