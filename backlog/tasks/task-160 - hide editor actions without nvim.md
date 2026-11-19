---
id: TASK-160
title: 'hide editor actions without nvim'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-159
ordinal: 160000
---

## Description

When the active backend has no `EditorSession`, the editor-only UI must disappear instead of failing:
Open in Neovim, the live cursor, show-at-revision and the editor key hints. A local session should
look deliberately local, not broken.

Change: `openspec/changes/purrage-local-git-backend/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 Open in Neovim is hidden or disabled with a reason
- [ ] #2 the status bar shows no dead cursor for a local session
- [ ] #3 no key path calls a missing editor method
- [ ] #4 Pull request still opens the file when an editor is present
- [ ] #5 the same controls return when a Neovim backend is selected

## Verify

- [ ] widget test: local mode has no Open in Neovim control
- [ ] widget test: Neovim mode still has it
- [ ] manual: press the former editor keys in local mode; nothing throws
