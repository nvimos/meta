---
id: TASK-38
title: 'look into generating a cheat-sheet from existing keys'
status: Done
assignee: []
created_date: '2026-11-10'
labels:
  - todo-2026-neovim011
  - new-setup-2026
dependencies: []
ordinal: 38000
---

## Description

look into generating a cheat-sheet from existing keys

- ideally some logical patterns and rearrangement ideas should emerge
    - which key groups help with that
        - the ui is easier to read too
    - no. the ui / interface sucked. abandon effort
    - abdul keymaps is much better. works as a modal with search
    - maybe save as custom help files -> cheatsheet.txt
- consider exclude or include defaults
  - toggle builtin keymaps?
    (in the cheatsheet, or the search ui)
      - must be manually redeclared. prob not worth it for all

From `todo-2026-neovim011.md`, section "new setup 2026".

## Acceptance Criteria

- [x] #1 should be a reference at a glance
- [x] #2 sudormrfbin/cheatsheet.nvim
- [ ] #3 move the :CheatsheetGenerate snippet to lazy setup
- [ ] #4 make the telescope ui first column wider
- [ ] #5 adjust the script for more granular groups (first column)
- [ ] #6 look into generating several cheatsheets
- [ ] #7 one for lsp
- [ ] #8 one for map-convoluted
- [ ] #9 one for map-*
- [ ] #10 add them to Mylunsj
- [x] #11 done for folds to define the descriptions

## Original notes

```markdown
-[x] look into generating a cheat-sheet from existing keys
    - ideally some logical patterns and rearrangement ideas should emerge
        - which key groups help with that
            - the ui is easier to read too
    -[x] should be a reference at a glance
    -[x] sudormrfbin/cheatsheet.nvim
        - no. the ui / interface sucked. abandon effort
        - abdul keymaps is much better. works as a modal with search
        - maybe save as custom help files -> cheatsheet.txt
        -[n] move the :CheatsheetGenerate snippet to lazy setup
        -[n] make the telescope ui first column wider
        -[n] adjust the script for more granular groups (first column)
        -[n] look into generating several cheatsheets
            -[n] one for lsp
            -[n] one for map-convoluted
            -[n] one for map-*
            -[n] add them to Mylunsj
    - consider exclude or include defaults
      - [x] done for folds to define the descriptions
      - toggle builtin keymaps?
        (in the cheatsheet, or the search ui)
          - must be manually redeclared. prob not worth it for all
```
