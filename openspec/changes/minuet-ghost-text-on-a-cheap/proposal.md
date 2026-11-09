# minuet ghost text on a cheap, good prepaid model

Status: To Do (backlog TASK-59)

## Why

minuet ghost text on a cheap, good prepaid model

- candidates: DeepSeek, Qwen (their HTTP APIs), and Claude (minuet `claude` provider, block commented out in
  lua/lazyp/langs-comps/minuet.lua); compare price, latency and suggestion quality against Codestral and local ollama
- not `claude -p`: starting the CLI per request is too slow for ghost text
- keys from the gitignored lua/genja/local/secrets.lua, like the other providers

## What Changes

- (to be worked out)

## Impact

- Source: `todo-2027.md`, section "new setup 2027"

## Original notes

```markdown
- [ ] minuet ghost text on a cheap, good prepaid model (2026-11-05, from todo-ideas #14)
  - candidates: DeepSeek, Qwen (their HTTP APIs), and Claude (minuet `claude` provider, block commented out in
    lua/lazyp/langs-comps/minuet.lua); compare price, latency and suggestion quality against Codestral and local ollama
  - not `claude -p`: starting the CLI per request is too slow for ghost text
  - keys from the gitignored lua/genja/local/secrets.lua, like the other providers
```
