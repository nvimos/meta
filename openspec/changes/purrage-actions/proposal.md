# local Git actions and the Purrage action model

Tags: integrate-purrage
Status: Needs Test (approved and built on 2026-11-19; nine tasks done, three wait for the user's test; see doc-76). Part 3 of 5 in the Purrage integration.
Tasks: TASK-188, TASK-162, TASK-163, TASK-164, TASK-165, TASK-166, TASK-167, TASK-168, TASK-169, TASK-170, TASK-184, TASK-185.

## Why

The read-only backend (part 2) lets Ops show a local repository. It cannot change one. Ops Changes
needs its existing actions on the local backend, and the future Purrage mode needs Purrage's proven
whole-file actions: track, untrack, ignore and delete.

Purrage's action layer is worth reusing because it already solves the hard parts:

- optimistic row moves before git runs, with a failure restoring only that action's rows
- a serialized action queue, so two clicks cannot fight over the index
- an action that is still pending prevents a stale `git status` from flickering the list back
- every result carries the action, origin, command and parameters, so the console and notices can
  say what happened
- the ignore rules know the difference between a root `.gitignore`, a folder `.gitignore`, the local
  exclude file and the global ignore file, and handle nested repositories

Ops' `Changes` state already does part of this. A file stage or unstage moves the rows locally
before the backend answers (`act(..., optimistic:)`, `_moveLocally` in `lib/state/changes.dart`),
and a `_pending` count keeps a refresh from flipping the move back while an action runs. Hunk
actions are not optimistic, because only git knows the shifted line numbers.

What Ops lacks is the rest of Purrage's discipline: actions are not queued (two clicks run side by
side), a failed move is put back only by the full refresh after every action, not by restoring that
action's own rows, and the result is an error string rather than a record of the action, origin,
command and parameters. The local backend needs the same action discipline on both sides.

## The idea

Bring Purrage's action model into Ops as shared state logic, not as a second app: one status store
and one action queue per repository, under two thin mode states (Changes, and the Add and Ignore
mode), each owning only its cursor, selection and filter.

Local implementations of the existing Ops actions:

- stage, unstage and discard whole files
- stage, unstage and discard hunks
- commit, checkout, merge and rebase
- the same error text and command reporting Ops already shows

The Add and Ignore mode's actions (the Purrage mode's final name), built on the same machinery:

- track (stage a whole file), untrack (`git rm --cached`, never deleting from disk)
- ignore, with the rules engine, ignore targets, already-ignored checks and nested-repository guards
- delete through the trash, with the row leaving the list first
- file manager operations and hidden-file repair where the local platform needs it; these are
  general Ops services any mode can call (Tasks, Repos), not part of the mode

The action result type, notices and Log entries are shared. The mode's state is built here and
testable without widgets; its view arrives in part 5. Ops Changes can use the local actions
immediately.

Commit stays in Ops Changes only. Purrage's commit bar (`lib/ui/commit_bar.dart`) is not ported.

## Scope

- Port Purrage's `Changes` action queue, optimistic row changes, `ActionResult` and failure/notice
  reporting into Ops' state layer.
- Port the ignore rules and ignore-match parsing from Purrage.
- Implement local `stage`/`unstage`/`discard`, file and hunk variants, commit, checkout, merge and
  rebase.
- Add the Purrage mode state: status rows, selection, filter, track/untrack/ignore/delete.
- Port the file manager, trash and hidden-write handling needed by those actions.
- Keep the Neovim backend's action behaviour unchanged.

## Out of scope

- The Purrage mode view, list widgets, ignore pane or dialog. That is part 5.
- The project crawler. That is part 4.
- Reworking Ops' diff view or commit bar beyond wiring them to the local backend.
- Changing the Neovim backend's merge-conflict worktree; it can stay there until later.

## Done when

- A local repository can stage, unstage, discard, commit, checkout, merge and rebase from Ops.
- Track, untrack, ignore and delete work from the state layer and are covered by tests.
- An action failure restores only its own rows and produces the same kind of report Ops already
  shows.
- No Purrage view is needed to exercise the actions; tests drive the state objects.

## Decided (2026-11-19, the user)

| question | answer |
|---|---|
| State shape | **two thin mode states over a shared core**: one status store and one action queue per repository; the core's interface is designed first (Claude) and the port builds on it |
| Commit bar | **dropped**: commit only in Changes |
| File manager, trash, hidden write | **general Ops services**, behind the process seams |
| Notices and console | Purrage's **notice bar replaces the snackbar**, keeping the Details button and staying open while hovered; the Console is ported as the **Log** mode |
| Backend calls no part owned | Tasks file writes (TASK-184) and local jobs (TASK-185) are part 3; `dirs`/`cd` become part 4 hints; the merge-conflict worktree stays on Neovim for now |

## Open questions

None left for this part.
