---
id: TASK-59
title: 'minuet on cheap prepaid model'
status: To Do
assignee: []
created_date: '2026-11-05'
labels:
  - nvim-config
  - todo-2027
  - new-setup-2027
dependencies: []
ordinal: 59000
---

## Description

minuet ghost text on a cheap, good prepaid model

- candidates: DeepSeek, Qwen (their HTTP APIs), and Claude (minuet `claude` provider, block commented out in
  lua/lazyp/langs-comps/minuet.lua); compare price, latency and suggestion quality against Codestral and local ollama
- not `claude -p`: starting the CLI per request is too slow for ghost text
- keys from the gitignored lua/genja/local/secrets.lua, like the other providers

From `todo-2027.md`, section "new setup 2027".

- Guides (how it works, how to try it):
  - `backlog/docs/doc-49 - guide-ghost-text-minuet-llm.md`: Local ghost text: minuet-ai.nvim and llm.nvim on ollama (2026-10-31)
  - `backlog/docs/doc-68 - guide-minuet-providers.md`: minuet-ai.nvim providers (2026-10-31)

## Original notes

```markdown
- [ ] minuet ghost text on a cheap, good prepaid model (2026-11-05, from todo-ideas #14)
  - candidates: DeepSeek, Qwen (their HTTP APIs), and Claude (minuet `claude` provider, block commented out in
    lua/lazyp/langs-comps/minuet.lua); compare price, latency and suggestion quality against Codestral and local ollama
  - not `claude -p`: starting the CLI per request is too slow for ghost text
  - keys from the gitignored lua/genja/local/secrets.lua, like the other providers
```
