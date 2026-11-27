---
id: TASK-212
title: 'treesitter parsers per enabled language'
status: To Do
assignee: []
created_date: '2026-11-27'
labels:
  - nvim-config
  - completion
dependencies: []
ordinal: 212000
---

## Description

The treesitter parsers come from a fixed list in the config's `lua/lazyp/my/load-treesitter.lua`,
apart from the languages switched on in genja-completion011. Each language module (and each
completion feature that needs one) names its parsers next to its servers and tools; the config
installs the parsers of the enabled languages plus a short base list, instead of the fixed list.
Nothing is uninstalled; leftovers show in `:checkhealth genja.lsp` and `make status`.

Change: `openspec/changes/lang-treesitter-parsers/`.

## Acceptance Criteria

- [ ] #1 `parsers` field in `genja.Lang`, filled in every language module (mapping in the proposal, checked against LazyVim and AstroCommunity)
- [ ] #2 features gitcommit, gitignore and sshconfig name their parsers
- [ ] #3 `require('genja.lsp').parsers()`: base list plus enabled languages and features, without loading mason
- [ ] #4 `load-treesitter.lua` installs `parsers()` plus the config's own short list (yaml, xml), still scheduled after the first screen
- [ ] #5 `:checkhealth genja.lsp` lists parsers wanted but missing, and installed but not wanted
- [ ] #6 `make status` in `tests/` shows the parsers per language
- [ ] #7 plugin README, plugin CLAUDE.md and the config's CLAUDE.md ("Filetypes and parsers") updated

## Verify

- [ ] manual: switch `c_cpp` on in `local.lua`, restart; `c` and `cpp` get installed and a `.c` file highlights
- [ ] manual: switch a language off; its parsers are no longer installed on a fresh data dir, and checkhealth lists the old ones as not wanted
- [ ] manual: `make startup` shows no new cost before UIEnter
