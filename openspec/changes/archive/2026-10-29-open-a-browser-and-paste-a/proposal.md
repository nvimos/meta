# open a browser and paste a query to perplexity

Status: Done (backlog TASK-39)

## Why

open a browser and paste a query to perplexity

- gonna clutter ui if add them in the same way as the perplexity eff-two item and keybinds
- should be a toggle-provider on the fly kind of config, via eff-two
  - provide user func :PasteSearch [-provider name] [-save]
    - set active provider for runtime session
    - optionally persist choice in plugin-spec setup function (clever / simple lua pattern)
- the feature / module should be «paste to ai-search in browser», using {{provider}}
    (doc-wip/readme.2026-10-29.paste-search.md)

## What Changes

- move into plug-wip/genja-paste-ai.nvim
- add providers
- add gemini
- add manus
- add chatgpt
- add grok
- done 2026-10-29: :PasteSearch (:Xty, :Pplx), <F2> lookup, -save to lua/genja/local/paste-ai.lua

## Impact

- Source: `todo-2026-neovim011.md`, section "new setup 2026"

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
