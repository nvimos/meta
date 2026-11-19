---
id: TASK-169
title: 'local actions in ops changes'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-163
  - TASK-164
  - TASK-165
ordinal: 169000
---

## Description

Wire the local actions into Ops Changes so stage, unstage, discard (file and hunk), commit, checkout,
merge and rebase work against `LocalBackend`. Keep the existing optimistic behaviour and the Neovim
path intact; do not duplicate the action model.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 every Changes action works on a local repository
- [ ] #2 a click changes the rows at once and git confirms after
- [ ] #3 a failure restores the previous rows and shows the report
- [ ] #4 the Neovim backend still performs the same actions
- [ ] #5 no action calls the concrete backend class
- [ ] #6 the Purrage mode and Changes share the status-list/action state, or a named base, instead of two copies

## Verify

- [ ] test: stage and discard a file in a temp local repo
- [ ] test: commit the staged index from Changes
- [ ] manual: the same flow against Neovim
