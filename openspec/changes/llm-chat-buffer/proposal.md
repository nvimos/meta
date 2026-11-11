# LLM chat in a buffer

Status: To Do (backlog TASK-27)

## Why

The genja-ask popup answers one question; minuet covers ghost text. A running conversation, like the
browser chat, has no home in the editor yet, and codecompanion's chat may or may not fit.

## What Changes

- survey first: codecompanion, avante, gp.nvim, parrot and others against the model below
  (`backlog/docs/doc-7 - llm-chat-survey.md`); use one only if it fits, else build on genja-ask
- one running conversation per buffer: ask, the answer is appended, the next question goes below it
- questions close as folds by themselves; answers can be folded by hand
- any provider, not tied to one vendor

## Impact

- `plug-wip/genja-ask.nvim`, `lua/lazyp/langs-comps/codecompanion.lua`
