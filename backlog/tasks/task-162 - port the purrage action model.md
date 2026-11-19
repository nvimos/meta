---
id: TASK-162
title: 'port the purrage action model'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-156
  - TASK-188
ordinal: 162000
---

## Description

Port Purrage's action discipline into Ops' state layer: the serialized action queue, optimistic row
changes, `ActionResult`, `ActionFailure`, notices and the Log/report data. Keep the action code
free of widgets. Build it on the shared status store and action queue interface from TASK-188; do
not redesign that interface here (raise a Handoff entry instead).

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 actions run one at a time in a queue
- [x] #2 an optimistic row change can be undone without touching another action's rows
- [x] #3 a pending action suppresses a stale refresh
- [x] #4 every result carries action, origin, command, parameters and changed count
- [x] #5 failure text keeps git's own words and the command line

## Verify

- [x] test: two queued actions finish in order
- [x] test: a failure restores only its own rows
- [x] test: a refresh during a pending action does not flicker the list back
