---
id: TASK-159
title: 'open folder and choose backend'
status: Needs Test
assignee:
  - claude
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-154
  - TASK-156
ordinal: 159000
---

## Description

Make the Connect screen a list of recent folders and Neovim addresses, each remembering its backend,
with a way to add a folder or an address. Choosing a folder creates a `LocalBackend`. The directory
command-line argument opens a local repository right away (decided 2026-11-19, even while the local
backend is read-only); an address still selects Neovim.

Change: `openspec/changes/purrage-local-git-backend/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 the Connect screen lists recent folders and addresses, each opening with its own backend, and can add either kind
- [x] #2 a folder creates a LocalBackend and enters the normal mode shell
- [x] #3 `ops.exe <directory>` opens locally without starting a Neovim
- [x] #4 an address still selects the Neovim backend
- [x] #5 switching backends resets the modes and their stale state

## Verify

- [x] test: select a temp repo by path and reach the mode shell
- [x] test: a `127.0.0.1:port` argument still selects Neovim
- [ ] manual: no console window appears when opening a local folder
