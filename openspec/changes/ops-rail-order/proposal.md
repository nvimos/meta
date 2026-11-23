# the rail in the user's order

Tags: ops, ui
Status: In progress, for TASK-200.

## Why

The mode rail listed the modes in a fixed order, and every mode was always there. Someone who lives
in Changes and Tasks and never opens History wants those two on top and History gone, without
losing the way back to it.

## The idea

- Drag an icon up or down the rail to move its mode. A drop line shows where it will land, on the
  side the mode ends up. The order is saved in the state file and the next start uses it.
- Right-click an icon to hide its mode. Alt+1..9, Alt+[ / Alt+] and the wheel skip hidden modes.
  At least one mode stays. Settings lists the hidden ones and shows one again in the place it was
  dragged to; **Reset the rail** restores the default order and shows every mode.
- The saved order and hidden set are mode names: a name that no longer exists is dropped, a new
  mode comes last, duplicates go.
- A click is not a drag. A press picks the icon up only after the pointer has travelled far enough,
  so the small movement that comes with a click still opens the mode.

## Use cases

- I click Changes and my hand moves a few pixels as I press. Changes opens; the icon doesn't dim
  and nothing follows the pointer.
- I press Tasks and pull it up the rail. After a short distance the icon lifts, the drop line shows
  under Pull request, and on release Tasks is second.
- On the touchscreen I tap a mode with a finger. The tap opens it; a finger needs to travel further
  than a mouse before a drag starts.

## Technical

- Shipped (ops commits `3553ec5`, `7027b7a`): `RailState` in `lib/ui/mode_rail.dart`, the rail's
  `Draggable` / `DragTarget` rows, the Settings list and reset.
- Drag threshold: Flutter's `Draggable` uses `ImmediateMultiDragGestureRecognizer`, whose slop for a
  mouse is `kPrecisePointerHitSlop`, 1 px. Any wobble during a click started a drag and the click
  was lost. Windows' own threshold is about 4 px (`SM_CXDRAG`), macOS and browser drag-and-drop
  3-5 px. The rail uses 8 px for a mouse.
  - `ThresholdDraggable` (`lib/ui/threshold_draggable.dart`) overrides `Draggable.createRecognizer`
    with a `ThresholdMultiDragGestureRecognizer`: it claims the pointer once it has moved more than
    `max(kDragThreshold, computeHitSlop(kind))`, so a mouse needs 8 px and a finger Flutter's touch
    slop (`kTouchSlop`, 18 px)
  - mouse and touch are told apart by the pointer kind: the Windows embedder reports a finger as
    `PointerDeviceKind.touch` and a mouse as `mouse` (pen as `stylus`); nothing app-side is needed
  - the drag starts at the press point and the travel is applied at once, so the feedback appears
    under the pointer (`pointerDragAnchorStrategy`)
