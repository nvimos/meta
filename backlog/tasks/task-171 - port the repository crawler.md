---
id: TASK-171
title: 'port the repository crawler'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-155
ordinal: 171000
---

## Description

Port Purrage's `RepoBrowser`: walk a start directory for `.git` checkouts, skip build/cache/system
trees, cap the depth, stop at a repository boundary, and produce a scan report. State layer only.

Change: `openspec/changes/purrage-project-discovery/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 a `.git` folder and a `.git` file both identify a repository
- [ ] #2 the walk does not enter a discovered repository's own subfolders
- [ ] #3 the skip list and the shallower `AppData` rule are honoured
- [ ] #4 depth is configurable and a rescan replaces a running scan
- [ ] #5 the scan report carries visited, found, skipped, elapsed and slow directories

## Verify

- [ ] test: a fake tree with repos, nested repos and skipped folders
- [ ] test: stop a scan and start another
- [ ] test: the report matches the fake tree
