---
id: TASK-22
title: 'php full support'
status: Needs Test
assignee: []
created_date: '2026-11-05'
labels:
  - nvim-config
  - todo-ideas
  - ideas-october
  - todo-2026-neovim011
  - release-v2026
dependencies: []
ordinal: 22000
priority: medium
---

## Description

PHP project out of the box

- examples: Drupal site; Symfony app with a React front end; custom app with Behat
- gaps add: React side (jsx/tsx, eslint, a JS test runner)
- have: phpactor in WSL (completion, diagnostics, refactors), framework detection WordPress/Laravel/Symfony,
  phpstan/php-cs-fixer/phpcs/pint from vendor/bin (plug-wip/genja-completion011.nvim/lua/genja/lang/php.lua),
  laravel-ls + blade-nav (lua/lazyp/langs/php-laravel.lua), neotest pest/phpunit (php-neotest.lua),
  overseer php_test template, emmet, typescript lang module, treesitter html/php/phpdoc/blade/js/ts/json/yaml
- gaps (from a grep, not tested): no treesitter css/scss/twig; no CSS or HTML LSP, no eslint/stylelint/biome;
  no twig (Symfony, Drupal); no Behat runner; Drupal not detected; composer.json / package.json scripts not offered as tasks (check overseer)
      parsers css scss twig jsdoc regex (9a8aa25, need a C compiler: winget install LLVM.LLVM);
      cssls + html lang modules (c18994b, 0ed9ee4); eslint + stylelint with a project config (e7bad3d);
      Drupal: phpactor indexes .module etc., ft mapping, drupal-check (236948c, dbc21f8);
      `<F2>` composer/npm scripts (bac05c1); Behat overseer template via ddev in WSL (23d563c)

From `todo-ideas.md`, section "ideas october".

- v2026 release checklist item 12 (was TASK-52): PHP gaps (auto-todo 2026-11-05 did all but a JS test runner, untested):...

- Guides (how it works, how to try it):
  - `backlog/docs/doc-52 - guide-behat.md`: Behat runner (2026-11-05)
  - `backlog/docs/doc-54 - guide-css-html-lsp.md`: CSS and HTML language servers (2026-11-05)
  - `backlog/docs/doc-55 - guide-drupal.md`: Drupal projects (2026-11-05)
  - `backlog/docs/doc-56 - guide-f2-scripts.md`: composer and npm scripts as tasks (2026-11-05)
  - `backlog/docs/doc-57 - guide-lint-go-js-css.md`: golangci-lint, eslint, stylelint (2026-11-05)
  - `backlog/docs/doc-59 - guide-parsers-web-go.md`: Treesitter parsers for PHP-project web files and Go (2026-11-05)

## Acceptance Criteria

- [x] #1 `<F2>` scripts: automated test, fixtures tests/f2/eff-two/, :OverseerToggle (5fe22f0)
- [x] #2 React side: a JS test runner (vitest / jest through neotest), not decided yet

## Verify

Hands-on checks, kept apart from the build steps.

- [x] auto-todo 2026-11-05 (guides doc-wip/readme.2026-11-05.*.md, all untested):
- [x] both, picked by the project's config file (vitest wins), lua/lazyp/langs/php-neotest.lua (2026-11-10); untested
- [ ] try it by hand (marked untested in the notes)

## Original notes

```markdown
- [ ] PHP project out of the box (goal in CLAUDE.md ## Goal, 2026-11-05)
  - examples: Drupal site; Symfony app with a React front end; custom app with Behat
  - gaps add: React side (jsx/tsx, eslint, a JS test runner)
  - have: phpactor in WSL (completion, diagnostics, refactors), framework detection WordPress/Laravel/Symfony,
    phpstan/php-cs-fixer/phpcs/pint from vendor/bin (plug-wip/genja-completion011.nvim/lua/genja/lang/php.lua),
    laravel-ls + blade-nav (lua/lazyp/langs/php-laravel.lua), neotest pest/phpunit (php-neotest.lua),
    overseer php_test template, emmet, typescript lang module, treesitter html/php/phpdoc/blade/js/ts/json/yaml
  - gaps (from a grep, not tested): no treesitter css/scss/twig; no CSS or HTML LSP, no eslint/stylelint/biome;
    no twig (Symfony, Drupal); no Behat runner; Drupal not detected; composer.json / package.json scripts not offered as tasks (check overseer)
  - [x] auto-todo 2026-11-05 (guides doc-wip/readme.2026-11-05.*.md, all untested):
        parsers css scss twig jsdoc regex (9a8aa25, need a C compiler: winget install LLVM.LLVM);
        cssls + html lang modules (c18994b, 0ed9ee4); eslint + stylelint with a project config (e7bad3d);
        Drupal: phpactor indexes .module etc., ft mapping, drupal-check (236948c, dbc21f8);
        `<F2>` composer/npm scripts (bac05c1); Behat overseer template via ddev in WSL (23d563c)
    - [x] `<F2>` scripts: automated test, fixtures tests/f2/eff-two/, :OverseerToggle (5fe22f0)
  - [x] React side: a JS test runner (vitest / jest through neotest), not decided yet
    - [x] both, picked by the project's config file (vitest wins), lua/lazyp/langs/php-neotest.lua (2026-11-10); untested
```
