---
id: TASK-155
title: 'port purrage git foundations'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies: []
ordinal: 155000
---

## Description

Port Purrage's local git foundations into Ops: `Repo`, `GitRepo`, the porcelain status parser,
`paths.dart`, `hidden_write.dart` and the `ProcessRunner`/`Env`/`DirectoryLister` seams. Add the
`git` package dependency. This is a mechanical move of proven code, not a redesign.

Change: `openspec/changes/purrage-local-git-backend/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 `Repo.open` finds the repository from a folder and reports a useful failure otherwise
- [x] #2 the status parser covers conflicts, staged, changed, untracked and rename pairs
- [x] #3 UTF-8 paths and Windows argument batching behave as in Purrage
- [x] #4 process, environment and directory listing go through the seams, so tests can fake them
- [x] #5 temp-repo tests clean up their folders and leave no git process behind

## Verify

- [x] test: parse fixture status strings for every section and code
- [x] test: open a temporary repository and read a known status
- [x] test: a fake process runner can answer status without git
