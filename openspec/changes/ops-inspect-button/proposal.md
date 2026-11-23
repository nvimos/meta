# an inspect button in the debug build

Tags: ops, debug
Status: Proposed, for TASK-203. Not started.

## Why

Flutter has a select mode that I have seen in the app: click any part of the UI and it outlines that
element and names the widget class behind it. It is the quickest way to learn what a pane, a grid or
a row is called in the code, to name it in a request or find it in `lib/`. Today it only turns on
from outside the app (DevTools, the IDE), and I'm not always sure what turned it on.

## The idea

- In the debug build, a second button next to the debug bar's bug button turns the select mode on
  and off.
- While it is on, a click picks the element under the pointer instead of doing what it normally
  does: the element is outlined and its class is shown, with its size.
- The release build has no button and no select mode.

## Use cases

- I want to ask for a change to the strip above the diff. I turn inspect on, click the strip, read
  `ViewBar`, turn inspect off and write the request with that name.
- I click a row and see `HoverRow`, then the cell inside it and see `PathName`.

## Technical

- The mode is Flutter's widget inspector selection, available in debug and profile builds. The app
  can switch its overlay on with `WidgetsBinding.instance.debugShowWidgetInspectorOverrideNotifier`
  (`value = true` / `false`); `WidgetsApp` then wraps the app in `WidgetInspector`. To check on
  Flutter 3.50: the exact name, and how the overlay's own select and exit buttons behave on desktop.
- The button only exists when `kDebugMode`; an atom with a tooltip ("Inspect: click an element to
  see its widget") and the pointer cursor, lit while the mode is on.
- What it names is the Flutter class (`Padding`, `Text`, `HoverRow`), not the role in the interface
  the debug bar shows. A follow-up could show the debug bar's role name for the picked element when
  one is known (`focusRoles`).
- The inspector creates its overlay and listens to pointer events only while on; off, it costs
  nothing.
- Effort: small, an hour or two with a widget test (the button toggles the notifier and is absent in
  a non-debug build).
