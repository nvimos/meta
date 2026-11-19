---
id: TASK-181
title: 'final mode rail and keys'
status: Needs Test
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-175
  - TASK-176
  - TASK-177
  - TASK-178
  - TASK-179
  - TASK-180
ordinal: 181000
---

## Description

Settle the final shell: mode rail entries, the key table and Help, focus roles, theme and widgets.
Each duplicate widget follows the user's choice in doc-76's widget table. Remove the duplicate
widgets and dead keys the merge leaves behind.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 the mode rail lists Pull request, Changes, Add and Ignore, History, Tasks, Repos, Settings, Log, Help, on Alt+1 … Alt+9
- [x] #2 every new key is in the handler, the Help table and `PLAN.md`
- [x] #3 focus roles and the debug bar name the new panes
- [x] #4 there is one widget for each repeated control and one theme token per colour
- [x] #5 no duplicated key binding or dead Help row remains

## Verify

- [x] widget test: rail and key help contain the new modes and keys
- [x] analyze: no unused widget or import
- [ ] manual: keyboard-only pass through every mode
