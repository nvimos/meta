---
id: TASK-178
title: 'settings and editor detection'
status: To Do
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-159
ordinal: 178000
---

## Description

Port Purrage's Settings and its editor/terminal detection: the saved editor choice, `nvim-qt` first,
`git var GIT_EDITOR`, `VISUAL`, `EDITOR`, known editors and Notepad; terminal choice and folder
opener; scan depth; prefs in Ops' `state.json`. Settings is a mode on the rail (decided). Claude
reviews the view against the UI rules before Done.

Change: `openspec/changes/purrage-mode-and-ui/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [ ] #1 a local session can open a file in the detected editor at a line
- [ ] #2 the editor choice survives a restart
- [ ] #3 the terminal launcher and folder opener work on Windows
- [ ] #4 scan depth is editable and applies to the next crawl
- [ ] #5 a missing editor is a clear message, not a crash

## Verify

- [ ] test: detection order with fake PATH/environment
- [ ] test: an unset choice falls back to the detected editor
- [ ] manual: open a file from the Add and Ignore mode and from Changes
