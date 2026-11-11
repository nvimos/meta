---
id: TASK-112
title: 'docs, todo files and skills: finished work, Oct-Nov 2026'
status: Needs Test
assignee: []
created_date: '2026-10-24'
labels:
  - docs
  - from-config
dependencies: []
ordinal: 112000
---

## Description

Finished work on docs, todo files and skills, 2026-10-24 .. 2026-11-09: solved issues and done ideas from the config's
`todo-issue/` and `todo-done/`, one step each. The files, with their sub-steps and commits, are in
`legacy/nvim-config/`.

Built; the Verify list holds the hand tests the issue files left open.

## Acceptance Criteria

- [x] #1 skills: /close-issues covers all uncommitted changes, timestamped file names (2026-10-24; `solved-26.10.24-06.42-close-issues-v2.md`)
- [x] #2 doc: how to paste into a floaterm (2026-10-24; `solved-26.10.24-17.31-floaterm-paste.md`)
- [x] #3 skills: /close-issues renamed to commit-close-issues (2026-10-24; `solved-26.10.24-17.31-skill-rename.md`)
- [x] #4 skills: project skills in nvim-* folders (2026-10-24; `solved-26.10.24-17.40-skills-nvim.md`)
- [x] #5 doc-wip: test guides named the old ask / paste keys (2026-10-25; `solved-26.10.25-00.07-guides-keys.md`)
- [x] #6 docs: file list and cheatsheet follow the lua/genja/ext move (2026-10-28; `solved-26.10.28-23.12-ext-docs.md`)
- [x] #7 todo: netrw notes and idea, small todo fixes (2026-10-28; `solved-26.10.28-23.12-todo-netrw.md`)
- [x] #8 doc-wip: career session notes (2026-10-29; `solved-26.10.29-20.56-salary-notes.md`)
- [x] #9 todo: todo files to markdown, test results moved to todo-done (2026-10-29; `solved-26.10.29-20.56-todo-files.md`)
- [x] #10 doc-wip: consultant rate notes (2026-10-29; `solved-26.10.29-22.26-consultant-rate.md`)
- [x] #11 todo: todo-2026-neovim011.md items closed (2026-10-29; `solved-26.10.29-22.26-neovim011-todo.md`)
- [x] #12 docs: CLAUDE.md names the todo files by their .md names (2026-10-29; `solved-26.10.29-22.26-todo-md-names.md`)
- [x] #13 style: whitespace in hilite.lua and zexp.lua (2026-10-29; `solved-26.10.29-22.26-whitespace.md`)
- [x] #14 todo: todo-ideas.md links the renamed .md todo files (2026-10-29; `solved-26.10.29-22.49-todo-links.md`)
- [x] #15 tidy: whitespace in completion specs and init (2026-10-31; `solved-26.10.31-14.42-whitespace-tidy.md`)
- [x] #16 tidy: blank lines (2026-10-31; `solved-26.10.31-20.02-tidy.md`)
- [x] #17 todo: scan commits up to 5c637f8 into the idea files (2026-11-03; `solved-26.11.03-14.10-todo-scan.md`)
- [x] #18 docs: ask-popup guide paths (2026-11-05; `solved-26.11.05-20.22-ask-guide.md`)
- [x] #19 skill: commit-close-issues also reads and commits plug-wip repos (2026-11-06; `solved-26.11.06-15.13-skill-plug-wip.md`)
- [x] #20 docs: add-a-language checklist read against Go (2026-11-07; `solved-26.11.07-04.10-add-a-language.md`)
- [x] #21 todo: languages and tooling missing for the grafana/terraform/k8s demo repo (2026-11-07; `solved-26.11.07-06.01-grafana-langs.md`)
- [x] #22 docs: survey LazyVim extras and AstroCommunity packs before adding a language (2026-11-07; `solved-26.11.07-06.01-lazyvim-survey.md`)
- [x] #23 skills: close-issues fixes loose ends before committing (2026-11-09; `solved-26.11.09-23.43-close-issues-leftovers.md`)
- [x] #24 docs: notes from review and dictation (2026-11-09; `solved-26.11.09-23.43-review-notes.md`)

## Verify

Hands-on checks, kept apart from the build steps.

- [ ] test: run `/close-issues` with changes from several features, some of them staged (`solved-26.10.24-06.42-close-issues-v2.md`)
- [ ] background sessions can't write the issue files in the main checkout (edit guard); see `todo-issue/01-close-issues-skill.md` (`solved-26.10.24-06.42-close-issues-v2.md`)
- [ ] CLAUDE.md still names `.claude/skills/close-issues/` (`solved-26.10.24-17.31-skill-rename.md`)
- [ ] nvim-auto-todo step 8 still writes ~/.claude/skills/auto-todo/runs.md (`solved-26.10.24-17.40-skills-nvim.md`)
- [ ] readme.2026-10-23.ask-popup.md still names lua/genja/ask.lua (now plug-wip/genja-ask.nvim) (`solved-26.10.25-00.07-guides-keys.md`)
- [ ] CLAUDE.md still names todo-2026-neovim011.txt and todo-2027.txt (`solved-26.10.29-20.56-todo-files.md`)
- [ ] test: the PR-langs, PR-k8s-yaml, PR-wsl-docker branches in a real session (servers attach, lint output, parsers) (`solved-26.11.07-06.01-grafana-langs.md`)
