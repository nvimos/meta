---
id: TASK-210
title: 'ops tooltips: place them below a large mouse pointer'
status: To Do
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - ui
  - accessibility
dependencies: []
ordinal: 210000
---

## Description

ops: with Windows' large mouse pointer (Accessibility > Mouse pointer size), tooltips appear under the pointer and are hidden by it. Detect the pointer size (`CursorBaseSize`, re-read on `WM_SETTINGCHANGE`) and move every tooltip below it (`TooltipThemeData.verticalOffset`); a Settings row (Tooltip distance: Automatic or a number) for when detection is wrong.

Change: `openspec/changes/ops-tooltips-below-large-cursor/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 with a large pointer every tooltip shows fully below it
- [ ] #2 a pointer size change in Windows applies without a restart
- [ ] #3 Settings can set the distance by hand
<!-- AC:END -->
