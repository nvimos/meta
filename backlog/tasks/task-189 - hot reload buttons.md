---
id: TASK-189
title: 'hot reload buttons'
status: Needs Test
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies: []
ordinal: 189000
---

## Description

Port Purrage's hot reload and hot restart into Ops (the user wants them): `lib/state/hot_reload.dart`
(135 lines; it connects to the app's own Dart VM service, which `flutter run` registers, and calls
`reloadSources` / the restart service) and the two `HotButtons` in the status bar. Debug builds only:
a release build has no VM service, so the buttons are not drawn there. It needs nothing from the rest
of the programme, so it goes first and both agents use it while they build the other tasks.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 under `make live` / `flutter run`, the reload button reloads changed code and keeps the state
- [ ] #2 the restart button restarts the app from `main`
- [ ] #3 a release build shows neither button
- [x] #4 a failed reload says why in one line (the action error UI), not a crash
- [x] #5 both buttons have the pointer cursor and a tooltip; reload and restart are timed as `app.reload` / `app.restart`

## Verify

- [x] test: a fake `HotReload` with `available: false` draws no buttons
- [x] test: a fake that throws reports the message
- [ ] manual: `make live`, change a label, press reload
