---
id: TASK-200
title: 'ops rail order: drag to reorder, hide modes, and a drag threshold'
status: In Progress
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - ui
dependencies: []
ordinal: 200000
---

## Description

ops: the mode rail is in the user's order. Drag an icon to move a mode, right-click to hide it, Settings to show it again. A click must not turn into a drag: a press lifts the icon only after the pointer moved 8 px (a finger: 18 px).

Change: `openspec/changes/ops-rail-order/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 drag to reorder, right-click to hide, Settings to show and reset; saved by mode name
- [x] #2 a press moving less than the drag threshold is a click; a widget test covers both sides
- [ ] #3 checked in the app with the mouse
- [ ] #4 checked on the touchscreen: tap opens, a finger drag reorders
<!-- AC:END -->
