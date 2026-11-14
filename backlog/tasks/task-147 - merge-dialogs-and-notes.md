---
id: TASK-147
title: 'merge dialogs and notes in ops'
status: To Do
assignee: []
created_date: '2026-11-14'
labels:
  - frontend
  - ops
dependencies:
  - TASK-144
  - TASK-145
  - TASK-146
ordinal: 147000
---

## Description

The Ops side of merging beside the checkout. `PrState.canMerge` and `PrState.merge`
(`lib/state/pr.dart`) stop refusing a dirty main checkout as a whole. `lib/ui/pr_view.dart` gains:

- the dialog for files the merge changes that have uncommitted edits: the files, and stash, apply,
  pop (default), discard modified files, move main only, refuse
- the unsaved-buffer refusal with the path, the buffer number and a button that opens the buffer in
  a new tab
- the notes: merged, stopped on a conflict (where it waits, open it or throw it away), base moved
  during the merge

Change: `openspec/changes/merge-beside-checkout/`.

## Acceptance Criteria

- [ ] #1 Merge no longer refuses a dirty main checkout as a whole
- [ ] #2 the overlap dialog lists the files and offers the choices, pop the default
- [ ] #3 the unsaved-buffer note opens the buffer in a new tab
- [ ] #4 the conflict note says where the conflict waits and offers open and throw away

## Verify

- [ ] manual: merge touching a file with uncommitted edits: the dialog lists it; each choice does what it says
- [ ] manual: unsaved buffer on a merged file: the note shows the buffer number; the button opens it in a new tab
- [ ] manual: conflict: the note opens the merge worktree's file
