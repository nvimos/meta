---
id: TASK-19
title: 'abbrev fail search bug'
status: Done
assignee: []
created_date: '2026-11-02'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 19000
---

## Description

abbrev: /FAIL`<CR>` searches for "/FAIL`<C-]><CR>`" (literal text, no search)

- source: lua/genja/abbreviations.vim:38, the cmdline `<CR>` map returns the single-quoted string `'<C-]><CR>'` for every cmdtype but `:`; in an `<expr>` map the <> is typed literally, and the Vim-only `<C-]>` is only needed for `:` abbreviations (a3e07a3, 80c8fa1)
- fix: only `:` gets the `<C-]>` prefix, other cmdtypes return `"\<CR>"` (double quotes, real key), or no map at all for `/` `?`
- test: `/FAIL<CR>`, `?FAIL<CR>`, `:s/a/b/<CR>`, `jj`, `g` still work
- 2026-11-02: fixed (abbreviations.vim: `"\<CR>"` for non-`:`); `/FAIL<CR>` tested by hand, the rest of the test list open (82cd9a4)

From `todo-ideas.md`, section "ideas october".

## Acceptance Criteria

- [x] #1 abbrev: `/FAIL<CR>` searched for the text `<C-]><CR>` (2026-11-02; `legacy/nvim-config/todo-issue/solved-26.11.02-18.49-abbrev-search-cr.md`)

## Verify

- [ ] test: `?FAIL<CR>`, `:s/a/b/<CR>`, `jj`, `g` still work

## Original notes

```markdown
- [x] abbrev: /FAIL`<CR>` searches for "/FAIL`<C-]><CR>`" (literal text, no search)
  - source: lua/genja/abbreviations.vim:38, the cmdline `<CR>` map returns the single-quoted string `'<C-]><CR>'` for every cmdtype but `:`; in an `<expr>` map the <> is typed literally, and the Vim-only `<C-]>` is only needed for `:` abbreviations (a3e07a3, 80c8fa1)
  - fix: only `:` gets the `<C-]>` prefix, other cmdtypes return `"\<CR>"` (double quotes, real key), or no map at all for `/` `?`
  - test: `/FAIL<CR>`, `?FAIL<CR>`, `:s/a/b/<CR>`, `jj`, `g` still work
  - 2026-11-02: fixed (abbreviations.vim: `"\<CR>"` for non-`:`); `/FAIL<CR>` tested by hand, the rest of the test list open (82cd9a4)
```
