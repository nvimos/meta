---
id: TASK-17
title: 'diagnostics: `<leader>ttt` disables all diagnostics (LSP, nvim-lint: vale, gitleaks,...'
status: Needs Test
assignee: []
created_date: '2026-11-02'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 17000
---

## Description

diagnostics: `<leader>ttt` disables all diagnostics (LSP, nvim-lint: vale, gitleaks,...

- today: lua/genja/map-lsp.lua toggle_diagnostics, `vim.diagnostic.enable(not vim.diagnostic.is_enabled())`
- check that every source goes away and comes back, also in buffers opened while off
- 2026-11-02: already works: enable(false) without a filter covers every namespace and later buffers

From `todo-ideas.md`, section "ideas october".

## Acceptance Criteria

- [x] #1 `<leader>ttt` in every buffer, not only after LspAttach; `<leader>tt3` the limit of 3; tested (b829ae5)

## Verify

Hands-on checks, kept apart from the build steps.

- [x] zen z1/z2 turn diagnostics off; z0 turns them on again (unless off before zen) with the limit of 3; untested (333bf79)
- [x] try it by hand (marked untested in the notes)

## Original notes

```markdown
- [x] diagnostics: `<leader>ttt` disables all diagnostics (LSP, nvim-lint: vale, gitleaks, ...) and toggles them back on
  - today: lua/genja/map-lsp.lua toggle_diagnostics, `vim.diagnostic.enable(not vim.diagnostic.is_enabled())`
  - check that every source goes away and comes back, also in buffers opened while off
  - 2026-11-02: already works: enable(false) without a filter covers every namespace and later buffers
  - [x] zen z1/z2 turn diagnostics off; z0 turns them on again (unless off before zen) with the limit of 3; untested (333bf79)
  - [x] `<leader>ttt` in every buffer, not only after LspAttach; `<leader>tt3` the limit of 3; tested (b829ae5)
```
