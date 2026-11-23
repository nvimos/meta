---
id: TASK-203
title: 'ops inspect button: toggle the widget select mode from the debug bar'
status: To Do
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - debug
dependencies: []
ordinal: 203000
---

## Description

ops, debug build only: a button next to the debug bar's bug button turns Flutter's widget select mode on and off. While on, a click outlines the element under the pointer and names its widget class.

Change: `openspec/changes/ops-inspect-button/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 the button sits beside the bug button in debug builds and is absent in release
- [ ] #2 it toggles the select mode; a click then names the element's class
<!-- AC:END -->
