# hidden modes and panes stay idle

Tags: performance
Status: Draft, for TASK-192.

## Why

The shell keeps every mode built in an `IndexedStack`, so a mode keeps its state and scroll when
you come back. But "built" has come to mean "working": each state listens to the backend's git
hints and re-queries what it shows, whether it is on screen or not ("a git hint from the backend
makes each state re-query what it shows"). With nine modes, one save in Neovim can set off RPCs,
git calls and rebuilds for eight screens nobody looks at. The same holds for panes inside a mode
that a switch or a toggle hides.

It is the I/O side of the rule in CLAUDE.md, *proportional work*: an interaction, or an outside
event, costs in proportion to what it changes on screen.

## The idea

- A hidden mode or pane does no work. When an event would make it re-query, it only marks itself
  stale.
- When it is shown again, a stale part refreshes once, before or right after its first frame; a
  part that is not stale shows what it had, with no call at all.
- What stays live while hidden is named, with a reason: the status store (shared by Changes and
  Add and Ignore, and the source of the badges), the jobs, the connection, anything the rail or
  the status bar shows.
- The ignore and preview panes of Add and Ignore are the first case (change `ops-ignore-pane`);
  this change carries the logic to the rest.

## Where it applies

To be checked mode by mode, applicable or not:

- Pull request: branches, commits, the diff of the selected file
- Changes: the diff of the selected file (the lists come from the shared status store)
- Add and Ignore: done in `ops-ignore-pane`
- Tasks: the workspace reload on git hints, the inbox count (the count may need to stay live if a
  badge shows it)
- Repos: the crawl and the hints
- Settings, Log, Help: likely nothing to do
- panes: the review panel, the preview of other modes, the network dialog

## Technical notes

- One small building block, not nine copies: a `Visibility`-aware mixin or a `ValueListenable<bool>`
  "shown" per mode, set by the shell from the `IndexedStack` index (it already knows it for the
  `ExcludeSemantics` flags), and a `markStale()` / `refreshIfStale()` pair in the states.
- A state's git-hint listener calls `shown ? refresh() : markStale()`.
- Tests: a git hint while hidden makes no backend call (a counting fake backend), showing the mode
  makes exactly one; a mode that was not stale makes none.
- Measure before and after with the `rpc <module>.<fn>` timings: calls per git hint, while working
  in one mode.
