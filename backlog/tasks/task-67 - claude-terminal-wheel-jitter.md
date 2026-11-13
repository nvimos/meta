---
id: TASK-67
title: 'claude terminal wheel jitter'
status: To Do
assignee: []
created_date: '2026-10-28'
labels:
  - nvim-config
  - todo-2027
  - new-setup-2027
dependencies: []
ordinal: 67000
---

## Description

claude terminal: mouse wheel scroll jitters in terminal mode (nvim-qt, mouse wheel)

- scrolling up goes up, down, up, then scrolls as usual; wanted: scroll inside claude
- done 2026-10-28: scrolloff 0 in terminal windows (lua/genja/ext/term.lua), enough for now
- find the side: log the wheel keys nvim gets while scrolling in claude
      :lua _G.wheel_log = {}; vim.on_key(function(k) local t = vim.fn.keytrans(k); if t:find('ScrollWheel') then table.insert(_G.wheel_log, t) end end, vim.api.nvim_create_namespace('wheel_log'))
      :lua print(table.concat(_G.wheel_log, ' '))
  - Up Down Up …: nvim-qt sends the reverse step; check nvim-qt issues, maybe filter in nvim
  - Up Up Up …: claude mishandles them; claude-code issue #83298 (first wheel event after a direction change)
- compare: nvim TUI in Windows Terminal, same claude

From `todo-2027.md`, section "new setup 2027".

## Original notes

```markdown
- [ ] claude terminal: mouse wheel scroll jitters in terminal mode (nvim-qt, mouse wheel)
  - scrolling up goes up, down, up, then scrolls as usual; wanted: scroll inside claude
  - done 2026-10-28: scrolloff 0 in terminal windows (lua/genja/ext/term.lua), enough for now
  - find the side: log the wheel keys nvim gets while scrolling in claude
        :lua _G.wheel_log = {}; vim.on_key(function(k) local t = vim.fn.keytrans(k); if t:find('ScrollWheel') then table.insert(_G.wheel_log, t) end end, vim.api.nvim_create_namespace('wheel_log'))
        :lua print(table.concat(_G.wheel_log, ' '))
    - Up Down Up …: nvim-qt sends the reverse step; check nvim-qt issues, maybe filter in nvim
    - Up Up Up …: claude mishandles them; claude-code issue #83298 (first wheel event after a direction change)
  - compare: nvim TUI in Windows Terminal, same claude
```
