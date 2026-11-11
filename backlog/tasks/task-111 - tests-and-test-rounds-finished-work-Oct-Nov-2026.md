---
id: TASK-111
title: 'tests and test rounds: finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-26'
labels:
  - tests
  - from-config
dependencies: []
ordinal: 111000
---

## Description

Finished work on tests and test rounds, 2026-10-26 .. 2026-11-07: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

## Acceptance Criteria

- [x] #1 tests: runner through pwsh, per-name groups, timings for every case, plan/status/slow/failed (2026-10-26; `solved-26.10.26-22.30-test-runner.md`)
- [x] #2 todo-test: test notes moved into todo-test/ (2026-10-26; `solved-26.10.26-23.48-todo-test-move.md`)
- [x] #3 tests: diag-limit test moved to tests/ui/ (2026-10-29; `solved-26.10.29-20.56-diag-limit-tests.md`)
- [x] #4 tests: which-key groups vs mappings, warnings both ways (2026-10-29; `solved-26.10.29-22.26-which-groups-test.md`)
- [x] #5 tests: comps011 gopls timed out on a cold go build cache (2026-10-31; `solved-26.10.31-06.53-go-warmup.md`)
- [x] #6 tests: make timings lists slowest last and hides fast cases (2026-10-31; `solved-26.10.31-06.53-timings-order.md`)
- [x] #7 tests: fail when a linter of lua/genja/ext/lint.lua is not installed (2026-10-31; `solved-26.10.31-12.14-linters-installed.md`)
- [x] #8 tests: llm dir, minuet <M-y> completes a shebang (2026-10-31; `solved-26.10.31-13.30-llm-minuet-test.md`)
- [x] #9 tests: markdownlint, gitleaks and vale on one markdown file (2026-10-31; `solved-26.10.31-20.02-lint-md-mixed.md`)
- [x] #10 tests: guided session results (2026-10-31, evening) (2026-10-31; `solved-26.10.31-20.02-test-results.md`)
- [x] #11 tests: copilot case skips when copilot.vim is not in lazy (2026-11-02; `solved-26.11.02-18.53-copilot-skip.md`)
- [x] #12 tests: NOTE of a passing case in yellow, shorter line (2026-11-03; `solved-26.11.03-14.02-tests-note.md`)
- [x] #13 tests: :vert term shell names case typed a char the menu waits for (2026-11-06; `solved-26.11.06-15.13-test-cmdline-shell.md`)
- [x] #14 tests: which-key groups with buffer-local keys not listed as empty (2026-11-06; `solved-26.11.06-15.13-test-which-groups.md`)
- [x] #15 tests: automated test for the <F2> script group (2026-11-07; `solved-26.11.07-02.07-f2-scripts-test.md`)
- [x] #16 tests: guided round, read aloud with the audible-wizard skill (2026-11-07; `solved-26.11.07-04.10-test-round.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: `make gather`, then `make slow` and `make timings`: other dirs' cases show up (`solved-26.10.26-22.30-test-runner.md`)
- [ ] test: `make plan`, `make status`: tables and estimates read well (`solved-26.10.26-22.30-test-runner.md`)
- [ ] test: break a test, `make test`, then `make failed`: only it reruns, verbose (`solved-26.10.26-22.30-test-runner.md`)
- [ ] test: default `make test`: slow line after the summary (`solved-26.10.26-22.30-test-runner.md`)
- [ ] test: `make test D=ui` in tests/ (`solved-26.10.29-20.56-diag-limit-tests.md`)
- [ ] test: `make test D=comps011 G=warmup` then `G=gopls` in tests/ (`solved-26.10.31-06.53-go-warmup.md`)
- [ ] test: `make timings`, `make timings V=1`, `make timings V=2` in tests/ (`solved-26.10.31-06.53-timings-order.md`)
- [ ] test: `make test D=comps011 G=md-mixed` (`solved-26.10.31-20.02-lint-md-mixed.md`)
- [ ] zen in nvim-qt: z0 keeps the maximized size; questions recorded there (`solved-26.10.31-20.02-test-results.md`)
- [ ] genja-commit split window (todo-issue/solved-26.10.31-20.02-commit-split.md) (`solved-26.10.31-20.02-test-results.md`)
- [ ] test: `make test D=completion` shows the case as skipped, not failed (`solved-26.11.02-18.53-copilot-skip.md`)
- [ ] test: `make test D=llm` in `tests/` (`solved-26.11.03-14.02-tests-note.md`)
- [ ] the `O` progress mark for pass-with-notes is still green (`solved-26.11.03-14.02-tests-note.md`)
- [ ] test: make -C tests D=completion (`solved-26.11.06-15.13-test-cmdline-shell.md`)
- [ ] test: make -C tests D=ui (`solved-26.11.06-15.13-test-which-groups.md`)
- [ ] minuet staged diff: find why codestral ignores it (`solved-26.11.07-04.10-test-round.md`)
- [ ] test: <M-g> with ollama after <M-r> (`solved-26.11.07-04.10-test-round.md`)
