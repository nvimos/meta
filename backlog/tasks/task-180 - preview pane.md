---
id: TASK-180
title: 'preview pane'
status: Needs Test
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-168
  - TASK-175
ordinal: 180000
---

## Description

Port Purrage's preview pane into the Add and Ignore mode only (decided 2026-11-19): its text, PDF
(`pdfrx`) and image adapters and the preview state. Changes keeps its diff and gets no preview.
Claude reviews the view against the UI rules before Done.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 the preview pane appears in the Add and Ignore mode only
- [x] #2 a selected text file previews without changing the list
- [x] #3 a binary or unsupported file says so
- [x] #4 the preview does not block the UI on a large file
- [x] #5 a PDF and an image preview through the ported adapters

## Verify

- [x] widget test: a text preview and an unsupported file
- [ ] manual: move the cursor through mixed files
- [x] check: no new dependency left unused
