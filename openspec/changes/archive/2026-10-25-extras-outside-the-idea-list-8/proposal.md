# extras outside the idea list

Status: Done (backlog TASK-8)

## Why

extras outside the idea list

comps011 lsp/cmp/lint with groups and timings (9f5f014); tests/Makefile runs every dir

## What Changes

- telescope keymaps: `<M-r>` after `<M-f>`/`<M-x>` cycles the groups of the refined list; tested (2debb3b)
- tests: map-plugin miss log and health (af13aed), claudefterm per project (63800da),
- aerial: nav float 5% see-through (cbe6c13)
- gitsigns: `<leader>mGs` attaches skipped buffers again (e9e50f7)
- f2: groups of at most 6 chars, main list `group  label` in one column (5edddfa)
- floaterm: :PwshFterm (50e4b8a)
- mason: make mason-luals reinstalls lua-language-server headless (19d67f5)
- :ToggleDiagnostics for the current buffer (38e3d2d)
- f2 diag: hide excess undoes show all (620545d); pickers: matched chars in Visual fg, bold (00b05e5)
- genja-finder: `<M-Up>` rescans in the parent dir (93a8b69); `<C-]>` opens the entry, a dir entry itself (7bc4759, 31b74cd)
- statusline: [Nameless] for unnamed buffers (eddb6e5); telescope key footer dropped, key help kept (5c6e9a7)
- md: substitutions wrap vim key notation in backticks (c4d6b26)
- commit popup also on `<leader>gcm` and `<leader>C` (39dab59); `<leader>ei` tab-local from stdpath (7b05312)
- nvim-qt: nvim-qt.qss stylesheet, dark title bar note in ginit.vim (41e5bb6)

## Impact

- Source: `todo-ideas.md`, section "ideas october"

## Original notes

```markdown
- [x] extras outside the idea list (2026-10-25)
  - [x] telescope keymaps: `<M-r>` after `<M-f>`/`<M-x>` cycles the groups of the refined list; tested (2debb3b)
  - [x] tests: map-plugin miss log and health (af13aed), claudefterm per project (63800da),
          comps011 lsp/cmp/lint with groups and timings (9f5f014); tests/Makefile runs every dir
  - [x] aerial: nav float 5% see-through (cbe6c13)
  - [x] gitsigns: `<leader>mGs` attaches skipped buffers again (e9e50f7)
  - [x] f2: groups of at most 6 chars, main list `group  label` in one column (5edddfa)
  - [x] floaterm: :PwshFterm (50e4b8a)
  - [x] mason: make mason-luals reinstalls lua-language-server headless (19d67f5)
  - [x] :ToggleDiagnostics for the current buffer (38e3d2d)
  - [x] f2 diag: hide excess undoes show all (620545d); pickers: matched chars in Visual fg, bold (00b05e5)
  - [x] genja-finder: `<M-Up>` rescans in the parent dir (93a8b69); `<C-]>` opens the entry, a dir entry itself (7bc4759, 31b74cd)
  - [x] statusline: [Nameless] for unnamed buffers (eddb6e5); telescope key footer dropped, key help kept (5c6e9a7)
  - [x] md: substitutions wrap vim key notation in backticks (c4d6b26)
  - [x] commit popup also on `<leader>gcm` and `<leader>C` (39dab59); `<leader>ei` tab-local from stdpath (7b05312)
  - [x] nvim-qt: nvim-qt.qss stylesheet, dark title bar note in ginit.vim (41e5bb6)
```
