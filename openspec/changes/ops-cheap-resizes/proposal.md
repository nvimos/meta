# a resize costs only what moves

Tags: performance
Status: In Progress, for TASK-198.

## Why

Add and Ignore's side pane got this pass in TASK-191 (`215a61a`). The edge anchors on the pointer's
x at drag start, so no delta is lost between frames; the width goes through a `ValueNotifier`
that only the pane listens to, so the list and the preview are relaid but never rebuilt; and the
content widget stays the same instance on every frame of the drag.

The other resizes have not had it. The Help mode takes 80-220 ms per width change in a widget test,
though its content does not depend on the exact width: every `LayoutBuilder` pass built all key
groups, tables and highlighted spans again, and ran `splitColumns` again, for a change that only
needs a new layout. The Pull request and Changes left panes (`ResizablePane`) still add
`details.delta` to the width of the last build and `setState` on every pointer event: the same
lost-delta lever that the side pane had, and a rebuild per event.

## The idea

For every drag-to-resize and every layout the window drives:

- anchor the drag on the pointer (start size and start x), not on the last built size
- one listener, at the widget that sizes; the neighbours and the content keep their widget
  instances and are relaid, not rebuilt
- cache derived data by what it depends on: Help's column split and its rows depend on the column
  count and the search query, not on the width
- a width change that keeps the same structure is layout only

## Where it applies

- Help (first, TASK-198): the key columns reflow with the window
- Pull request and Changes: the left sidebar edge (`ResizablePane`)
- Tasks: the detail panel and the list as the window narrows
- Add and Ignore's side pane: done in TASK-191, the reference

## Technical notes

- Help: `_columns` ran inside `LayoutBuilder` and built new `_KeyColumn`s, `Table`s and
  `Text.rich` spans every time. The split is now cached by column count and the column widgets by
  (count, query), so `Row` gets the same instances and Flutter skips their build. Measured before:
  80-220 ms per width change; `splitColumns` itself was at most 0.34 ms, and
  `IntrinsicColumnWidth` was not the cost.
- `ResizablePane`: replace `d.delta.dx` with the anchor, keep the width in a `ValueNotifier` so only
  its `LayoutBuilder` listens, as `SidePane` does.
- Measure with a `UiTiming` span (`help.resize`, `pr.resizeSide`, `changes.resizeSide`), and test
  that a width change keeps the same content widget instances (`identical`).
