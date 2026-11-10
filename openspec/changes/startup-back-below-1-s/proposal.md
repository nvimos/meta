# startup back below 1 s

Status: To Do (backlog TASK-96)

## Why

The startup test failed at 01:15 on 2026-11-10 (1.04-1.47 s, limit 1 s).

## What Changes

- find what grew and trim it

## Impact

- config: lua/genja/lazy-plug-spec.lua, lua/lazyp/my/load-treesitter.lua
