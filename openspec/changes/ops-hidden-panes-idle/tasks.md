# Tasks

## 1. Build

- [ ] 1.1 measure: backend calls per git hint while working in one mode (the `rpc` timings)
- [ ] 1.2 the shell tells each mode whether it is shown (from the `IndexedStack` index)
- [ ] 1.3 a shared `markStale()` / `refreshIfStale()` building block for the states
- [ ] 1.4 go through the modes and panes listed in the proposal; name what stays live and why
- [ ] 1.5 PLAN.md (Performance) and CLAUDE.md (the rule, for new states)

## 2. Verify

- [ ] 2.1 tests: a git hint while hidden makes no backend call; showing a stale mode makes one; a
  mode that is not stale makes none
- [ ] 2.2 measure again: calls per git hint, before and after
