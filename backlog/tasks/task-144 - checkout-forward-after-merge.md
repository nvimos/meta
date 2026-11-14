---
id: TASK-144
title: 'bring the checkout forward after a merge'
status: To Do
assignee: []
created_date: '2026-11-14'
labels:
  - backend
dependencies:
  - TASK-143
ordinal: 144000
---

## Description

When base is the branch checked out in the main checkout, bring the folder forward to the new base
after the merge with `git read-tree -m -u "$old" "$commit"`, changing only the files the merge
changed, and then reload Neovim buffers on those files (`:checktime`).

Before anything moves, compare the files the merge changes with the files that have uncommitted
changes. On an overlap, Ops shows a dialog listing those files (TASK-147) and the backend does the
choice: stash, apply, pop (default; `git stash push -- <files>`, bring forward, `git stash pop
--index`, the stash kept if it ends in markers), discard the modified files, move main only, or
refuse.

Change: `openspec/changes/merge-beside-checkout/` ("Bringing the main checkout forward", "The merge
changes a file I am editing").

## Acceptance Criteria

- [ ] #1 `read-tree -m -u` from the old to the new base when base is checked out in the main checkout
- [ ] #2 overlapping files are found before anything moves
- [ ] #3 the four choices on an overlap: stash/apply/pop, discard, move main only, refuse
- [ ] #4 buffers on merged files are reloaded

## Verify

- [ ] manual: uncommitted edits in other files, merge into checked-out `main`: edits kept, merged files on disk
- [ ] manual: stash, apply, pop with overlapping lines: markers in the file, the stash kept
- [ ] manual: each of discard, move main only and refuse does what it says
- [ ] manual: an open buffer on a merged file shows the merged text
