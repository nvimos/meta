# the Purrage mode and the remaining Purrage UI

Tags: integrate-purrage
Status: Open proposal, not decided, not to be implemented yet. Part 5 of 5 in the Purrage integration.
Tasks: TASK-175, TASK-176, TASK-177, TASK-178, TASK-179, TASK-180, TASK-181, TASK-182, TASK-183, TASK-187, TASK-189.

## Why

Parts 1 to 4 give Ops a local backend, local actions, the Purrage action model, and project
discovery. None of it is visible yet. This part turns the Purrage functionality into a mode inside
Ops and finishes the UI merge.

Ops remains the leading app: its shell, mode rail, theme, key contract, Pull request, Changes and
Tasks views stay. Purrage contributes the file-triage workflow, its views and its small tools. It is
not a second app inside the window.

## The idea

The final mode rail, numbered Alt+1 … Alt+9 in this order (History comes from the
`history-mode` proposal):

1. **Pull request** — Ops, unchanged
2. **Changes** — Ops' diff, hunks, staged list and commit; now backed by either backend
3. **Add and Ignore** — the whole-file mode from Purrage: a status list, add, untrack, ignore,
   delete, with the preview pane
4. **History** — the stacked-branches view
5. **Tasks** — Ops, unchanged
6. **Repos** — the crawler from part 4 (the current Directories mode, widened, Browse folded in)
7. **Settings** — from Purrage, for editors, terminals, scan depth and prefs
8. **Log** — Purrage's Console, renamed: the action and scan reports
9. **Help** — merged key tables

The overlapping Changes views are resolved by purpose, not by choosing one:

- Ops Changes stays the diff and hunk mode, with checkout, merge/rebase and commit.
- Add and Ignore is the fast whole-file triage list: add, untrack, ignore, delete, with the
  optimistic rows and the ignore pane. It is what Purrage was for.
- Both are thin states over one status store and action queue.
- Commit is only in Changes; Purrage's commit bar is not ported.

Purrage's notice bar replaces Ops' snackbar in every mode. It keeps Ops' Details button (the
selectable trace) and stays open while the mouse is over it.

The UI sources:

- Purrage's file list, row sections, selection model and ignore pane/dialog become the Add and
  Ignore view, restyled to Ops' theme and keys.
- Purrage's Browse view is folded into the Repos view over the crawler state.
- Purrage's Settings view, editor detection and terminal launcher are ported, with Ops' `Prefs`
  storage.
- Purrage's Console view and scan/action reports are ported as the Log mode.
- Purrage's preview pane and adapters (text, image, PDF through `pdfrx`) are ported into the Add
  and Ignore mode only.
- Purrage's widgets and theme tokens are merged into Ops' existing ones; each duplicate is decided
  once, by the user, in the widget table of `backlog/docs/doc-76`, and every mode follows.

The Purrage repository is frozen from stage 0 (bug fixes only) and archived after TASK-183.

## Scope

- Add the Add and Ignore view and wire it to the actions from part 3.
- Port the ignore pane and ignore dialog.
- Build the Repos view over the part 4 state, with Browse folded in.
- Port Settings, including editor detection, terminal choice, folder opener, scan depth and prefs.
- Port Console as Log, with the action/scan report formatting.
- Replace the snackbar with Purrage's notice bar (Details button, open while hovered).
- Port the preview pane into the Add and Ignore mode.
- Merge the key tables, help, rail entries (Alt+1 … Alt+9) and tooltips into one contract.
- Remove the separate Purrage app from the workflow: no `OpsLauncher`, no “open this folder in Ops”
  hand-off, no second window.

## Out of scope

- Any new backend capability; parts 1 to 4 must already provide it.
- Reworking Pull request, Tasks or the conflict view.
- Purrage's development tooling beyond hot reload. The hot reload and restart buttons are in: the
  user wants them (TASK-189, debug builds only, done first so both agents have them).
- Windows-only exploration beyond what Ops already supports.

## Done when

- A user can open a local folder, triage files in the Add and Ignore mode, open the ignore pane,
  commit in Changes, browse repositories and configure the editor and terminal, all in Ops.
- The Neovim backend still provides Pull request, editor actions and the remote use case.
- No feature requires starting Purrage.
- The key table, help and mode rail describe the final modes without duplicates.
- The Add and Ignore mode and Ops Changes do not both own the same file list or the same state.

## Decided (2026-11-19, the user)

| question | answer |
|---|---|
| Mode name | **Add and Ignore** |
| Commit bar | **dropped**; commit only in Changes |
| Preview pane | **Add and Ignore mode only** |
| Settings | **a mode** on the rail |
| Console | **renamed Log**; the notice bar replaces the snackbar, keeps Details, stays open while hovered |
| Rail | **all nine numbered**, Alt+1 … Alt+9, History included |
| Duplicate widgets | **Purrage's additions are taken** (the user asked for them); Ops' version stays where it does more; row by row in doc-76's widget table |
| Purrage repository | **frozen** from stage 0, **archived** after TASK-183 |

## Open questions

- the user reviews doc-76's widget table; until then it stands as written
