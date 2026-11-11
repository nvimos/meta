# Bootstrap script and CI

Status: To Do (backlog TASK-116)

## Why

An outside review (`backlog/docs/doc-1 - cleanup-release-2026.md`) found the config hard to adopt: a
serious install needs Neovim 0.11+, Git, curl, ripgrep, fd, Node, Python, PowerShell 7, GNU Make, Go,
PHP, a C compiler, Nerd Fonts, WSL and Docker, installed by hand, and nothing shows the tests pass.

## What Changes

- `bootstrap.ps1` (Windows) and `bootstrap.sh` (Linux, Termux) install every dependency and are safe to re-run
- GitHub Actions run `tests/` and an install-and-enable-everything test; badges in the README
- manual install tests on other machines: TASK-82 (Lumix), TASK-86 (Linux, Termux, VPS, `NVIM_APPNAME`)

## Impact

- new: `bootstrap.ps1`, `bootstrap.sh`, `.github/workflows/`; README install section
- tasks: TASK-116 (bootstrap), TASK-117 (CI)
