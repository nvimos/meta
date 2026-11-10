Project: Folio, a Linear-style workspace for OpenSpec and Backlog.md, inside the Nvim-backed review app

Add a project-management part to the Flutter desktop app from `flutter.md` (the GitHub Desktop-style
review app, `~/es/nvimos-poc-frontend`). It turns a repo's planning files into an app that feels like
Linear: dense, calm, everything clickable, nothing that looks like Markdown. Same app, same Neovim
connection, same backend plugin (`~/es/nvimos-poc-backend`); a third mode next to "Pull request"
and "Changes". "Folio" is the working name from the mock-up.

Why

OpenSpec (Fission-AI) has each change agreed on before code is written: proposal, spec deltas
(ADDED / MODIFIED / REMOVED requirements), design note and task list, archived into a living spec.
The AI writes most of it, but the human loop (read, approve, archive; four files per change, delta
syntax, slash commands) is cumbersome, and OpenSpec Desktop is an early macOS-only beta. Backlog.md
(MrLesk) is the lighter cousin: one Markdown file per task, a terminal kanban (`backlog board`) and a
local web UI (`backlog browser`), but no record of how the system's behavior changed.

The two have different jobs, and this repo (`~/es/nvimos-meta`) already uses both side by side:
- Backlog.md tracks what to do. It is the closest match to how I worked before (`legacy/`: a running
  log of dated bullets grouped by year, with commit hashes and "tested" / "untested" notes).
- OpenSpec records what a change does to the system. Use it for changes that touch behavior across
  files or languages (e.g. PHP and Go out-of-the-box defaults: which LSP and completion behaviors
  changed), not for one-line keybinding tweaks. The living spec is what I trust when I come back to
  the project in three months, instead of the chat history or five thousand lines of config.

Core use case

In the evening I triage: pick tasks for agents tonight, approve the drafted proposals. In the morning
the inbox shows what moved; I open each task, review its agent branch in the Pull request view, try
it by hand from its Verify list, and mark it Needs Test, Done or back to In Progress. Finished
changes get archived into the living spec. Anything I want to edit opens in Neovim.

Look and feel: inspired by Linear

Take Linear's ideas, not its name, logo or assets.
- Layout: a sidebar (projects / sources, milestones, views), the issue list as the main pane, and a
  detail panel that slides in from the right instead of a separate page.
- Density with calm: tight rows, muted chrome, one strong accent color, status and priority icons.
  Dark theme first.
- A triage inbox as the default view: what changed since I last looked, and what needs attention.
- Everything is a record you can open: changes, tasks, requirements, milestones, living specs,
  legacy notes, file paths. Every id, link and reference is clickable.
- No Markdown look anywhere. Render each field as its own typed element: the proposal as short
  paragraph blocks, spec requirements as cards with an Added / Modified / Removed pill (not +/- diff
  lines), scenarios inside the card, tasks as a checklist, dates and statuses as badges.
- Keyboard for everything, mouse still first-class: J / K move, Enter opens, Esc closes, C creates,
  / searches, Ctrl+K command palette.
- Every change is instant in the UI and written to the files right after.

Screens

1. Inbox / dashboard: OpenSpec changes grouped Draft / Active / Completed with progress bars;
   Backlog tasks grouped by status; a "Needs attention" list: stale active changes, in-progress
   tasks with no linked change, legacy items still marked untested, tasks whose branch has
   unreviewed commits. Quick actions: new change, new task, run `openspec view` / `list` / `status`.
2. Issue list and board: all tasks, grouped by status, priority, label or milestone; saved views
   ("Needs Test", "agent tonight"); filters and search.
3. Change detail: name, status badge, dates, links to its Backlog tasks; tabs Proposal, Spec,
   Design, Tasks. Spec tab: requirement cards with pills. Tasks tab: a live checklist that writes
   back to tasks.md, Build and Verify kept apart. Actions: Archive into spec, Open in Neovim, View
   raw.
4. Task detail: title, status, priority, labels, linked change, description, acceptance criteria,
   definition of done, Verify steps; a move-to-next-status button; its branch and "Review".
5. Spec browser: the living spec as a tree of capabilities and requirements with search; clicking a
   requirement shows every change that ever touched it.
