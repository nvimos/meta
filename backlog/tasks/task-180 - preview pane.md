---
id: TASK-180
title: 'preview pane'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-168
ordinal: 180000
---

## Description

Port Purrage's preview pane into the Add and Ignore mode only (decided 2026-11-19): its text, PDF
(`pdfrx`) and image adapters and the preview state. Changes keeps its diff and gets no preview.
Claude reviews the view against the UI rules before Done.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 the preview pane appears in the Add and Ignore mode only
- [ ] #2 a selected text file previews without changing the list
- [ ] #3 a binary or unsupported file says so
- [ ] #4 the preview does not block the UI on a large file
- [ ] #5 a PDF and an image preview through the ported adapters

## Verify

- [ ] widget test: a text preview and an unsupported file
- [ ] manual: move the cursor through mixed files
- [ ] check: no new dependency left unused
