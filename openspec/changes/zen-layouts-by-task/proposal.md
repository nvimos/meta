# Zen layouts by task

Status: Needs Test (backlog TASK-21)

## Why

One zen mode doesn't fit every job. Reading code or prose wants nothing but the text; working wants a
little UI (limited diagnostics, a line width marker); debugging wants all of it, with the debug panes
beside the code. Today z1 and z2 differ only in width and line numbers.

## What Changes

- z1: reading and prose, usable for anything: only the text, centred
- z2: some UI: limited diagnostics, a maximum line width marker
- z3: UI heavy: no zen float, maximized, numbers, all diagnostics, the debug UI as splits in the
  current tab (outside z3 the debug UI keeps its own tab)
- z0: off, restores the window size, diagnostics and options from before

## Impact

- `lua/genja/map-plugin/zenmode.lua` (keys z0..z3), the dap UI setup (`lua/lazyp/langs/dap*.lua`)
- built on the config's `PR-zen` branch, not merged; test session in that branch's `todo-test/zen-modes.md`
- open: dap-ui or dap-view in z3; open the debug UI at once or on the first stop
