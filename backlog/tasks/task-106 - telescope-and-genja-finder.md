---
id: TASK-106
title: 'telescope and genja-finder'
status: Needs Test
assignee: []
created_date: '2026-10-25'
labels:
  - nvim-config
  - telescope
  - from-config
dependencies: []
ordinal: 106000
---

## Description

Finished work on telescope and genja-finder, 2026-10-25 .. 2026-11-09: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-17 - guide-refine-exclude.md`: Telescope refine: `<M-x>` exclude (idea 25)
  - `backlog/docs/doc-20 - guide-telescope-keymaps.md`: Telescope keymaps: refine keys and desc groups (#26b)
  - `backlog/docs/doc-36 - guide-telescope-explore.md`: Telescope: usability exploration (spec, open questions) + key footer prototype
  - `backlog/docs/doc-43 - guide-telescope-default-keys.md`: Telescope: default keys to switch off, and named keys in `<C-/>`

## Acceptance Criteria

- [x] #1 telescope: key footer prototype and exploration spec (2026-10-25; `solved-26.10.25-00.07-telescope-footer.md`)
- [x] #2 genja-finder: `<M-Up>` rescans in the parent dir, one-off (2026-10-25; `solved-26.10.25-12.41-finder-parent-dir.md`)
- [x] #3 genja-finder refine: shorter key descs, no notify on `<M-n>` before `<M-f>` (2026-10-25; `solved-26.10.25-12.41-refine-descs.md`)
- [x] #4 telescope: footer removed, key help in the empty results kept (2026-10-25; `solved-26.10.25-12.41-telescope-virthelp.md`)
- [x] #5 genja-finder: `<C-]>` opens the entry in pickers (2026-10-25; `solved-26.10.25-16.41-telemap-open.md`)
- [x] #6 genja-finder: <C-]> on a directory entry opens the entry itself (2026-10-26; `solved-26.10.26-23.48-finder-dir-entry.md`)
- [x] #7 ui-select: <CR> in the telescope dropdown reported cancel before the pick (2026-10-28; `solved-26.10.28-22.34-ui-select-cr.md`)
- [x] #8 ui-select: legendary dropdown a third bigger, mylunsj back to dropdown size (2026-10-29; `solved-26.10.29-22.49-legendary-size.md`)
- [x] #9 telescope: a picker can replace the prompt hint (2026-10-30; `solved-26.10.30-01.46-telescope-hint.md`)
- [x] #10 telescope: key help missing in insert mode for pickers without normal-mode maps (2026-10-31; `solved-26.10.31-20.02-virthelp.md`)
- [x] #11 telescope: `<leader>` opens oldfiles (2026-11-03; `solved-26.11.03-14.02-oldfiles-key.md`)
- [x] #12 genja-finder: <M-t> opens marked or selected entries in tabs, picker stays (2026-11-06; `solved-26.11.06-15.13-finder-tabs.md`)
- [x] #13 ccc: picker keys closer to habit (2026-11-09; `solved-26.11.09-23.43-ccc-keys.md`)
- [x] #14 genja-finder.nvim: move live grep/find and their togglers into (undated; `ideas-01-genja-finder.md`)
- [x] #15 code actions - view in telescope (undated; `ideas-12-code-actions-telescope.md`)
- [x] #16 context-sensitive telescope dropdown on <F2> (closed 2026-10-23: all sub-items done, tests green) (undated; `ideas-18-f2-context.md`)
- [x] #17 telescope: picker keys to the location/quickfix list (<M-l/q> marked, <M-L/Q> append, (undated; `ideas-22-telescope-list-keys.md`)
- [x] #18 urlview.nvim: visual gx and <leader>gx pick URLs, <Tab> marks, <CR> opens all marked (a9ef21d, 4a3aed3, 082fd2d) (undated; `ideas-23-urlview.md`)
- [x] #19 telescope refine decorator in steps (undated; `ideas-25-telescope-refine.md`)
- [x] #20 telescope: mousability (closed 2026-10-23) (undated; `ideas-30-31-mouse.md`)
- [x] #21 telescope (undated; `ideas-53-telescope-explore.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: `<leader>jM`, `<F1>`, `<C-F1>`: the footer line (`solved-26.10.25-00.07-telescope-footer.md`)
- [ ] answer the spec questions (`solved-26.10.25-00.07-telescope-footer.md`)
- [ ] test: `<F1>`, `<M-Up>` twice, `<M-r>`: back on the root cycle; `<M-Up>` at the drive root notifies (`solved-26.10.25-12.41-finder-parent-dir.md`)
- [ ] test: key help in `<F1>` shows the short descs; `<M-n>` before `<M-f>` does nothing (`solved-26.10.25-12.41-refine-descs.md`)
- [ ] test: `<leader>jM`, `<F1>`, `<C-F1>`: table shows before input, goes on typing, back on no results (`solved-26.10.25-12.41-telescope-virthelp.md`)
- [ ] test: `<C-]>` in a picker opens the selected file (`solved-26.10.25-16.41-telemap-open.md`)
- [ ] add the key to readme.cheatsheet.md (`solved-26.10.25-16.41-telemap-open.md`)
- [ ] test: F2 or a find picker, select a dir, `<C-]>`: oil opens that dir (`solved-26.10.26-23.48-finder-dir-entry.md`)
- [ ] test: :LspRestart powershell_es, rename, pick "I accept"; rename goes through (`solved-26.10.28-22.34-ui-select-cr.md`)
- [ ] test: <leader>ca code action still runs once (`solved-26.10.28-22.34-ui-select-cr.md`)
- [ ] add `<leader>'` to `readme.cheatsheet.md` (`solved-26.11.03-14.02-oldfiles-key.md`)
- [ ] test: <F1> grep, <Tab> two results, <M-t>; both tabs open at their line, picker still open (`solved-26.11.06-15.13-finder-tabs.md`)
- [ ] test: `<leader>ic`, then `?`, `<Tab>`, `a`, `<Esc>` (`solved-26.11.09-23.43-ccc-keys.md`)
