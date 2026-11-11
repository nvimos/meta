---
id: TASK-21
title: 'zen modes: switch between layouts by task'
status: Needs Test
assignee: []
created_date: '2026-11-05'
labels:
  - todo-ideas
  - ideas-october
  - todo-2026-neovim011
  - release-v2026
dependencies: []
ordinal: 21000
---

## Description

zen modes: switch between layouts by task

Change: `openspec/changes/zen-layouts-by-task/`

- z1: only the code
- z2 (or a new key): digging, debugging, jumping around code: sidebars (aerial), dropbar and the like shown
- today: lua/genja/map-plugin/zenmode.lua, z1 width 120, z2 width 80 + relnum + maximized, z0 off; both hide diagnostics
- open: keep z1/z2 as they are and add z3 for the debug layout, or redefine z2?
- decided 2026-11-05 (`backlog/docs/doc-8 - php-debug.md`): z1 reading and prose (usable for anything);
  z2 some UI: limited diagnostics, max-width line; z3 UI heavy, debug panes as splits in the z3 view
  (not a separate tab; outside z3 the debug tab default stays).
- open questions 2026-11-05 (parked by user): zen-mode's float hides other windows, so z3 can't
  hold debug splits beside it.
  1. z3 = no zen float, maximized, number + relnum, colorcolumn, all diagnostics, debug UI as splits in the current tab?
  2. z3 debug UI: dap-ui or dap-view?
  3. z3 opens the debug UI at once, or on the first stop (as splits)?
  4. z2 today turns diagnostics off; change to diagnostics on with the limit?

From `todo-ideas.md`, section "ideas october".
- v2026 release checklist item 10 (was TASK-50): zen layouts by task (z1 code only, a digging/debug layout)

## Acceptance Criteria

- [x] #1 z0 restores the window size in nvim-qt: a wait between frameless and maximize (98aa8a4)

## Branch

Built 2026-11-05 and 2026-11-10 on `PR-zen-z3` in the config repo (e371803, c0ae83d, 58289ea), not merged yet:
z3 debug layout, z2 with limited diagnostics, z0 restores; z3 maximizes nvim-qt, no colorcolumn.

## Verify

- [ ] the test session in the branch's `todo-test/zen-modes.md` (guided, one step per question)
- [ ] merge the branch into the working branch

## Original notes

```markdown
- [ ] zen modes: switch between layouts by task (not thought through yet, 2026-11-05)
  - z1: only the code
  - z2 (or a new key): digging, debugging, jumping around code: sidebars (aerial), dropbar and the like shown
  - today: lua/genja/map-plugin/zenmode.lua, z1 width 120, z2 width 80 + relnum + maximized, z0 off; both hide diagnostics
  - open: keep z1/z2 as they are and add z3 for the debug layout, or redefine z2?
  - decided 2026-11-05 (todo-test/php-debug.md): z1 reading and prose (usable for anything);
    z2 some UI: limited diagnostics, max-width line; z3 UI heavy, debug panes as splits in the z3 view
    (not a separate tab; outside z3 the debug tab default stays).
  - open questions 2026-11-05 (parked by user): zen-mode's float hides other windows, so z3 can't
    hold debug splits beside it.
    1. z3 = no zen float, maximized, number + relnum, colorcolumn, all diagnostics, debug UI as splits in the current tab?
    2. z3 debug UI: dap-ui or dap-view?
    3. z3 opens the debug UI at once, or on the first stop (as splits)?
    4. z2 today turns diagnostics off; change to diagnostics on with the limit?
  - [x] z0 restores the window size in nvim-qt: a wait between frameless and maximize (98aa8a4)
```
