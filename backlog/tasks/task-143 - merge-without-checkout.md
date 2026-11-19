---
id: TASK-143
title: 'clean merge without a checkout'
status: To Do
assignee: []
created_date: '2026-11-14'
labels:
  - backend
dependencies: []
ordinal: 143000
---

## Description

Merge a PR branch into base in git's object store, without a work tree: `git merge-tree --write-tree`,
`git commit-tree` with both parents, then `git update-ref` with the old value of base, so a base that
moved in the meantime is not overwritten.

The clean path is used when base is not the branch checked out in the main checkout. When base is
checked out, Merge works as today. Hooks on the merge commit do not matter (`commit-tree` runs none).

When base moved during the merge, nothing is saved and Ops offers to rebase head onto the new base,
then merge it. Rebase is the strong preference (decided 2026-11-15): the history of base stays one
straight line. The user confirms the offer; it does not run by itself. The
backend (`git.merge` in the relay, branch `PR-merge-action`) runs the commands.

Change: `openspec/changes/merge-beside-checkout/` (sections "A clean merge, without a work tree" and
"Main moved while I was deciding").

## Acceptance Criteria

- [ ] #1 merge-tree, commit-tree and update-ref with the old value, in `git.merge`
- [ ] #2 used only when base is not the branch checked out in the main checkout
- [ ] #3 base moved during the merge: nothing saved, Ops offers to rebase head onto the new base, then merge
- [ ] #4 `main` checked out in an agent's worktree: that worktree is left alone

## Verify

- [ ] manual: clean main checkout on base: Merge works as before
- [ ] manual: main checkout on another branch: merging into `main` leaves the branch, files and buffers alone
- [ ] manual: commit to `main` while the merge is running: no merge commit, the offer to merge again appears
- [ ] manual: accept the offer: head is rebased onto the new `main`, then merged; `main` history is linear
