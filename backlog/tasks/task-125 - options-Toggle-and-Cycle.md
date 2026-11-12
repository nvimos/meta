---
id: TASK-125
title: 'options: :Toggle and :Cycle'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - options
  - issue
  - nvim-config
dependencies: []
ordinal: 125000
---

## Description

options: generic commands to flip a boolean or step through an option's values, completed. Commits: config 5f4c03d.

## Acceptance Criteria

- [x] #1 lua/genja/ext/opt-cycle.lua, commands in plugin/opt-cycle.lua (Vimscript draft dropped)
- [x] #2 completion: option names, then values with the current one; notification as :set prints it
- [x] #3 cheatsheet, lua/genja/readme.md

## Verify

- [ ] test: `:Toggle wr<Tab>`, `:Toggle wrap`: notification `nowrap` / `wrap`
- [ ] test: `:Cycle conceallevel <Tab>` lists 0-3; `:Cycle signcolumn` steps through its values
- [ ] test: `:Cycle tabstop 2 4 8` repeated; `:Cycle statusline` warns
