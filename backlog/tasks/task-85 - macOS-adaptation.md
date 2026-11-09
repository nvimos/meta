---
id: TASK-85
title: 'macOS adaptation'
status: To Do
assignee: []
created_date: '2026-11-10'
labels:
  - todo-2028
  - later-2028
dependencies: []
ordinal: 85000
---

## Description

macOS adaptation

- macOS shares the Unix-style Neovim paths and shell model with Linux, but it is not simply interchangeable:
- The existing code appears to have some macOS branches, but the project’s testing and development center of gravity is still Windows.

From `todo-2028.md`, section "later: 2028".

## Acceptance Criteria

- [ ] #1 install dependencies through Homebrew rather than winget;
- [ ] #2 use native PHP and language servers instead of WSL;
- [ ] #3 replace xdg-open with open where the existing abstraction does not already handle it;
- [ ] #4 use zsh/bash-compatible terminal commands;
- [ ] #5 inspect C compiler and Tree-sitter parser requirements;
- [ ] #6 verify GUI font handling and Nerd Font installation;
- [ ] #7 replace Windows-only PowerShell preview and task behavior.

## Original notes

```markdown
- [ ] macOS adaptation
  - macOS shares the Unix-style Neovim paths and shell model with Linux, but it is not simply interchangeable:
  - [ ] install dependencies through Homebrew rather than winget;
  - [ ] use native PHP and language servers instead of WSL;
  - [ ] replace xdg-open with open where the existing abstraction does not already handle it;
  - [ ] use zsh/bash-compatible terminal commands;
  - [ ] inspect C compiler and Tree-sitter parser requirements;
  - [ ] verify GUI font handling and Nerd Font installation;
  - [ ] replace Windows-only PowerShell preview and task behavior.
  - The existing code appears to have some macOS branches, but the project’s testing and development center of gravity is still Windows.
```
