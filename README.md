# meta

Planning for [On-Screen Nvim](https://github.com/nvimos/onscreen): ideas, todos and their state, kept out of
the config repo. The same backlog is here twice, in two task formats, to compare them and keep one
(or both):

- `backlog/`: [Backlog.md](https://github.com/MrLesk/Backlog.md), one Markdown file per task with a YAML
  header (status, labels, date). Open tasks in `backlog/tasks/`, finished and dropped ones in
  `backlog/archive/tasks/`, longer notes in `backlog/docs/`. Works with the `backlog` CLI and board
  (`npm i -g backlog.md`, then `backlog board`), or as plain files.
- `openspec/`: [OpenSpec](https://github.com/Fission-AI/OpenSpec), one folder per change with
  `proposal.md` (why, what changes, impact) and `tasks.md`. Open changes in `openspec/changes/`, finished
  ones in `openspec/changes/archive/<date>-<id>/`. Works with the `openspec` CLI (`openspec list`).

Each OpenSpec change names its Backlog.md task (`TASK-<n>`); `index.tsv` lists both side by side.

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
`todo-2028.md` and `todo-ideas/` by `tools/convert-from-nvim.py`. Every task keeps its original text
under "Original notes". The original files are in `legacy/`, as they were, with the squash files
(rankings and estimates of the auto-todo runs).
