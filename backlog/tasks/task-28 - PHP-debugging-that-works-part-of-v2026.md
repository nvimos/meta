---
id: TASK-28
title: 'PHP debugging that works, part of v2026'
status: Needs Test
assignee: []
created_date: '2026-11-05'
labels:
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 28000
---

## Description

PHP debugging that works, part of v2026

- keep nvim-dap + nvim-dap-ui unless the UI test says otherwise; compare nvim-dap-view
- PHP runs in DDEV inside WSL (weasel-ddev): Xdebug networking and pathMappings untested
- session, gaps and questions: todo-test/php-debug.md
      `<leader>dK` `dl` `dB` `dp` (17e6c2b); nvim-dap-view on `<leader>dv` (8f5b8d2); untested

From `todo-ideas.md`, section "ideas october".

## Acceptance Criteria

- [x] #1 dap-ui on the first stop in its own tab, `!` flips F1-F8, :DdevXdebugHost, :DebugCli / :DebugBehat,

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] try it by hand (marked untested in the notes)

## Original notes

```markdown
- [ ] PHP debugging that works, part of v2026 (2026-11-05)
  - keep nvim-dap + nvim-dap-ui unless the UI test says otherwise; compare nvim-dap-view
  - PHP runs in DDEV inside WSL (weasel-ddev): Xdebug networking and pathMappings untested
  - session, gaps and questions: todo-test/php-debug.md
  - [x] dap-ui on the first stop in its own tab, `!` flips F1-F8, :DdevXdebugHost, :DebugCli / :DebugBehat,
        `<leader>dK` `dl` `dB` `dp` (17e6c2b); nvim-dap-view on `<leader>dv` (8f5b8d2); untested
```
