# Lumix adaptation

Status: To Do (backlog TASK-82)

## Why

Lumix adaptation

- But the project explicitly says Linux has not been tested as a clean installation. A usable Linux adaptation would likely require:
- Some parts already contain portability logic. For example, the config knows about bash on Linux, xdg-open, macOS detection, and platform-specific path separators. But that is different from having a supported Linux profile.

## What Changes

- Linux should use the conventional configuration location: ~/.config/nvim
- replacing or bypassing the PowerShell-based test runner;
- changing tests/Makefile from pwsh.exe to a POSIX shell or installing PowerShell Core;
- removing the WSL-specific PHP path and running phpactor natively;
- replacing wsl.exe commands with direct Linux commands;
- using fd, rg, locate, or another native file index instead of es.exe;
- checking every cmd.exe/PowerShell task and shell wrapper;
- adapting Windows-only Markdown preview behavior, especially the “open a new PowerShell window” workflow;
- verifying terminal, path, clipboard, and executable detection behavior.

## Impact

- Source: `todo-2027.md`, section "git add improvement"

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
