# keymaps tracker: keep counts in memory, write them once on exit

Status: To Do (backlog TASK-63)

## Why

keymaps tracker: keep counts in memory, write them once on exit

- today: plug-wip/abdul-keymaps.nvim/lua/keymaps/tracker.lua writes stdpath('data')/keymaps/usage.json
  every 10th use of a key (`record()`), and again on VimLeavePre
- change: `record()` only counts in memory; one write from a VimLeavePre autocmd in its own augroup
- edge cases, nvim must always exit cleanly:
  - dir missing: mkdir -p; dir or file not writable, disk full: pcall the write, no error, no hang on :qa
  - write to a temp file next to usage.json, then rename, so a crash mid-write keeps the old file
  - unreadable or corrupt usage.json at start: start empty, keep the bad file as usage.json.bak
  - several nvim instances: re-read the file before writing and add this session's counts, not overwrite
  - crash or kill (no VimLeavePre): this session's counts are lost; accepted, or a timer flush every few minutes
  - `:KeymapsStats` and `get_top()` read the in-memory table, so they stay current without a write
- context: `:KeymapsStats` shows only the top 10 and plain keys fill it; a longer or filtered list
  (leader/plugin maps only) would make the counts useful

## What Changes

- (to be worked out)

## Impact

- Source: `todo-2027.md`, section "new setup 2027"

## Original notes

```markdown
- [ ] keymaps tracker: keep counts in memory, write them once on exit (2026-11-07)
  - today: plug-wip/abdul-keymaps.nvim/lua/keymaps/tracker.lua writes stdpath('data')/keymaps/usage.json
    every 10th use of a key (`record()`), and again on VimLeavePre
  - change: `record()` only counts in memory; one write from a VimLeavePre autocmd in its own augroup
  - edge cases, nvim must always exit cleanly:
    - dir missing: mkdir -p; dir or file not writable, disk full: pcall the write, no error, no hang on :qa
    - write to a temp file next to usage.json, then rename, so a crash mid-write keeps the old file
    - unreadable or corrupt usage.json at start: start empty, keep the bad file as usage.json.bak
    - several nvim instances: re-read the file before writing and add this session's counts, not overwrite
    - crash or kill (no VimLeavePre): this session's counts are lost; accepted, or a timer flush every few minutes
    - `:KeymapsStats` and `get_top()` read the in-memory table, so they stay current without a write
  - context: `:KeymapsStats` shows only the top 10 and plain keys fill it; a longer or filtered list
    (leader/plugin maps only) would make the counts useful
```
