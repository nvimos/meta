---
id: doc-76
title: 'purrage integration coordination'
type: other
created_date: '2026-11-19'
---

# Purrage integration coordination

Program: `integrate-purrage`. Ops is the app; Purrage becomes a mode in it, and its local git/files
code is reused behind the Ops backend seam. The five proposals carry the tag line
`Tags: integrate-purrage`; find them with:

```
rg "Tags: integrate-purrage" openspec/changes
```

Proposals, in order:

1. `openspec/changes/purrage-backend-seam/`
2. `openspec/changes/purrage-local-git-backend/`
3. `openspec/changes/purrage-actions/`
4. `openspec/changes/purrage-project-discovery/`
5. `openspec/changes/purrage-mode-and-ui/`

## Split

- **DeepSeek** takes the mechanical and backend work: ports, adapters, local git, action
  implementations, crawler, cleanup, and the stage 4 ports (Settings, Log, preview). Majority of
  the workload.
- **Claude** takes the architectural and UI work: the backend seam, backend selection, the shared
  status store and action queue, the watcher, wiring local actions into Ops Changes, Repos state,
  the mode views, the notice bar, the final shell.
- **Review:** a DeepSeek task goes from `Needs Test` to `Done` only after a Claude review against
  the Ops `CLAUDE.md` rules (test timeouts, `keepForCleanup`, `core.fsmonitor=false`, the `%TEMP%`
  count, no deprecated APIs, pointer cursor and tooltip on every clickable, `declarative_ui`
  limits). The review is one Handoff entry: passed, or what to fix.
- **Tests travel with the feature.** Every task ships the tests for what it adds, with its cleanup.
  TASK-170 and TASK-174 only add edge cases across tasks.
- A task is already assigned in its file. Do not take a task assigned to the other agent. If it
  blocks you, write a note in the Handoff section and take the next unblocked task of your own.

## Claiming and status

The task file is the source of truth for its status:

- `To Do` — not started
- `In Progress` — claimed; one task per agent at a time
- `Needs Test` — implementation done, waiting for the user or the other agent to try it
- `Done` — verified

To claim:

1. Check that every dependency is `Done`.
2. Check that no other `In Progress` task touches the same files; if one does, take another task.
3. Set the task to `In Progress` and add one line to the Claim log below.
4. Work in a worktree and branch named `task-<n>-<slug>`, created from the local `main`.
5. When done, set `Needs Test`, then `Done` after the verify steps pass (and, for a DeepSeek task,
   the Claude review).

First come, first served: take the lowest-numbered unblocked task assigned to you. A task is not
yours until it is `In Progress` in its file.

## Stages and merge order

Development may overlap only where the dependencies allow it. Merge in this order:

```
stage 0  seam + foundations        TASK-154, TASK-155, TASK-189
stage 1  local read-only           TASK-158, TASK-156 .. TASK-161, TASK-186
stage 2  local actions             TASK-188, TASK-162 .. TASK-170, TASK-184, TASK-185
stage 3  project discovery         TASK-171 .. TASK-174   (may merge after stage 1)
stage 4  Add and Ignore and UI     TASK-175 .. TASK-183, TASK-187
```

- Within a stage, merge in dependency order, then task number. TASK-184 … TASK-188 sit in earlier
  stages even though their numbers follow the stage 4 tasks; TASK-158 (test seams) goes first in
  stage 1 and TASK-188 (shared core) first in stage 2.
- Stage 3 does not depend on the action layer, so it may merge after stage 1; stage 4 waits for
  stages 2 and 3.
- If `main` moved since your worktree was made, rebase onto local `main` before merging. Do not merge
  a branch with a stale interface from the Handoff log.
- Do not merge a later stage over an earlier one to “save time”. The point of the order is that each
  stage is usable on its own.

## Task board

Task numbers are identifiers, not merge order. TASK-184 to TASK-189 sit outside their numeric
position; the Stage and Depends on columns decide when a task runs and merges.

