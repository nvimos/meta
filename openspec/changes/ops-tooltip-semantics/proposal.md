# tooltips without orphan accessibility nodes

Tags: accessibility, ui
Status: In progress, for TASK-199.

## Why

`make live` fills the log with bursts of the same line:

```
[ERROR:flutter/shell/platform/common/accessibility_bridge.cc(114)] Failed to update ui::AXTree, error: 2495 will not be in the tree and is not the new root
```

The Windows accessibility bridge (the part of the Flutter engine that hands the semantics tree to
Narrator and other screen readers) refuses an update that contains a node no parent lists. A screen
reader then misses that node, and the log is noisy enough to hide real errors.

The id in the message is the next free one, so it doesn't say which widget it was. One tooltip
shown once is enough to produce a whole burst: its bubble's node is sent again on every frame of
the fade in and out.

This is a different cause from the earlier error 144 (hidden modes in the `IndexedStack`), which
`ExcludeSemantics` on the hidden modes addressed.

## The cause

On desktop a tooltip's bubble is drawn in the root overlay, far from the widget it explains. Flutter
moves the bubble's semantics node under the tooltip's owner, so a screen reader meets it in the right
place: the tooltip's `OverlayPortal` tags its owner with a `traversalParentIdentifier`, and the
bubble carries the matching `traversalChildIdentifier`.

When several such owners merge into one semantics node, Flutter keeps only the first identifier
(`SemanticsConfiguration.absorb` in `semantics.dart`:
`_traversalParentIdentifier ??= child._traversalParentIdentifier`, Flutter 3.50). This happens, for
example, in a tappable row with a tooltip on its state letter and a second tooltip somewhere else.
Showing the second tooltip then makes a bubble that has no traversal parent. Flutter drops it from
its own hit-test and traversal lists but still sends it as a dirty node, and the bridge rejects it.

Reproduced in a widget test: two tooltips inside one tappable node; showing the first leaves no
orphan, showing the second leaves one; the same second tooltip wrapped in
`Semantics(container: true)` leaves none. A single tooltip in a tappable node is fine.

## The idea

- A tooltip that would share a semantics node with another overlay portal (a second tooltip, a menu
  anchor, an autocomplete) gets a node of its own: `Semantics(container: true)` around it, or
  around the smallest part that holds it.
- A test helper shows every tooltip on a screen, one at a time, and fails when it leaves an
  orphan overlay node: one that is attached to the semantics tree but cannot be reached from the
  root in traversal order, the order the engine builds the platform tree from. The view tests call
  it for their mode, so the next nested tooltip fails a test instead of the log.
- Look for the same kind of problem in other places: anything that sends a semantics node the
  platform tree can't hold.

## Where it applies

What the helper and a set of probes found (2026-11-20).

Merged tooltips, the cause above:

- Add and Ignore: the "The highlighted files (v)" tab of the side pane switch (`_SideTab`,
  `lib/ui/add_ignore_view.dart`) leaves an orphan; the other tooltips of the view, the rows
  included, are fine
- clean with the helper: Repos, the Ignore dialog and the Ignore pane, Settings, Log, the rev picker,
  the status bar, the preview pane, the merge actions, the commit message, the Tasks list and detail
  panel
- not covered yet, the view tests end on a screen without tooltips: Directories, the network
  dialog, the checkout dialog, Help; Pull request and Changes have no widget test of their own with
  data

Similar problems, the same orphan by another way:

- **a mode switch while a tooltip is shown.** The bubble is in the root overlay, outside the
  mode's `ExcludeSemantics` and outside the `IndexedStack`'s offstage child; when the owner's mode
  is hidden, the owner's node goes and the bubble stays. Both probes (owner excluded, owner
  offstage) leave one orphan for as long as the bubble shows (a keyboard switch, `Alt+2`, with the
  mouse resting on a tooltip). Fix: `Tooltip.dismissAllToolTips()` in the shell's `_setMode` when
  the mode changes; a probe shows the bubble is gone in the same frame, with no orphan.
- **an autocomplete list under a field that also has a tooltip.** `RawAutocomplete` is an overlay
  portal too; an open option list under a `Tooltip` around the field leaves an orphan. An
  autocomplete alone is fine. The rev picker (`lib/ui/pr_view.dart`) has no tooltip around the
  field (its `ClearButton` has one inside it), and its test passes; a tooltip added around a picker
  would bring this case in.
- not a problem: a list scrolled so that a row with a shown tooltip leaves the view (the row is
  disposed with its bubble, or the bubble keeps a parent); `PopupMenuButton` and `showMenu` open a
  route, not an overlay portal.

## Technical notes

- `test/support/tooltip_semantics.dart`: `expectTooltipsInSemantics(tester)` shows each
  on-screen `Tooltip` with `TooltipState.ensureTooltipVisible`, pumps, checks
  `orphanOverlayNodes(tester)`, and dismisses it again (`Tooltip.dismissAllToolTips`).
- `orphanOverlayNodes` collects the nodes with a `traversalChildIdentifier` from the hit-test
  children (`visitChildren`) and the nodes reachable through
  `debugListChildrenInOrder(DebugSemanticsDumpOrder.traversalOrder)`; the difference is the orphans.
- The bubble node has no label of its own (the message is the owner's `tooltip` property), so a
  test can't look for the bubble by its text.
- An upstream Flutter issue is worth filing: a merge could keep all the identifiers, or the bubble
  could fall back to its hit-test parent.
- CLAUDE.md gets the cause and the fix next to the note about error 144.
