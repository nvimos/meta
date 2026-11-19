---
id: TASK-188
title: 'shared status store and action queue'
status: Needs Test
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-154
ordinal: 188000
---

## Description

Design the shared core the two file modes sit on (decided 2026-11-19: two thin mode states over a
shared core): one status store and one action queue per repository. Changes and the Add and Ignore
mode each keep only their own cursor, selection and filter. This task writes the interfaces, moves
Ops' current `Changes` optimistic/pending logic onto them with no change in behaviour, and records
them in doc-76's Interface changes table. TASK-162 then ports Purrage's queue, per-action rollback
and `ActionResult` behind the same interfaces.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 one status store per repository is the only owner of the file list
- [x] #2 the action queue interface covers optimistic change, rollback of that action's rows, and result
- [x] #3 `ChangesState` reads the store and runs actions through the queue, with unchanged behaviour
- [x] #4 the interfaces are recorded in doc-76 before the task reaches Needs Test

## Verify

- [x] test: the existing Changes tests pass unchanged
- [x] test: two mode states over one store see the same rows after an action
- [x] review: TASK-162 and TASK-168 can build on it without changing it
