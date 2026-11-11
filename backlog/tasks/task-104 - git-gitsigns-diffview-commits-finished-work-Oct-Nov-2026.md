---
id: TASK-104
title: 'git: gitsigns, diffview, commits: finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-25'
labels:
  - git
  - from-config
dependencies: []
ordinal: 104000
---

## Description

Finished work on git, 2026-10-25 .. 2026-11-09: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

## Acceptance Criteria

- [x] #1 gitsigns: off in markdown by default, toggle per buffer (2026-10-25; `solved-26.10.25-00.07-gitsigns-skip-ft.md`)
- [x] #2 genja-commit: commit message in a split instead of a float (2026-10-31; `solved-26.10.31-20.02-commit-split.md`)
- [x] #3 genja-commit: switch the <M-g> backend on the fly (2026-11-07; `solved-26.11.07-04.10-commit-backend.md`)
- [x] #4 git: fsmonitor daemons keep handles in repos and block folder renames (2026-11-08; `solved-26.11.08-20.58-git-fsmonitor.md`)
- [x] #5 git: plain diffview, red/green sides, other diff viewers to try (2026-11-09; `solved-26.11.09-23.43-diff-viewers.md`)
- [x] #6 git: quitting nvim waited for the fsmonitor daemons to stop (2026-11-09; `solved-26.11.09-23.43-fsmonitor-detach.md`)
- [x] #7 find a free git mirror (undated; `2026-git-mirror.md`)
- [x] #8 reconfigure local git-webui (undated; `2026-git-webui.md`)
- [x] #9 move gitea definition to w11s-cut project (todo-ideas #33, skipped 2026-10-23, done 2026-10-24) (undated; `2026-gitea-to-setup.md`)
- [x] #10 git: gitsigns.nvim (Neovim): stage or reset hunks from the buffer. (undated; `ideas-09-gitsigns.md`)
- [x] #11 gitcommit: plug-wip/genja-commit.nvim (details in its CLAUDE.md) (wip) (undated; `ideas-14-gitcommit.md`)
- [x] #12 git: Neogit + gitsigns + diffview + mini.git, fugitive disabled (9126c56, dcbb29d) (undated; `ideas-37-git-neogit-gitsigns-diffview.md`)
- [x] #13 for commit and paste popups (undated; `ideas-50-popup-submit-keys.md`)
- [x] #14 f2 context: show git staged files and hunks (undated; `ideas-51-f2-git-staged.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] ~~test: a tracked .md: no signs; `<leader>mGs` twice~~ failed: `<leader>mGs` didn't attach (2026-10-25) (`solved-26.10.25-00.07-gitsigns-skip-ft.md`)
- [ ] test: a tracked .md: no signs; `<leader>mGs`: signs; again: gone (`solved-26.10.25-00.07-gitsigns-skip-ft.md`)
- [ ] test: <leader>mGc opens the bottom split with winbar hints (`solved-26.10.31-20.02-commit-split.md`)
- [ ] test: leave and come back: still open; q/<Esc> close, reopen keeps the draft; <C-s> commits (`solved-26.10.31-20.02-commit-split.md`)
- [ ] test: commit popup, <M-r> until ollama, then <M-g> writes a message (`solved-26.11.07-04.10-commit-backend.md`)
- [ ] test: open a file in a repo with `core.fsmonitor=true`, run git status, `:GitFsmonitorStop` prints `stopped <repo>` (`solved-26.11.08-20.58-git-fsmonitor.md`)
- [ ] test: quit nvim, check no `git fsmonitor--daemon` process is left for that repo (`solved-26.11.08-20.58-git-fsmonitor.md`)
- [ ] open: repos only visited by Neogit or lazy without a buffer or `:cd` are not recorded (`solved-26.11.08-20.58-git-fsmonitor.md`)
- [ ] test: `:Lazy install`, then `:DiffviewOpen v2026...develop`: labels, colors, `<leader>mGd`, j/k preview (`solved-26.11.09-23.43-diff-viewers.md`)
- [ ] test: F2 in an oil buffer of a repo: `diffview open`, codediff, unified, deltaview items (`solved-26.11.09-23.43-diff-viewers.md`)
- [ ] open: keep one or two viewers, drop the rest (`solved-26.11.09-23.43-diff-viewers.md`)
- [ ] test: quit nvim in a repo with `core.fsmonitor=true`: no delay, no daemon left for that repo (`solved-26.11.09-23.43-fsmonitor-detach.md`)
