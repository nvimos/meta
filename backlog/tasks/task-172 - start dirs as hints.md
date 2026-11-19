---
id: TASK-172
title: 'start dirs as hints'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-171
ordinal: 172000
---

## Description

Add the hint layer over the crawler: genja-startdirs and `v:oldfiles` when a Neovim backend is
connected, `Prefs` recent projects when not, and the active/connected repository first. Hints order
or seed the crawl; they are not the source of truth.

Change: `openspec/changes/purrage-project-discovery/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 a hint that is a repository is promoted in the list
- [ ] #2 a hint that is not a repository or no longer exists is kept and marked stale (the view shows it greyed with Remove)
- [ ] #6 the crawl starts in the Neovim cwd when connected; otherwise the last folder used, home on a first run
- [ ] #3 the connected repository and active directory appear first
- [ ] #4 local mode works with no Neovim and no start-dirs plugin
- [ ] #5 the existing Active Directory behaviour is unchanged

## Verify

- [ ] test: hints from a fake source, some valid and some stale
- [ ] test: local mode with no Neovim still lists crawled repos
- [ ] test: connected repo is first
