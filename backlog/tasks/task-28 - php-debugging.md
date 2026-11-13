---
id: TASK-28
title: 'php debugging'
status: Needs Test
assignee: []
created_date: '2026-11-05'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
  - todo-2026-neovim011
  - release-v2026
dependencies: []
ordinal: 28000
---

## Description

PHP debugging that works, part of v2026

- keep nvim-dap + nvim-dap-ui unless the UI test says otherwise; compare nvim-dap-view
- PHP runs in DDEV inside WSL (weasel-ddev): Xdebug networking and pathMappings untested
- session, gaps and questions: `backlog/docs/doc-8 - php-debug.md`
      `<leader>dK` `dl` `dB` `dp` (17e6c2b); nvim-dap-view on `<leader>dv` (8f5b8d2); untested

From `todo-ideas.md`, section "ideas october".
- v2026 release checklist item 7 (was TASK-47): PHP debugging works in DDEV/WSL, UI chosen: `backlog/docs/doc-8 - php-debug.md`

## Acceptance Criteria

- [x] #1 dap-ui on the first stop in its own tab, `!` flips F1-F8, :DdevXdebugHost, :DebugCli / :DebugBehat,
- [x] #2 dap: PHP debugging with DDEV in WSL, guided test session (2026-11-05; `legacy/nvim-config/todo-issue/solved-26.11.05-20.22-php-debug.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] try it by hand (marked untested in the notes)
- [ ] test: the 7 steps under "Implemented 2026-11-05" in backlog/docs/doc-8 - php-debug.md
- [ ] test: :DebugCli php -v, :DebugBehat on a .feature
- [ ] test: <leader>dB, <leader>dp, <leader>dl
- [ ] hollow ○ breakpoints and continue skipping breakpoints: diagnose with <leader>dl
- [ ] z3 with debug splits (questions in todo-ideas.md "zen modes")

## Original notes

```markdown
- [ ] PHP debugging that works, part of v2026 (2026-11-05)
  - keep nvim-dap + nvim-dap-ui unless the UI test says otherwise; compare nvim-dap-view
  - PHP runs in DDEV inside WSL (weasel-ddev): Xdebug networking and pathMappings untested
  - session, gaps and questions: todo-test/php-debug.md
  - [x] dap-ui on the first stop in its own tab, `!` flips F1-F8, :DdevXdebugHost, :DebugCli / :DebugBehat,
        `<leader>dK` `dl` `dB` `dp` (17e6c2b); nvim-dap-view on `<leader>dv` (8f5b8d2); untested
```
