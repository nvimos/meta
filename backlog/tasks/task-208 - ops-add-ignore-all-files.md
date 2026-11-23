---
id: TASK-208
title: 'ops Add and Ignore: a toggle that shows every tracked file too'
status: In Progress
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - ui
dependencies: []
ordinal: 208000
---

## Description

ops: a button left of the preview, ignore panes and reload buttons in Add and Ignore (and the key `T`) shows all files git tracks, not only the changed and untracked ones, in a Tracked section. The mode becomes a quick file browser with the preview beside it.

Change: `openspec/changes/ops-add-ignore-all-files/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 the toggle shows a Tracked section with every clean tracked file; off hides it
- [ ] #2 a changed file is not listed twice; tracked rows can be untracked and ignored
- [ ] #3 the choice is remembered; a cursor move does not rebuild the rows
<!-- AC:END -->
