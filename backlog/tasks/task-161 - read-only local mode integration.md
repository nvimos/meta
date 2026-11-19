---
id: TASK-161
title: 'read-only local mode integration'
status: Needs Test
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-156
  - TASK-157
  - TASK-159
  - TASK-186
ordinal: 161000
---

## Description

Make Pull request, Changes and Tasks load a local repository with the read-only backend. Align model
mismatches between the ported git code and Ops' models; do not add actions yet. This is the proof
that the local path works end to end.

Change: `openspec/changes/purrage-local-git-backend/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 Pull request lists branches, commits and a diff for a local repo
- [x] #2 Changes lists staged, changed and untracked rows without an editor
- [x] #3 Tasks reads the local planning folder and its `.nvimos` tracking
- [x] #4 the same repository through Neovim still gives the same models
- [x] #5 a refresh after a local edit shows the new state
- [x] #6 an edit made outside Ops reaches the views through the repository watcher (TASK-186)
- [x] #7 the Tasks changed-paths hint has a local value instead of staying empty

## Verify

- [x] test: a temp repo drives all three modes through LocalBackend
- [x] test: the Neovim backend still passes its mode tests
- [ ] manual: open a real checkout locally and compare the list to `git status`
