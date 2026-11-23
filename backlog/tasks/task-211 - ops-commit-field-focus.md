---
id: TASK-211
title: 'ops commit field focus: typing after cc keeps only the first letter'
status: Done
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - bug
  - accessibility
dependencies: []
ordinal: 211000
---

## Description

ops: in Changes, `cc` and a burst of typing left only the first letter in the commit field; the field lost the keyboard a frame later. The X that appears with the first letter gave the field a new semantics node, the Windows accessibility bridge sent the old one "lost accessibility focus", and a Material TextField on Windows unfocuses on that.

Change: `openspec/changes/ops-commit-field-focus/` (approved; debugging notes in `debugging.md`)

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 the cause is found and written down, with how it was found
- [x] #2 the buttons inside the commit field and `ClearButton` are their own semantics node; tests running as Windows keep the field's focused node after the first letter
- [x] #3 verified in `make live`: `cc` and a quick burst land every letter in the field (a filter field not checked by hand yet)
- [x] #4 the temporary commit trace is removed
<!-- AC:END -->
