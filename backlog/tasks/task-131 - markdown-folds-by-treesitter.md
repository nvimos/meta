---
id: TASK-131
title: 'markdown folds by treesitter'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - markdown
dependencies: []
ordinal: 131000
---

## Description

markdown: every markdown buffer folds by headings through treesitter, the closed fold shows its first line
without a line count, 'conceallevel' starts at 2. Commits: config fd5c309.

## Acceptance Criteria

- [x] #1 `after/ftplugin/markdown.lua`: foldmethod expr, `vim.treesitter.foldexpr()`, foldlevel 3
- [x] #2 `lua/genja/ext/md-foldtext.lua`: 'foldtext' with the first line and its treesitter highlights, no count
  (this nvim has no `vim.treesitter.foldtext`)
- [x] #3 `after/ftplugin/markdown.vim`: `conceallevel=2` instead of 1
- [x] #4 `lua/genja/readme.md`: line for `ext/md-foldtext.lua`

## Verify

- [ ] test: open a markdown file with `##` and `###` headings, `zc` on a heading: the closed line shows the
  heading text, coloured, no "N lines"
- [ ] test: `:set foldlevel?` is 3 and folds deeper than level 3 start closed
- [ ] test: `:set conceallevel?` is 2 and backticks are hidden
- [ ] test: inline `**bold**` or code in a heading: the closed line shows it without errors in `:messages`
