---
id: TASK-192
title: 'Hidden modes and panes stay idle until shown'
status: To Do
assignee: []
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - performance
dependencies: []
ordinal: 192000
---

## Description

Every mode stays built in the shell's `IndexedStack`, and each one re-queries the backend on git
hints even while hidden. A hidden mode or pane should only mark itself stale and refresh once when
shown. The Add and Ignore ignore and preview panes do it first (TASK-191); this carries it to the
other modes and panes where it applies.

Change: `openspec/changes/ops-hidden-panes-idle/`.
