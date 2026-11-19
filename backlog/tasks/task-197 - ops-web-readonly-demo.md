---
id: TASK-197
title: 'ops web demo: the app in the browser on a fake repo (draft, to discuss)'
status: To Do
assignee: []
created_date: '2026-11-19'
labels:
  - ops
  - frontend
  - web
dependencies: []
ordinal: 197000
---

## Description

ops: a static web build of Ops as a demo, no install. A fake `RepoBackend` in Dart runs every mode on a baked-in demo repo and this project's planning; writes are mocked in browser storage and never reach a remote. Draft: the proposal lists open questions to talk through before building.

Change: `openspec/changes/ops-web-readonly-demo/`

## Acceptance Criteria

- [ ] #1 open questions in the proposal answered
- [ ] #2 the web build runs on a static host with the demo repo and the planning snapshot
- [ ] #3 stage, commit, merge with conflicts and ignore work against the fake repo, kept in browser storage, with Reset
