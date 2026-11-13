---
id: TASK-128
title: 'terminal: insert mode leaks into a new oil tab'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - terminal
  - issue
  - nvim-config
dependencies: []
ordinal: 128000
---

## Description

terminal: a tab opened from a terminal window left oil in insert mode; <F3> typed into the top entry. Commits: config daeaf4c.

## Acceptance Criteria

- [x] #1 lua/genja/ext/term.lua: terminal-mode autocmd checks after the command (vim.schedule) that the terminal is still current

## Verify

- [ ] test: from a running terminal, <leader>et: oil in normal mode, <F3> opens mylunsj
- [ ] test: jumping into a terminal window still starts terminal mode
