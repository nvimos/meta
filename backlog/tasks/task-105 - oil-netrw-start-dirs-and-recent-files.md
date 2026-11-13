---
id: TASK-105
title: 'oil, netrw, start dirs and recent files'
status: Needs Test
assignee: []
created_date: '2026-10-24'
labels:
  - nvim-config
  - files
  - from-config
dependencies: []
ordinal: 105000
---

## Description

Finished work on files, 2026-10-24 .. 2026-11-07: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-12 - guide-genja-recent.md`: genja-recent: recent files by frecency (#35)
  - `backlog/docs/doc-18 - guide-startdirs.md`: Start dirs plugin (idea 36)
  - `backlog/docs/doc-35 - guide-startdirs-frecency.md`: Start dirs ranked by frecency
  - `backlog/docs/doc-46 - guide-unsaved-picker.md`: Unsaved buffers picker (2026-10-29)
  - `backlog/docs/doc-50 - guide-netrw-nvim.md`: netrw.nvim: icons in netrw (2026-10-31)
  - `backlog/docs/doc-67 - guide-genja-oily.md`: genja-oily.nvim: .oily moved into its own plugin

## Acceptance Criteria

- [x] #1 edit: wrap selected lines as "line", (2026-10-24; `solved-26.10.24-17.31-wrap-lines.md`)
- [x] #2 oil: `Stardirs` typo in action descs (2026-10-24; `solved-26.10.24-17.40-startdirs-desc.md`)
- [x] #3 startdirs: `:Mydirs` opens the picker, `:Mydirs reset` deletes the usage file (2026-10-24; `solved-26.10.24-18.39-mydirs-cmd.md`)
- [x] #4 startdirs: `<M-n>` jumps should not count as a use (2026-10-24; `solved-26.10.24-18.39-startdirs-jump-nocount.md`)
- [x] #5 startdirs: `<M-1>` should open the most used dir (2026-10-24; `solved-26.10.24-18.39-startdirs-rank-jump.md`)
- [x] #6 unsaved: picker layout, E13 overwrite, :q and :x through the wrapper, tests (2026-10-30; `solved-26.10.30-01.46-unsaved-fixes.md`)
- [x] #7 explorer: :Lexplore gave E117 netrw#Lexplore (2026-10-31; `solved-26.10.31-20.02-netrw-oil.md`)
- [x] #8 oil: jump between changed entries, commit one entry (2026-11-03; `solved-26.11.03-14.10-oil-changed-jump.md`)
- [x] #9 oil: start dirs helper named for what it returns (2026-11-06; `solved-26.11.06-15.13-oil-startdirs-name.md`)
- [x] #10 oil: å opens the preview, jolemak quirk (2026-11-07; `solved-26.11.07-01.34-oil-preview-quirk.md`)
- [x] #11 oil: preview keys for jolemak (2026-11-07; `solved-26.11.07-02.10-oil-preview-keys.md`)
- [x] #12 oil: auto confirm creation of a single dir / file (undated; `ideas-06-oil-auto-confirm.md`)
- [x] #13 oil:    normal gga -> git add (undated; `ideas-07-oil-gga-git-add.md`)
- [x] #14 <S-F1>: search from oil plugin current dir. (undated; `ideas-08-s-f1-search-oil-dir.md`)
- [x] #15 oil:    hide a set of predefined folders based on PWD/.oily. (undated; `ideas-15-oil-oily-hide.md`)
- [x] #16 recent files (done 2026-10-23, untested: backlog/docs/doc-12 - guide-genja-recent.md) (undated; `ideas-35-recent-files.md`)
- [x] #17 add keys in oil to auto-add a location (item) from the list to the startdirs (undated; `ideas-36-startdirs.md`)
- [x] #18 set up a pre-write handler for this: (undated; `ideas-54-unsaved-picker.md`)
- [x] #19 consider pros and cons of adding  <https://github.com/prichrd/netrw.nvim> (undated; `ideas-55-netrw-nvim.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: V-select lines, <leader>w,; also with <C-v> (`solved-26.10.24-17.31-wrap-lines.md`)
- [ ] test: <leader>wsp, <leader>wsT (`solved-26.10.24-17.31-wrap-lines.md`)
- [ ] test: `3]c`, `[c` (`solved-26.11.03-14.10-oil-changed-jump.md`)
- [ ] test: `ggC` on a file with other changes staged: those stay staged (`solved-26.11.03-14.10-oil-changed-jump.md`)
- [ ] stale oil ids after a reload (`Entry N missing parent url`): self-heal idea in todo-2027.md (`solved-26.11.07-02.10-oil-preview-keys.md`)
