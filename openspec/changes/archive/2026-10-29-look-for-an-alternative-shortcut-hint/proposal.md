# look for an alternative shortcut-hint plugin

Status: Done (backlog TASK-33)

## Why

look for an alternative shortcut-hint plugin

- testing out legendary
  - tests that all defined key groups appear with a prefix
  - warn if not, not failure. list the missing groups
- which-key feels clunky
  - maybe look into a different layout mode

## What Changes

- improve sorting and grouping of which-key
- make an automated test ui/which-groups
- tests/ui/test_which_groups.lua, both ways: empty groups, <leader> prefixes without a group (2026-10-29)
- preset helix; modern and a narrower classic commented out (2026-10-29)

## Impact

- Source: `todo-2026-neovim011.md`, section "new setup 2026"

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
