---
id: TASK-199
title: 'ops tooltip semantics: no orphan accessibility nodes from nested tooltips'
status: In Progress
assignee: []
created_date: '2026-11-20'
labels:
  - ops
  - accessibility
dependencies: []
ordinal: 199000
---

## Description

ops: `make live` logs bursts of `Failed to update ui::AXTree, error: <id> will not be in the tree and is not the new root`. A tooltip that shares a semantics node with another overlay portal (a second tooltip in a row) shows a bubble whose node has no parent; the Windows accessibility bridge rejects it on every frame of the fade.

Change: `openspec/changes/ops-tooltip-semantics/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 the cause is found and reproduced in a widget test
- [ ] #2 a test helper shows every tooltip of a screen and fails on an orphan overlay node; the view tests of every mode call it
- [x] #3 similar problems in the code are looked for and listed in the proposal
- [ ] #4 what the helper finds is fixed; a `make live` run shows no `Failed to update ui::AXTree` while hovering tooltips
<!-- AC:END -->
