# macOS adaptation

Status: To Do (backlog TASK-85)

## Why

macOS adaptation

- macOS shares the Unix-style Neovim paths and shell model with Linux, but it is not simply interchangeable:
- The existing code appears to have some macOS branches, but the project’s testing and development center of gravity is still Windows.

## What Changes

- install dependencies through Homebrew rather than winget;
- use native PHP and language servers instead of WSL;
- replace xdg-open with open where the existing abstraction does not already handle it;
- use zsh/bash-compatible terminal commands;
- inspect C compiler and Tree-sitter parser requirements;
- verify GUI font handling and Nerd Font installation;
- replace Windows-only PowerShell preview and task behavior.

## Impact

- Source: `todo-2028.md`, section "later: 2028"

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
