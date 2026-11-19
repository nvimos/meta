---
id: TASK-173
title: 'directories over the crawler'
status: To Do
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-171
  - TASK-172
ordinal: 173000
---

## Description

Rework the Directories state, renamed Repos, so it is a view over the crawler plus hints, not a list
supplied only by genja-startdirs. Keep Active Directory, picking and opening the project; no view
yet. A stale hint can be removed from the state.

Change: `openspec/changes/purrage-project-discovery/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 the list is the crawl result ordered by the hints
- [ ] #2 picking a directory still makes it the Active Directory
- [ ] #3 opening a project still chooses the first mode with work
- [ ] #4 no Neovim connection is required for the list
- [ ] #5 the start-dirs backend call is optional, not required

## Verify

- [ ] test: state with fake crawler and fake hints
- [ ] test: pick and open with no Neovim
- [ ] test: connected hints reorder without dropping crawl results
