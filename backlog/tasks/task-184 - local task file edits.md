---
id: TASK-184
title: 'local task file edits'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-157
  - TASK-162
ordinal: 184000
---

## Description

Implement the local `setLines`, `create` and `move` operations that the Tasks mode uses for status,
priority, checkbox, archive and new-change writes. The relay guards changes through loaded buffers;
the local implementation needs the same expect-check against the file on disk.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 `setLines` replaces ranges and honours the expected old lines
- [x] #2 a file changed since it was read is refused, not overwritten
- [x] #3 `create` writes a new file and refuses an existing one
- [x] #4 `move` handles a file and a folder into the archive
- [x] #5 line endings and the final newline are preserved

## Verify

- [x] test: edit a task's status and read the file back
- [x] test: an expected-lines mismatch is refused
- [x] test: create and move in a temp planning folder
