# backend seam for a second repository backend

Tags: integrate-purrage
Status: Needs Test (approved and built on 2026-11-19; the task waits for the user's test; see doc-76). Part 1 of 5 in the Purrage integration.
Tasks: TASK-154.

## Why

Ops reaches the repository only through `Backend` in `lib/backend/backend.dart`: one concrete class
that owns the Neovim RPC connection, the relay plugin calls and the event stream. Every mode depends
on it. That is why the app cannot work without Neovim and the relay plugin, even though almost
everything it asks for is git, files or processes.

Ops already hides part of that: `ops.exe <directory>` starts a headless Neovim in the folder on a
free loopback port (`lib/state/nvim_launcher.dart`), and finds the relay checkout next to the app or
in `~/ws`. So the problem is not that the user has to start Neovim by hand. It is the dependency
itself: an `nvim` on the machine, a relay checkout the launcher can find, the start-up and RPC cost
of every call, and an editor process kept alive for work that needs none.

The calls divide unevenly:

- 38 feature calls in `Backend`
- only three are editor calls: `open`, `show`, and the unused `getText`
- the rest are git, merge worktrees, file reads and writes, jobs, directories and `.nvimos` tracking;
  of these, `dirs` (genja-startdirs, `v:oldfiles`), `cd` and `pluginRoot` read Neovim's own state
  and need a local answer of their own
- `Session` attaches four event domains: `buffers`, `windows`, `git` and `jobs`; only `windows`
  (the cursor), `git` (refresh hints) and `jobs` are used, `buffers` is ignored, and `diagnostics`
  is not attached

A second backend needs a seam, not a rewrite of the modes.

## The idea

Split today's `Backend` into two pieces:

- `RepoBackend` — the repository operations the modes need: repository info, branches, log, diff,
  status, stage/discard, commit, checkout/merge/rebase, file list/read/write, jobs, tracking
- `EditorSession` — optional editor operations: open a file at a line, show a revision read-only,
  the live cursor and the current buffer text

The existing implementation becomes `NvimBackend`, wrapping the same relay calls and event stream.
It is still the only implementation at the end of this proposal; nothing user-visible changes.

`Session` holds a `RepoBackend` and an optional `EditorSession`. UI that needs an editor checks for
the capability and hides or disables the editor-only parts when it is absent. The Connect screen is
not changed yet.

## Scope

- Extract the interface from the current class; keep the models in `lib/backend/models.dart`.
- Keep `NvimBackend` behaviour identical, including the handshake, API version, event ordering and
  resync.
- Express the optional editor capability so the mode code does not ask `session.backend` for
  `open`/`show` when there is no editor.
- Keep the `Session.run((b) => ...)` shape the state classes already use.

## Out of scope

- Any local implementation; that is part 2.
- Any change to the Connect screen, the mode rail or the UI.
- Removing Neovim. The Neovim backend stays for local and remote use throughout the programme.

## Done when

- The app behaves exactly as before, against the same relay plugin.
- The existing tests pass without changes to their expectations.
- No mode calls the concrete RPC class directly.

## Decided (2026-11-19, the user)

| question | answer |
|---|---|
| Interfaces | **two**: `RepoBackend`, and an `EditorSession` that is null without an editor, so the compiler stops a mode calling `open`/`show` unchecked; `NvimBackend` implements both |
| Event stream | **split by owner**: `RepoBackend` emits git hints and jobs, `EditorSession` emits the cursor; `NvimBackend` keeps one RPC stream with seq and resync underneath |
| Status bar without an editor | **nothing**: the cursor area is simply absent, no badge and no button |

## Open questions

None left for this part.
