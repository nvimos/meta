---
id: TASK-110
title: 'color adjustments'
status: Needs Test
assignee: []
created_date: '2026-10-24'
labels:
  - nvim-config
  - look
  - from-config
dependencies: []
ordinal: 110000
---

## Description

Finished work on look, 2026-10-24 .. 2026-11-08: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-19 - guide-tabline-click.md`: Tabline: resizing nvim-qt walked to the last tab (idea 32)
  - `backlog/docs/doc-22 - guide-winsize.md`: Window sizes (idea 28)
  - `backlog/docs/doc-23 - guide-wrapfold.md`: Fold markers with a title (idea 29b)
  - `backlog/docs/doc-34 - guide-messages.md`: :Messages and F2: jump from errors in :messages to file:line
  - `backlog/docs/doc-37 - guide-zen-toggles.md`: Zen toggles: switching, size memory, diagnostics limit
  - `backlog/docs/doc-51 - guide-aerial-follow.md`: aerial sidebar follows the file (2026-11-05)
  - `backlog/docs/doc-61 - guide-colorcolumn.md`: colorcolumn on/off (2026-11-10)

## Acceptance Criteria

- [x] #1 intro: `~` in column 0 of the intro lines, vanilla look (2026-10-24; `solved-26.10.24-08.19-intro-tilde.md`)
- [x] #2 gui: nvim-qt toggles from keys, picker, right-click, F2 (2026-10-24; `solved-26.10.24-17.31-gui-toggles.md`)
- [x] #3 hilite: darker Search/IncSearch/CurSearch background (2026-10-24; `solved-26.10.24-17.31-search-colors.md`)
- [x] #4 ui: shorter descs for oil actions and <M-?> (2026-10-24; `solved-26.10.24-17.31-short-descs.md`)
- [x] #5 zen: <leader>z0/z1/z2 moved out of map-convoluted.lua (2026-10-24; `solved-26.10.24-17.31-zen-keys.md`)
- [x] #6 gui: test Makefile pointed at the old mylunsj path (2026-10-24; `solved-26.10.24-17.40-gui-test-path.md`)
- [x] #7 zen: <leader>z0 closes zen and stays closed (2026-10-24; `solved-26.10.24-17.40-zen-off.md`)
- [x] #8 gui: <leader>mQw and right-click frameless stopped working (2026-10-24; `solved-26.10.24-18.04-frameless-set.md`)
- [x] #9 aerial: `<leader>oO` / `<leader>oo` outline keys, `<Esc>` closes the nav float (2026-10-25; `solved-26.10.25-00.07-aerial-outline-keys.md`)
- [x] #10 messages: jump from lua traces in :messages to file:line (2026-10-25; `solved-26.10.25-00.07-messages-jump.md`)
- [x] #11 zen: z1 <-> z2 reopens, z0 restores size and diagnostics limit (2026-10-25; `solved-26.10.25-00.07-zen-toggles.md`)
- [x] #12 genja-statusline: `[Nameless]` for normal buffers without a name (2026-10-25; `solved-26.10.25-12.41-statusline-nameless.md`)
- [x] #13 hilite: matched chars in pickers use Visuals foreground, bold, no background (2026-10-25; `solved-26.10.25-12.41-telescope-matching.md`)
- [x] #14 nvim-qt: dark title bar on Windows 11 (2026-10-25; `solved-26.10.25-16.41-nvim-qt-dark.md`)
- [x] #15 statusline: plain separators in terminals, Nerd Font icons in a GUI (2026-10-26; `solved-26.10.26-23.48-statusline-glyphs.md`)
- [x] #16 dropbar: <leader>; crumb letters from jwfasrzxc (2026-10-28; `solved-26.10.28-23.12-dropbar-pivots.md`)
- [x] #17 gui: colorscheme set in init.vim, Gui* settings grouped (2026-10-28; `solved-26.10.28-23.12-gui-colors.md`)
- [x] #18 intro: :help you page (2026-10-28; `solved-26.10.28-23.12-help-you.md`)
- [x] #19 hilite: dimmer underline on markdown links (2026-10-29; `solved-26.10.29-20.53-markdown-link-underline.md`)
- [x] #20 hilite: diagnostic colours per severity (2026-10-29; `solved-26.10.29-20.56-diag-colours.md`)
- [x] #21 messages: :Messages -yank puts all of :messages into the clipboard (2026-10-30; `solved-26.10.30-01.46-messages-yank.md`)
- [x] #22 ui: :HiInspect shows highlight groups under the cursor in a split (2026-10-31; `solved-26.10.31-06.53-hi-inspect.md`)
- [x] #23 hilite: blink.cmp documentation popup colours (2026-10-31; `solved-26.10.31-10.23-blink-doc-colours.md`)
- [x] #24 hilite: diagnostic virtual text and markdown link colours (2026-10-31; `solved-26.10.31-20.02-hilite.md`)
- [x] #25 hilite: muted diagnostic underline and virtual text colours (2026-11-03; `solved-26.11.03-14.02-diag-colours.md`)
- [x] #26 zen: z0 left the nvim-qt window maximized (2026-11-05; `solved-26.11.05-20.22-zen-restore.md`)
- [x] #27 statusline: same-named files in a diff show the same winbar name (2026-11-08; `solved-26.11.08-20.58-winbar-names.md`)
- [x] #28 redefine all standard fold commands with better descriptions «Fold: …» (undated; `ideas-11-fold-descriptions.md`)
- [x] #29 json/yaml: display the outer key, or even path somewhere in the statusbar or tabbar (undated; `ideas-13-winbar-keypath.md`)
- [x] #30 find a plugin to rotate window / pane layouts (undated; `ideas-28-window-sizes.md`)
- [x] #31 bug in winbar or statusbar (fixed 2026-10-23) (undated; `ideas-32-resize-last-tab.md`)
- [x] #32 test out zen mode toggles (lua/genja/map-plugin/zenmode.lua, moved from map-convoluted.lua) (undated; `ideas-44-zen-toggles.md`)
- [x] #33 when a lua trace makes it to the :messages list (undated; `ideas-46-messages-jump.md`)
- [x] #34 <leader>; - set follow up actions to jwfasrzxc instead of abc... (undated; `ideas-52-dropbar-letters.md`)
- [x] #35 Aerial (undated; `tested-2026-10-29.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: /search, check the colors (`solved-26.10.24-17.31-search-colors.md`)
- [ ] `" Diagnosticz` comment typo (`solved-26.10.24-17.31-search-colors.md`)
- [ ] test: g? in oil, which-key on <M-?> (`solved-26.10.24-17.31-short-descs.md`)
- [ ] typo `Stardirs` -> `Startdirs`? (`solved-26.10.24-17.31-short-descs.md`)
- [ ] test: <leader>z1, <leader>z2, <leader>z0 in nvim-qt (`solved-26.10.24-17.31-zen-keys.md`)
- [ ] z0 reopens zen at width 80: should it stay closed? (`solved-26.10.24-17.31-zen-keys.md`)
- [ ] test: `<leader>oO`: the float is barely see-through (winblend 2) (`solved-26.10.25-00.07-aerial-outline-keys.md`)
- [ ] test: `:luafile` a failing file, `:Messages`, `<CR>`; `:Messages -quick` (`solved-26.10.25-00.07-messages-jump.md`)
- [ ] test: z1, z2, z1, z0 in nvim-qt (`solved-26.10.25-00.07-zen-toggles.md`)
- [ ] does setting `&columns`/`&lines` resize the nvim-qt window or only the grid? (`solved-26.10.25-00.07-zen-toggles.md`)
- [ ] test: `:enew`: statusline and winbar show `[Nameless]`; help and quickfix keep their labels (`solved-26.10.25-12.41-statusline-nameless.md`)
- [ ] test: `<F1>`, type a word: matches readable in lunaperche (`solved-26.10.25-12.41-telescope-matching.md`)
- [ ] test: Windows dark app mode, start nvim-qt with `-platform windows:darkmode=1`, title bar is dark (`solved-26.10.25-16.41-nvim-qt-dark.md`)
- [ ] test: `-stylesheet %LOCALAPPDATA%\nvim\nvim-qt.qss` with `GuiTabline 1` / `GuiScrollBar 1` (`solved-26.10.25-16.41-nvim-qt-dark.md`)
- [ ] statusline.lua: `local Dirseparator` inside the `if` shadows the outer one, so the GUI never gets its icon; drop `local` (`solved-26.10.26-23.48-statusline-glyphs.md`)
- [ ] test: nvim in Windows Terminal and in nvim-qt: separators and tab close mark (`solved-26.10.26-23.48-statusline-glyphs.md`)
- [ ] test: <leader>; shows j w f … on the crumbs (`solved-26.10.28-23.12-dropbar-pivots.md`)
- [ ] test: nvim-qt start: colours, no tabline, mouse hides while typing (`solved-26.10.28-23.12-gui-colors.md`)
- [ ] test: :help you opens it; start screen shows the line (`solved-26.10.28-23.12-help-you.md`)
- [ ] test: open a markdown file, check links show a faint grey underline; `:Inspect` on a link (`solved-26.10.29-20.53-markdown-link-underline.md`)
- [ ] test: `@markup.link.label` keeps its colour and the dim underline (`solved-26.10.29-20.53-markdown-link-underline.md`)
- [ ] test: a buffer with errors, warnings and hints reads well (`solved-26.10.29-20.56-diag-colours.md`)
- [ ] test: :HiInspect on a Lua keyword shows the @keyword chain and colours; again reuses the split (`solved-26.10.31-06.53-hi-inspect.md`)
- [ ] hi @nvim.diagnostic.float has no effect (note in the file) (`solved-26.10.31-20.02-hilite.md`)
- [ ] `DiagnosticVirtualTextError` is set twice in a row; drop the first (`solved-26.11.03-14.02-diag-colours.md`)
- [ ] test: z1, z2, z1, z0 (`solved-26.11.05-20.22-zen-restore.md`)
- [ ] test: `:DiffTool dir1 dir2` on two folders with the same file names, check both winbars show different parents (`solved-26.11.08-20.58-winbar-names.md`)
- [ ] test: normal buffer outside a diff still shows the file name only (`solved-26.11.08-20.58-winbar-names.md`)
- [ ] test: reload with `:ReloadLua genja-statusline.winbar`, then `:redrawstatus!` (`solved-26.11.08-20.58-winbar-names.md`)
- [ ] open: `winbar_extra` is flagged undefined-field by LuaLS in `winbar.lua` (old, not touched) (`solved-26.11.08-20.58-winbar-names.md`)
- [ ] confirm: resize nvim-qt by any edge, tab stays (untested list) (`ideas-32-resize-last-tab.md`)
