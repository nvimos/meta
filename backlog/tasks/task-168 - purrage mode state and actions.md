---
id: TASK-168
title: 'purrage mode state and actions'
status: To Do
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
  - TASK-166
  - TASK-167
ordinal: 168000
---

## Description

Build the state object for the future Add and Ignore mode (the Purrage mode's final name): rows and
sections, selection (plain, ctrl, shift), filter, cursor, track, untrack, ignore and delete. This is
Purrage's `Changes` state adapted to Ops' models, as a thin state over the shared core from
TASK-188; no view yet. No commit: Purrage's commit bar is not ported.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 rows group into conflicts, staged, changed and untracked
- [ ] #2 rows are Ops' `Status` model, not a second Purrage `StatusRow` truth
- [ ] #3 selection follows plain, ctrl and shift click, and prunes on reload
- [ ] #4 track, untrack, ignore and delete work through the action queue
- [ ] #5 the cursor survives a reload when the path still exists
- [ ] #6 the state is driveable without widgets

## Verify

- [ ] test: selection and filter with a fixture row set
- [ ] test: track/untrack/ignore/delete through a fake repo
- [ ] test: a failed action restores only its rows
