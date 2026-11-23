---
id: TASK-195
title: 'ops release promote: prerelease first, promote a tested build'
status: To Do
assignee: []
created_date: '2026-11-19'
labels:
  - ops
  - ci
dependencies: []
ordinal: 195000
---

## Description

ops: release builds (weekly CI, `make release`) publish as prereleases; a manual promote workflow makes a tested one the Latest release, without building again.

Change: `openspec/changes/ops-release-promote/`

## Acceptance Criteria

- [ ] #1 CI and `make release` publish prereleases
- [ ] #2 a promote workflow (and `make promote TAG=`) marks a prerelease Latest
- [ ] #3 promote refuses a tag that is not a prerelease
