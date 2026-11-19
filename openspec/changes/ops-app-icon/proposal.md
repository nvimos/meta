# ops app icon

Status: In Progress (backlog TASK-130)

## Why

`ops.exe` still ships the default Flutter icon, so on the taskbar it looks like any other Flutter
app. The front end drives Neovim; its icon should say so, and set it apart from Neovim's own.

## What Changes

- a new app icon for the front end, drawn from what the Flutter and Neovim logos share
  (flat slanted slabs, the 45° fold, the green and blue) without copying either mark
- clear at the sizes Windows uses: 16 (title bar), 24, 32 (taskbar), 48, 256
- one source drawing in the repo, the `.ico` built from it

## Done so far (2026-11-12)

- four concepts drawn as SVG and previewed at 48/32/24/16 px on light and dark:
  https://claude.ai/artifact/Rma5DomFSsgcDq2oNvSbu3
  - A. Prompt: a folded chevron as a prompt plus a green block cursor, on a dark tile (recommended:
    the tile keeps an outline on any taskbar, readable at 16 px)
  - B. Slab N: green and blue pillars, a light ribbon as the diagonal; the closest to both parents,
    so also the closest to the Neovim mark
  - C. Diamond: a green/blue diamond with a white chevron cut through; the least literal
  - D. Seam: a rounded tile cut on the 45° line, green and blue, a cursor on the blue side;
    loses the most detail at 16 px
- the page source: `concepts.html` next to this proposal (one SVG `<symbol>` per concept)

## Impact

- `nvimos-poc-frontend/windows/runner/resources/app_icon.ico` (the only icon the runner uses)
- new: the source drawing, e.g. `nvimos-poc-frontend/assets/icon/ops.svg`, and a make target that
  builds the `.ico` from it
- open: which concept; a hand-tuned 16 px version or the scaled one; the tool for SVG to `.ico`
  (ImageMagick, or a small Dart script with `package:image`)
