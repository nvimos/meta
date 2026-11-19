# local Git backend, read-only

Tags: integrate-purrage
Status: Needs Test (approved and built on 2026-11-19; four tasks done, four wait for the user's test; see doc-76). Part 2 of 5 in the Purrage integration.
Tasks: TASK-155, TASK-156, TASK-157, TASK-158, TASK-159, TASK-160, TASK-161, TASK-186.

## Why

Ops cannot show a repository without Neovim. A local folder should open in the app, the Pull request
and Changes views should read it, and the Tasks view should read its planning files, with no editor
running at all.

Purrage already has a working local Git layer: repository discovery, a careful `git status
--porcelain=v1 -z` parser, branches, commits, `.gitignore` handling, file reads and writes, and
Windows-specific path handling. It is the part worth taking. Ops should not grow a second local git
implementation next to it.

The goal is not to merge Purrage's app into Ops. It is to reuse Purrage's local layer behind the
backend seam from part 1, as `LocalBackend`.

## The idea

`LocalBackend` implements `RepoBackend` directly:

- repository discovery and open from a folder (`Repo.open`, `GitDir.fromExisting` or an equivalent)
- `git status --porcelain=v1 -z --untracked-files=all --find-renames`, decoded as UTF-8 and parsed
  into Ops' `Status` model
- branches, log and diff, ported from relay's `nvimos.git` commands into the local backend
- file list and read, from the filesystem
- `.nvimos` tracking parsing, without a Neovim buffer in between
- no editor capability; `EditorSession` is absent

The starting path is a folder. The Connect screen becomes a list of recent folders and Neovim
addresses, each remembering its backend; a folder entry creates a `LocalBackend` and the modes run
against it.

`ops.exe <directory>` exists already and today starts a headless Neovim in that folder
(`lib/main.dart`, `lib/state/nvim_launcher.dart`). It changes meaning: a directory opens a
`LocalBackend` right away, even while the local backend is still read-only. An address
(`127.0.0.1:port`) still selects Neovim.

The local backend watches the repository itself, since there is no relay to send git hints: one
debounced file watcher on the worktree and on `.git` (`index`, `HEAD`, `refs/`, `packed-refs`),
raising the same git change signal the Neovim backend raises. The History mode's refs watcher is the
same watcher, not a second one.

The app-facing models stay Ops' models. Purrage's `StatusRow` and `Section` are not allowed to become
a second truth: its parser feeds Ops' `Status`, `Branches`, `Commit`, `DiffFile` and `Hunk`.

## Scope

- Add the `git` package dependency (Purrage uses it) or an equivalent process layer; keep Purrage's
  UTF-8 status decoding and argument batching.
- Port `Repo`, `GitRepo`, the status parser, `paths.dart` and the `.nvimos` tracking parser.
- Implement the read-only half of `RepoBackend`: branches, log, diff, status, file list/read.
- Port relay's `diffparse.lua` to Dart line by line, reusing relay's cases as fixtures.
- Add the repository watcher (shared with the History mode).
- Add the recent-entries Connect screen and backend selection in `Session`.
- Make Pull request, Changes and Tasks load from a local repository.
- Hide “Open in Neovim”, the live cursor and other editor-only UI when there is no editor.
- Keep the Neovim backend working exactly as before.

## Out of scope

- Any mutation: no stage, discard, commit, checkout or merge. That is part 3.
- The Purrage mode or any Purrage view. That is part 5.
- The project crawler and Directories. That is part 4.
- Merge-conflict worktrees. They stay on the Neovim backend, or move later.
- Removing relay or the Neovim backend.

## Done when

- A local folder opens with no Neovim running and looks like a normal Ops session.
- Pull request, Changes and Tasks read the local repository.
- The same folder still works through the Neovim backend, and the two paths agree on the models.
- No editor-only control is shown in local mode.
- The local backend is testable with a temporary repository and the process/file seams, without a
  headless Neovim.

## Decided (2026-11-19, the user)

| question | answer |
|---|---|
| Change hints | **watch from the start**: one debounced watcher on the worktree and `.git`, shared with History; no timer |
| Diff parsing | **port `diffparse.lua`** line by line, relay's cases as fixtures, plus a parity test against the Neovim backend |
| `ops.exe <directory>` | **local right away**; an address still selects Neovim |
| Connect screen | **a recent list** of folders and addresses, each remembering its backend |

## Open questions

None left for this part.
