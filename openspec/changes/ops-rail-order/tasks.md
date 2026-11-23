# Tasks

## 1. Order and hidden modes (shipped)

- [x] 1.1 drag an icon to reorder; the drop line on the side it lands; saved by name
- [x] 1.2 right-click to hide; keys and wheel skip hidden modes; at least one stays
- [x] 1.3 Settings lists hidden modes and shows them again; Reset the rail
- [x] 1.4 repair the saved state at startup (unknown names, new modes, duplicates)

## 2. Drag threshold

- [x] 2.1 `ThresholdDraggable`: a press becomes a drag only after 8 px for a mouse, Flutter's touch
  slop (18 px) for a finger; below that it stays a click
- [x] 2.2 widget test: a 5 px wobble opens the mode, a 12 px move picks the icon up
- [ ] 2.3 try it in the app with the mouse: a click never lifts the icon, a drag doesn't feel sticky
- [ ] 2.4 verify on the touchscreen: a tap opens the mode, a drag with a finger reorders, and the
  rail doesn't scroll instead (does the Windows embedder deliver touch as `PointerDeviceKind.touch`
  there, and is 18 px right for a finger?)
