---
id: TASK-175
title: 'purrage mode view'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-168
ordinal: 175000
---

## Description

Build the Add and Ignore mode view (the Purrage mode's final name): the whole-file status list with sections, cursor, selection, filter and
row actions for add, untrack, ignore and delete. Use Ops' shell, theme, keys and widgets; this is not
a second app.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 the list shows conflicts, staged, changed and untracked sections
- [ ] #2 plain, ctrl and shift selection work with mouse and keyboard
- [ ] #3 add, untrack, ignore and delete are reachable from the row and the keys
- [ ] #4 the active list keeps its row in view and lights its title
- [ ] #5 the mode follows the Ops pointer, tooltip and focus rules

## Verify

- [ ] widget test: render a fixture list, move and select
- [ ] widget test: a row action updates through the state object
- [ ] manual: use the mode on a local checkout
