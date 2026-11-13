---
id: TASK-119
title: 'frontend connect and retry'
status: Needs Test
assignee: []
created_date: '2026-11-11'
labels:
  - frontend
dependencies: []
ordinal: 119000
---

## Description

The connect screen tried every 2 s, forever. Now it tries once at startup; Retry tries again and
Start Neovim opens `nvim` in its own console with the backend plugin, then connects (up to 10 s).

## Acceptance Criteria

- [x] #1 `Session.connect` tries once, no retry timer, also after "Neovim went away"
- [x] #2 `lib/state/nvim_launcher.dart`: finds the backend checkout (`NVIMOS_BACKEND` or next to a parent folder), starts nvim through `cmd /c start`
- [x] #3 connect screen: Retry and Start Neovim buttons; tests in `test/session_test.dart`, `test/nvim_launcher_test.dart`

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] start the app with no Neovim: one try, the reason shows, nothing retries
- [ ] Start Neovim from the release exe and from `make run`: a console opens and the app connects
- [ ] quit that Neovim: "Neovim went away", Retry after starting it again
