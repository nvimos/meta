---
id: TASK-76
title: 'extract the F2 context picker into its own plugin, e.g. plug-wip/genja-eff-two.nvim'
status: To Do
assignee: []
created_date: '2026-11-09'
labels:
  - nvim-config
  - todo-2027
  - f2-plugin
dependencies: []
ordinal: 76000
---

## Description

extract the F2 context picker into its own plugin, e.g. plug-wip/genja-eff-two.nvim

- name: `genja-f2.nvim` would match the lua/genja/f2 folder and module names
- survey first: commander.nvim, legendary.nvim (launchers, probably not context pickers)
- step 1, in the config: `f2.add_source(mod)`, plain explicit registration, replacing the hardcoded `sources` list in init.lua
- step 2: generic sources move with the plugin: make, scripts, git (oil add), adhoc
- sources tied to this config stay and register themselves: diag, msgs, lsp, lookup, claude, gui
- group names: lua/genja/f2/groups.lua; callers need a way to add their own (todo in that file)
- costs
  - changes across plugin and config are two commits
  - tests/f2 moves with it, or runs from the config's test Makefile
  - `DevReloadF2` reaches into genja-finder.telemap

From `todo-2027.md`, section "f2 plugin".

## Original notes

```markdown
- [ ] extract the F2 context picker into its own plugin, e.g. plug-wip/genja-eff-two.nvim (2026-11-09)
  - name: `genja-f2.nvim` would match the lua/genja/f2 folder and module names
  - survey first: commander.nvim, legendary.nvim (launchers, probably not context pickers)
  - step 1, in the config: `f2.add_source(mod)`, plain explicit registration, replacing the hardcoded `sources` list in init.lua
  - step 2: generic sources move with the plugin: make, scripts, git (oil add), adhoc
  - sources tied to this config stay and register themselves: diag, msgs, lsp, lookup, claude, gui
  - group names: lua/genja/f2/groups.lua; callers need a way to add their own (todo in that file)
  - costs
    - changes across plugin and config are two commits
    - tests/f2 moves with it, or runs from the config's test Makefile
    - `DevReloadF2` reaches into genja-finder.telemap
```
