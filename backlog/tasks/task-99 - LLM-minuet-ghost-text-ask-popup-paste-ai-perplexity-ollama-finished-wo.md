---
id: TASK-99
title: 'LLM: minuet ghost text, ask popup, paste-ai, perplexity, ollama: finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-29'
labels:
  - nvim-config
  - llm
  - from-config
dependencies: []
ordinal: 99000
---

## Description

Finished work on LLM, 2026-10-29 .. 2026-11-05: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

- Guides (how it works, how to try it):
  - `backlog/docs/doc-10 - guide-ask-popup.md`: Ask popup (#16)
  - `backlog/docs/doc-25 - guide-ask-floaterm-send.md`: Ask popup: `<M-p>` sends to the claude floaterm (idea 19)
  - `backlog/docs/doc-45 - guide-paste-search.md`: Paste search: one provider for all lookups
  - `backlog/docs/doc-49 - guide-ghost-text-minuet-llm.md`: Local ghost text: minuet-ai.nvim and llm.nvim on ollama (2026-10-31)
  - `backlog/docs/doc-68 - guide-minuet-providers.md`: minuet-ai.nvim providers (2026-10-31)

## Acceptance Criteria

- [x] #1 perplexity: search moved to a module, right-click on a selection (2026-10-29; `solved-26.10.29-20.56-perplexity-module.md`)
- [x] #2 lookup: paste search plugin with providers (2026-10-29; `solved-26.10.29-22.26-paste-search.md`)
- [x] #3 paste-ai: more search providers, (ai) mark in the picker (2026-10-29; `solved-26.10.29-22.49-paste-providers.md`)
- [x] #4 paste-ai: :Google, :Perplexity, :Xty always use their provider; :Wot alias; :Pplx removed (2026-10-29; `solved-26.10.29-22.59-paste-commands.md`)
- [x] #5 minuet: :CheckHealthSimpleMinuet, modelled on :CheckHealthSimpleLsp (2026-10-31; `solved-26.10.31-10.23-minuet-health.md`)
- [x] #6 minuet: no completions from ollama; providers and keys (2026-10-31; `solved-26.10.31-10.23-minuet-providers.md`)
- [x] #7 minuet: Codestral by default, curl retry removed (2026-10-31; `solved-26.10.31-12.14-minuet-codestral.md`)
- [x] #8 ai: shelve llm.nvim and copilot.vim (2026-10-31; `solved-26.10.31-20.02-ghost-shelve.md`)
- [x] #9 minuet: ghost text takes over gitcommit buffers (2026-10-31; `solved-26.10.31-20.02-minuet-gitcommit.md`)
- [x] #10 paste-ai: right-click search with a picked provider (2026-10-31; `solved-26.10.31-20.02-paste-provider.md`)
- [x] #11 minuet: ghost text on ollama, README note (2026-11-05; `solved-26.11.05-20.22-minuet-ollama.md`)
- [x] #12 <m-?>:  popup with ai chat to ask some random question. (done 2026-10-23, untested: backlog/docs/doc-10 - guide-ask-popup.md) (undated; `ideas-16-ask-popup.md`)
- [x] #13 codecompanion «idea 19a companion» (lua/lazyp/langs-comps/codecompanion.lua) (closed 2026-10-23: spec kept, trial untested) (undated; `ideas-19a-codecompanion.md`)
- [x] #14 voice input in nvim (closed 2026-10-23: stop at Win+H; whisper.cpp build spec in todo-2027.txt) (undated; `ideas-20-voice-input.md`)
- [x] #15 copilot.vim: ghost text, keys in the cheatsheet (7d3d537, 53744b7); loads only for gitcommit, <leader>at toggles the other filetypes (e02ab60) (undated; `ideas-27-copilot.md`)
- [x] #16 want true "Ghost Text" (gray text inside the buffer like GitHub Copilot) rather than a popup menu, it is highly recommended to use llm.nvim or copilot.vim architectural alternatives alongside blink.cmp. (undated; `ideas-56-ghost-text-minuet-llm.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: select text, right-click, Perplexity: selection opens the browser (`solved-26.10.29-20.56-perplexity-module.md`)
- [ ] test: each new provider once (yandex, claude, google-ai, kagi, ...) (`solved-26.10.29-22.49-paste-providers.md`)
- [ ] test: :Xty, :Wot; current provider unchanged after :Google; :Pplx is unknown (`solved-26.10.29-22.59-paste-commands.md`)
- [ ] suggestions ignore the staged diff (todo-ideas.md #14) (`solved-26.10.31-20.02-minuet-gitcommit.md`)
- [ ] test Windows voice typing (Win+H) in insert mode: free (untested list) (`ideas-20-voice-input.md`)
