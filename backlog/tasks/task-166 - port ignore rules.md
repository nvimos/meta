---
id: TASK-166
title: 'port ignore rules'
status: Done
assignee:
  - deepseek
created_date: '2026-11-19'
labels:
  - frontend
  - ops
  - purrage
dependencies:
  - TASK-156
ordinal: 166000
---

## Description

Port Purrage's ignore layer: rule scopes (file, extension, folder), targets (root/folder
`.gitignore`, local exclude, global ignore), `git check-ignore` parsing, section append, line
replacement and the nested-repository guard. No view yet.

Change: `openspec/changes/purrage-actions/`.
Coordination: `backlog/docs/doc-76 - purrage integration coordination.md`.

## Acceptance Criteria

- [x] #1 a rule is previewed for each scope without writing
- [x] #2 one batched `check-ignore` answers for many paths
- [x] #3 rules append under the Purrage section without duplicate lines
- [x] #4 line endings and the final newline are preserved
- [x] #5 a path in a nested repository is not given a rule in the outer one

## Verify

- [x] test: each scope and target on a temp repo
- [x] test: Windows drive letters in `check-ignore` output parse correctly
- [x] test: CRLF and LF ignore files both survive an append
