---
id: TASK-183
title: 'verify the integration end to end'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-169
  - TASK-170
  - TASK-174
  - TASK-175
  - TASK-176
  - TASK-177
  - TASK-178
  - TASK-179
  - TASK-180
  - TASK-181
  - TASK-182
  - TASK-184
  - TASK-185
  - TASK-186
  - TASK-187
ordinal: 183000
---

## Description

Close the programme: verify the five proposals' acceptance criteria on a real checkout and with the
Neovim backend, and record what remains open. This is the integration gate, not a feature task.

Change: all five `openspec/changes/purrage-*` proposals.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 a local folder opens, reads, triages, commits and browses with no Neovim
- [ ] #2 the same folder works through the Neovim backend, including open/show
- [ ] #3 the Add and Ignore mode and Ops Changes do not duplicate state or actions
- [ ] #4 Tasks edits, archives and starts a local job without Neovim
- [ ] #5 the key table, Help, README and `PLAN.md` describe the final app
- [ ] #6 every remaining issue is recorded as a task or an open question

## Verify

- [ ] test: the whole suite on a clean `%TEMP%`
- [ ] manual: local and Neovim walks on the same repository
- [ ] review: the five proposals' acceptance criteria are ticked or explained
