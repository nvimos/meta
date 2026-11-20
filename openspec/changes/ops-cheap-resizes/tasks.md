# Tasks

## 1. Build

- [x] 1.1 Help: cache the split by column count and the column tree by (count, query), so a
  width change in the same structure lays out and does not rebuild the key rows
- [x] 1.2 Help: a `UiTiming` span (`help.resize`), and the rule in CLAUDE.md and PLAN.md
- [x] 1.3 Help: freeze the table on a width change; scale it uniformly to the new width; reflow
  150 ms after the last change; one-line descriptions while resizing, wrapping at rest
- [x] 1.4 Help: 360 px columns, a 250 px floor, and clip the right edge below it (no setting)
- [ ] 1.5 keep-alive stack in the shell: hidden modes keep state and scroll but are not laid out.
  **Tried and reverted 2026-11-20**: a hidden mode that changed (a load, a notice) was left dirty,
  and the semantics pass then logged `!semantics.parentDataDirty` /
  `!childSemantics.renderObject._needsLayout` in a storm; it also changed when layout-built content
  (a filter field) appeared on a mode switch. Needs a design where a dirty hidden subtree lays
  itself out, or leaves the render tree, without losing its state
- [ ] 1.6 hidden panes that are still built use the same primitive; checked: Add and Ignore builds
  one of its two side panes at a time, so there is nothing to skip today
- [ ] 1.7 Pull request and Changes sidebar: anchor the drag on the pointer; only the pane listens
  to the width, through a `ValueNotifier`

## 2. Verify

- [x] 2.1 Help: a widget test starts a drag (one compact rebuild), checks that the next drag frame
  keeps the same `RichText` instances, and that the reflow restores wrapping
- [x] 2.2 Help: a width change keeps the old table until 150 ms, then reflows; a column is never
  below 250 px; the overflow is clipped
- [ ] 2.3 keep-alive stack: a hidden mode does not lay out on a resize (a counting child), and a
  shown mode lays out once; selection and scroll survive a switch
- [ ] 2.4 in the app: resize the window in Help and drag both sidebars; the edge follows the
  pointer, Help scales and snaps, and the content does not flicker
- [ ] 2.5 measure again and record the before and after in the tasks
