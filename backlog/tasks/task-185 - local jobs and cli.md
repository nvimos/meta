---
id: TASK-185
title: 'local jobs and cli'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-155
ordinal: 185000
---

## Description

Implement the local `startJob`, `cancelJob` and `cli` calls so Tasks can start an agent, show its
progress, cancel it, and run `openspec archive` without a Neovim process.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 a local job starts, streams or collects output, and reports its end
- [ ] #2 cancel stops the process and emits the same job event shape
- [ ] #3 `cli` runs a command in the planning folder and returns exit code, stdout and stderr
- [ ] #4 a job keeps running when the app closes, as the relay's detached jobs do
- [ ] #5 a failed start is an error result, not a hung job

## Verify

- [ ] test: a short local job reaches finished with its output
- [ ] test: cancel ends a long job
- [ ] test: `cli('openspec', ['--version'])` returns a result
