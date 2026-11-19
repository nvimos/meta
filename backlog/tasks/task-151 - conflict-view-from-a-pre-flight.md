---
id: TASK-151
title: 'conflict view from a pre-flight merge check'
status: To Do
assignee: []
created_date: '2026-11-15'
labels:
  - frontend
  - backend
dependencies:
  - TASK-146
  - TASK-150
ordinal: 151000
---

## Description

Clicking Merge runs `git merge-tree --write-tree --name-only --messages <base> <head>` first. With no
conflict, the merge runs as before. With conflicts, the merge does not run: the conflict view opens, a
third diff mode beside unified and side-by-side, listing the conflicted files. Each conflict hunk shows
ours and theirs, and a pick takes either side for that hunk (Meld-style). A conflicted file can be opened
in a new nvim-qt instance on that file, not in diff mode. Resolving happens in the merge worktree from
TASK-146, never in the main checkout. Resolve re-runs the pre-flight before the view opens.

Change: `openspec/changes/merge-conflict-view/` (proposal and spec, "A conflict opens the conflict view",
"Pick either side per hunk", "Open a conflicted file in nvim", "Re-check on Resolve").

## Acceptance Criteria

- [ ] #1 Merge with a conflict opens the conflict view and does not run the merge; base does not move
- [ ] #2 Merge with no conflict runs the plain merge with no view opened
- [ ] #3 each conflict hunk shows ours and theirs, and a pick writes that side for that hunk only
- [ ] #4 "open in nvim" starts a new nvim-qt instance on the conflicted file
- [ ] #5 Resolve re-runs the pre-flight; a conflict gone since the dialog gives a plain merge and says so

## Verify (by hand)

- [ ] #V1 on a repo with `config/routes.yaml` changed on both branches, Merge opens the view on that file
- [ ] #V2 pick theirs for one hunk, ours for another; the preview shows both picks, the other hunks unchanged
- [ ] #V3 `git status` and `git branch` in the main checkout are unchanged after the view opens
- [ ] #V4 commit `main` in another worktree, then click Resolve: the view reflects the new state
