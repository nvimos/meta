---
id: TASK-153
title: 'finish a resolved merge: commit in the merge worktree, move base with a guard'
status: To Do
assignee: []
created_date: '2026-11-15'
labels:
  - backend
dependencies:
  - TASK-152
  - TASK-144
ordinal: 153000
---

## Description

After verify passes, the commit in the merge worktree completes the merge (a merge commit on the
detached base). Base then moves with `git update-ref refs/heads/<base> <merge-sha> <old-base>`, which
fails and keeps the merge pending if base moved since the merge started. When base is the branch checked
out in the main checkout, the folder is brought forward as in TASK-144. The merge worktree is removed
once the merge is committed or thrown away. The outcome is a merge on `main` for now; the two alternatives
(an extra commit on the branch being merged, or a diff applied to the branch with `main` untouched) are
written in PLAN.md and not built here.

Change: `openspec/changes/merge-conflict-view/` ("Everything resolved", "Main moved while I was
resolving", "How it works in git").

## Acceptance Criteria

- [ ] #1 a verified resolution commits in the merge worktree and moves base to the merge commit
- [ ] #2 base moved since the merge started: the update fails, base keeps its new commit, nothing is lost
- [ ] #3 the merge worktree is removed after commit or after abort
- [ ] #4 a clean merge (no view) still moves base and leaves no worktree behind

## Verify (by hand)

- [ ] #V1 resolve and commit: `git log --oneline -1 main` shows the merge commit with two parents
- [ ] #V2 commit `main` in another worktree during the resolve, then commit: refused, `main` keeps that commit
- [ ] #V3 `git worktree list` shows no `merge.` worktree after the commit or after abort
- [ ] #V4 `%TEMP%\nvimos-ops` has no leftover `merge.*` folder after a run
