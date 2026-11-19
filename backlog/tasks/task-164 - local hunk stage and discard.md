---
id: TASK-164
title: 'local hunk stage and discard'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-163
ordinal: 164000
---

## Description

Implement hunk-level stage, unstage and discard on the local backend. Port the patch building and
`git apply` handling from relay, using Ops' existing `Hunk`/`DiffFile` models.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 stage and unstage a hunk in a file with several hunks
- [ ] #2 discard a hunk without touching the other hunks
- [ ] #3 a context mismatch refuses the action and reports why
- [ ] #4 the same file staged through the Neovim backend behaves the same
- [ ] #5 no whole-file write loses data on failure

## Verify

- [ ] test: multi-hunk temp repo, stage the middle hunk, inspect the index
- [ ] test: discard one hunk, keep the other changes
- [ ] test: a stale hunk is refused
