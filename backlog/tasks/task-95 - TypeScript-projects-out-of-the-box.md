---
id: TASK-95
title: 'TypeScript projects out of the box'
status: Needs Test
assignee: []
created_date: '2026-11-10'
labels:
  - typescript
  - goal
dependencies: []
ordinal: 95000
---

## Description

A project that is only TypeScript gets what a PHP project gets: React, Vue, Angular, Svelte, Astro on Node,
with lint, tests and a debugger for the server and the browser (README goal, 2026-11-10).

## Acceptance Criteria

- [x] #1 vue, angular, svelte, astro languages (genja-completion011 1f0eef1)
- [x] #2 parsers svelte, astro, angular; eslint in svelte and astro (config cd7ee4d)
- [x] #3 js-debug-adapter: Node launch, npm run dev, attach; Chrome on the dev server (config cd7ee4d)
- [x] #4 neotest-vitest and neotest-jest by config file (config 1ee4bd2)

## Verify

- [ ] one sample app per framework, the steps in the config's doc-wip/readme.2026-11-10.typescript.md
- [ ] Node and Chrome debugging stop at a breakpoint
