---
id: TASK-82
title: 'Lumix adaptation'
status: To Do
assignee: []
created_date: '2026-11-10'
labels:
  - nvim-config
  - todo-2027
  - git-add-improvement
dependencies: []
ordinal: 82000
---

## Description

Lumix adaptation

- But the project explicitly says Linux has not been tested as a clean installation. A usable Linux adaptation would likely require:
- Some parts already contain portability logic. For example, the config knows about bash on Linux, xdg-open, macOS detection, and platform-specific path separators. But that is different from having a supported Linux profile.

From `todo-2027.md`, section "git add improvement".

## Acceptance Criteria

- [ ] #1 Linux should use the conventional configuration location: ~/.config/nvim
- [ ] #2 replacing or bypassing the PowerShell-based test runner;
- [ ] #3 changing tests/Makefile from pwsh.exe to a POSIX shell or installing PowerShell Core;
- [ ] #4 removing the WSL-specific PHP path and running phpactor natively;
- [ ] #5 replacing wsl.exe commands with direct Linux commands;
- [ ] #6 using fd, rg, locate, or another native file index instead of es.exe;
- [ ] #7 checking every cmd.exe/PowerShell task and shell wrapper;
- [ ] #8 adapting Windows-only Markdown preview behavior, especially the “open a new PowerShell window” workflow;
- [ ] #9 verifying terminal, path, clipboard, and executable detection behavior.
- [ ] #10 test on a real Lumix

## Original notes

```markdown
- [ ] Lumix adaptation
  - [ ] Linux should use the conventional configuration location: ~/.config/nvim
  - But the project explicitly says Linux has not been tested as a clean installation. A usable Linux adaptation would likely require:
  - [ ] replacing or bypassing the PowerShell-based test runner;
  - [ ] changing tests/Makefile from pwsh.exe to a POSIX shell or installing PowerShell Core;
  - [ ] removing the WSL-specific PHP path and running phpactor natively;
  - [ ] replacing wsl.exe commands with direct Linux commands;
  - [ ] using fd, rg, locate, or another native file index instead of es.exe;
  - [ ] checking every cmd.exe/PowerShell task and shell wrapper;
  - [ ] adapting Windows-only Markdown preview behavior, especially the “open a new PowerShell window” workflow;
  - [ ] verifying terminal, path, clipboard, and executable detection behavior.
  - Some parts already contain portability logic. For example, the config knows about bash on Linux, xdg-open, macOS detection, and platform-specific path separators. But that is different from having a supported Linux profile.
```
