---
id: TASK-145
title: 'refuse merge on unsaved buffers'
status: To Do
assignee: []
created_date: '2026-11-14'
labels:
  - backend
dependencies:
  - TASK-143
ordinal: 145000
---

## Description

A buffer with unsaved changes on a file the merge changes must never be overwritten. Merge refuses up
front and names the path and the buffer number, so Ops can offer to open that buffer in a new tab
(TASK-147).

Change: `openspec/changes/merge-beside-checkout/` ("The merge changes a file with unsaved changes in
Neovim").

## Acceptance Criteria

- [ ] #1 the check runs before anything moves and covers every modified buffer on a merged file
- [ ] #2 the refusal carries the path and the buffer number

## Verify

- [ ] manual: unsaved edit in a buffer on a file the merge changes: refused, path and buffer number shown, nothing moved
