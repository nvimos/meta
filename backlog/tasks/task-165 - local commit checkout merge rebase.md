---
id: TASK-165
title: 'local commit checkout merge rebase'
status: To Do
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

- [ ] #1 commit uses `git commit -F -` and returns the new HEAD
- [ ] #2 checkout with stash preserves and restores local changes
- [ ] #3 checkout with force discards them only when asked
- [ ] #4 merge and rebase return the new sha or the up-to-date marker
- [ ] #5 failures keep git's message and leave no half-finished state of our making
- [ ] #6 a conflicting merge is aborted and reported; the worktree conflict flow stays on Neovim for now

## Verify

- [ ] test: commit in a temp repo, read the message back
- [ ] test: checkout with a dirty tree, both stash and force
- [ ] test: a clean merge and an up-to-date rebase
