---
id: TASK-161
title: 'read-only local mode integration'
status: To Do
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

- [ ] #1 Pull request lists branches, commits and a diff for a local repo
- [ ] #2 Changes lists staged, changed and untracked rows without an editor
- [ ] #3 Tasks reads the local planning folder and its `.nvimos` tracking
- [ ] #4 the same repository through Neovim still gives the same models
- [ ] #5 a refresh after a local edit shows the new state
- [ ] #6 an edit made outside Ops reaches the views through the repository watcher (TASK-186)
- [ ] #7 the Tasks changed-paths hint has a local value instead of staying empty

## Verify

- [ ] test: a temp repo drives all three modes through LocalBackend
- [ ] test: the Neovim backend still passes its mode tests
- [ ] manual: open a real checkout locally and compare the list to `git status`
