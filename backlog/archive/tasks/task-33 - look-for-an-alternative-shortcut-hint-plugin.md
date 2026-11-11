---
id: TASK-33
title: 'look for an alternative shortcut-hint plugin'
status: Done
assignee: []
created_date: '2026-10-29'
labels:
  - nvim-config
  - todo-2026-neovim011
  - new-setup-2026
dependencies: []
ordinal: 33000
---

## Description

look for an alternative shortcut-hint plugin

- testing out legendary
  - tests that all defined key groups appear with a prefix
  - warn if not, not failure. list the missing groups
- which-key feels clunky
  - maybe look into a different layout mode

From `todo-2026-neovim011.md`, section "new setup 2026".

## Acceptance Criteria

- [x] #1 improve sorting and grouping of which-key
- [x] #2 make an automated test ui/which-groups
- [x] #3 tests/ui/test_which_groups.lua, both ways: empty groups, <leader> prefixes without a group (2026-10-29)
- [x] #4 preset helix; modern and a narrower classic commented out (2026-10-29)

## Original notes

```markdown
- [x] look for an alternative shortcut-hint plugin
  - testing out legendary
  - [x] improve sorting and grouping of which-key
  - [x] make an automated test ui/which-groups
    - [x] tests/ui/test_which_groups.lua, both ways: empty groups, <leader> prefixes without a group (2026-10-29)
    - tests that all defined key groups appear with a prefix
    - warn if not, not failure. list the missing groups
  - which-key feels clunky
    - maybe look into a different layout mode
    - [x] preset helix; modern and a narrower classic commented out (2026-10-29)
```
