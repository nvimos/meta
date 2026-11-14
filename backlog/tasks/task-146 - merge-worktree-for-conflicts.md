---
id: TASK-146
title: 'merge worktree for conflicts'
status: To Do
assignee: []
created_date: '2026-11-14'
labels:
  - backend
dependencies:
  - TASK-143
ordinal: 146000
---

## Description

A merge with conflicts waits in a worktree of Ops's own, never in the main checkout. One per PR
branch, in `%TEMP%\nvimos-ops\merge.<repo>.<branch>` (`/` in the branch becomes `-`), on a
detached HEAD at the old base. After the conflict is resolved and committed there, base moves to the merge
commit (update-ref with the old value) and the main checkout is brought forward (TASK-144). The
worktree is removed once the merge is committed or thrown away; a folder deleted from temp is
pruned and made again.

Change: `openspec/changes/merge-beside-checkout/` ("The merge has conflicts", "A merge with
conflicts, in the merge worktree").

## Acceptance Criteria

- [ ] #1 the worktree is made on a conflict, at the path above, detached at the old base
- [ ] #2 commit there moves base; abort throws it away; both remove the worktree
- [ ] #3 a worktree folder deleted by hand is pruned and made again

## Verify

- [ ] manual: conflicting merge: main checkout free of markers, base not moved, the conflict in the merge worktree
- [ ] manual: resolve and commit in the merge worktree: base moves, the worktree is gone
- [ ] manual: throw the conflict away: base unchanged, the worktree is gone
