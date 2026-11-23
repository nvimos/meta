---
id: TASK-207
title: 'ops AsciiDoc preview: render .adoc like markdown'
status: To Do
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - ui
dependencies:
  - TASK-202
ordinal: 207000
---

## Description

ops: AsciiDoc files (`.adoc`, `.asciidoc`) render in the preview like markdown: the same Rendered / Text switch, links that open in the preview with back and forward. Likely converted to HTML in Dart and drawn by the HTML renderer the preview already has. A build option, `make configure asciidoc=on|off`.

Change: `openspec/changes/ops-asciidoc-preview/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 an AsciiDoc file renders: sections, lists, tables, source blocks, admonitions
- [ ] #2 the Rendered / Text switch covers it
- [ ] #3 `xref:` links open in the preview with back / forward
<!-- AC:END -->