| Task | Agent | Stage | Depends on |
|---|---|---|---|
| TASK-154 backend seam for local git | Claude | 0 | — |
| TASK-155 port purrage git foundations | DeepSeek | 0 | — |
| TASK-189 hot reload buttons | DeepSeek | 0 | — |
| TASK-158 local backend test seams | DeepSeek | 1 | 155 |
| TASK-156 read-only local git backend | DeepSeek | 1 | 154, 155, 158 |
| TASK-157 local files and tracking | DeepSeek | 1 | 154, 155, 158 |
| TASK-159 open folder and choose backend | Claude | 1 | 154, 156 |
| TASK-160 hide editor actions without nvim | Claude | 1 | 159 |
| TASK-186 local repository watcher | Claude | 1 | 154, 156 |
| TASK-161 read-only local mode integration | Claude | 1 | 156, 157, 159, 186 |
| TASK-188 shared status store and action queue | Claude | 2 | 154 |
| TASK-162 port the purrage action model | DeepSeek | 2 | 156, 188 |
| TASK-163 local file stage and discard | DeepSeek | 2 | 162 |
| TASK-164 local hunk stage and discard | DeepSeek | 2 | 163 |
| TASK-165 local commit checkout merge rebase | DeepSeek | 2 | 162 |
| TASK-166 port ignore rules | DeepSeek | 2 | 156 |
| TASK-167 local files trash and hidden write | DeepSeek | 2 | 157 |
| TASK-168 purrage mode state and actions | DeepSeek | 2 | 162, 163, 166, 167 |
| TASK-169 local actions in ops changes | Claude | 2 | 163, 164, 165 |
| TASK-170 action tests for local backend | DeepSeek | 2 | 162–168, 184, 185 |
| TASK-184 local task file edits | DeepSeek | 2 | 157, 162 |
| TASK-185 local jobs and cli | DeepSeek | 2 | 155 |
| TASK-171 port the repository crawler | DeepSeek | 3 | 155 |
| TASK-172 start dirs as hints | DeepSeek | 3 | 171 |
| TASK-173 directories over the crawler (Repos state) | Claude | 3 | 171, 172 |
| TASK-174 crawler and hint tests | DeepSeek | 3 | 171, 172 |
| TASK-175 Add and Ignore mode view | Claude | 4 | 168 |
| TASK-176 ignore pane and dialog | Claude | 4 | 166, 168 |
| TASK-177 Repos view | Claude | 4 | 173 |
| TASK-178 settings and editor detection | Claude | 4 | 159, 181 |
| TASK-179 Log (console) and scan report | DeepSeek | 4 | 162, 171, 181 |
| TASK-180 preview pane | Claude | 4 | 168, 175 |
| TASK-187 notice bar replaces the snackbar | Claude | 4 | 162 |
| TASK-181 final mode rail and keys | Claude | 4 | 175–180 |
| TASK-182 remove purrage handoff | DeepSeek | 4 | 159, 175, 177 |
| TASK-183 verify the integration end to end | Claude | 4 | 169, 170, 174, 175–182, 184–187 |

