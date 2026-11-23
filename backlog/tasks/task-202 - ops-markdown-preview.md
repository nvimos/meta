---
id: TASK-202
title: 'ops markdown preview: rendered markdown with a Rendered / Text switch'
status: In Progress
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - ui
dependencies:
  - TASK-204
ordinal: 202000
---

## Description

ops: the preview pane shows markdown as raw text. Render it (headings, lists, tables, code), with a switch next to the Preview label to go back to the text; the switch remembers the choice. Links work like a small browser: a local markdown link opens in the preview with the mouse's back and forward buttons, a web link goes to the system. A build option (`make configure markdown=on|off`, on by default), with `flutter_markdown_plus`.

Change: `openspec/changes/ops-markdown-preview/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 a markdown file in the preview is rendered; text stays selectable
- [x] #2 a Rendered / Text switch beside the Preview label, markdown files only, remembered
- [x] #3 relative images and links resolve; a markdown link opens in the preview, back and forward walk the trail; a web link opens in the browser
- [ ] #4 checked in the app on real repo files
- [ ] #5 code blocks highlighted (with the text view, later)
<!-- AC:END -->
