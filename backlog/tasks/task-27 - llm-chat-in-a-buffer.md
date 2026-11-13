---
id: TASK-27
title: 'LLM chat in a buffer, like the browser chat'
status: To Do
assignee: []
created_date: '2026-11-05'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
  - todo-2026-neovim011
  - release-v2026
dependencies: []
ordinal: 27000
---

## Description

LLM chat in a buffer, like the browser chat

Change: `openspec/changes/llm-chat-buffer/`

- open a buffer, ask; it thinks, appends the answer; type a follow-up below it, the next answer is appended; one running conversation
- maybe a separate input buffer (simpler), but questions and answers live in the chat buffer
- folds: questions close automatically as folds; responses can be closed by hand when needed
- likely an extension of the genja-ask popup (plug-wip/genja-ask.nvim)
- survey session, test steps and questions: `backlog/docs/doc-7 - llm-chat-survey.md`
- first: survey existing chat plugins (codecompanion, avante, gp.nvim, parrot, others); use one only if its interface fits
  the mental model above; otherwise build our own and take the ideas that work (what to do, what to avoid)
- any provider, not tied to ChatGPT
- today: codecompanion.nvim chat with Claude Code over ACP (lua/lazyp/langs-comps/codecompanion.lua,
  doc-wip/readme.idea19-companion.md) already works this way; genja-ask popup is one question, one answer;
  minuet covers ghost text. Find out what's missing in codecompanion before building one

From `todo-ideas.md`, section "ideas october".
- v2026 release checklist item 9 (was TASK-49): LLM chat: survey first (`backlog/docs/doc-7 - llm-chat-survey.md`), then use one or build on...

## Original notes

```markdown
- [ ] LLM chat in a buffer, like the browser chat (2026-11-05; an idea, to be fleshed out)
  - open a buffer, ask; it thinks, appends the answer; type a follow-up below it, the next answer is appended; one running conversation
  - maybe a separate input buffer (simpler), but questions and answers live in the chat buffer
  - folds: questions close automatically as folds; responses can be closed by hand when needed
  - likely an extension of the genja-ask popup (plug-wip/genja-ask.nvim)
  - survey session, test steps and questions: todo-test/llm-chat-survey.md
  - first: survey existing chat plugins (codecompanion, avante, gp.nvim, parrot, others); use one only if its interface fits
    the mental model above; otherwise build our own and take the ideas that work (what to do, what to avoid)
  - any provider, not tied to ChatGPT
  - today: codecompanion.nvim chat with Claude Code over ACP (lua/lazyp/langs-comps/codecompanion.lua,
    doc-wip/readme.idea19-companion.md) already works this way; genja-ask popup is one question, one answer;
    minuet covers ghost text. Find out what's missing in codecompanion before building one
```
