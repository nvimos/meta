# blink.cmp in place of nvim-cmp

Status: Done (backlog TASK-36)

## Why

nvim-cmp felt slow and its setup had grown around the config's own sources. Neovim 0.11 also has
built-in LSP completion; both were worth comparing before porting the config's sources.

## What Changes

- compared the built-in `vim.lsp.completion` with blink.cmp; LSP-only is too little (no buffer words,
  paths, cmdline)
- blink.cmp replaces nvim-cmp; the `lua/genja/completion/*` features ported to one source builder
- cmdline keys as in plain Vim

## Impact

- design and how-to: `design.md` (was the config's doc-wip guide)
- `plug-wip/genja-completion011.nvim` (notes: README, "Alternatives to nvim-cmp"); tests/completion
- commits 2d6b4bd, 00268c4, 191c6cf, 55c1296; follow-ups in TASK-100
