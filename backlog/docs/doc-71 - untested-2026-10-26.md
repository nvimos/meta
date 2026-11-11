---
id: doc-71
title: 'Untested features, 2026-10-26'
type: guide
created_date: '2026-10-26'
---

# Untested features, 2026-10-26

For a later guided session: one feature per question. Each line: feature,
key or command to try, file, guide. Older ones: backlog/docs/doc-70 - untested-2026-10-24.md.

## Session auto-todo-20261026-2311

- [ ] checkmake: no minphony warnings, `:w` a Makefile (lint/checkmake.ini, lua/genja/ext/lint.lua) -> backlog/docs/doc-38 - guide-checkmake-config.md
- [ ] popups: `<C-s>` / `<M-CR>` submit in the commit popup (`<leader>mGc`) and the ask popup (`<M-?>`) (plug-wip/genja-commit.nvim, plug-wip/genja-ask.nvim) -> backlog/docs/doc-40 - guide-popup-submit-keys.md
- [ ] telescope: `<C-/>` in a picker shows your keys by desc; uncomment one key in either default list (after/plugin/telescope-after.lua, lua/lazyp/new/genja-finder.lua) -> backlog/docs/doc-43 - guide-telescope-default-keys.md
- [ ] claude marker: `:ClaudeFtermMarkerToggle` off/on, `:ClaudeFterm` starts new; `/rename` in a .txt file writes `!!` marker (plug-wip/genja-claudefterm.nvim) -> backlog/docs/doc-41 - guide-session-marker-toggle.md
- [ ] F2 git staged: oil, `<F2>`, `staged (N files)`, `<C-p>` cached diff, `<CR>` unstages (lua/genja/f2/collect/git.lua) -> backlog/docs/doc-39 - guide-f2-git-staged.md
