---
id: TASK-177
title: 'projects view'
status: Needs Test
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

- [x] #1 the view lists crawled repositories, ordered by hints
- [x] #2 the active and connected repositories are marked and first
- [x] #3 a folder can be chosen as the crawl start
- [x] #4 a scan can be started and its progress/report is visible
- [x] #5 picking and opening a project keep the current behaviour

## Verify

- [x] widget test: fixture crawler, render and pick
- [x] widget test: a stale hint shows greyed, and Remove takes it away
- [ ] manual: browse a real home folder and open a repo
