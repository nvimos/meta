---
id: TASK-157
title: 'local files and tracking'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-154
  - TASK-155
  - TASK-158
ordinal: 157000
---

## Description

Implement the file half of `LocalBackend`: list files under the planning folders, read file text, and
parse `.nvimos` tracking directly from disk. Missing files and missing folders are normal answers, not
errors.

Change: `openspec/changes/purrage-local-git-backend/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 `listFiles` walks the requested dirs and returns repo-relative paths
- [ ] #2 `readFiles` returns existing text and an explicit missing answer
- [ ] #3 `.nvimos` tracking resolves `~`, absolute and relative paths like the relay
- [ ] #4 a malformed `.nvimos` does not crash the Tasks load
- [ ] #5 paths use forward slashes at the app boundary

## Verify

- [ ] test: list and read a temp planning folder with nested files
- [ ] test: `.nvimos` with no file, with a valid tracking dir and with a missing dir
- [ ] test: a non-UTF-8 file does not take the app down
