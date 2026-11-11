---
id: TASK-39
title: 'open a browser and paste a query to perplexity'
status: Done
assignee: []
created_date: '2026-10-29'
labels:
  - nvim-config
  - todo-2026-neovim011
  - new-setup-2026
dependencies: []
ordinal: 39000
---

## Description

open a browser and paste a query to perplexity

- gonna clutter ui if add them in the same way as the perplexity eff-two item and keybinds
- should be a toggle-provider on the fly kind of config, via eff-two
  - provide user func :PasteSearch [-provider name] [-save]
    - set active provider for runtime session
    - optionally persist choice in plugin-spec setup function (clever / simple lua pattern)
- the feature / module should be «paste to ai-search in browser», using {{provider}}
    (backlog/docs/doc-45 - guide-paste-search.md)

From `todo-2026-neovim011.md`, section "new setup 2026".

## Acceptance Criteria

- [x] #1 move into plug-wip/genja-paste-ai.nvim
- [x] #2 add providers
- [x] #3 add gemini
- [x] #4 add manus
- [x] #5 add chatgpt
- [x] #6 add grok
- [x] #7 done 2026-10-29: :PasteSearch (:Xty, :Pplx), <F2> lookup, -save to lua/genja/local/paste-ai.lua

## Original notes

```markdown
-[x] open a browser and paste a query to perplexity
    -[x] move into plug-wip/genja-paste-ai.nvim
    -[x] add providers
      - [x] add gemini
      - [x] add manus
      - [x] add chatgpt
      - [x] add grok
      - gonna clutter ui if add them in the same way as the perplexity eff-two item and keybinds
      - should be a toggle-provider on the fly kind of config, via eff-two
        - provide user func :PasteSearch [-provider name] [-save]
          - set active provider for runtime session
          - optionally persist choice in plugin-spec setup function (clever / simple lua pattern)
      - the feature / module should be «paste to ai-search in browser», using {{provider}}
      - [x] done 2026-10-29: :PasteSearch (:Xty, :Pplx), <F2> lookup, -save to lua/genja/local/paste-ai.lua
          (doc-wip/readme.2026-10-29.paste-search.md)
```
