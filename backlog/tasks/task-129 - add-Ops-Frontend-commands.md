---
id: TASK-129
title: 'ops: :Ops / :Frontend start the front end app'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - ops
  - issue
  - nvim-config
dependencies: []
ordinal: 129000
---

## Description

ops: commands that start the latest Flutter front end build connected to this nvim. Commits: config f8faa32.

## Acceptance Criteria

- [x] #1 plugin/ops.lua: :Ops and :Frontend run build/windows/x64/runner/Release/ops.exe with this nvim's address
- [x] #2 listens first if needed: relay's served address, 127.0.0.1:6666, else a free port; records it in nvimos.served
- [x] #3 readme.cheatsheet.md: Ops desktop app section

## Verify

- [ ] test: fresh nvim, :Ops: "listening on 127.0.0.1:6666", the app connects
- [ ] test: second nvim, :Ops: listens on another port, its app connects
- [ ] test: without a build: "no build at ..." error
