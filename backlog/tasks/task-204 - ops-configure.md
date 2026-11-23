---
id: TASK-204
title: 'ops configure: make configure pdf=on markdown=off for the build options'
status: Done
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - build
dependencies: []
ordinal: 204000
---

## Description

ops: one `make configure` step for the build options, in the spirit of `./configure`: `make configure pdf=on markdown=off`; without options it prints the configuration. It writes `pubspec_overrides.yaml` and replaces the `pdf-on` / `pdf-off` / `pdf-status` targets. Markdown rendering (TASK-202) is built on top of it.

Change: `openspec/changes/ops-configure/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 `make configure` sets pdf and markdown, keeps what is left out, prints the configuration without options
- [x] #2 `make release` configures what it ships first
- [x] #3 the old pdf targets and `tool/pdf.ps1` are gone; docs name `make configure`
<!-- AC:END -->
