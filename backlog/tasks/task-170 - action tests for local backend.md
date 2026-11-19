---
id: TASK-170
title: 'action tests for local backend'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-162
  - TASK-163
  - TASK-164
  - TASK-165
  - TASK-166
  - TASK-167
  - TASK-168
  - TASK-184
  - TASK-185
ordinal: 170000
---

## Description

Each action task ships its own tests; this task adds the edge cases that cut across them, for the
local action model and the Add and Ignore mode state, without widgets or Neovim: queue order,
optimistic restore, pending refresh, ignore edge cases and file failures. A criterion already covered
by a task's own tests is ticked by pointing at that test.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 every action has a success and a failure test
- [x] #2 optimistic restore is tested for multi-row actions
- [x] #3 a pending action blocks a stale refresh
- [x] #4 ignore duplicates, nested repos and CRLF are covered
- [x] #5 task file edits and the expect-check are covered
- [x] #6 local jobs, cancel and `cli` results are covered
- [x] #7 tests leave no temp folder or git process behind

## Verify

- [ ] test: the new test file runs with no Neovim
- [ ] test: the same file passes twice in a row
- [ ] check: `%TEMP%` count unchanged
