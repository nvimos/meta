# TypeScript projects out of the box

Status: Needs Test (backlog TASK-95)

## Why

A project that is only TypeScript should get what a PHP project gets, without days of setup.

## What Changes

- vue, angular, svelte, astro languages in genja-completion011
- parsers, eslint for svelte and astro
- js-debug-adapter for Node and Chrome
- neotest-vitest / neotest-jest

## Impact

- config: lua/genja/ext/debug-js.lua, lua/lazyp/debug/dap-php.lua, lua/lazyp/langs/php-neotest.lua
- plugin: lua/genja/lang/{typescript,vue,angular,svelte,astro}.lua
