---
id: TASK-114
title: 'skills: /close-issues follow-ups'
status: Needs Test
assignee: []
created_date: '2026-10-24'
labels:
  - skills
  - from-config
dependencies: []
ordinal: 114000
---

## Description

/close-issues (now `nvim-commit-close-issues`) writes the session's solved issues and commits them.
Since 2026-11-11 it writes them as Backlog.md tasks in nvimos-meta instead of `todo-issue/` files.

## Acceptance Criteria

- [x] #1 `.claude/skills/close-issues/SKILL.md`: one checklist file per issue, commit-plan grouping copied in, one commit per issue (dc4c987)
- [x] #2 `.gitignore`: `/.claude/*` plus `!/.claude/skills/`, so project skills are tracked
- [x] #3 `CLAUDE.md`: `todo-issue/` added to the backlog list
- [x] #4 first run: wrote this file

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: run `/close-issues` after a session with code changes and staged "not ours" files; check one commit per issue and that the staged files stay staged
- [ ] skill: when no file is split by hunk, use `git commit -- <paths>` instead of the patch, unstage, re-stage step
- [ ] skill: in a background session, write the issue files in a worktree (edits in the main checkout are blocked)

## Original notes

```markdown
- [x] 01. skills: /close-issues closes the session's issues as todo-issue/ files and commits them (2026-10-24)
    - [x] `.claude/skills/close-issues/SKILL.md`: one checklist file per issue, commit-plan grouping copied in, one commit per issue (dc4c987)
    - [x] `.gitignore`: `/.claude/*` plus `!/.claude/skills/`, so project skills are tracked
    - [x] `CLAUDE.md`: `todo-issue/` added to the backlog list
    - [x] first run: wrote this file
    - [ ] test: run `/close-issues` after a session with code changes and staged "not ours" files; check one commit per issue and that the staged files stay staged
    - [ ] skill: when no file is split by hunk, use `git commit -- <paths>` instead of the patch, unstage, re-stage step
    - [ ] skill: in a background session, write the issue files in a worktree (edits in the main checkout are blocked)
```

From `legacy/nvim-config/todo-issue/01-close-issues-skill.md`.
