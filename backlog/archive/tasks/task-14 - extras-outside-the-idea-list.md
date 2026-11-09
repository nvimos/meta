---
id: TASK-14
title: 'extras outside the idea list'
status: Done
assignee: []
created_date: '2026-10-31'
labels:
  - todo-ideas
  - ideas-october
dependencies: []
ordinal: 14000
---

## Description

extras outside the idea list

wrapper saved in sessions (140ed09); `<S-Insert>` sends `<C-v>` to pwsh terminals (df0a668)
`<M-j>`/`<M-k>` walk the menu (aa7cdc5); `<M-f>` previous, `<M-w>` first, `<M-s>` 3 down (9693171);
no menu on one-char commands, :w`<CR>` map dropped (c655f23)
keys from gitignored local/secrets.lua (3e90c60, 6122927); :CheckHealthSimpleMinuet (3e5a645);
Codestral by default (a300cea); provider guide doc-wip/readme.minuet-providers.md (0c3e3a3)
:CheckHealthSimpleLsp (7d43221)
llm dir with minuet `<M-y>` (ae71dd3), telescope key help (48936c2), lint md-mixed (3d74e10)
diagnostic virtual text and link colours (698b3a6)

From `todo-ideas.md`, section "ideas october".

## Acceptance Criteria

- [x] #1 netrw.nvim icons (c30c591); ghost text: minuet-ai.nvim and llm.nvim on ollama (d7d084f); both in todo-done/
- [x] #2 terminal: bare :terminal opens pwsh on Windows, bash on Linux (80c8fa1); idle shells under a 'shell'
- [x] #3 cmdline: `<Up>`/`<Down>` history until a menu walk, no preselect (fc6cd99); `<C-BS>` deletes a word (8351d8f);
- [x] #4 minuet: answers only `<M-y>` unless blink auto-complete is on (6dead7f); qwen2.5-coder, all providers,
- [x] #5 :HiInspect shows highlight groups under the cursor (17dceca); :CheckHealthLspSimple renamed
- [x] #6 completion doc window: menu colours, rounded frame, padding (29e8c26, 08a6f5c, 7390836)
- [x] #7 lint: runs cancelled by nvim-lint no longer reported as exit code 1 (cd4a0ab)
- [x] #8 tests: gopls go-list warmup (a3f049a), make timings slowest last (cd57bdf), mason linters installed (ef9867a),
- [x] #9 ecolog: ecolog2 with ecolog-lsp, else ecolog.nvim v1 (d7842a2, ca842c0)
- [x] #10 copilot.vim and llm.nvim shelved, keys commented out (18ed193, 1185287)
- [x] #11 oil: :Lexplore works again (e7b8ece); telescope key help in insert mode without n maps (48936c2)
- [x] #12 markdown: gq wraps checkbox items under the text (58538ea); md-fix follows editorconfig sections (aeab075)
- [x] #13 diag-align toggle on `<leader>tta` and in `<F2>` (27648c7); right-click paste search with a picked provider (fa42e84);

## Original notes

```markdown
- [x] extras outside the idea list (2026-10-31)
  - [x] netrw.nvim icons (c30c591); ghost text: minuet-ai.nvim and llm.nvim on ollama (d7d084f); both in todo-done/
  - [x] terminal: bare :terminal opens pwsh on Windows, bash on Linux (80c8fa1); idle shells under a 'shell'
        wrapper saved in sessions (140ed09); `<S-Insert>` sends `<C-v>` to pwsh terminals (df0a668)
  - [x] cmdline: `<Up>`/`<Down>` history until a menu walk, no preselect (fc6cd99); `<C-BS>` deletes a word (8351d8f);
        `<M-j>`/`<M-k>` walk the menu (aa7cdc5); `<M-f>` previous, `<M-w>` first, `<M-s>` 3 down (9693171);
        no menu on one-char commands, :w`<CR>` map dropped (c655f23)
  - [x] minuet: answers only `<M-y>` unless blink auto-complete is on (6dead7f); qwen2.5-coder, all providers,
        keys from gitignored local/secrets.lua (3e90c60, 6122927); :CheckHealthSimpleMinuet (3e5a645);
        Codestral by default (a300cea); provider guide doc-wip/readme.minuet-providers.md (0c3e3a3)
  - [x] :HiInspect shows highlight groups under the cursor (17dceca); :CheckHealthLspSimple renamed
        :CheckHealthSimpleLsp (7d43221)
  - [x] completion doc window: menu colours, rounded frame, padding (29e8c26, 08a6f5c, 7390836)
  - [x] lint: runs cancelled by nvim-lint no longer reported as exit code 1 (cd4a0ab)
  - [x] tests: gopls go-list warmup (a3f049a), make timings slowest last (cd57bdf), mason linters installed (ef9867a),
        llm dir with minuet `<M-y>` (ae71dd3), telescope key help (48936c2), lint md-mixed (3d74e10)
  - [x] ecolog: ecolog2 with ecolog-lsp, else ecolog.nvim v1 (d7842a2, ca842c0)
  - [x] copilot.vim and llm.nvim shelved, keys commented out (18ed193, 1185287)
  - [x] oil: :Lexplore works again (e7b8ece); telescope key help in insert mode without n maps (48936c2)
  - [x] markdown: gq wraps checkbox items under the text (58538ea); md-fix follows editorconfig sections (aeab075)
  - [x] diag-align toggle on `<leader>tta` and in `<F2>` (27648c7); right-click paste search with a picked provider (fa42e84);
        diagnostic virtual text and link colours (698b3a6)
```
