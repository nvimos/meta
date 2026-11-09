# ollama serve on demand, via a Windows service

Status: To Do (backlog TASK-79)

## Why

ollama serve on demand, via a Windows service

- today it is started by hand (or the tray app) before minuet's ollama provider works
- start the service when nvim needs it (minuet's openai_fim_compatible, gen.nvim, llm.nvim); stop it when idle
- check: ollama's own Windows service support, else a service wrapper (nssm, sc.exe)
- :CheckHealthSimpleMinuet already reports when the server does not answer

## What Changes

- (to be worked out)

## Impact

- Source: `todo-2027.md`, section "git add improvement"

## Original notes

```markdown
- [ ] ollama serve on demand, via a Windows service (2026-10-31)
  - today it is started by hand (or the tray app) before minuet's ollama provider works
  - start the service when nvim needs it (minuet's openai_fim_compatible, gen.nvim, llm.nvim); stop it when idle
  - check: ollama's own Windows service support, else a service wrapper (nssm, sc.exe)
  - :CheckHealthSimpleMinuet already reports when the server does not answer
```
