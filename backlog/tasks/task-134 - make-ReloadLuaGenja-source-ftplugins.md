---
id: TASK-134
title: 'make :ReloadLuaGenja source ftplugins'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - reload
dependencies: []
ordinal: 134000
---

## Description

reload: `:ReloadLuaGenja` only reloaded Lua modules; it now also sources the config's `ftplugin/` and
`after/ftplugin/` files again for every loaded buffer's filetype. Commits: config cfa03da.

## Acceptance Criteria

- [x] #1 `lua/genja/ext/user-command/reload-lua.lua`: `reload_ftplugins` sources the files per window (so
  window options land there), hidden loaded buffers inside the buffer
- [x] #2 a failing ftplugin file gets its own error message; the summary names the file count
- [x] #3 `lua/genja/readme.md`: line for `reload-lua.lua` updated

## Verify

- [ ] test: change `foldlevel` in `after/ftplugin/markdown.lua`, `:ReloadLuaGenja` in a markdown window: the
  option follows, the message reads "reloaded N modules, M ftplugin files"
- [ ] test: a syntax error in an ftplugin file: an error message lists the file, nothing else breaks

## Notes

- Filetypes with no loaded buffer are skipped on purpose; their files load from disk when such a buffer opens.
