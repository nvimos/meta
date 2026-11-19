---
id: TASK-167
title: 'local files trash and hidden write'
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
ordinal: 167000
---

## Description

Port the local file operations needed by the Purrage mode: the file manager, trash/delete and the
Windows hidden/system repair. The app must never delete a file permanently when the trash can take
it.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 trash/delete handles files and folders
- [ ] #2 a failed delete restores the rows and reports why
- [ ] #3 a hidden or system dot file can be written and restored
- [ ] #4 no operation follows a link out of the repository
- [ ] #5 platform paths use the existing `paths.dart` conventions

## Verify

- [ ] test: delete a temp file through the trash seam
- [ ] test: write a file with the hidden attribute and read it back
- [ ] manual: delete a folder in a real checkout, confirm it is recoverable
