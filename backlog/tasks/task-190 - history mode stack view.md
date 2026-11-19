---
id: TASK-190
title: 'history mode stack view'
status: To Do
assignee: []
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - history
dependencies:
  - TASK-186
  - TASK-181
ordinal: 190000
---

## Description

Build the History mode's first view, Stack (the 4th entry of the final rail, today a "not built yet"
note): the local branches as a tree by ancestry and the `Stacked-On:` trailer, the merge order, the
worktrees and the agents' task state, with review, merge next and restack, live on the repository
watcher (TASK-186). Not part of the Purrage programme; the rail entry was reserved by it.

Change: `openspec/changes/history-mode/`.

## Acceptance Criteria

- [ ] #1 the Stack view draws the branches, their state and their order from git alone
- [ ] #2 a row opens in Pull request against its parent; `m` toggles the base
- [ ] #3 merge next (fast-forward only) and restack (stops at the first conflict) work, with the old tips tagged
- [ ] #4 the view follows ref changes from the repository watcher, no timer

## Verify

- [ ] test: fixture repositories for a straight stack, a diverged trailer and a rewritten parent
- [ ] manual: a stack of three branches in worktrees
