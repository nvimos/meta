---
id: TASK-163
title: 'local file stage and discard'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-162
ordinal: 163000
---

## Description

Implement whole-file local actions behind `RepoBackend`: stage, unstage and discard, including
deletions. Use one batched git call per action where Windows argument limits allow it, and the
action model from TASK-162.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 stage and unstage move whole files between sections
- [x] #2 discard restores a tracked file and removes an untracked one safely
- [x] #3 a deleted file stages its deletion
- [x] #4 a failure restores exactly the affected rows
- [x] #5 the Neovim backend's file actions are unchanged

## Verify

- [x] test: stage, unstage and discard in a temp repo
- [x] test: a missing path and a permission failure produce the expected report
- [x] test: the action queue stays ordered
