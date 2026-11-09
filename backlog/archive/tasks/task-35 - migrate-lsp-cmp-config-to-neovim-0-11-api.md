---
id: TASK-35
title: 'migrate lsp, cmp config to neovim 0.11+ api'
status: Done
assignee: []
created_date: '2026-11-10'
labels:
  - todo-2026-neovim011
  - new-setup-2026
dependencies: []
ordinal: 35000
---

## Description

migrate lsp, cmp config to neovim 0.11+ api

- first figure out what the minimal config is:
  try it in a bare WSL and in a Termux environment (not now)

From `todo-2026-neovim011.md`, section "new setup 2026".

## Acceptance Criteria

- [x] #1 ask claude to rewrite based on existing files
- [x] #2 make it modular or feature-per-file
- [x] #3 put essential functionality into separate files
- [x] #4 :help completion
- [x] #5 :commands completion
- [x] #6 lua lsp
- [x] #7 shell lsp
- [ ] #8 how to extract into minimal config?
- [x] #9 undo require(lspconfig).«lang».setup()
- [x] #10 migrate to vim.lsp.config and vim.lsp.enable
- [x] #11 fix: no completion menu while typing (cmp.setup() was never called)

## Original notes

```markdown
-[x] migrate lsp, cmp config to neovim 0.11+ api
    - [x] ask claude to rewrite based on existing files
    - [x] make it modular or feature-per-file
    - [x] put essential functionality into separate files
        -[x] :help completion
        -[x] :commands completion
        -[x] lua lsp
        -[x] shell lsp
        -[ ] how to extract into minimal config?
            - first figure out what the minimal config is:
              try it in a bare WSL and in a Termux environment (not now)
    -[x] undo require(lspconfig).«lang».setup()
    -[x] migrate to vim.lsp.config and vim.lsp.enable
    -[x] fix: no completion menu while typing (cmp.setup() was never called)
```
