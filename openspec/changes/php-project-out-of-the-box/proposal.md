# PHP project out of the box

Status: Needs Test (backlog TASK-22)

## Why

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

## What Changes

- `<F2>` scripts: automated test, fixtures tests/f2/eff-two/, :OverseerToggle (5fe22f0)
- React side: a JS test runner (vitest / jest through neotest), not decided yet

## Impact

- Source: `todo-ideas.md`, section "ideas october"

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
