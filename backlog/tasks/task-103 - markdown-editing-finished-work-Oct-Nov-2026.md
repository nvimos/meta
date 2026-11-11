---
id: TASK-103
title: 'markdown editing: finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-24'
labels:
  - nvim-config
  - markdown
  - from-config
dependencies: []
ordinal: 103000
---

## Description

Finished work on markdown editing, 2026-10-24 .. 2026-11-03: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-14 - guide-md-checklist.md`: F2 markdown: lines to checklist (idea 34)
  - `backlog/docs/doc-33 - guide-md-fix.md`: Markdown: fixers, fix on save, abbreviations
  - `backlog/docs/doc-64 - guide-md-fix-indicator.md`: md-fix busy mark in the statusline (2026-11-10)
  - `backlog/docs/doc-65 - guide-md-links.md`: Markdown: bare URLs to inline links (2026-11-10)

## Acceptance Criteria

- [x] #1 markdown: <F2> preview with glow in a new terminal (2026-10-24; `solved-26.10.24-08.19-md-glow.md`)
- [x] #2 markdown: autocorrect mistakes (2026-10-25; `solved-26.10.25-00.07-md-fix.md`)
- [x] #3 md: substitutions that wrap vim key notation in backticks (2026-10-25; `solved-26.10.25-12.41-md-keys-escape.md`)
- [x] #4 markdown: settings live in after/ftplugin only (2026-10-28; `solved-26.10.28-23.12-markdown-ftplugin.md`)
- [x] #5 markdown: md-fix expands tabs, backticks vim keys, toggle (2026-10-29; `solved-26.10.29-20.56-md-fix-keys-tabs.md`)
- [x] #6 markdown: wrapped list lines line up after the marker (2026-10-29; `solved-26.10.29-20.56-md-formatlistpat.md`)
- [x] #7 md-fix: heed editorconfig sections for markdown, else spaces (2026-10-31; `solved-26.10.31-20.02-md-editorconfig.md`)
- [x] #8 markdown: gq wrapped - [ ] items under the checkbox (2026-10-31; `solved-26.10.31-20.02-md-wrap.md`)
- [x] #9 markdown: `]j` `[j` (`]y` `[y`) jump to the next / previous open checkbox (2026-11-03; `solved-26.11.03-14.02-md-box-jump.md`)
- [x] #10 f2 context: markdown (undated; `ideas-34-md-checklist.md`)
- [x] #11 disable gitsigns indicators in markdown files by default (undated; `ideas-41-gitsigns-markdown.md`)
- [x] #12 markdown lang (undated; `ideas-45-markdown-fix.md`)
- [x] #13 like the markdown F2 context action to convert list items into (undated; `ideas-61-md-links.md`)
- [x] #14 statusline indicator while markdown-reformat is working (undated; `ideas-62-md-fix-indicator.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: path with spaces or a `'` in it (`solved-26.10.24-08.19-md-glow.md`)
- [ ] linux: pick a terminal ($TERMINAL, x-terminal-emulator) (`solved-26.10.24-08.19-md-glow.md`)
- [ ] test: `teh ` in a .md; `:w` fixes `#Heading` (`solved-26.10.25-00.07-md-fix.md`)
- [ ] decide the ft setting suggestions (linebreak, spell, list continuation) (`solved-26.10.25-00.07-md-fix.md`)
- [ ] test: markdown buffer wraps, no spell; gitcommit wraps, spell on (`solved-26.10.28-23.12-markdown-ftplugin.md`)
- [ ] test: :w on a file with tab-indented lists and <C-x> in prose; <leader>tm turns it off (`solved-26.10.29-20.56-md-fix-keys-tabs.md`)
- [ ] test: gq on a long `- [ ] item` line indents after the checkbox (`solved-26.10.29-20.56-md-formatlistpat.md`)
- [ ] markdownlint MD007 (indent 2) may re-indent lists to a width that doesn't fit tab size 4 (`solved-26.10.31-20.02-md-editorconfig.md`)
- [ ] test: `3]j` in a todo file (`solved-26.11.03-14.02-md-box-jump.md`)
- [ ] test: guide backlog/docs/doc-65 - guide-md-links.md (`ideas-61-md-links.md`)
- [ ] test: guide backlog/docs/doc-64 - guide-md-fix-indicator.md (`ideas-62-md-fix-indicator.md`)
