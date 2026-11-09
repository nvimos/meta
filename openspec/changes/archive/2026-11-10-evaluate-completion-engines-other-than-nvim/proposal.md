# evaluate completion engines other than nvim-cmp

Status: Done (backlog TASK-36)

## Why

evaluate completion engines other than nvim-cmp

(notes: plug-wip/genja-completion011.nvim/README.md, "Alternatives to nvim-cmp")
    - is LSP-only enough? what about buffer words, paths, cmdline?
    - no it's not enough, maybe for some kind of minimalist setup
      - some kinks with selection. mainly works fine
        can'd describe the issue yet. feels a bit off
        but works faster and it's more powerful

## What Changes

- built-in: vim.lsp.completion.enable({ autotrigger = true }) / 'autocomplete'
- blink.cmp
- port lua/genja/completion/* features
- compare speed and menu feel with nvim-cmp

## Impact

- Source: `todo-2026-neovim011.md`, section "new setup 2026"

## Original notes

```markdown
-[x] evaluate completion engines other than nvim-cmp
    (notes: plug-wip/genja-completion011.nvim/README.md, "Alternatives to nvim-cmp")
    -[x] built-in: vim.lsp.completion.enable({ autotrigger = true }) / 'autocomplete'
        - is LSP-only enough? what about buffer words, paths, cmdline?
        - no it's not enough, maybe for some kind of minimalist setup
    -[x] blink.cmp
        - [x] port lua/genja/completion/* features
        - [x] compare speed and menu feel with nvim-cmp
          - some kinks with selection. mainly works fine
            can'd describe the issue yet. feels a bit off
            but works faster and it's more powerful
```
