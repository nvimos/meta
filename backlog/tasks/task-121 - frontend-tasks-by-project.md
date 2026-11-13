---
id: TASK-121
title: 'frontend: tasks from the .nvimos planning folder, filtered by project'
status: Needs Test
assignee: []
created_date: '2026-11-11'
labels:
  - frontend
  - backend
dependencies: []
ordinal: 121000
---

## Description

Several repos (the nvim config, the backend, the frontend) share nvimos-meta for their planning. A
`.nvimos` file at a repo root names the folder (`tracking`) and the repo's `project` label there;
the Tasks mode reads from it and shows only that project's tasks.

## Acceptance Criteria

- [x] #1 backend `lua/nvimos/tracking.lua`: reads `.nvimos`; `files.*` and the CLI work in the planning folder; the planning watcher watches it (`test/test_12_tracking.lua`)
- [x] #2 frontend `Workspace`: `tracking`, `project`, `projectOnly`; a task belongs with its project label, or with none of `projects:` in config.yml (shared); a change goes with its task
- [x] #3 new tasks get the project label, numbers count every project's tasks; Open in Neovim opens the absolute path
- [x] #4 sidebar: "from nvimos-meta" and a pill this project / all projects; key `a`
- [x] #5 `.nvimos` in the config (nvim-config), the backend (backend) and the frontend (frontend); meta tasks labelled

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] the app on Neovim in the frontend repo: only frontend tasks and shared ones, "from nvimos-meta"
- [ ] `a` shows every project's tasks, `a` again only frontend's
- [ ] edit a task in nvimos-meta outside the app: the list follows
- [ ] the app on Neovim in the nvim config: only nvim-config tasks
