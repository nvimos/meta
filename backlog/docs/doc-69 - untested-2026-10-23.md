---
id: doc-69
title: 'Untested features, 2026-10-23'
type: guide
created_date: '2026-10-23'
---

# Untested features, 2026-10-23

For a later guided session: one feature per question. Each line: feature,
key or command to try, file, guide.

## Session auto-todo-20261023-2048

- [x] telescope keymaps: <leader>jM, <M-r>/<M-R> desc groups, <M-f>/<M-x>/<BS> (lua/genja/ext/telescope-keymaps.lua) -> backlog/docs/doc-20 - guide-telescope-keymaps.md
    - 2026-10-24: steps 1-4, 6 by hand; <M-r> after <M-f> lost the filter, fixed; `make test D=telescope-keymaps` in tests/ (10 cases)
- [x] claude per project: :ClaudeFterm in two repos, <leader>mC / :ClaudeFterm! picker, <M-d> kill (plug-wip/genja-claudefterm.nvim) -> backlog/docs/doc-11 - guide-claude-per-project.md
    - 2026-10-24: unit tests, `make test D=claudefterm` in tests/ (tests/claudefterm/, 15 cases, fake claude); "paste starts claude" skips on Windows (headless terminal output goes to the outer console)
    - found: several FloatermKills in a row (kill() with 2+ terminals just started) sometimes crash the headless test nvim on Windows; maybe at :s:/quit too, not seen by hand
- [ ] linters: :MasonToolsInstall, then a .md / .yaml / workflow / playbook / Makefile with errors (lua/genja/ext/lint.lua) -> backlog/docs/doc-13 - guide-lint-first-wave.md
    - 2026-11-05: markdownlint MD018 ok; tools all installed except ansible-lint in WSL
    - 2026-11-05: checkmake works, but turned off by choice (commented out in lua/genja/ext/lint.lua by_ft + mason, and its comps011 case)
- [ ] recent files: <C-F1> project first, <M-a> all, saved file ranks first (plug-wip/genja-recent.nvim, lua/genja/ext/recent.lua) -> backlog/docs/doc-12 - guide-genja-recent.md
- [ ] right-click per filetype: markdown checkbox, oil git add, LSP entries, Morning (lua/genja/ext/popup-menu.lua) -> backlog/docs/doc-15 - guide-mouse-morning.md
- [ ] statusline clicks: file -> oil, branch -> Neogit, E/W -> loclist (genja-statusline clicks) -> backlog/docs/doc-15 - guide-mouse-morning.md
- [ ] :Morning: click a start dir, a recent file, a todo line; R, q (lua/genja/ext/morning.lua) -> backlog/docs/doc-15 - guide-mouse-morning.md
- [ ] ask popup: <M-?>, <C-CR>, y, <CR> follow-up, <M-t>/<M-m>/<M-e>/<M-s>/<M-r>, visual selection (lua/genja/ask.lua) -> backlog/docs/doc-10 - guide-ask-popup.md
- [ ] mini.starter: enabled = true, start nvim without files (lua/lazyp/ui/mini-starter.lua) -> backlog/docs/doc-15 - guide-mouse-morning.md

## Session auto-todo-20261023-1924

- [ ] fold markers with a title: visual `zf`, `<leader>wwf`, `:WrapFold` (lua/genja/ext/user-command/wrapfold.lua) -> backlog/docs/doc-23 - guide-wrapfold.md
- [ ] right-click Actions (g.), click/double-click in telescope, new actions source/claude (lua/genja/fn.vim, actions.lua) -> backlog/docs/doc-16 - guide-popup-actions.md
- [ ] ~ swaps true/false, +/-, </> …; <M-~> plain (lua/genja/ext/tilde.lua) -> backlog/docs/doc-21 - guide-tilde-dial.md
- [ ] dial.nvim <C-a>/<C-x>, g<C-a> per filetype groups (lua/lazyp/new/dial.lua) -> backlog/docs/doc-21 - guide-tilde-dial.md
- [ ] F2 markdown checklist: visual <F2> > markdown task (lua/genja/ext/md-checklist.lua) -> backlog/docs/doc-14 - guide-md-checklist.md
- [ ] telescope <M-x> exclude, <BS> undo (genja-finder refine.lua) -> backlog/docs/doc-17 - guide-refine-exclude.md, plugin README
- [ ] window sizes: <M-=> <M--> <M-0>, <leader>wr resize mode (lua/genja/ext/winsize.lua) -> backlog/docs/doc-22 - guide-winsize.md
- [ ] smart-splits.nvim: enable the spec to compare (lua/lazyp/new/smart-splits.lua) -> backlog/docs/doc-22 - guide-winsize.md
- [ ] resize keeps the tab: resize nvim-qt by any edge on tab 1 of 3, tab stays (real cause: VimResized tabdo, lua/genja/auto-alias.vim, PR-fix-32-resize-tab) -> todo-done/ideas-32-resize-last-tab.md
- [ ] tabline: clicks outside the labels do nothing (genja-statusline tabline.lua) -> backlog/docs/doc-19 - guide-tabline-click.md
- [ ] start dirs: <leader>sp/sa/sr/se, <M-1>..<M-4>, oil ,s ,S, ranked mydirs (plug-wip/genja-startdirs.nvim) -> backlog/docs/doc-18 - guide-startdirs.md

## Earlier, still untested

- [ ] voice typing: Win+H in insert mode, in nvim-qt and in a terminal (#20) -> todo-ideas.md #20
- [ ] gitsigns keys: <leader>h… stage/reset/preview, ]c [c, ih (lua/genja/map-plugin/gitsigns.lua) -> readme.cheatsheet.md Git
- [ ] Neogit / diffview / mini.git keys: <leader>mg, <leader>mGl, <leader>mGc, <leader>md/mh/mH, <leader>hc (#37) -> readme.cheatsheet.md Git
- [ ] genja-commit: commit popup, lint while typing, <M-g> message, Conventional Commits mode (#14) -> plug-wip/genja-commit.nvim/README.md
- [ ] <C-F1> oldfiles with refine keys <M-f> <M-n> <BS> (lua/genja/map-telescope.lua) -> plug-wip/genja-finder.nvim/README.md
- [ ] genja-finder scope: from:arg root in oil, prompt title last three parts, unix path labels (#8) -> doc-wip/squash-ideas-oct-17.details.done.md #8
- [ ] F2 git add picker: <C-p> preview, <M-t> tabs, <M-e> edit, :F2Reload (#18) -> lua/genja/f2/readme.testing-manual.md
- [ ] F2 adhoc: go mod init for a .go file without go.mod (#18) -> doc-wip/readme.idea18-f2-context.md
- [ ] claude floaterm: :ClaudeFterm [flags], <leader>pc popup, <leader>pC paste, session marker via /rename (#19) -> doc-wip/squash-ideas-oct-17.details.md #19
- [ ] claude terminal: hourglass cursor while claude starts (4e79669) (#19a) -> todo-ideas.md
- [ ] codecompanion: <leader>ac / <leader>aa (#19a) -> doc-wip/readme.idea19-companion.md
- [ ] focus.nvim: off by default; excluded buftypes when on (lua/lazyp/ui/focus.lua) -> doc-wip/squash-ideas-oct-17.done.md extras

## Run by Claude (fast checks only)

- f2 unit tests: `make test` in lua/genja/f2/: 50 cases, 0 fails (2026-10-23).
- Headless smoke checks per item above; noted in each guide.
