---
id: TASK-196
title: 'ops: show the planning from a GitHub snapshot when there is no local meta checkout'
status: To Do
assignee: []
created_date: '2026-11-19'
labels:
  - ops
  - frontend
  - tasks
dependencies: []
ordinal: 196000
---

## Description

ops: a `.nvimos` with `tracking_remote = nvimos/meta` lets a fresh clone show its tasks: when the local tracking folder is missing, Ops fetches an archive of the planning repo's `main` into its cache and shows it read-only, with a bar for its age, Refresh and Clone.

Change: `openspec/changes/tracking-remote-snapshot/`

## Acceptance Criteria

- [ ] #1 `.nvimos` takes `tracking_remote` and `tracking_ref`
- [ ] #2 no local tracking folder: the snapshot is fetched without being asked and the Tasks mode shows it
- [ ] #3 the snapshot is read-only, with a bar showing its source and age, Refresh and Clone
- [ ] #4 a failed fetch keeps the old snapshot; the archive is extracted safely (only backlog/ and openspec/)
