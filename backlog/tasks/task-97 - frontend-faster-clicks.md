---
id: TASK-97
title: 'frontend faster clicks'
status: Needs Test
assignee: []
created_date: '2026-11-11'
labels:
  - performance
  - frontend
dependencies: []
ordinal: 97000
---

## Description

In `~/es/nvimos-poc-frontend`, checking items feels slow: it takes a while before a checkbox
shows as checked. Measure where the time goes and fix both kinds of click:

- Tasks checklists (task detail, a change's Tasks tab, the review panel). `Workspace.edit` is
  already optimistic, but each edit re-parses every planning file on the UI thread, and the file
  write triggers a full reload (every planning file, branches, commits ahead); a reload that
  started before the click can finish after it and show the old state for a moment.
- Changes stage checkboxes. Not optimistic: a click waits for the stage call, `git status` and
  the file's diff before it redraws.

Add UI timing instrumentation: record every UI interaction per session, and write a state file
when the app quits. On during development, off in production. Hook it where clicks already
pass (backend wrapper, state actions, Flutter's global pointer route), not into click handlers.

## Original instructions

The user's words, 2026-11-11:

> So the app seems kind of slow when I check items and so on. It takes a while before they are
> checked. Can you do the classical UI trick where you change the UI right after the click? And
> then as the responses come in, you either reject the change or do nothing. I mean, if the
> change applied, so I'm coming from a web client server kind of perspective, before you do any
> radical changes to the Flutter app. Can you tell me if this is even possible? Or maybe I should
> drop the old thinking and ask you to optimize the performance instead. What do you think about
> that?

> I want you to measure and fix both. Also, what do you think about implementing some kind of
> instrumentation so that we can actively monitor all the UI interactions? I mean, actively as in
> per session, and record them. And then when the app quits, update some kind of state file. This
> should be called UI timing instrumentation. And during development, it should be on, and for
> production, it should be off. Is that viable? I mean, that way we have a solid way to monitor
> the performance of the UI throughout the lifetime of the app. Is it possible to implement that
> in a clean way? Without obstructing the all the click handling events in the app?

## Plan

The answer given: optimistic UI is the right pattern and possible in Flutter (the Tasks edits
already do it); measure first, then fix:

1. Measure each step of one click (Tasks check, Changes stage) with the instrumentation.
2. Tasks: re-parse only the edited file; skip the reload our own write triggers; never let an
   older reload overwrite a newer edit.
3. Changes: stage and unstage of a whole file moves it to the other list at once; when git
   answers, keep it, or put it back and show the error. Hunk staging stays as it is (line
   numbers shift).

## Done (frontend 0610d7c)

- `UiTiming` started in `main.dart`, saved on quit (`AppLifecycleListener.onExitRequested`).
- Spans: every backend call, `tasks.edit` / `tasks.load` / `tasks.rebuild`, `changes.<action>`
  (stage, unstage, stageAll, stageHunk, commit, ...), `changes.refresh`, `pr.refresh`.
- Tasks: an edit re-parses only its file; the reload from our own write is skipped; a reload that
  started before an edit keeps the edit. `Task.number` is computed once (it built a RegExp in
  every sort comparison).
- Changes: whole-file stage / unstage (and stage all) move the file at once; the refresh after git
  keeps it or puts it back. Hunk staging still waits for git.
- Tests: `ui_timing_test.dart`, the optimistic and failing cases in `changes_state_test.dart`,
  `timing_measure_test.dart` (prints the timings, fails if a check flips back).

## Timings (debug, headless Neovim, ms p50 / p95)

Tasks check, 300 tasks + 60 changes, 6 clicks (`test/timing_measure_test.dart`):

| step                          | before         | after              |
|-------------------------------|----------------|--------------------|
| click to new state in memory  | 63 / 74        | 4 / 5              |
| full re-parse per edit        | 57 / 74        | (one file) 4 / 5   |
| reload after own write        | 648 / 700      | none               |
| write through Neovim (saved)  | 249 / 314      | 93-170 / 114-318   |
| clicks that ended unchecked   | 3 of 6         | 0 of 6             |

Changes stage of one file (`changes_state_test.dart`, 10 round trips):

| step                          | before                      | after                    |
|-------------------------------|-----------------------------|--------------------------|
| click to file in other list   | 475 / 550 (stage+status+diff) | the next frame         |
| `git stage` / `git status` / diff RPC | 220 / 168 / 88      | same, after the move     |
| hunk staging                  | 565                         | unchanged (not optimistic) |

## Acceptance Criteria

- [x] #1 a Tasks checkbox shows its new state in the next frame, and no reload flips it back
- [x] #2 a Changes stage checkbox moves the file at once; a failed stage puts it back with the error
- [ ] #3 `ui-timing.json` holds per-session timings after a debug run; a release build writes nothing
- [x] #4 timings before and after the fixes are recorded in this task