6. Legacy viewer: the old notes, read-only, grouped by year, with search and a "Promote to task"
   button per bullet that pre-fills a new task file.

Milestones: dated sections in a `milestones.md`, or derived from OpenSpec archive dates, so a
milestone is "everything archived between these two points". No database.

Data (files in the repo)

This repo's layout is the reference:
- Backlog.md: `backlog/tasks/task-<n> - <slug>.md`, YAML header (id, title, status, labels,
  priority, created_date, dependencies, ordinal) and sections (Description, acceptance criteria,
  `## Verify`, Original notes); finished and dropped in `backlog/archive/tasks/`.
- OpenSpec: `openspec/changes/<id>/proposal.md` (Status line naming its `TASK-<n>`), `tasks.md`
  (`## 1. Build`, `## 2. Verify`), `design.md`, `specs/<capability>/spec.md` deltas; archive in
  `openspec/changes/archive/<date>-<id>/`; living spec in `openspec/specs/`; `openspec/config.yaml`.
- `index.tsv` links tasks and changes; `legacy/` holds the old notes.
- Statuses: To Do, In Progress, Needs Test (built, waiting to be tried by hand), Done, Dropped.
A repo may have only one of the two formats; support each alone and link them when both exist.

Tie-in with the review app
- A task links to a branch (its `TASK-<n>` or change id in the branch name or commits, or set by
  hand). The card shows the branch, commit count and unreviewed state.
- "Review" opens the Pull request view for that branch against main, with the Verify list beside
  the diff, so trying and ticking happen in one place. The PR view links back to the task.

Agents
- "New change" from one sentence: start an agent (Claude Code headless, OpenSpec propose
  instructions) that drafts proposal, deltas, design and tasks; the app shows them for approval.
- Show the state of agent work per task when the branch or a log tells it; no orchestration beyond
  starting one.

Architecture: hybrid data layer
- Content from files: a repo service walks `openspec/changes`, `openspec/specs`, `backlog/tasks`
  and `legacy/`, parses Markdown and YAML (deltas split on the ADDED / MODIFIED / REMOVED headers)
  and caches typed models.
- Aggregates from the CLIs: `openspec view`, `list` and `status` with `--json` (progress, missing
  artifacts), merged into the cached models on a timer or on refresh. The UI never waits on a CLI for
  content it can already show. If a CLI is missing, the app still works from the files.
- As in `flutter.md`, all of it runs through Neovim: the backend plugin gets `tasks.*` functions
  (list, read, write, archive, CLI calls) next to `git.*`; file edits go through Neovim buffers;
  the backend's file and git events give live updates within a second or two.
- Writes keep the files as a human or the CLIs would write them: no reformatting of untouched
  parts. Where a CLI does the action (`openspec archive`, `backlog task edit`), call it.

Non-goals for the first version
- Our own task format, a database or a server; sync with GitHub Issues, Jira or Linear itself.
- Editing prose inside the app (beyond checkboxes, status, priority, labels); that happens in Neovim.
- Multiple repos, users or permissions; time tracking, estimates, sprint planning.
- Agent orchestration beyond "start one for this change".

Deliverable for the POC

A "Tasks" mode in the review app that:
- Shows this repo's changes and tasks in a Linear-style sidebar, list and detail panel, with no raw
  Markdown,
- Has the inbox with "Needs attention", requirement cards with pills, and live checklists,
- Archives a finished change into the living spec and shows which changes touched a requirement,
- Promotes a legacy note into a task,
- Opens the Pull request view for a task's branch with its Verify list beside the diff,
- Opens any record's file in Neovim at the line,
- Picks up changes made in Neovim or by an agent within a second or two.

Order: read-only list and detail on this repo's files, then statuses, checkboxes and keyboard, then
the inbox and "Needs attention", then branch link and review tie-in, then archive and spec browser,
then legacy promote and milestones, then "New change" with an agent.

Source: Grok conversation "OpenSpec Inquiry"
<https://grok.com/share/bGVnYWN5_08dd64e6-2dfd-4a0a-a318-3707097cdc52> (full text in the print
`poc-project-man.pdf`), including its HTML prototype and the "Folio" mock-up, neither of which is
saved here.
