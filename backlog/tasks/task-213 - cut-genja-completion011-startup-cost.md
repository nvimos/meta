---
id: TASK-213
title: 'cut genja-completion011 startup cost'
status: To Do
assignee: []
created_date: '2026-11-27'
labels:
  - nvim-config
  - completion
  - performance
dependencies: []
ordinal: 213000
---

## Description

genja-completion011 is the largest item in a start after the 2026-11-27 profiling session: ~74 ms
own and ~138 ms total warm, ~114 ms own and ~361 ms total cold, loaded at VeryLazy before nvim takes
input. Split it so an empty start sets up only completion and the LSP part (mason, servers) loads
on the first filetype that has a server; touch Mason only when a package is missing; trace the
`spawn` seen during startup. Measure each step with `make startup-jitprof-plugins N=5`.

Change: `openspec/changes/comps-startup-cost/`.

Related: TASK-96 (startup below 1 s).

## Acceptance Criteria

- [ ] #1 an empty start loads blink.cmp and the cmdline sources, no mason or mason-lspconfig
- [ ] #2 the first FileType with an enabled server sets up LSP, and that buffer attaches
- [ ] #3 installed servers come from a listing of `mason/packages/`; `registry.refresh()`, ensure_installed and tool installs run only when a wanted package is missing, deferred
- [ ] #4 `nvim_get_runtime_file()` checks before `require` replaced, the missing-language warning kept
- [ ] #5 the startup `spawn` traced to its caller and moved out of startup or dropped
- [ ] #6 before and after numbers per step noted in this task
- [ ] #7 plugin CLAUDE.md updated

## Verify

- [ ] test: `make test D=comps011 G=lsp`, `G=ready`, `G=mason`, `G=cmp` pass in `tests/`
- [ ] manual: `nvim` with no file; `make startup-jitprof-plugins N=5` shows no mason lines
- [ ] manual: `nvim foo.lua` and `nvim foo.php`; the server attaches to the first buffer without `:e`
- [ ] manual: remove one installed server folder; on the next start it installs in the background and attaches when done
