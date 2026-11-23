# Tasks

## 1. Find the cause

- [x] 1.1 read the semantics tree of the running app over the VM service (node 2495 is gone by then;
  the id is the next free one, not a place)
- [x] 1.2 trace the overlay portal semantics in Flutter: only the first `traversalParentIdentifier`
  survives a merge
- [x] 1.3 reproduce in a widget test: the second tooltip in one tappable node leaves an orphan, a
  `Semantics(container: true)` around it fixes it

## 2. Test helper (in progress)

- [x] 2.1 `test/support/tooltip_semantics.dart`: show every tooltip, fail on orphan overlay nodes
  (found by `traversalChildIdentifier`; the bubble node has no label)
- [x] 2.2 call it from the view tests that show tooltips: Add and Ignore, Repos, Ignore dialog and
  pane, Settings, Log, rev picker, status bar, preview pane, merge actions, commit message, Tasks
- [ ] 2.3 cover the rest: Directories, network dialog, checkout dialog, Help (place the call where
  tooltips are on screen), Pull request and Changes with data
- [x] 2.4 fix `_SideTab` in Add and Ignore (`Semantics(container: true)`), so its test passes

## 3. Look for similar problems

- [x] 3.1 other overlay portals: an open `RawAutocomplete` under a field with a `Tooltip` leaves an
  orphan; the rev picker doesn't do that today; `PopupMenuButton` and `showMenu` are routes
- [x] 3.2 other ways to orphan a bubble: a mode switch while a tooltip shows (owner excluded or
  offstage) leaves one; a list scrolling the row away does not
- [x] 3.3 findings recorded in the proposal
- [x] 3.4 fix the mode switch: `Tooltip.dismissAllToolTips()` in the shell's `_setMode` when the
  mode changes; the shell test checks that the bubble is gone after `Alt+1` (in the full shell the
  left-behind bubble kept a parent, so the test can't check for an orphan there; the minimal probe
  with `ExcludeSemantics` or an offstage `IndexedStack` child did leave one)

## 4. Wrap up

- [x] 4.1 CLAUDE.md: the cause, the fix, the helper
- [ ] 4.2 check a `make live` run: no `Failed to update ui::AXTree` while hovering tooltips and
  switching modes by key
- [ ] 4.3 file the Flutter issue
