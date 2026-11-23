# tooltips clear of a large mouse pointer

Tags: ops, ui, accessibility
Status: Proposed, for TASK-210. Not started.

## Why

Windows lets the mouse pointer be made much bigger (Settings > Accessibility > Mouse pointer and
touch, size 1 to 15). With a pointer about four times the usual size, the app's tooltips appear
right under it and are hidden by it: the explanation is there but cannot be read.

## The idea

- The app knows how big the pointer is and places every tooltip below the pointer's reach, so the
  whole tooltip shows under the arrow.
- It follows a change: making the pointer bigger or smaller in Windows moves the tooltips on the
  next one shown, without a restart.
- A setting in Settings for when the detection is wrong or not wanted: **Tooltip distance**,
  `Automatic` (from the pointer size) or a fixed distance.

## Use cases

- My pointer is at size 6. I rest it on the rail's Changes icon. The tooltip appears under the tip
  of the arrow, below its body, and I can read it.
- I set the pointer back to size 1. The tooltips sit close to their items again, as before.
- Automatic guesses wrong on my machine. In Settings I set the distance by hand.

## Technical

- Where Windows keeps the size
  - `HKCU\Control Panel\Cursors\CursorBaseSize` (DWORD, pixels: 32 by default, up to 256), which
    the accessibility size slider writes; `HKCU\SOFTWARE\Microsoft\Accessibility\CursorSize` (1-15)
    is the slider's step
  - `GetSystemMetrics(SM_CYCURSOR)` gives the nominal cursor size, but on recent Windows it does not
    always follow the accessibility size: the registry value is the one to trust, checked on a real
    machine first
  - read it in the runner (`windows/runner`, C++, `RegGetValueW`) and hand it to Dart over a method
    channel, or from Dart with `win32` FFI; the runner also sees `WM_SETTINGCHANGE` (sent when the
    pointer size changes) and tells Dart to read it again
- Placing the tooltips
  - Flutter places a tooltip relative to its widget, not the pointer: `verticalOffset` from the
    widget's centre (24 by default), `preferBelow`. One app-wide value in the theme
    (`TooltipThemeData.verticalOffset`) moves them all
  - the distance: the pointer's height in logical pixels (`CursorBaseSize / devicePixelRatio`,
    the arrow's hot spot is its top-left) minus the half height of a small target, at least the
    default 24; a widget that sets its own `verticalOffset` adds to it rather than overrides it
  - a tooltip near the bottom of the window flips above (Flutter does this already when there is
    no room below)
- The setting
  - `Prefs`: `tooltipDistance` (`auto` or a number); Settings gets a row with Automatic and a number
    field, showing what Automatic found ("pointer 128 px → 64 px")
  - off Windows (macOS, Linux) Automatic is the default 24
- Tests: the theme's offset follows a given pointer size; the setting overrides it; a fake
  settings-change message makes the next tooltip use the new size
