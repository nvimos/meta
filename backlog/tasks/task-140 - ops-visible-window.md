---
id: TASK-140
title: 'ops: :Ops starts the app with a visible window'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - ops
dependencies: []
ordinal: 140000
---

## Description

ops: `:Ops` started the front end app through `jobstart`, which on Windows spawns a hidden window, so the app
ran unseen. It now uses `vim.uv.spawn` with `hide = false`. Commits: config 09c171e.
Found in another session; filed here with its commit.

## Acceptance Criteria

- [x] #1 `plugin/ops.lua`: `vim.uv.spawn` detached with a visible window; the handle is closed on exit and
  unref'd so nvim can quit
- [x] #2 a failed spawn is reported with the reason

## Verify

- [ ] test: `:Ops` opens the app in a visible window
- [ ] test: `:q` in nvim is not blocked while the app runs
- [ ] test: with a wrong executable path the error names it

## Notes

- Not written in this session; the verify steps come from the diff.
