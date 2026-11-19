---
id: TASK-176
title: 'ignore pane and dialog'
status: Needs Test
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-166
  - TASK-168
ordinal: 176000
---

## Description

Port Purrage's ignore pane and dialog: the rules around the focused file, which rule matches, the
scope and target choices, the preview before writing, and the line delete/dirname edit.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 the pane lists the ignore files and the matching rule for the focused row
- [x] #2 the dialog previews the rules and the rows they cover
- [x] #3 already-ignored rows are named before the click
- [x] #4 a rule can be deleted or moved one folder up
- [x] #5 the pane follows the cursor with no git call per keypress

## Verify

- [x] widget test: the dialog with a fixture row set
- [x] widget test: the pane updates after a cursor move
- [ ] manual: write a rule, see the file leave the list
