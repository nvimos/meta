# ai, llm, code generation

Status: Done (backlog TASK-31)

## Why

ai, llm, code generation

- gemini via genja-ask (plug-wip/genja-ask.nvim, backends/cli.lua)
- gen.nvim (lua/lazyp/langs-comps/gen.lua), ollama http api
- (maybe) via cli
- (maybe) via http api
- (maybe) via local sock
- maybe hack some round-robin, auto retry util
- maybe delegate to cli tools
- genja-ask: claude -p, claudefterm, gemini, copilot, aichat
- copilot
- gemini
- copilot.vim (lua/lazyp/langs-comps/copilot.lua)
- ask random questions
- ask about current file
- genja-ask popup (<M-?>), codecompanion chat

## What Changes

- integrate at leas one from online, free tier
- integrate ollama
- integrate at least one
- auto-code-completion suggestions
- chatbot

## Impact

- Source: `todo-2026-neovim011.md`, section "new setup 2026"

## Original notes

```markdown
-[x] ai, llm, code generation (closed 2026-10-29: done in the code)
    -[x] integrate at leas one from online, free tier
        - gemini via genja-ask (plug-wip/genja-ask.nvim, backends/cli.lua)
    -[x] integrate ollama
        - gen.nvim (lua/lazyp/langs-comps/gen.lua), ollama http api
        - (maybe) via cli
        - (maybe) via http api
        - (maybe) via local sock
    -[x] integrate at least one
        - maybe hack some round-robin, auto retry util
        - maybe delegate to cli tools
        - genja-ask: claude -p, claudefterm, gemini, copilot, aichat
    -[x] auto-code-completion suggestions
        - copilot
        - gemini
        - copilot.vim (lua/lazyp/langs-comps/copilot.lua)
    -[x] chatbot
        - ask random questions
        - ask about current file
        - genja-ask popup (<M-?>), codecompanion chat
```
