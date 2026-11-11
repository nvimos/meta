---
id: TASK-18
title: 'lint: :ValeSync runs by itself when the shared styles are missing'
status: Needs Test
assignee: []
created_date: '2026-10-31'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 18000
---

## Description

lint: :ValeSync runs by itself when the shared styles are missing

- today vale is skipped until :ValeSync (lua/genja/ext/lint.lua prepare_vale), no hint that it's off
- 2026-11-02: the first lint without styles starts the sync once per session, then lints all buffers again; untested (1c67fc5)

From `todo-ideas.md`, section "ideas october".

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] try it by hand (marked untested in the notes)

## Original notes

```markdown
- [x] lint: :ValeSync runs by itself when the shared styles are missing (asked 2026-10-31)
  - today vale is skipped until :ValeSync (lua/genja/ext/lint.lua prepare_vale), no hint that it's off
  - 2026-11-02: the first lint without styles starts the sync once per session, then lints all buffers again; untested (1c67fc5)
```
