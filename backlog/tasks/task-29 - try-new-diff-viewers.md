---
id: TASK-29
title: 'try the new diff viewers and their modes'
status: To Do
assignee: []
created_date: '2026-11-09'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 29000
---

## Description

try the new diff viewers and their modes

- diffview, set up plain: panels left/bottom, no icons or hints, `<leader>mGd` and F2 `diffview toggle mode` flip side by side / inline (`diff1_inline`),
  red left / green right (fold in lua/genja/hilite.lua, hook in lua/lazyp/git/diffview.lua), `diffopt` histogram (opt.lua), fillchars `diff: `
- F2 in an oil buffer in a repo (lua/genja/f2/collect/git.lua): `diffview open` (FROM, TO pickers, `FROM...TO`),
  `codediff changes | branches | history | pr`
- installed to compare, nothing mapped: unified.nvim (`:Unified`), deltaview.nvim (`:DeltaView [ref]`, `:Delta`, `:DeltaMenu[!]`),
  codediff.nvim (`:CodeDiff`; first use downloads its diff library: `:CodeDiff install`)
- check: `:Lazy install`; `diff1_inline` and the hook colors exist in the installed diffview (`:h diffview.defaults`);
  `-C` / `--repo` flags in the codediff items; unified.nvim against a branch ref; which viewer replaces which (keep one or two)
- research on sleek diffview configs: the subagent report of this session; alternatives not looked at: nvim.difftool, mini.diff, octo.nvim

From `todo-ideas.md`, section "ideas october".

## Original notes

```markdown
- [ ] try the new diff viewers and their modes (2026-11-09; all untested)
  - diffview, set up plain: panels left/bottom, no icons or hints, `<leader>mGd` and F2 `diffview toggle mode` flip side by side / inline (`diff1_inline`),
    red left / green right (fold in lua/genja/hilite.lua, hook in lua/lazyp/git/diffview.lua), `diffopt` histogram (opt.lua), fillchars `diff: `
  - F2 in an oil buffer in a repo (lua/genja/f2/collect/git.lua): `diffview open` (FROM, TO pickers, `FROM...TO`),
    `codediff changes | branches | history | pr`
  - installed to compare, nothing mapped: unified.nvim (`:Unified`), deltaview.nvim (`:DeltaView [ref]`, `:Delta`, `:DeltaMenu[!]`),
    codediff.nvim (`:CodeDiff`; first use downloads its diff library: `:CodeDiff install`)
  - check: `:Lazy install`; `diff1_inline` and the hook colors exist in the installed diffview (`:h diffview.defaults`);
    `-C` / `--repo` flags in the codediff items; unified.nvim against a branch ref; which viewer replaces which (keep one or two)
  - research on sleek diffview configs: the subagent report of this session; alternatives not looked at: nvim.difftool, mini.diff, octo.nvim
```
