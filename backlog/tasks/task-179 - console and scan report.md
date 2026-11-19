---
id: TASK-179
title: 'console and scan report'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-162
  - TASK-171
ordinal: 179000
---

## Description

Port Purrage's Console view as the **Log** mode, with its report formatting: one entry per action,
its command, origin, parameters and result, plus the crawler's scan report. The snackbar's
replacement by the notice bar is TASK-187, not this task; the error pane stays. Claude reviews the
view against the UI rules before Done.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 an action adds one readable entry with its command and result
- [ ] #2 a failure opens to the full report without losing git's words
- [ ] #3 a scan adds its summary and slow/wide directory detail
- [ ] #4 the Log is selectable and scrolls
- [ ] #5 the view does not query git or the filesystem itself

## Verify

- [ ] widget test: render a success and a failure entry
- [ ] widget test: a scan report renders
- [ ] manual: perform an action, read the Log
