---
id: TASK-201
title: 'ops dev icon: a wrench on the debug build''s icon'
status: To Do
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - build
dependencies: []
ordinal: 201000
---

## Description

ops: the dev (debug) build and the release build look the same in the taskbar. The dev build gets the ops icon with a small wrench over it (handle from the bottom-right corner, head toward the centre); release, single and the GitHub release keep the plain icon. `Runner.rc` picks the icon by `_DEBUG`, so nothing is swapped before a build.

Change: `openspec/changes/ops-dev-icon/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 `ops-dev.svg` with the wrench; it reads at 16 px
- [ ] #2 `make icon` builds both icons
- [ ] #3 a debug build shows the wrench in the exe, window and taskbar; a release build doesn't
<!-- AC:END -->
