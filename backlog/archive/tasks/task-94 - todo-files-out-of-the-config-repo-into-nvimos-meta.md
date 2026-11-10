---
id: TASK-94
title: 'todo files out of the config repo into nvimos/meta'
status: Done
assignee: []
created_date: '2026-11-10'
labels:
  - c-users-jazzo
  - cleanup-release-2026
dependencies: []
ordinal: 94000
---

## Description

todo files out of the config repo into nvimos/meta

From `legacy/todo-cleanup-release-2026.md`, section "cleanup release 2026".

## Acceptance Criteria

- [x] #1 nvimos/meta with Backlog.md and OpenSpec side by side (2026-11-10)
- [x] #2 todo-ideas.md, todo-202x.md, squash files, todo-ideas/ removed from the config, pointer left (config 35103bf)
- [x] #3 skills (auto-todo, update-todo, close-issues) and CLAUDE.md point at meta (config 35103bf)

## Final Summary

Done 2026-11-10: meta created (public), both formats, the config's todo files removed; `todo.md` in the config points here.
The PR-* branches still edit todo-ideas.md: merging them gives a modify/delete conflict; take the delete and move their notes here.

## Original notes

```markdown
- [ ] todo files out of the config repo into nvimos/meta (2026-11-10)
  - [x] nvimos/meta with Backlog.md and OpenSpec side by side (2026-11-10)
  - [ ] todo-ideas.md, todo-202x.md, squash files, todo-ideas/ removed from the config, pointer left
  - [ ] skills (auto-todo, update-todo, close-issues) and CLAUDE.md point at meta
```
