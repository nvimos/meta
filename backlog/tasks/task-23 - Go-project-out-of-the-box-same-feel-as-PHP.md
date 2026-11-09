---
id: TASK-23
title: 'Go project out of the box, same feel as PHP'
status: Needs Test
assignee: []
created_date: '2026-11-05'
labels:
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 23000
---

## Description

Go project out of the box, same feel as PHP

- have: gopls (plug-wip/genja-completion011.nvim/lua/genja/lang/go.lua: go.work roots, organize imports + format on save,
  code lenses on `<leader>cl`), go.nvim with dap (lua/lazyp/langs/go.lua), treesitter go
- gaps (from a grep, not tested): golangci-lint not in lua/genja/ext/lint.lua; treesitter gomod/gosum/gotmpl;
  templ, sql, proto, Dockerfile parsers; tests through neotest-golang or go.nvim (decide one)
      .golangci.*file, sample examples/go/.golangci.toml (e7bad3d); neotest-golang, go.nvim's :GoTest* kept (1037aa2)
      sql on PR-langs, dockerfile on PR-wsl-docker; untested

From `todo-ideas.md`, section "ideas october".

## Acceptance Criteria

- [x] #1 parsers templ, sql, proto, dockerfile: templ and proto in load-treesitter.lua (2026-11-10);

## Verify

Hands-on checks, kept apart from the build steps.

- [x] auto-todo 2026-11-05 (untested): parsers gomod gosum gotmpl (9a8aa25); golangci-lint only with a
- [ ] try it by hand (marked untested in the notes)

## Original notes

```markdown
- [ ] Go project out of the box, same feel as PHP (after PHP, 2026-11-05)
  - have: gopls (plug-wip/genja-completion011.nvim/lua/genja/lang/go.lua: go.work roots, organize imports + format on save,
    code lenses on `<leader>cl`), go.nvim with dap (lua/lazyp/langs/go.lua), treesitter go
  - gaps (from a grep, not tested): golangci-lint not in lua/genja/ext/lint.lua; treesitter gomod/gosum/gotmpl;
    templ, sql, proto, Dockerfile parsers; tests through neotest-golang or go.nvim (decide one)
  - [x] auto-todo 2026-11-05 (untested): parsers gomod gosum gotmpl (9a8aa25); golangci-lint only with a
        .golangci.*file, sample examples/go/.golangci.toml (e7bad3d); neotest-golang, go.nvim's :GoTest* kept (1037aa2)
  - [x] parsers templ, sql, proto, dockerfile: templ and proto in load-treesitter.lua (2026-11-10);
        sql on PR-langs, dockerfile on PR-wsl-docker; untested
```
