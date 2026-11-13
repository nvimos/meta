---
id: TASK-108
title: 'which-key, keymaps, mouse and layouts'
status: Needs Test
assignee: []
created_date: '2026-10-25'
labels:
  - nvim-config
  - keys
  - from-config
dependencies: []
ordinal: 108000
---

## Description

Finished work on keys, 2026-10-25 .. 2026-11-09: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-15 - guide-mouse-morning.md`: Mouse: right-click per filetype, clickable statusline, :Morning (#30/31)
  - `backlog/docs/doc-16 - guide-popup-actions.md`: Right-click entry for the `g.` menu (idea 17b)
  - `backlog/docs/doc-24 - guide-aerial-outline-keys.md`: Outline keys under `<leader>o` (aerial)
  - `backlog/docs/doc-32 - guide-map-plugin-health.md`: map-plugin: miss log and :checkhealth
  - `backlog/docs/doc-40 - guide-popup-submit-keys.md`: Commit and ask popups: submit keys that work in Windows Terminal
  - `backlog/docs/doc-47 - guide-which-groups-test.md`: Test: which-key groups vs mappings
  - `backlog/docs/doc-48 - guide-which-key-helix.md`: which-key: helix layout

## Acceptance Criteria

- [x] #1 telescope-keymaps: `<M-r>` after `<M-f>`/`<M-x>` went back to the full list (2026-10-25; `solved-26.10.25-00.07-keymaps-rotate-refine.md`)
- [x] #2 map-plugin: unit tests for the miss log and :checkhealth (2026-10-25; `solved-26.10.25-00.07-map-plugin-tests.md`)
- [x] #3 keymaps: `<leader>ei` portable and tab-local (2026-10-25; `solved-26.10.25-16.41-edit-init-map.md`)
- [x] #4 mouse: remove nvims default "How-to disable mouse" popup item (2026-10-25; `solved-26.10.25-16.41-popup-menu.md`)
- [x] #5 keys: <leader>ts toggles spelling (2026-10-28; `solved-26.10.28-23.12-spell-toggle.md`)
- [x] #6 which-key: helix layout, modern and narrow classic to try (2026-10-29; `solved-26.10.29-22.26-which-key-helix.md`)
- [x] #7 which-key: window at the left edge, more group labels (2026-10-29; `solved-26.10.29-22.49-which-key-groups.md`)
- [x] #8 which-key: fixed popup height so the centred box stops jumping (2026-10-29; `solved-26.10.29-22.59-which-key-height.md`)
- [x] #9 keymaps: <C-BS> on the command line deletes a word backwards (2026-10-31; `solved-26.10.31-06.53-cmdline-ctrl-bs.md`)
- [x] #10 map: mouse clicks do what the pointer is on (2026-11-09; `solved-26.11.09-23.43-mouse-clicks.md`)
- [x] #11 popup: the right-click menu in one file, with submenus (2026-11-09; `solved-26.11.09-23.43-right-click-menu.md`)
- [x] #12 which keys (closed 2026-10-23) (undated; `ideas-26-which-keys.md`)
- [x] #13 improve: key maps map-plug (undated; `ideas-38-map-plugin-health.md`)
- [x] #14 <leader>oO opens the same ui as <leader>mO (undated; `ideas-40-aerial-outline-keys.md`)
- [x] #15 custom keymap logger: count which keys/binds I use more than others (undated; `ideas-57-keymap-logger.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: `<leader>ei` opens lua/genja/ in a new tab, cwd changes only in that tab (`solved-26.10.25-16.41-edit-init-map.md`)
- [ ] test: right click, the item and separator are gone (`solved-26.10.25-16.41-popup-menu.md`)
- [ ] test: <leader>ts twice (`solved-26.10.28-23.12-spell-toggle.md`)
- [ ] test: `:echo foo bar` then <C-BS> leaves `:echo foo ` (`solved-26.10.31-06.53-cmdline-ctrl-bs.md`)
- [ ] test: click a quickfix entry from another window, a closed fold, a menu item; side buttons (`solved-26.11.09-23.43-mouse-clicks.md`)
- [ ] test: `:Unsaved`, click and right-click a row (`solved-26.11.09-23.43-mouse-clicks.md`)
- [ ] test: right-click in markdown, oil, an LSP buffer and a visual selection; open the LSP submenu (`solved-26.11.09-23.43-right-click-menu.md`)
