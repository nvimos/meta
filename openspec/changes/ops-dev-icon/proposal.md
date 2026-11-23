# a wrench on the dev build's icon

Tags: ops, build
Status: Proposed, for TASK-201. Not started; may be built later.

## Why

The dev (debug) build and the release build of ops look the same in the taskbar, the window title
and Explorer. With both running, or a release copy in `~/.local/bin` next to a fresh debug build,
it is easy to click the wrong one and test the wrong version.

## The idea

- The dev build carries its own icon: the ops icon with a small wrench laid over it. The handle
  comes in from the bottom-right corner; the head points toward the centre, its open jaw facing the
  middle.
- The release build, the one-file exe and the GitHub release keep the plain icon.
- Nothing has to be swapped before a build: both icons live in the repo, and the build picks one.

## Use cases

- I run `make live` while yesterday's release is open. The taskbar shows two ops icons; the one
  with the wrench is the build I'm editing.
- I pin the release exe to the taskbar. Starting a dev build next to it doesn't merge into the
  pinned icon's look: the wrench tells them apart.

## Technical

- The art: `assets/icon/ops-dev.svg`, a copy of `ops.svg` with the wrench added.
  - `tool/icon.ps1` reads only `<rect rx>` and `<polygon>`; the wrench fits that: the handle a
    four-corner polygon along the diagonal, the head a polygon with the jaw notch cut in
  - an outline in the background colour drawn first, so the wrench reads over the logo
- The `.ico`: the script already takes `-Svg` and `-Out`, so it writes
  `windows/runner/resources/app_icon_dev.ico` beside `app_icon.ico`; `make icon` builds both
- Picking the icon: `windows/runner/Runner.rc` is compiled per build, and Flutter's CMake defines
  `_DEBUG` for Debug:
  ```
  #ifdef _DEBUG
  IDI_APP_ICON ICON "resources\\app_icon_dev.ico"
  #else
  IDI_APP_ICON ICON "resources\\app_icon.ico"
  #endif
  ```
  - the window and taskbar load `IDI_APP_ICON` from the exe, so they follow
  - `make dev`, `make run`, `make live` get the wrench; `make build`, `single`, `release` don't
- Open questions
  - check that the resource compiler sees `_DEBUG` (one debug build settles it)
  - at 16 px the wrench is 6-8 px: render the PNG frames and look before wiring it in
  - Explorer caches icons by path; `Debug\ops.exe` may show the old icon until the cache refreshes
