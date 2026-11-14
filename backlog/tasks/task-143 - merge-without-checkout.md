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
moved in the meantime is not overwritten and the user is asked to merge again.

This is the fallback path: it is used only where today's Merge would refuse (base checked out and
dirty) or would switch the main checkout to another branch. A clean main checkout on base merges as
today. The backend (`git.merge` in relay, branch `PR-merge-action`) runs the commands.

Change: `openspec/changes/merge-beside-checkout/` (sections "A clean merge, without a work tree" and
"Main moved while I was deciding").

## Acceptance Criteria

- [ ] #1 merge-tree, commit-tree and update-ref with the old value, in `git.merge`
- [ ] #2 used only where today's Merge would refuse or switch the main checkout's branch
- [ ] #3 base moved during the merge: nothing saved, the result says to merge again
- [ ] #4 `main` checked out in an agent's worktree: that worktree is left alone

## Verify

- [ ] manual: clean main checkout on base: Merge works as before
- [ ] manual: main checkout on another branch: merging into `main` leaves the branch, files and buffers alone
- [ ] manual: commit to `main` while the merge question is open, then confirm: no merge commit, a note to merge again
- [ ] check: the merge commit runs no hooks (`commit-tree`); decide if that matters
