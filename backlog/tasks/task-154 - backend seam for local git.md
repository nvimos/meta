---
id: TASK-154
title: 'backend seam for local git'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies: []
ordinal: 154000
---

## Description

Extract `RepoBackend` from today's `Backend` and add the optional `EditorSession` capability. The
existing implementation becomes `NvimBackend` and remains the only one; no user-visible behaviour
changes. This is the seam the local backend and the Purrage mode will use.

Change: `openspec/changes/purrage-backend-seam/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 `RepoBackend` covers every non-editor call the modes make today
- [ ] #2 `EditorSession` covers open, show, cursor and current buffer text, and is optional
- [ ] #3 `NvimBackend` implements both with the current relay calls and event stream
- [ ] #4 `Session` holds the interface, not the concrete RPC class
- [ ] #5 no mode or state class imports `Backend` directly

## Verify

- [ ] test: the existing suite passes without changed expectations
- [ ] manual: connect to relay and exercise Pull request, Changes, Tasks and Directories
- [ ] review: no behaviour or error text changed
