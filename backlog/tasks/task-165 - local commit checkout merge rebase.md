---
id: TASK-165
title: 'local commit checkout merge rebase'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-162
ordinal: 165000
---

## Description

Implement the remaining local git actions: commit from the staged index, checkout with stash/force,
merge and rebase with the same results and messages as the relay backend.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 commit uses `git commit -F -` and returns the new HEAD
- [x] #2 checkout with stash preserves and restores local changes
- [x] #3 checkout with force discards them only when asked
- [x] #4 merge and rebase return the new sha or the up-to-date marker
- [x] #5 failures keep git's message and leave no half-finished state of our making
- [x] #6 a conflicting merge is aborted and reported; the worktree conflict flow stays on Neovim for now

## Verify

- [x] test: commit in a temp repo, read the message back
- [x] test: checkout with a dirty tree, both stash and force
- [x] test: a clean merge and an up-to-date rebase
