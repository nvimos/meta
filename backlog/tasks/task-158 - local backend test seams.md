---
id: TASK-158
title: 'local backend test seams'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-155
ordinal: 158000
---

## Description

Make the local backend testable without a real process or a real repository: fake process runner,
fake environment and fake directory lister, plus a `makeRepo`-style temp repository helper with
registered cleanup. This is the test foundation for every later local task, so it comes right after
TASK-155 and before TASK-156/157, which write their tests on it. Each later task brings its own tests.

Change: `openspec/changes/purrage-local-git-backend/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 a fake process runner can return status, log and diff output
- [ ] #2 a temp repository is a `git init` fixture with `core.fsmonitor=false`, registered with `keepForCleanup`
- [ ] #3 every temp folder is removed when the test file ends
- [ ] #4 no headless Neovim is needed for local backend tests
- [ ] #5 the helper is shared by later local action tests

## Verify

- [ ] test: one test drives the ported `GitRepo` through fakes only
- [ ] test: a temp repo test runs twice in a row without leftovers
- [ ] check: the `%TEMP%` `nvimos_*` count is unchanged after the run
