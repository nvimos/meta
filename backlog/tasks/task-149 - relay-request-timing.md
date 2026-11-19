---
id: TASK-149
title: 'time relay requests'
status: To Do
assignee: []
created_date: '2026-11-14'
labels:
  - backend
dependencies: []
ordinal: 149000
---

## Description

The relay times every request Ops makes, per endpoint (`<module>.<fn>`), with the time spent in git,
and writes a per-session summary quietly to `%LOCALAPPDATA%\nvimos\relay-timing.json` when Neovim
exits and every few minutes before that. The point is to find the slow parts; put next to Ops's
`ui-timing.json`, the difference is the transport and the queue.

Change: `openspec/changes/relay-request-timing/`.

## Acceptance Criteria

- [ ] #1 every public function of the modules Ops calls is timed, keyed as Ops keys its `rpc` timings
- [ ] #2 git time per request, from one hook in `repo.run`
- [ ] #3 per session and endpoint: n, avg, p50, p95, max, total, git, errors
- [ ] #4 the last 30 sessions kept, totals sorted by total time with each endpoint's share
- [ ] #5 written on exit and every few minutes, with no message; a failed write is swallowed
- [ ] #6 `NVIMOS_TIMING=0` turns it off
- [ ] #7 README names the file and the switch

## Verify

- [ ] test: call a few endpoints, force a write, read back the summary with the right keys and counts
- [ ] test: a raising endpoint is counted under errors and still raises to the caller
- [ ] test: with `NVIMOS_TIMING=0` nothing is recorded or written
- [ ] manual: use Ops for a while, quit Neovim; `relay-timing.json` has the session, and its endpoints match the `rpc` keys in `ui-timing.json`
