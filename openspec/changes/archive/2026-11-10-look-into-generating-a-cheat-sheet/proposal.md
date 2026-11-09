# look into generating a cheat-sheet from existing keys

Status: Done (backlog TASK-38)

## Why

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

## What Changes

- should be a reference at a glance
- sudormrfbin/cheatsheet.nvim
- move the :CheatsheetGenerate snippet to lazy setup
- make the telescope ui first column wider
- adjust the script for more granular groups (first column)
- look into generating several cheatsheets
- one for lsp
- one for map-convoluted
- one for map-*
- add them to Mylunsj
- done for folds to define the descriptions

## Impact

- Source: `todo-2026-neovim011.md`, section "new setup 2026"

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
