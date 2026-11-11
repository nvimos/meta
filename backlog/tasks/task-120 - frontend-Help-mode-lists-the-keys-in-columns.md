---
id: TASK-120
title: 'frontend: Help mode lists the keys in columns'
status: Needs Test
assignee: []
created_date: '2026-11-11'
labels:
  - frontend
dependencies: []
ordinal: 120000
---

## Description

The key list was one long column. It now fills the pane in columns about 360 px wide, groups in
order, columns of even height, so every key fits on one screen.

## Acceptance Criteria

- [x] #1 `splitColumns` (lowest tallest column, order kept) and a LayoutBuilder in `lib/ui/help_view.dart`
- [x] #2 `test/help_view_test.dart`: the split, and every group visible at 1600x900

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] `?` on a wide window: all keys on one screen
- [ ] a narrow window: fewer columns, it scrolls
