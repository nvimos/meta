---
id: TASK-174
title: 'crawler and hint tests'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-171
  - TASK-172
ordinal: 174000
---

## Description

TASK-171 and TASK-172 ship their own tests; this task adds the edge cases across them: the skip
list, depth changes, scan replacement, stale hints and the hint ordering, with a fake directory
lister. No real home folder scan and no Neovim.

Change: `openspec/changes/purrage-project-discovery/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 repository detection covers `.git` folders and files
- [x] #2 nested repositories are not listed as separate checkouts
- [x] #3 skip rules and `AppData` depth are tested
- [x] #4 hint promotion and stale hints are tested
- [x] #5 tests run fast enough for the normal suite

## Verify

- [x] test: the whole crawler suite runs under the project's test timeout
- [x] test: no real drive is walked
- [x] check: no temp folders left behind
