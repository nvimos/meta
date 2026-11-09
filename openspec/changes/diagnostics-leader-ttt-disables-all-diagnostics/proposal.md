# diagnostics: `<leader>ttt` disables all diagnostics (LSP, nvim-lint: vale, gitleaks,...

Status: Needs Test (backlog TASK-17)

## Why

diagnostics: `<leader>ttt` disables all diagnostics (LSP, nvim-lint: vale, gitleaks,...

- today: lua/genja/map-lsp.lua toggle_diagnostics, `vim.diagnostic.enable(not vim.diagnostic.is_enabled())`
- check that every source goes away and comes back, also in buffers opened while off
- 2026-11-02: already works: enable(false) without a filter covers every namespace and later buffers

## What Changes

- `<leader>ttt` in every buffer, not only after LspAttach; `<leader>tt3` the limit of 3; tested (b829ae5)

## Impact

- Source: `todo-ideas.md`, section "ideas october"

## Original notes

```markdown
- [x] diagnostics: `<leader>ttt` disables all diagnostics (LSP, nvim-lint: vale, gitleaks, ...) and toggles them back on
  - today: lua/genja/map-lsp.lua toggle_diagnostics, `vim.diagnostic.enable(not vim.diagnostic.is_enabled())`
  - check that every source goes away and comes back, also in buffers opened while off
  - 2026-11-02: already works: enable(false) without a filter covers every namespace and later buffers
  - [x] zen z1/z2 turn diagnostics off; z0 turns them on again (unless off before zen) with the limit of 3; untested (333bf79)
  - [x] `<leader>ttt` in every buffer, not only after LspAttach; `<leader>tt3` the limit of 3; tested (b829ae5)
```
