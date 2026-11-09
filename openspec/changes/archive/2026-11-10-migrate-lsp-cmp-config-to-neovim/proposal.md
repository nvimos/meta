# migrate lsp, cmp config to neovim 0.11+ api

Status: Done (backlog TASK-35)

## Why

migrate lsp, cmp config to neovim 0.11+ api

- first figure out what the minimal config is:
  try it in a bare WSL and in a Termux environment (not now)

## What Changes

- ask claude to rewrite based on existing files
- make it modular or feature-per-file
- put essential functionality into separate files
- :help completion
- :commands completion
- lua lsp
- shell lsp
- how to extract into minimal config?
- undo require(lspconfig).«lang».setup()
- migrate to vim.lsp.config and vim.lsp.enable
- fix: no completion menu while typing (cmp.setup() was never called)

## Impact

- Source: `todo-2026-neovim011.md`, section "new setup 2026"

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
