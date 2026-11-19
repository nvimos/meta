---
id: TASK-187
title: 'notice bar replaces the snackbar'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-162
ordinal: 187000
---

## Description

Replace Ops' action snackbar (`showActionError`) with Purrage's notice bar and grouped notices, in
every mode (decided 2026-11-19). Keep what Ops' snackbar does well: the Details button that opens the
selectable trace, and the notice staying open while the mouse is over it. The ErrorPane for a failed
load stays. A notice links to its entry in the Log mode (TASK-179) once that exists.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 every former `showActionError` call shows the notice bar instead
- [ ] #2 Details opens the full, selectable trace with Neovim's or git's own words
- [ ] #3 the notice does not close while hovered, and closes on its timer after the mouse leaves
- [ ] #4 repeated failures of one action group into one notice
- [ ] #5 the Details button has the pointer cursor and a tooltip

## Verify

- [ ] widget test: a failed action shows the notice; hover keeps it open; Details shows the trace
- [ ] check: no `ScaffoldMessenger` snackbar call remains for action errors
- [ ] manual: fail an action in Changes and in Tasks
