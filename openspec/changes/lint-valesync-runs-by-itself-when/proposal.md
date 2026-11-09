# lint: :ValeSync runs by itself when the shared styles are missing

Status: Needs Test (backlog TASK-18)

## Why

lint: :ValeSync runs by itself when the shared styles are missing

- today vale is skipped until :ValeSync (lua/genja/ext/lint.lua prepare_vale), no hint that it's off
- 2026-11-02: the first lint without styles starts the sync once per session, then lints all buffers again; untested (1c67fc5)

## What Changes

- (to be worked out)

## Impact

- Source: `todo-ideas.md`, section "ideas october"

## Original notes

```markdown
- [x] lint: :ValeSync runs by itself when the shared styles are missing (asked 2026-10-31)
  - today vale is skipped until :ValeSync (lua/genja/ext/lint.lua prepare_vale), no hint that it's off
  - 2026-11-02: the first lint without styles starts the sync once per session, then lints all buffers again; untested (1c67fc5)
```
