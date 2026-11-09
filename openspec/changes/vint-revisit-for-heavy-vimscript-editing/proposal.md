# vint: revisit for heavy vimscript editing

Status: To Do (backlog TASK-68)

## Why

vint: revisit for heavy vimscript editing

- vint disabled (2026-10-24): broken on Windows. Python 3.13 venv: no `pkg_resources`
      (Vimjas/vint#394, draft PR #397; pinning setuptools<81 in the mason venv gets past it),
      then `PosixPath` can't be instantiated on Windows (#378, open since 2022). Last release 2019.
      Revisit for heavy vimscript editing: Linux/WSL only, or a fork. (266485f)

## What Changes

- (to be worked out)

## Impact

- Source: `todo-2027.md`, section "new setup 2027"

## Original notes

```markdown
- [ ] vint: revisit for heavy vimscript editing (from todo-ideas #14e, moved 2026-10-31)
  - vint disabled (2026-10-24): broken on Windows. Python 3.13 venv: no `pkg_resources`
        (Vimjas/vint#394, draft PR #397; pinning setuptools<81 in the mason venv gets past it),
        then `PosixPath` can't be instantiated on Windows (#378, open since 2022). Last release 2019.
        Revisit for heavy vimscript editing: Linux/WSL only, or a fork. (266485f)
```
