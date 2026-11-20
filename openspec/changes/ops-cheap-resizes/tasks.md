# Tasks

## 1. Build

- [x] 1.1 Help: cache the split by column count and the column tree by (count, query), so a
  width change in the same structure lays out and does not rebuild the key rows
- [x] 1.2 Help: a `UiTiming` span (`help.resize`), and the rule in CLAUDE.md and PLAN.md
- [ ] 1.3 Help: freeze the table on a width change; scale it uniformly to the new width; reflow
  150 ms after the last change; one-line descriptions while resizing, wrapping at rest
- [ ] 1.4 Help: 360 px columns, a 250 px floor, and clip the right edge below it (no setting)
- [ ] 1.5 keep-alive stack in the shell: hidden modes keep state and scroll but are not laid out;
  a shown mode lays out once
- [ ] 1.6 hidden panes that are still built use the same primitive
- [ ] 1.7 Pull request and Changes sidebar: anchor the drag on the pointer; only the pane listens
  to the width, through a `ValueNotifier`

## 2. Verify

- [x] 2.1 Help: a widget test lays the view out at two widths with the same column count and
  expects the same `RichText` widget instances; the search still highlights and the columns reflow
- [ ] 2.2 Help: a width change keeps the old table until 150 ms, then reflows; a column is never
  below 250 px; the overflow is clipped
- [ ] 2.3 keep-alive stack: a hidden mode does not lay out on a resize (a counting child), and a
  shown mode lays out once; selection and scroll survive a switch
- [ ] 2.4 in the app: resize the window in Help and drag both sidebars; the edge follows the
  pointer, Help scales and snaps, and the content does not flicker
- [ ] 2.5 measure again and record the before and after in the tasks
