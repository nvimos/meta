---
id: TASK-182
title: 'remove purrage handoff'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-159
  - TASK-175
  - TASK-177
ordinal: 182000
---

## Description

Remove the separate-app hand-off now that Ops owns the local workflow: Purrage's `OpsLauncher`, the
“open this folder in Ops” path, and the stale docs that describe Ops as needing Neovim for local
work. Update the README and `PLAN.md` where they name the old flow. The Purrage repository is
frozen from stage 0 (bug fixes only); this task adds a README note pointing to Ops, and the user
archives it after TASK-183.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 no Ops launch path remains in Purrage's code or docs
- [x] #2 Ops' README explains the recent list (folders and Neovim addresses) and the Add and Ignore mode
- [x] #6 Purrage's README says it is frozen and points to Ops
- [x] #3 `PLAN.md` names the final modes and the optional Neovim backend
- [x] #4 no dead link to the old hand-off remains
- [x] #5 the docs do not claim Neovim is required for local use

## Verify

- [x] check: `rg OpsLauncher` and the old hand-off text return nothing
- [x] manual: follow the README from a clean local folder
- [x] review: no implementation change hidden in this task
