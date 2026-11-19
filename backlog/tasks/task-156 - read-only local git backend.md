---
id: TASK-156
title: 'read-only local git backend'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-154
  - TASK-155
  - TASK-158
ordinal: 156000
---

## Description

Implement the read-only half of `LocalBackend`: branches, log, diff, status and repository info,
using Ops' models. Port relay's `nvimos.git` branch, log and diff commands into Dart; do not invent a
second status model. The diff parser is a line-by-line port of relay's `diffparse.lua` (decided),
with relay's cases as fixtures. The parity test against the Neovim backend uses `TestNvim` and the
relay checkout; every other test runs without Neovim.

Change: `openspec/changes/purrage-local-git-backend/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 `LocalBackend` implements `RepoBackend` without an editor session
- [ ] #2 branches and current branch match `git for-each-ref` and `branch --show-current`
- [ ] #3 log and diff produce the same `Commit`, `PrDiff` and `DiffFile` shapes Ops already uses
- [ ] #4 status feeds Ops' `Status`, not Purrage's `StatusRow`
- [ ] #5 a local repository can be opened and read with no Neovim process

## Verify

- [ ] test: a temp repo with branches, commits, a modified file and an untracked file
- [ ] test: the same repo read through `LocalBackend` matches the Neovim backend's models
- [ ] analyze: no new warnings
