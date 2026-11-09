# extras outside the idea list

Status: Done (backlog TASK-7)

## Why

extras outside the idea list

one shared state per Gui* function; neovim-gui-shim on again; tested (3580a06, ad94a79)
:Mydirs reset deletes the usage file; tested (1132d6b)

## What Changes

- cmdline: `<C-j>`/`<C-k>` pick items, `<Up>`/`<Down>` back to history (0de4d52)
- map-lsp: descs for nvim 0.11 gr* defaults, references on gR, [d ]d go the way their descs say (5e788aa)
- markdown: `<F2>` glow preview in a new pwsh window, Windows only (21cfe96)
- intro: eob ~ drawn in column 0 like vanilla (81a4659)
- gui: nvim-qt toggles on `<leader>mQ`…, GuiFuncs picker (`<F3>`, `<F2>` gui), right-click frameless,
- edit: visual `<leader>w`, wraps lines as "line",; title case on `<leader>wsT`, sort paragraph `<leader>wsp` (8f25155)
- f2 git: `<M-a>` git adds the file, picker stays open (e6c04ac)
- hilite: darker Search/IncSearch/CurSearch background (a1b0857)
- startdirs: `<M-1>`…`<M-4>` jump by rank and don't count a use; :Mydirs picker,

## Impact

- Source: `todo-ideas.md`, section "ideas october"

## Original notes

```markdown
- [x] extras outside the idea list (2026-10-24)
  - [x] cmdline: `<C-j>`/`<C-k>` pick items, `<Up>`/`<Down>` back to history (0de4d52)
  - [x] map-lsp: descs for nvim 0.11 gr* defaults, references on gR, [d ]d go the way their descs say (5e788aa)
  - [x] markdown: `<F2>` glow preview in a new pwsh window, Windows only (21cfe96)
  - [x] intro: eob ~ drawn in column 0 like vanilla (81a4659)
  - [x] gui: nvim-qt toggles on `<leader>mQ`…, GuiFuncs picker (`<F3>`, `<F2>` gui), right-click frameless,
          one shared state per Gui* function; neovim-gui-shim on again; tested (3580a06, ad94a79)
  - [x] edit: visual `<leader>w`, wraps lines as "line",; title case on `<leader>wsT`, sort paragraph `<leader>wsp` (8f25155)
  - [x] f2 git: `<M-a>` git adds the file, picker stays open (e6c04ac)
  - [x] hilite: darker Search/IncSearch/CurSearch background (a1b0857)
  - [x] startdirs: `<M-1>`…`<M-4>` jump by rank and don't count a use; :Mydirs picker,
          :Mydirs reset deletes the usage file; tested (1132d6b)
```
