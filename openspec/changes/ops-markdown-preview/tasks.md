# Tasks

## 1. Build option

- [x] 1.1 `packages/ops_markdown_on` (`flutter_markdown_plus` 1.0.12) and `ops_markdown_off` (stub);
  `make configure markdown=on|off`
- [x] 1.2 `flutter_markdown_plus` builds and analyzes clean; the app analyzes with the stub too
- [ ] 1.3 look at it on real repo files in the app (README, a task, a proposal with tables and code)

## 2. Rendered view

- [x] 2.1 render markdown in the preview pane; both views built at load, the switch reads nothing
- [x] 2.2 theme: headings, code, tables, quotes in the app's colours
- [x] 2.3 selectable text (inside the pane's `SelectionArea`); relative pictures from the repo, web
  pictures show their alt text
- [ ] 2.4 syntax highlighting in code blocks: the text view has none either today; later, with
  `re_highlight` for both

## 3. The switch

- [x] 3.1 Rendered / Text switch (`SegmentedButton`) in the Preview header, markdown files only;
  tooltips, pointer cursor; absent when markdown is off
- [x] 3.2 the choice is kept in `Prefs` (`previewMarkdown`)

## 4. Links

- [x] 4.1 a local `.md` link shows that file in the preview and records the current one for back
- [x] 4.2 `NavHistory` gets forward: back moves the jump onto forward, forward repeats it, a new
  push clears it; the mouse's forward button in the shell
- [x] 4.3 web links go to the system (`FileManager.openUrl`); other local files open like the Open
  button
- [x] 4.4 links show the pointer cursor
- [ ] 4.5 a link's target as a tooltip (a `TextSpan` has no tooltip of its own; needs a hover
  lookup or a custom link builder)

## 5. Done

- [x] 5.1 tests: rendered by default, the switch, a link and its pointer cursor, link resolution,
  back / forward; `expectTooltipsInSemantics`
- [x] 5.2 `PLAN.md`: the preview section, the forward button; Help and the Keys table