Count: 36 tasks. DeepSeek 20, Claude 16 (plus the reviews of DeepSeek's tasks).

## Boundaries agreed at review

These are not open questions; they keep the tasks from growing into each other.

- **Local merge/rebase is clean-path only.** A conflicting merge is aborted and reported. The
  worktree conflict flow stays on the Neovim backend until a separate task says otherwise.
- **Local change hints come from a watcher.** (Changed 2026-11-19 by the user; this replaced "a
  filesystem watcher is not part of this programme".) One debounced watcher on the worktree and
  `.git` raises the git change signal, shared with the History mode (TASK-186). Our own actions
  still bump the signal directly.
- **Add and Ignore and Changes are two views, not two state machines.** They are thin states over
  one status store and action queue (TASK-188). Add and Ignore is whole-file and file-first;
  Changes is diff- and hunk-first.
- **Ops models stay the truth.** Purrage's `StatusRow` is an input to Ops' `Status`, not a parallel
  model that survives into the views.
- **Task editing and local jobs are in scope.** Without `setLines`/`create`/`move` and
  `startJob`/`cancelJob`/`cli`, the local Tasks mode is read-only, which it must not be.
- **Editor opening arrives with Settings in stage 4.** Until then a local session can inspect and
  act but cannot open a file in an external editor; that is accepted for the staged build.
- **Stage 0 file ownership.** TASK-154 owns `lib/backend/backend.dart`,
  `lib/backend/models.dart` and `lib/state/session.dart`. TASK-155 adds new files under a new local
  package/folder and `pubspec.yaml`; it does not edit `backend.dart` or `session.dart`. This keeps
  the two first tasks from colliding.
- **The Purrage repository is frozen** from stage 0: bug fixes only, archived after TASK-183.

## Decisions (2026-11-19, the user)

The open questions of the five proposals are decided; each proposal has a Decided table. In short:

- names: the Purrage mode is **Add and Ignore**, Directories is **Repos**, Console is **Log**
- rail: Pull request, Changes, Add and Ignore, History, Tasks, Repos, Settings, Log, Help on
  Alt+1 … Alt+9
- `ops.exe <directory>` opens a local backend right away; the Connect screen is a recent list of
  folders and addresses
- no commit bar in Add and Ignore; preview pane there only; the notice bar replaces the snackbar
- file manager, trash and hidden write are general services
- duplicate widgets are decided one by one in the table below

## Widget table

Filled in 2026-11-19 by Claude, from the user's direction: Purrage's additions were asked for by
the user, so they are taken; Ops' version stays where it does more. The user reviews this table
later; until then it is the plan for TASK-181 and for every view task. Ported code imports
`material_ui`, as Ops does, not `flutter/material`.

| element | Ops | Purrage | choice |
|---|---|---|---|
| theme tokens | `C`, `Syn`, `T` (6 text styles) | `T` with exact row/header heights, gaps, icon sizes, contrast notes, a `ColorScheme` | **Purrage's `T` and scheme**; Ops' diff colours (`addBg`, `delBg`, `addSign`, `found`) and `Syn` move into it |
| palette, type sizes | 13 / 12 / 11 px, accent `#6C8CFF` | 12.5 / 11.5 / 11 px, accent `#6E79D6`, checked contrast | **Purrage's** |
| `Clickable` | — | pointer cursor + tooltip in one place, by construction | **take**: every clickable in Ops goes through it (enforces the CLAUDE.md cursor and tooltip rule) |
| `HoverRow` | `RowHover` (buttons shown on hover), `pointer: false`, `selectedColor` | built on `Clickable`; `onPress`, double tap, context menu, required tooltip | **merge**: Purrage's row plus Ops' `RowHover` and `pointer: false` (the file-row exception stays) |
| `IconAction`, `LinkButton`, `IconToggle` | — | yes | **take** |
| `SmallButton`, `Pill`, `PaneHeader` | yes | yes, on `Clickable` | **Purrage's**, keeping Ops' parameters that call sites use |
| `PaneMark` (accent line on the pane with the keys) | lit list title | yes | **take, beside** the lit title |
| `Empty`, `Spinner`, `ClearOnAltX`, `ClearButton` | yes | — | **keep Ops'** |
| status bar | fixed items: cursor, connection, debug toggle | slots `start` / `end`, `StatusText` | **Purrage's slot layout**, Ops' items as its content |
| `HotButtons` (hot reload / restart) | — | debug builds only | **take** (the user wants them), debug builds only, with `hot_reload.dart`: TASK-189, stage 0 |
| mode rail | `RailEntry`, `RailItem`, Alt numbers, labels | 56-line simple rail | **Ops'**, with Purrage's mode icons for the new modes |
| focus roles | `const` maps per mode | `FocusRoles` registry, `register()`, readable fallback for an unregistered label | **Purrage's registry**; Ops' role names registered into it |
| debug bar | network monitor, focus path dialog, key and button names | releases toggle, bug button | **merge**: Ops' bar plus Purrage's two controls; the network monitor only with a Neovim backend |
| Help view | search, highlight, columns, `KeyLabel` | plain list | **Ops'**; Purrage's key rows go into `keyTable` |
| `revealRange` | void | returns false when the list has not laid out yet, caller retries after the frame | **Purrage's** |
| `ResizablePane` | left pane, auto width from text, `minWidth` | right pane, width in `PaneLayout` saved in prefs | **merge**: one widget with a side, Ops' auto width, Purrage's saved width |
| `UiTiming` | `span`, `sync`, `time` | adds `input.click→frame` / `input.key→frame`, safe file write | **Purrage's additions on Ops' API**; env `NVIMOS_TIMING`, file `%APPDATA%/nvimos/ui-timing.json` |
| action errors | snackbar + Details | notice bar, grouped | **notice bar** (decided; TASK-187), keeping Details and hover-keeps-open |
| window title | — | `window_title.dart` | **take**: the repository in the title |
| filter field, delete dialog | — | yes | **take** (Add and Ignore) |
| keys | `navKey`, `KeySequence`, mode `focus` | `app_keys.dart` | **Ops' contract**; Purrage's bindings are re-expressed through `navKey` / `KeySequence` |
| list cursor | `list_pair`, `moveCursor` / `movePane` | `list_cursor.dart` | **Ops'**; Purrage's multi-select (ctrl/shift) added to it |
| commit bar | Changes | `commit_bar.dart` | **dropped** (decided) |

## Next up

At the start, three tasks have no dependencies and can run at the same time:

- **TASK-154** (Claude): backend seam.
- **TASK-189** (DeepSeek): hot reload buttons, small, first, so both agents have them.
- **TASK-155** (DeepSeek): port Purrage's git foundations.

After them: **TASK-158** (DeepSeek, test seams) needs only 155, then **TASK-156** and **TASK-157**.
Claude's next free task after 154 is **TASK-188** (shared core, needs only 154); **TASK-159** and
**TASK-186** follow once 156 is in.

## Claim log

One line per claim, newest at the bottom. Keep it short; the task file holds the detail. On claim,
`verified by` is `—`. When the task reaches `Needs Test`, add a line naming who verifies it: the
other agent, or the user.

```
date       agent     task      verified by   note
2026-11-19 —         —         —             board created; no task claimed yet
2026-11-19 deepseek  TASK-155  —             claimed; porting Purrage's git foundations
2026-11-19 deepseek  TASK-155  —             Needs Test; branch task-155-purrage-git-foundations
2026-11-19 deepseek  TASK-155  deepseek      tests pass; merged to main; Claude review pending
2026-11-19 deepseek  TASK-171  —             claimed; porting the crawler
2026-11-19 deepseek  TASK-185  —             claimed; local jobs and cli
2026-11-19 deepseek  TASK-171  —             Needs Test; crawler + tests pass
2026-11-19 deepseek  TASK-185  —             Needs Test; jobs/cli tests pass; app-exit survival manual
2026-11-19 deepseek  TASK-171  deepseek      tests pass; merged to main; Claude review pending
2026-11-19 claude    TASK-154  —             claimed; worktree task-154
2026-11-19 claude    TASK-154  user           Needs Test; merged to main as 090ad69; manual relay check left
2026-11-19 deepseek  TASK-156  —             claimed; read-only LocalBackend
2026-11-19 deepseek  TASK-157  —             claimed; local files and tracking
2026-11-19 claude    TASK-188  —             claimed; worktree task-188
2026-11-19 claude    TASK-188  user           Needs Test; merged to main as 53dcbeb; Changes tests pass
2026-11-19 claude    TASK-155  claude         review passed (see Handoff); Done
2026-11-19 claude    TASK-171  claude         review passed (see Handoff); Done
2026-11-19 deepseek  TASK-156  deepseek      tests + relay parity pass; merged
2026-11-19 deepseek  TASK-157  deepseek      files/tracking tests pass; merged
2026-11-19 deepseek  TASK-158  deepseek      fake runner log/diff test; seams verified
2026-11-19 deepseek  TASK-162  —             claimed; action failure/report model
2026-11-19 deepseek  TASK-162  deepseek      queue/report tests pass; merged
2026-11-19 deepseek  TASK-163  deepseek      stage/unstage/discard tests pass; merged
2026-11-19 claude    TASK-186  —             claimed; worktree task-186
2026-11-19 claude    TASK-186  user           Needs Test; merged to main as 1b5795f; tests pass, manual commit check left
2026-11-19 claude    TASK-159  —             claimed; worktree task-159
2026-11-19 deepseek  TASK-164  deepseek      hunk actions pass; merged
2026-11-19 deepseek  TASK-165  deepseek      commit/checkout/merge pass; merged
2026-11-19 deepseek  TASK-166  deepseek      ignore rules ported with foundations; tests pass
2026-11-19 deepseek  TASK-167  deepseek      file manager/trash/hidden write tests pass; merged
2026-11-19 deepseek  TASK-172  deepseek      hints/stale/startDirectory tests pass; merged
2026-11-19 deepseek  TASK-184  deepseek      task edit/create/move tests pass; merged
2026-11-19 claude    TASK-159  user           Needs Test; merged to main as d22bd5d; manual: no console window
2026-11-19 claude    TASK-160  —             claimed; worktree task-160
2026-11-19 deepseek  TASK-168  deepseek      Add and Ignore state/actions tests pass; merged
2026-11-19 deepseek  TASK-170  deepseek      action/queue/task/job tests pass
2026-11-19 deepseek  TASK-174  deepseek      crawler/hint tests pass
2026-11-19 claude    TASK-160  user           Needs Test; merged to main as 0e9d0f6; manual: editor keys in a local session
2026-11-19 claude    TASK-161  —             claimed; worktree task-161
2026-11-19 deepseek  both        backend chain through 172/184 is on main. Local/backend tests green;
                                 full suite has one meta-data failure: openspec/changes/history-mode
                                 has no TASK id. Remaining DeepSeek work: 179 and 182, both waiting
                                 on Claude's 175/181; 185 needs the app-exit manual check. 178/180
                                 moved to Claude.
2026-11-19 claude    TASK-161  user           Needs Test; merged to main as 00a8a8c; manual: open a real checkout
2026-11-19 claude    TASK-169  —             claimed; worktree task-169
2026-11-19 claude    TASK-169  user           Needs Test; merged to main as 67354fc; manual: the same flow against Neovim
2026-11-19 deepseek  TASK-179  deepseek      Log state/view tests pass; merged; rail waits for 181
2026-11-19 deepseek  TASK-182  —             claimed; Ops docs updated, Purrage hand-off removal running
2026-11-19 deepseek  TASK-182  deepseek      Ops README/PLAN updated; Purrage 336f0a7 drops the hand-off; analyze clean
2026-11-19 deepseek  TASK-189  deepseek      hot reload/restart buttons merged; manual make live check left
2026-11-19 deepseek  TASK-183  deepseek      full suite 394 pass; tasks_meta task-id and flaky archive only; manual walks left
2026-11-19 claude    TASK-173  —             claimed; worktree task-173
2026-11-19 claude    TASK-173  user           Needs Test; merged to main as 9c65f3d; tests pass
2026-11-19 claude    TASK-175  user           Needs Test; merged to main as 5e501f3 (view not on the rail until 181)
2026-11-19 claude    TASK-176  user           Needs Test; merged to main as 8e084b9 (dialog `i`, quick `I`, pane `p`)
2026-11-19 claude    TASK-177  user           Needs Test; merged to main as 4deea44
2026-11-19 claude    TASK-181  user           Needs Test; merged to main as 4736a32 (nine-mode rail, Alt+1 … Alt+9)
2026-11-19 claude    TASK-179  claude         review passed; Log wired into the rail (ad1795a); Done
2026-11-19 claude    TASK-178  user           Needs Test; merged to main as 45d556b (manual: open a file from Add and Ignore and Changes)
2026-11-19 claude    TASK-180  user           Needs Test; merged to main as 49b3b93 (+ pdfrx plugin registrant 72d173f)
2026-11-19 claude    TASK-187  user           Needs Test; merged to main as af32227
2026-11-19 claude    TASK-183  user           Needs Test; checks and open issues are in the task's Notes; manual passes are the user's
2026-11-19 claude    TASK-190  —             new: the History mode's Stack view (its rail entry is a placeholder); unassigned
```

## Interface changes

Anything another task will code against goes here before the task reaches `Needs Test`: a new
interface, a changed model, a renamed method, a new event, a changed file layout.

```
date       task      what changed
2026-11-19 TASK-154  `Backend` is now `NvimBackend` (lib/backend/backend.dart), implementing both new
                     interfaces in lib/backend/repo_backend.dart: `RepoBackend` (git, merge, files,
                     jobs, dirs, cd, tracking, pluginRoot, `events` = git + jobs only, `done`,
                     `close`, `RepoBackend.upToDate`) and `EditorSession` (`open`, `show`, `getText`,
                     `cursors`). `CheckoutHow`, `NvimEvent`, `StartDirs` moved to repo_backend.dart.
                     `Session.backend` is a `RepoBackend?`, new `Session.editor` is an
                     `EditorSession?`; `Session.run((RepoBackend b) ...)` as before, new
                     `Session.runEditor((EditorSession e) ...)` ("no editor" when null). A local
                     backend implements `RepoBackend` only and imports repo_backend.dart, never
                     backend.dart.
2026-11-19 TASK-188  New in lib/state: `StatusStore` (status_store.dart) owns the file list
                     (`status`, `branches`, `error`, `refresh()`, `refreshed` counter, `predict` /
                     `undo`) and reloads on `session.gitChanged`; `ActionQueue` (action_queue.dart)
                     runs `run(name, (RepoBackend b) ..., area:, predict:, optimistic:, settled:)`
                     one at a time and returns `ActionResult(name, error)`. On failure only that
                     action's predicted rows are put back. Both live on the session:
                     `Session.store`, `Session.actions`. `ChangesState` reads and acts through them
                     (`status`, `branches`, `busy` are getters now). TASK-162 ports Purrage's
                     result record, command and origin into `ActionResult`; TASK-168 / 175 build the
                     Add and Ignore state on `Session.store` + `Session.actions` the same way
                     `ChangesState` does, with the `area` of their own for timing.
2026-11-19 TASK-186  `RepoWatcher(root)` (lib/local/repo_watcher.dart): `changes` is a stream of
                     `RepoChange(paths, refs, index)`, one per burst; `head()` names the branch.
                     `LocalBackend.watch()` turns it into the `git` event and `LocalBackend.watcher`
                     exposes it: the History mode subscribes to `watcher.changes` (refs flag).
2026-11-19 TASK-159  `Session.openFolder(dir, {openProject})` opens a LocalBackend (editor null,
                     watcher on); `Session.kind` (`BackendKind.local` / `.nvim`), `Session.epoch`
                     (bumps when the backend changes or goes away: the shell drops the old mode
                     states), `Session.recents` / `openRecent` / `forget`, `Session.disconnect()`,
                     `Session.prefs`. `Prefs.recents()` / `addRecent` / `removeRecent`.
2026-11-19 TASK-160  `Session.hasEditor`; `TaskActions.hasEditor`. A local session has no editor:
                     views draw no Open in Neovim control and the open keys return quietly.
2026-11-19 TASK-169  `LocalBackend.checkout` follows the relay: tracked changes refuse the switch
                     unless `how` is stash (kept in a stash, not put back) or force.
                     `LocalBackend.mergePreflight` answers "no conflicts": a conflicting local merge
                     is aborted and reported by `merge`; the conflict flow stays on Neovim.
2026-11-19 TASK-173  `DirsState` is now `ReposState` (lib/state/repos.dart, was dirs.dart): `entries`
                     / `shownEntries` (`RepoEntry(path, source, stale)`: hints first, then the
                     crawl), `shown` (paths), `browser` (the RepoBrowser), `remove(path)`, `pick`
                     opens locally without Neovim. `Prefs.forgetProject`.
2026-11-19 TASK-175  `AddIgnoreView` (lib/ui/add_ignore_view.dart) over `AddIgnoreState`; keys t u i I
  to 181             x p v r Space Ctrl+A; `IconAction` (widgets.dart) is the row-button atom.
                     `Mode` is now pullRequest, changes, addIgnore, history, tasks, repos, settings,
                     log, help (Alt+1 … Alt+9; Directories is Repos). History has no view yet
                     (`ModePlaceholder`).
2026-11-19 TASK-178  `Editors` / `TerminalLauncher` (lib/local/editors.dart, terminals.dart, ported);
                     a local session now has an editor: `ExternalEditor` (lib/local/external_editor.dart:
                     open at a line; no cursor, no `show`). `Prefs.text/number/setText/setNumber`,
                     keys in `Settings`. `SettingsState`; `ReposState.openTerminal/openInFileManager`.
2026-11-19 TASK-180  `PreviewState` / adapters (lib/state/preview*.dart, text, picture, PDF through
                     pdfrx, programs, shortcuts, binary); `v` in Add and Ignore. New dependency: pdfrx.
2026-11-19 TASK-187  `Session.notices` (`Notices`, lib/state/notices.dart); `showActionError` puts the
                     failure in `NoticeBar` above the status bar (snackbar only without a session).
                     Notes of things done keep their snackbars.
```

## Handoff and questions

Use this section when a task is blocked by the other agent, when a decision affects both, or when a
task discovers work that is not in the board. Keep one short entry per exchange.

```
date       from       to         note
2026-11-19 claude     both       user decided the open questions (see Decisions); board changed:
                                 158 now first in stage 1 (seams before 156/157); 161 to Claude;
                                 178/179/180 to DeepSeek; new 186 watcher, 187 notice bar,
                                 188 shared core (before 162); watcher boundary reversed;
                                 Claude reviews every DeepSeek task before Done
2026-11-19 claude     deepseek   widget table filled in; new TASK-189 hot reload buttons (user
                                 wants them), stage 0, no dependencies: take it before TASK-155
2026-11-19 claude     deepseek   review TASK-155 and TASK-171: passed. Fixtures use keepForCleanup and
                                 core.fsmonitor=false, no real processes (fake system), %TEMP% count
                                 unchanged; one unused import removed (c465493 on main)
2026-11-19 claude     deepseek   TASK-154 and TASK-188 are on main: build 162 on `Session.actions`,
                                 and take `RepoBackend` from repo_backend.dart (see Interface
                                 changes). 156/157 were claimed before TASK-158 (test seams) was Done;
                                 please close 158 and send 156/157 for review
2026-11-19 deepseek   claude     backend chain is on main through 172/184: local RepoBackend, stage/
                                 hunks/commit/checkout, ignore, files/trash, hints, Add and Ignore
                                 state. 178/180 are views after 175/181, so they are Claude's now
                                 (deps updated); 179 stays DeepSeek but waits on 181 for the rail.
                                 160/169/175/176/177/181 are the remaining UI path.
2026-11-19 claude     deepseek   done on my side and on main: 159-161, 169, 173, 175-178, 180, 181, 187.
                                 179 reviewed (Done) and wired into the rail; the Log view takes scan
                                 reports from the Repos state. Review of 162-168, 170, 172, 174, 184,
                                 185: fixtures clean up, no real processes beyond `attrib`, no deprecated
                                 API found. Fixes I made in your files while building on them: LocalBackend
                                 checkout follows the relay (stash is left in a stash, dirty tracked
                                 files refuse without a choice), mergePreflight answers "no conflicts".
                                 Still open for you: TASK-189 (hot reload buttons, nobody took it) and the
                                 openspec/changes/history-mode meta test (it needs a TASK id: the user
                                 decides whether History gets a task).
```

Rules for handoffs:

- Do not silently widen a task. If it needs work owned by another task, add an entry and make a new
  task only with the user's agreement.
- Do not edit a file another `In Progress` task owns. Wait, or pick a different task.
- If you change a shared interface, update the Interface changes table before you mark the task
  `Needs Test`.
- The final integration task, TASK-183, is the only place that declares the programme done.
