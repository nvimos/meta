---
id: TASK-193
title: 'Mark dead ignore rules in the Ignore panes'
status: To Do
assignee: []
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-191
ordinal: 193000
---

## Description

Mark lines of a `.gitignore` that can never have an effect: a negation under a folder an earlier
rule excludes (git does not look inside an excluded folder), a negation with nothing to re-include,
a duplicate line. In memory over the rules the pane already read, no git call; only shapes that can
be decided for certain.

Change: `openspec/changes/ops-dead-ignore-rules/`.
