---
id: TASK-206
title: 'ops HTML webview: show HTML pages with the real engine (WebView2)'
status: To Do
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - ui
dependencies:
  - TASK-202
ordinal: 206000
---

## Description

ops: the preview draws HTML without a browser (tags, basic CSS, no scripts). For real pages (built sites, script-driven reports) show them with WebView2, the Edge engine Windows 11 ships, as a build option. Fixed height, keys and focus, overlays and security are the work.

Change: `openspec/changes/ops-html-webview/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 a local HTML page shows as Edge draws it, in the preview
- [ ] #2 scripts off and no network unless allowed; links go through the app's back / forward
- [ ] #3 `make configure webview=on|off`; the light renderer stays when off
<!-- AC:END -->
