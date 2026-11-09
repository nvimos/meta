# oil: self-heal stale entry ids after `:Lazy reload oil.nvim`

Status: To Do (backlog TASK-62)

## Why

oil: self-heal stale entry ids after `:Lazy reload oil.nvim`

- reload empties oil's module-local cache (oil/cache.lua); open oil buffers keep the old ids,
  so preview and select fail with `Entry N missing parent url`
- call sites: `toggle_preview_fit` (lua/genja/oil/plug/preview.lua), `select_custom` (lua/genja/oil/open.lua)
- fix: one helper in lua/genja/oil/utils: pcall the oil call; on `missing parent url` run `:e!` on the oil buffer,
  put the cursor back on the same entry name, retry once; notify via SRC only if the retry fails
- workaround until then: `:e!` in each oil buffer, or restart nvim

## What Changes

- (to be worked out)

## Impact

- Source: `todo-2027.md`, section "new setup 2027"

## Original notes

```markdown
- [ ] oil: self-heal stale entry ids after `:Lazy reload oil.nvim` (2026-11-07)
  - reload empties oil's module-local cache (oil/cache.lua); open oil buffers keep the old ids,
    so preview and select fail with `Entry N missing parent url`
  - call sites: `toggle_preview_fit` (lua/genja/oil/plug/preview.lua), `select_custom` (lua/genja/oil/open.lua)
  - fix: one helper in lua/genja/oil/utils: pcall the oil call; on `missing parent url` run `:e!` on the oil buffer,
    put the cursor back on the same entry name, retry once; notify via SRC only if the retry fails
  - workaround until then: `:e!` in each oil buffer, or restart nvim
```
