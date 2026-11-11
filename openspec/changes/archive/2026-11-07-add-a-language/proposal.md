# Adding a language in one documented step

Status: Done (backlog TASK-55)

## Why

Each language (PHP, Go, C, TypeScript) was added in its own way, so the next one meant reading the
last. A checklist makes it one step and shows the gaps per language.

## What Changes

- `readme.add-a-language.md`: the checklist, read against Go
- languages turned on per spec, conservative defaults (TASK-34)

## Impact

- design and how-to: `design.md` (was the config's doc-wip guide)
- `readme.add-a-language.md` (7b69862), lang modules in `plug-wip/genja-completion011.nvim/lua/genja/lang/`
- checked against: PHP (TASK-22), Go (TASK-23), C (TASK-54), TypeScript (TASK-95)
