---
id: TASK-186
title: 'local repository watcher'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-154
  - TASK-156
ordinal: 186000
---

## Description

Without relay there is no git hint, so a local session must watch the repository itself (decided
2026-11-19: watch from the start, no timer). One debounced watcher on the worktree and on `.git`
(`index`, `HEAD`, `refs/`, `packed-refs`, and each worktree's `HEAD` and `index`) raises the same git
change signal `RepoBackend` emits for the Neovim backend. The History mode's refs watcher
(`openspec/changes/history-mode/`) is this watcher, not a second one.

Change: `openspec/changes/purrage-local-git-backend/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 an edit made outside Ops reaches the views without a manual refresh
- [ ] #2 a burst of changes (a checkout, a rebase) produces one refresh, not one per file
- [ ] #3 `.git/objects` churn and ignored build trees do not trigger refreshes
- [ ] #4 the watcher stops when the session closes or switches backend
- [ ] #5 the History mode can subscribe to ref changes from the same watcher

## Verify

- [ ] test: write a file in a temp repo, the change signal fires once after the debounce
- [ ] test: closing the session leaves no watcher running
- [ ] manual: `git commit` in a terminal shows up in Changes
