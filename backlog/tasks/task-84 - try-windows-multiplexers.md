---
id: TASK-84
title: 'try windows multiplexers'
status: To Do
assignee: []
created_date: '2026-11-02'
labels:
  - nvim-config
  - todo-2028
  - later-2028
dependencies: []
ordinal: 84000
---

## Description

try the Windows multiplexers, before the light-weight session idea above

- goal: shells inside nvim survive a restart; nvim's terminal runs `<mux> attach`, the mux keeps cwd and history
- psmux first: tmux commands and .tmux.conf, prefer tmux compatible; reboot restore via psmux-resurrect/continuum
  1. `winget install psmux`; split, detach, reattach from a second terminal
  2. `:terminal psmux new -A -s nvim-<project>` in nvim; quit nvim, reopen, attach again: same shell, same cwd
  3. pwsh and Git Bash as the shell; Unicode, colours, mouse; reported gap: no popups
- tmux-windows (winget arndawg.tmux-windows, tmux 3.6a port on ConPTY): same steps, compare
- zellij 0.44+ (native Windows since 0.44, x86_64 only): built-in session resurrection restores layout,
  cwd and commands; not tmux compatible (own keys, KDL config); try only if both above fail
- not checked: stability of any of them on Windows (no independent data found)

From `todo-2028.md`, section "later: 2028".

## Original notes

```markdown
- [ ] try the Windows multiplexers, before the light-weight session idea above (asked 2026-11-02)
  - goal: shells inside nvim survive a restart; nvim's terminal runs `<mux> attach`, the mux keeps cwd and history
  - psmux first: tmux commands and .tmux.conf, prefer tmux compatible; reboot restore via psmux-resurrect/continuum
    1. `winget install psmux`; split, detach, reattach from a second terminal
    2. `:terminal psmux new -A -s nvim-<project>` in nvim; quit nvim, reopen, attach again: same shell, same cwd
    3. pwsh and Git Bash as the shell; Unicode, colours, mouse; reported gap: no popups
  - tmux-windows (winget arndawg.tmux-windows, tmux 3.6a port on ConPTY): same steps, compare
  - zellij 0.44+ (native Windows since 0.44, x86_64 only): built-in session resurrection restores layout,
    cwd and commands; not tmux compatible (own keys, KDL config); try only if both above fail
  - not checked: stability of any of them on Windows (no independent data found)
```
