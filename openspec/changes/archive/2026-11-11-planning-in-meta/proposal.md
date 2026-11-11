# Planning in nvimos-meta

Status: Done (backlog TASK-94)

## Why

The todo files lived in the config repo and were mirrored into both Backlog.md and OpenSpec to compare
the formats. Two copies of every item drift, and the config kept writing new todo files.

## What Changes

- 2026-11-10: todo-ideas.md, todo-202x.md, the squash files and todo-ideas/ moved to `legacy/`
- 2026-11-11: the config's todo-2026.md, todo-done/, todo-issue/ and todo-test/ moved to
  `legacy/nvim-config/`; solved issues grouped by area into Backlog.md tasks (TASK-98..113);
  test notes into `backlog/docs/`
- duplicates merged: the v2026 checklist items into their idea tasks, fourteen "extras" batches into one
- OpenSpec keeps only design-shaped changes; the mirrored changes removed
- `/close-issues` writes Backlog.md tasks here

## Impact

- config commits 35103bf and the 2026-11-11 move; this repo's README, `index.tsv`, `openspec/config.yaml`
