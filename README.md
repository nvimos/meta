# meta

Planning for [On-Screen Nvim](https://github.com/nvimos/onscreen): ideas, todos and their state, kept out of
the config repo. Two formats, each for what it does best:

- `backlog/`: [Backlog.md](https://github.com/MrLesk/Backlog.md), every item: one Markdown file per task
  with a YAML header (status, labels, date). Open tasks in `backlog/tasks/`, finished and dropped ones in
  `backlog/archive/tasks/`, longer notes and test sessions in `backlog/docs/`. Works with the `backlog` CLI
  and board (`npm i -g backlog.md`, then `backlog board`), or as plain files.
- `openspec/`: [OpenSpec](https://github.com/Fission-AI/OpenSpec), only for work that needs a design: a
  folder per change with `proposal.md` (why, what changes, impact), `tasks.md` and spec deltas. Open changes
  in `openspec/changes/`, finished ones in `openspec/changes/archive/<date>-<id>/`, their specs merged into
  `openspec/specs/<capability>/spec.md`. Works with the `openspec` CLI (`openspec list`).

A change names its task (`Status: X (backlog TASK-<n>)`) and the task names its change (`Change:`);
`index.tsv` lists every task with its change, if any; it is generated (`tools/convert-from-nvim.py`) and not tracked. Nothing is copied into both formats.

## Build and verify are separate

A feature is often built before anyone has tried it. That state has its own status, so it doesn't
hide among the done items or the open ones:

| Status        | Meaning                                                   |
|---------------|-----------------------------------------------------------|
| `To Do`       | not started                                               |
| `In Progress` | some steps done                                           |
| `Needs Test`  | built, waiting to be tried by hand (the `## Verify` list) |
| `Done`        | built and tried                                           |
| `Dropped`     | not doing it                                              |

In Backlog.md the build steps are the acceptance criteria and the hands-on checks are a separate
`## Verify` section. In OpenSpec, `tasks.md` has `## 1. Build` and `## 2. Verify`.

## Scan

`make help` lists the targets (pwsh, Windows):

- `make open`: open tasks, by status
- `make review`: what waits to be tried, with the verify steps
- `make doing`: what is in progress, with the open steps
- `make status S='To Do'`: one status, with details

Without make: `python tools/scan.py 'Needs Test' --details`.

## Where it came from

Converted on 2026-11-10 from the config's `todo-ideas.md`, `todo-2026-neovim011.md`, `todo-2027.md`,
`todo-2028.md` and `todo-ideas/` by `tools/convert-from-nvim.py`; those files are in `legacy/`, with the
squash files (rankings and estimates of the auto-todo runs). On 2026-11-11 the rest followed: the
config's `todo-2026.md`, `todo-done/`, `todo-issue/` and `todo-test/` are in `legacy/nvim-config/`, the
solved issues grouped by area into tasks (TASK-98..113), the test notes in `backlog/docs/`, and the
duplicate tasks merged (`openspec/changes/archive/2026-11-11-planning-in-meta/`).
