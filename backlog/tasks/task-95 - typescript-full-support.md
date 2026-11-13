---
id: TASK-95
title: 'typescript full support'
status: Needs Test
assignee: []
created_date: '2026-11-10'
labels:
  - nvim-config
  - typescript
  - goal
dependencies: []
ordinal: 95000
---

## Description

A project that is only TypeScript gets what a PHP project gets: React, Vue, Angular, Svelte, Astro on Node,
with lint, tests and a debugger for the server and the browser (README goal, 2026-11-10).

- Guides (how it works, how to try it):
  - `backlog/docs/doc-63 - guide-js-tests.md`: JS/TS tests in neotest: vitest or jest (2026-11-10)
  - `backlog/docs/doc-66 - guide-typescript.md`: TypeScript projects out of the box (2026-11-10)

## Acceptance Criteria

- [x] #1 vue, angular, svelte, astro languages (genja-completion011 1f0eef1)
- [x] #2 parsers svelte, astro, angular; eslint in svelte and astro (config cd7ee4d)
- [x] #3 js-debug-adapter: Node launch, npm run dev, attach; Chrome on the dev server (config cd7ee4d)
- [x] #4 neotest-vitest and neotest-jest by config file (config 1ee4bd2)

## Verify

- [ ] one sample app per framework, the steps in the config's backlog/docs/doc-66 - guide-typescript.md
- [ ] Node and Chrome debugging stop at a breakpoint
