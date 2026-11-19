---
id: TASK-198
title: 'resize costs only what moves'
status: In Progress
assignee: []
created_date: '2026-11-20'
labels:
  - frontend
  - ops
  - performance
dependencies: []
ordinal: 198000
---

## Description

The Add and Ignore side pane showed how a resize should work (TASK-191): the edge anchors on the
pointer, only the pane listens to the width, and the content keeps its widget instances. Carry the
same pass to the other resizes. The Help mode rebuilds all key rows and spans on every window width
change (80-220 ms per frame in a widget test); its split and columns only depend on the column count
and the search query, so they can be cached and a resize becomes layout only. The Pull request and
Changes left panes still add drag deltas to the last built width and `setState` per pointer event.

Change: `openspec/changes/ops-cheap-resizes/`.
