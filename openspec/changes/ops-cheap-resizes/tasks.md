# Tasks

## 1. Build

- [x] 1.1 Help: cache the split by column count and the column widgets by (count, query), so a
  width change in the same structure lays out and does not rebuild the key rows
- [x] 1.2 Help: a `UiTiming` span (`help.resize`), and the rule in CLAUDE.md and PLAN.md
- [ ] 1.3 Pull request and Changes sidebar: anchor the drag on the pointer; only the pane listens
  to the width, through a `ValueNotifier`
- [ ] 1.4 go through the other resizes (Tasks detail, the narrow layouts) and do the same where it
  applies; name those that do not need it

## 2. Verify

- [x] 2.1 Help: a widget test lays the view out at two widths with the same column count and
  expects the same `RichText` widget instances; the search still highlights and the columns still
  reflow
- [ ] 2.2 sidebar: a test sends several drag updates in one frame and expects their exact sum
- [ ] 2.3 in the app: resize the window in Help and drag both sidebars; the edge follows the
  pointer and the content does not flicker
- [ ] 2.4 measure again and record the before and after in the tasks
