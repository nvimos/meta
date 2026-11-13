---
id: TASK-20
title: 'completion: blink cmdline completion of shell commands (`!cmd`, `:terminal cmd`) is...'
status: Needs Test
assignee: []
created_date: '2026-11-02'
labels:
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 20000
---

## Description

completion: blink cmdline completion of shell commands (`!cmd`, `:terminal cmd`) is...

- today: blink cmdline source in plug-wip/genja-completion011.nvim/lua/genja/completion/cmdline.lua; shell names come from getcompletion(..., 'shellcmd') = $PATH scan on every keypress (inferred, not profiled)
- upstream: blink recipe turns cmdline completion off for `:!` and `:%!` only, because Git Bash or WSL hang (<https://cmp.saghen.dev/recipes>); feature request to ignore commands in the cmdline source, not resolved in the results (<https://github.com/saghen/blink.cmp/issues/1029>); Neovim docs: shell command names come from $PATH (:h cmdline-completion)
- no PATH cache found upstream in Neovim or blink; a cache would be ours
- try: profile first (time getcompletion('', 'shellcmd') on this PATH); then cache the list in Lua, rebuild on PATH change or after 3 h, serve it from the cmdline source for `!` and `:terminal`; or drop shellcmd for `!` as the recipe does
- test: `!` then letters, `:terminal` then letters: menu appears within a keypress
- 2026-11-02: written: lua/genja/completion/shellcmd.lua, list in stdpath('state')/genja-completion011/shellcmd.txt, rebuilt after 3 h or on PATH change; `!word`, `:term word` and `:vert term word`; tests/completion/test_cmdline.lua: PATH-change rebuild and `:vert term` pass (make test D=completion); the 3 h age rebuild is untested (abfb666); :ResetPathCache deletes the list

From `todo-ideas.md`, section "ideas october".

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] try it by hand (marked untested in the notes)

## Original notes

```markdown
- [x] completion: blink cmdline completion of shell commands (`!cmd`, `:terminal cmd`) is very slow
  - today: blink cmdline source in plug-wip/genja-completion011.nvim/lua/genja/completion/cmdline.lua; shell names come from getcompletion(..., 'shellcmd') = $PATH scan on every keypress (inferred, not profiled)
  - upstream: blink recipe turns cmdline completion off for `:!` and `:%!` only, because Git Bash or WSL hang (<https://cmp.saghen.dev/recipes>); feature request to ignore commands in the cmdline source, not resolved in the results (<https://github.com/saghen/blink.cmp/issues/1029>); Neovim docs: shell command names come from $PATH (:h cmdline-completion)
  - no PATH cache found upstream in Neovim or blink; a cache would be ours
  - try: profile first (time getcompletion('', 'shellcmd') on this PATH); then cache the list in Lua, rebuild on PATH change or after 3 h, serve it from the cmdline source for `!` and `:terminal`; or drop shellcmd for `!` as the recipe does
  - test: `!` then letters, `:terminal` then letters: menu appears within a keypress
  - 2026-11-02: written: lua/genja/completion/shellcmd.lua, list in stdpath('state')/genja-completion011/shellcmd.txt, rebuilt after 3 h or on PATH change; `!word`, `:term word` and `:vert term word`; tests/completion/test_cmdline.lua: PATH-change rebuild and `:vert term` pass (make test D=completion); the 3 h age rebuild is untested (abfb666); :ResetPathCache deletes the list
```
