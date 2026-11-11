---
id: TASK-98
title: 'Claude Code terminal (claudefterm): finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-24'
labels:
  - claude-terminal
  - from-config
dependencies: []
ordinal: 98000
---

## Description

Finished work on Claude Code terminal (claudefterm), 2026-10-24 .. 2026-11-07: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

## Acceptance Criteria

- [x] #1 claude: closing a finished claude terminal failed with E444 when it was the last window (2026-10-24; `solved-26.10.24-06.42-claude-autoclose.md`)
- [x] #2 claude: <C-Up> in the claude terminal goes to normal mode (2026-10-24; `solved-26.10.24-08.19-claude-c-up.md`)
- [x] #3 claudefterm: `:ClaudeFterm -1` / `-one` opens claude without a split (2026-10-24; `solved-26.10.24-18.39-claudefterm-one.md`)
- [x] #4 genja-claudefterm: unit tests for one claude per project (2026-10-25; `solved-26.10.25-00.07-claudefterm-tests.md`)
- [x] #5 claudefterm: `kill() stops every terminal` crashed the test child about one run in three (2026-10-26; `solved-26.10.26-22.30-claudefterm-kill.md`)
- [x] #6 CLAUDE.md: prompts are dictated, some words arrive misheard (2026-10-26; `solved-26.10.26-22.30-voice-note.md`)
- [x] #7 auto-alias: :Ct as a short :ClaudeFterm (2026-10-26; `solved-26.10.26-23.48-ct-alias.md`)
- [x] #8 claudefterm: -ax starts claude with --ax-screen-reader (2026-10-29; `solved-26.10.29-22.26-claudefterm-ax.md`)
- [x] #9 claudefterm: `:Ct` behaves as `:Ct -1` (2026-11-03; `solved-26.11.03-14.02-ct-one.md`)
- [x] #10 claudefterm: remove session markers (2026-11-07; `solved-26.11.07-01.34-claudefterm-markers.md`)
- [x] #11 claudefterm: visual paste from a buffer without a file (2026-11-07; `solved-26.11.07-01.34-claudefterm-paste.md`)
- [x] #12 claude.md: point to the jolemak layout source for key quirks (2026-11-07; `solved-26.11.07-01.34-jolemak-layout.md`)
- [x] #13 claude: from nvim (undated; `ideas-19-claude-from-nvim.md`)
- [x] #14 claude session marker follow-up (from #19, todo-done/ideas-19-claude-from-nvim.md) (undated; `ideas-39-session-marker-toggle.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: `:ClaudeFterm` as the only window, `/exit` in claude: the window stays, on the origin buffer, no E444 (`solved-26.10.24-06.42-claude-autoclose.md`)
- [ ] test: claude in a split, `/exit`: the claude window closes (`solved-26.10.24-06.42-claude-autoclose.md`)
- [ ] several FloatermKills in a row sometimes crash the headless test nvim on Windows; check `:s:`/quit with 2+ claudes (`solved-26.10.25-00.07-claudefterm-tests.md`)
- [ ] test: `s:` with two claude terminals open: both close, session saved, nvim quits (`solved-26.10.26-22.30-claudefterm-kill.md`)
- [ ] test: `:Ct` and `:Ct --chrome` start claude like `:ClaudeFterm` (`solved-26.10.26-23.48-ct-alias.md`)
- [ ] test: `:Ct` in a normal buffer takes the window; `:Ct` again gives the buffer back (`solved-26.11.03-14.02-ct-one.md`)
