---
id: TASK-36
title: 'evaluate completion engines other than nvim-cmp'
status: Done
assignee: []
created_date: '2026-11-10'
labels:
  - todo-2026-neovim011
  - new-setup-2026
dependencies: []
ordinal: 36000
---

## Description

evaluate completion engines other than nvim-cmp

(notes: plug-wip/genja-completion011.nvim/README.md, "Alternatives to nvim-cmp")
    - is LSP-only enough? what about buffer words, paths, cmdline?
    - no it's not enough, maybe for some kind of minimalist setup
      - some kinks with selection. mainly works fine
        can'd describe the issue yet. feels a bit off
        but works faster and it's more powerful

From `todo-2026-neovim011.md`, section "new setup 2026".

## Acceptance Criteria

- [x] #1 built-in: vim.lsp.completion.enable({ autotrigger = true }) / 'autocomplete'
- [x] #2 blink.cmp
- [x] #3 port lua/genja/completion/* features
- [x] #4 compare speed and menu feel with nvim-cmp

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
