---
id: TASK-177
title: 'projects view'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-173
ordinal: 177000
---

## Description

Build the Repos view over the crawler and hint state: the starting directory, drives and folders,
the repository rows, the active/connected marker and the actions to pick or open one. This replaces
the old Directories list presentation and folds in Purrage's Browse view: one view, not two.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 the view lists crawled repositories, ordered by hints
- [ ] #2 the active and connected repositories are marked and first
- [ ] #3 a folder can be chosen as the crawl start
- [ ] #4 a scan can be started and its progress/report is visible
- [ ] #5 picking and opening a project keep the current behaviour

## Verify

- [ ] widget test: fixture crawler, render and pick
- [ ] widget test: a stale hint shows greyed, and Remove takes it away
- [ ] manual: browse a real home folder and open a repo
