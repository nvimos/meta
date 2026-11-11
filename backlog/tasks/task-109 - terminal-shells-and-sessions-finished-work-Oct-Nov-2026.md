---
id: TASK-109
title: 'terminal, shells and sessions: finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-25'
labels:
  - nvim-config
  - terminal
  - from-config
dependencies: []
ordinal: 109000
---

## Description

Finished work on terminal, shells and sessions, 2026-10-25 .. 2026-10-31: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-41 - guide-session-marker-toggle.md`: Claude session marker: switch it off, and markers in text files

## Acceptance Criteria

- [x] #1 floaterm: `:PwshFterm` (2026-10-25; `solved-26.10.25-07.40-pwsh-fterm.md`)
- [x] #2 term: terminal-mode cursor and clipboard paste (2026-10-25; `solved-26.10.25-07.40-term-cursor-paste.md`)
- [x] #3 ws: drafts for a frameless nvim-qt window only when maximized (2026-10-26; `solved-26.10.26-23.48-frameless-drafts.md`)
- [x] #4 opt-term: set_shape() with no name warns instead of erroring (2026-10-26; `solved-26.10.26-23.48-term-shape.md`)
- [x] #5 term: scrolloff 0 in terminal windows (2026-10-28; `solved-26.10.28-23.12-term-scrolloff.md`)
- [x] #6 terminal: mode on enter, window keys, float toggle, sessions with idle shells (2026-10-29; `solved-26.10.29-20.56-terminal-keys.md`)
- [x] #7 terminal: bare :terminal opens pwsh on Windows, bash on Linux (2026-10-31; `solved-26.10.31-06.21-terminal-shell.md`)
- [x] #8 sessions: save: dropped idle shells (2026-10-31; `solved-26.10.31-20.02-session-shells.md`)
- [x] #9 term: <S-Insert> ran each pasted line in pwsh (2026-10-31; `solved-26.10.31-20.02-term-paste.md`)
- [x] #10 terminal cursor: hollow box (unresolved, lua/genja/opt-term.lua) (undated; `ideas-48-terminal-cursor.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: `:PwshFterm`, `exit` closes it (`solved-26.10.25-07.40-pwsh-fterm.md`)
- [ ] test: `:terminal`, insert: steady bar in orange; `:TermCursorShape block` (`solved-26.10.25-07.40-term-cursor-paste.md`)
- [ ] test: copy two lines, `<S-Insert>` in a pwsh terminal: pasted, not run line by line (`solved-26.10.25-07.40-term-cursor-paste.md`)
- [ ] 48. hollow box cursor, blink set by the app in the terminal (todo-ideas.md) (`solved-26.10.25-07.40-term-cursor-paste.md`)
- [ ] pick one and move it into ginit.vim, or drop both (`solved-26.10.26-23.48-frameless-drafts.md`)
- [ ] test: `:TermCursorShape` without an argument: one warning (`solved-26.10.26-23.48-term-shape.md`)
- [ ] test: :setlocal scrolloff? in a claude terminal shows 0; wheel scrolling in insert mode (`solved-26.10.28-23.12-term-scrolloff.md`)
- [ ] test: <C-`> toggles the generic floaterm; <M-`> leaves a terminal (`solved-26.10.29-20.56-terminal-keys.md`)
- [ ] test: save: with an idle shell and a running claude, then :source ~/tmp/viss (`solved-26.10.29-20.56-terminal-keys.md`)
- [ ] test: `:term`, `:vert term`, `:tab te` open pwsh; `:term dir` still runs in cmd (`solved-26.10.31-06.21-terminal-shell.md`)
- [ ] test: `:g` quits, `:g/x/d` runs; `make test D=unsaved` in tests/ (`solved-26.10.31-06.21-terminal-shell.md`)
- [ ] test: on Linux `:term` opens bash, not zsh (`solved-26.10.31-06.21-terminal-shell.md`)
- [ ] test: `save:` with an idle pwsh terminal, restore brings it back (`solved-26.10.31-06.21-terminal-shell.md`)
- [ ] vim.cmd('terminal') and mapped :term still use 'shell' (`solved-26.10.31-06.21-terminal-shell.md`)
- [ ] restore the shell's current dir; which other terminals to save (todo-ideas.md) (`solved-26.10.31-20.02-session-shells.md`)
