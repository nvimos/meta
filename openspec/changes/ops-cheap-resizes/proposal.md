# a resize costs only what moves

Tags: performance
Status: In Progress, for TASK-198.

## Why

Add and Ignore's side pane got this pass in TASK-191 (`215a61a`). The edge anchors on the pointer's
x at drag start, so no delta is lost between frames; the width goes through a `ValueNotifier`
that only the pane listens to, so the list and the preview are relaid but never rebuilt; and the
content widget stays the same instance on every frame of the drag.

The other resizes have not had it. Help rebuilt every key group, table and highlighted span on
each width change; that part is fixed (the split and the column tree are cached by column count
and query), but the remaining cost is text layout: a hundred wrapped descriptions lay out again at
every new width, 80-220 ms per frame in a widget test. The shell's `IndexedStack` also lays out all
nine modes on every window resize, though only one is on screen. The Pull request and Changes left
panes (`ResizablePane`) still add `details.delta` to the width of the last build and `setState` on
every pointer event.

## The idea

For every drag-to-resize and every layout the window drives:

- anchor the drag on the pointer (start size and start x), not on the last built size
- one listener, at the widget that sizes; the neighbours and the content keep their widget
  instances and are relaid, not rebuilt
- a window resize is a special case: keep the last laid-out content, scale it while the width
  moves, and reflow once the window has been still for a moment
- a hidden mode or pane is not laid out at all; it keeps its state and scroll, and lays out when
  it is shown again

## Help: the decisions

- **Freeze and reflow.** A width change keeps the last laid-out table. The table reflows once,
  **150 ms** after the last width change (a window drag has no reliable end event).
- **Uniform scale.** While frozen, the table scales on both axes to the new width, so text is
  briefly smaller or larger but never stretched.
- **One line while resizing.** During the frozen state the descriptions are a single line with an
  ellipsis; normal wrapping returns with the reflow. This costs one rebuild at the start of the
  drag and one at the end, not one per frame.
- **360 px columns, 250 px floor.** The current look stays. No column-width setting. A column is
  never narrower than **250 px**, during the drag or at rest; below that the right edge is clipped
  (no horizontal scrollbar).
- `UiTiming` span `help.resize` times a width change to the painted frame.

## Hidden modes and panes

- Replace the shell's `IndexedStack` with a keep-alive stack: every mode's element and render
  object stay alive, so selection and scroll survive, but only the shown child is laid out and
  painted. A hidden mode never lays out on a window resize; it lays out once when shown.
- A child that was never laid out gets one layout the first time it is hidden (so it has a size);
  after that it waits.
- The same primitive applies to panes that are hidden inside a mode and still built.
- This is the layout side of `ops-hidden-panes-idle`, which stops hidden states from doing I/O.
- **Tried and reverted 2026-11-20.** The first version laid out a hidden child once and then never
  again. A hidden mode that changed (a load, a notice) stayed dirty; the semantics pass then threw
  `!semantics.parentDataDirty` and `!childSemantics.renderObject._needsLayout` every frame, and the
  live log filled with thousands of assertions. It also delayed layout-built content (a filter
  field) by a frame on a mode switch. The app is back on `IndexedStack`. A retry needs a dirty
  hidden subtree to lay itself out (a relayout boundary was not enough in practice) or to leave
  the render tree without losing its state.

## Technical notes

- Help: `_columns` ran inside `LayoutBuilder` and built new `_KeyColumn`s, `Table`s and
  `Text.rich` spans every time. The split is cached by column count and the column tree by
  (count, query). The new freeze keeps that tree and applies a uniform `Transform.scale`; a
  `Timer` (150 ms) ends the resize and rebuilds at the final width.
- The 250 px floor means the laid-out content width is
  `max(available, count * 250 + padding)`; the view clips rather than shrinking a column.
- `ResizablePane`: replace `d.delta.dx` with the anchor (the side pane already does this).
- Keep-alive stack: a `MultiChildRenderObjectWidget` over a `RenderBox` with
  `ContainerRenderObjectMixin`; `performLayout` lays out the shown child, and the first time
  each hidden child; `paint` and `hitTestChildren` use only the shown child. `ExcludeSemantics`
  stays as it is. Reverted: see the note above; the child must never stay dirty.
- Tests: Help keeps the same `RichText` instances on a drag frame and reflows after 150 ms; a
  column is at least 250 px and the overflow clips. The keep-alive stack tests are removed with
  the implementation.
