---
id: TASK-209
title: 'ops commit dialog: write and commit the message from any mode'
status: To Do
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - ui
dependencies: []
ordinal: 209000
---

## Description

ops: one key from any mode brings up the commit message as a dialog over the app: a resizable text area about 90 characters by 6 lines, Accept (commit), Hide (keep the text for next time), Cancel (clear it), an X in the corner; Esc and a click outside close it. The draft is shared with the Changes commit field. An idea to try.

Change: `openspec/changes/ops-commit-dialog-anywhere/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 the dialog comes up from every mode and commits what is staged
- [ ] #2 Hide keeps the text, Cancel clears it, Accept commits and clears it
- [ ] #3 the X, Esc and a click outside close it; the text area resizes and starts at about 90 × 6
<!-- AC:END -->
