---
id: TASK-184
title: 'local task file edits'
status: To Do
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

- [ ] #1 `setLines` replaces ranges and honours the expected old lines
- [ ] #2 a file changed since it was read is refused, not overwritten
- [ ] #3 `create` writes a new file and refuses an existing one
- [ ] #4 `move` handles a file and a folder into the archive
- [ ] #5 line endings and the final newline are preserved

## Verify

- [ ] test: edit a task's status and read the file back
- [ ] test: an expected-lines mismatch is refused
- [ ] test: create and move in a temp planning folder
