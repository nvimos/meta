---
id: TASK-74
title: 'adopt blink over cmp'
status: Dropped
assignee: []
created_date: '2026-11-10'
labels:
  - nvim-config
  - todo-2027
  - new-setup-2027
dependencies: []
ordinal: 74000
---

## Description

consider adopting blink over cmp or improve cmp behavior

- document cmp behavior and config with intent in mind
  - describe why each source is there and what for
- behavior
  - unstable suggestion box. it moves with the cursor and suggests every word (needs refinement for prose files)
    - debounce on location set. reset every 20-30 seconds.
      - should appear at start of sentences. or maybe at the top left corner. may be awkward if it precudes cursor.
      - the list of suggestions should probably stay in one place and if it started to show above, it should stay above
      - especially for text files. it's too annoying to see it skip up and down
      - maybe it should only show up after i press tab and if there is at least one suggestion

From `todo-2027.md`, section "new setup 2027".
- dropped 2026-11-11: blink.cmp already replaced nvim-cmp (TASK-10, TASK-36)

## Original notes

```markdown
- [ ] consider adopting blink over cmp or improve cmp behavior
  - document cmp behavior and config with intent in mind
    - describe why each source is there and what for
  - behavior
    - unstable suggestion box. it moves with the cursor and suggests every word (needs refinement for prose files)
      - debounce on location set. reset every 20-30 seconds.
        - should appear at start of sentences. or maybe at the top left corner. may be awkward if it precudes cursor.
        - the list of suggestions should probably stay in one place and if it started to show above, it should stay above
        - especially for text files. it's too annoying to see it skip up and down
        - maybe it should only show up after i press tab and if there is at least one suggestion
```
