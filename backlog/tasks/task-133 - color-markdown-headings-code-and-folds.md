---
id: TASK-133
title: 'color markdown headings, code and folds'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - colors
dependencies: []
ordinal: 133000
---

## Description

colors: markdown headings, inline code and comments, closed-fold text, fold column, the diagnostic float and
the hint underline, derived from the StatusLine orange and Normal. Commits: config a31c25d.

## Acceptance Criteria

- [x] #1 `lua/genja/hilite.lua`: `markdown_headings` (orange, bold for levels 1 and 2, a step darker per
  level, darker `#` markers), indigo `#a5b4fc` kept commented out
- [x] #2 `markdown_comment`: gray `MdComment`, no background; `after/ftplugin/markdown.lua` maps the html
  comment groups to it with winhighlight
- [x] #3 `markdown_code`: inline code is the StatusLine orange blended 65% towards the text color
- [x] #4 `folded`: closed-fold text blended 60% towards the text color
- [x] #5 `fold_column`: fold column markers moved towards the StatusLine orange, then 30% towards the
  background
- [x] #6 `diag_float` and `lua/genja/ext/diag-float.lua`: own background (Normal lightened 7%), two
  columns of padding on the left, one empty row below; lines colored like the virtual text
- [x] #7 `lua/genja/hilite.vim`: plain fallbacks, `DiagnosticUnderlineHint` `#707070`
- [x] #8 `lua/genja/init.lua` loads `genja.ext.diag-float`; `lua/genja/readme.md` lists it

## Verify

- [ ] test: markdown file: headings orange, `#` markers darker, levels 3 to 6 step down, 1 and 2 bold
- [ ] test: markdown: backticked words muted orange without a background, `<!-- comment -->` gray
- [ ] test: close a fold: its text is close to the normal text color; the fold column is a dim orange-brown
- [ ] test: `:ReloadLuaGenja` twice: the colors do not drift (nothing blends twice)
- [ ] test: diagnostic float (`<leader>ccc`): dark background, two columns on the left, an empty row at the
  bottom; open it twice and the padding is not added again
- [ ] test: the hint underline is dimmer than before; hover and completion floats keep the gray

## Notes

- The error and warning colors of the virtual text are about 3.2:1 on the float background; they may want
  lightening in `hilite.vim`.
- The `NOWORK` comment about `@nvim.diagnostic.float` in `hilite.vim` is obsolete.
