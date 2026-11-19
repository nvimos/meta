---
id: TASK-191
title: 'Ignore pane closer to Purrage, without the dead match lookup'
status: To Do
assignee: []
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies: []
ordinal: 191000
---

## Description

Rebuild the Add and Ignore mode's Ignore pane after Purrage's two panes: the list of every
`.gitignore` of the project (the top one "project .gitignore") and every line of the selected one.
The area is shared with the preview through a switch, resizable and remembered. Drop the "which rule
ignores this row" lookup: a row of the list can never be ignored, so it never matched, in Ops or in
Purrage. Remove the test that invents a match, and the Ignore dialog's dead "already ignored"
branch. The lines keep their hover buttons and get a right-click menu (Delete, Dirname, Open).

Change: `openspec/changes/ops-ignore-pane/`.
Notes: `nvimos-ops/doc-wip/readme.2026-11-19.ignore-pane.md`.
