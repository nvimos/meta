---
id: TASK-183
title: 'verify the integration end to end'
status: Needs Test
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-169
  - TASK-170
  - TASK-174
  - TASK-175
  - TASK-176
  - TASK-177
  - TASK-178
  - TASK-179
  - TASK-180
  - TASK-181
  - TASK-182
  - TASK-184
  - TASK-185
  - TASK-186
  - TASK-187
ordinal: 183000
---

## Description

Close the programme: verify the five proposals' acceptance criteria on a real checkout and with the
Neovim backend, and record what remains open. This is the integration gate, not a feature task.

Change: all five `openspec/changes/purrage-*` proposals.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 a local folder opens, reads, triages, commits and browses with no Neovim
- [x] #2 the same folder works through the Neovim backend, including open/show
- [x] #3 the Add and Ignore mode and Ops Changes do not duplicate state or actions
- [ ] #4 Tasks edits, archives and starts a local job without Neovim
- [x] #5 the key table, Help, README and `PLAN.md` describe the final app
- [x] #6 every remaining issue is recorded as a task or an open question

## Verify

- [x] test: the whole suite on a clean `%TEMP%`
- [ ] manual: local and Neovim walks on the same repository
- [ ] review: the five proposals' acceptance criteria are ticked or explained

## Notes

Checked 2026-11-19 by Claude, on main after TASK-187:

- Suite: 394 tests pass on a clean `%TEMP%`; the one failure is `tasks_meta_test`, for
  `openspec/changes/kanban-board-mode`, a change that is not part of this programme and names no task.
  `workspace_test` "archive merges deltas" is the known flaky one; `tasks_view_test` and
  `status_store_test` failed once each under full-suite load and pass alone.
- #1: `local_mode_test` and `local_changes_test` open a temp repository with the local backend and
  read Pull request, Changes and Tasks, stage, unstage, hunk, discard, commit, checkout and merge,
  with edits, task edits and a commit made outside reaching the views through the watcher.
- #2: the Neovim backend runs the same Changes, Pull request, Tasks and session tests as before; a
  session switches between the two backends (`open_folder_test`).
- #3: Changes, Add and Ignore share `Session.store` and `Session.actions` (`status_store_test`).
- #4 is checked at the backend level (`local_backend_test`, `local_jobs_test`); a full click-through of
  Tasks in a local session is for the user.
- Left for the user (manual): a real checkout opened locally and compared with `git status`; the
  keyboard pass through the nine modes; Open in an external editor from Add and Ignore and Changes;
  `ops.exe <folder>` shows no console window; a `git commit` in a terminal showing up in Changes;
  hot reload, once TASK-189 exists.

Open and recorded elsewhere:

- TASK-189 (hot reload buttons) is done and Needs Test; the manual `make live` reload is the only check left.
- TASK-190 (the History mode's Stack view); its rail entry shows "not built yet".
- The widget table in doc-76 awaits the user's review.
- A local session's buttons still say "Open in Neovim" while they open the editor Settings names.
- A conflicting merge or rebase in a local session is aborted and reported (the conflict view stays
  on the Neovim backend, by decision).
- `openspec/changes/kanban-board-mode` has no task.
- The Purrage repository is archived after the user has tried the result (decided).
