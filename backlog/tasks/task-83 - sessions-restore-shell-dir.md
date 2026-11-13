---
id: TASK-83
title: 'sessions: a saved shell comes back in its current dir, not the one it was started in...'
status: To Do
assignee: []
created_date: '2026-11-02'
labels:
  - nvim-config
  - todo-2028
  - later-2028
dependencies: []
ordinal: 83000
---

## Description

sessions: a saved shell comes back in its current dir, not the one it was started in...

- moved from todo-ideas.md 2026-11-02; asked 2026-10-31
- tricky: probably a week-long project, lots of testing and edge cases
- today lua/genja/ext/term.lua mksession: the term:// name keeps the start dir; only idle shells are saved
- which other terminals to save (e.g. `:terminal ssh a22`: reconnects on restore): needs more thought
- light-weight try: let a multiplexer keep the shells, nvim only reattaches
  - tmux itself is not native on Windows (WSL, MSYS2, Cygwin only)
  - native Windows options, checked 2026-11-02 (not tried):
    - psmux: Rust, ConPTY, tmux commands and .tmux.conf, sessions persist; `winget install psmux`
    - tmux-windows / tmuxw (turin-dev; winget arndawg.tmux-windows): tmux 3.6a port on ConPTY, detach/reattach
    - zellij 0.44+: runs natively on Windows, has sessions and a CLI
  - Windows Terminal splits don't persist or detach

From `todo-2028.md`, section "later: 2028".

## Original notes

```markdown
- [ ] sessions: a saved shell comes back in its current dir, not the one it was started in (tricky)
  - moved from todo-ideas.md 2026-11-02; asked 2026-10-31
  - tricky: probably a week-long project, lots of testing and edge cases
  - today lua/genja/ext/term.lua mksession: the term:// name keeps the start dir; only idle shells are saved
  - which other terminals to save (e.g. `:terminal ssh a22`: reconnects on restore): needs more thought
  - light-weight try: let a multiplexer keep the shells, nvim only reattaches
    - tmux itself is not native on Windows (WSL, MSYS2, Cygwin only)
    - native Windows options, checked 2026-11-02 (not tried):
      - psmux: Rust, ConPTY, tmux commands and .tmux.conf, sessions persist; `winget install psmux`
      - tmux-windows / tmuxw (turin-dev; winget arndawg.tmux-windows): tmux 3.6a port on ConPTY, detach/reattach
      - zellij 0.44+: runs natively on Windows, has sessions and a CLI
    - Windows Terminal splits don't persist or detach
```
