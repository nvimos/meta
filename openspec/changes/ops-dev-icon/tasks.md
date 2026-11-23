# Tasks

## 1. Art

- [ ] 1.1 `assets/icon/ops-dev.svg`: the ops icon with a wrench, handle from the bottom-right corner,
  head toward the centre, jaw facing the middle; an outline in the background colour
- [ ] 1.2 render the frames (16, 24, 32, 48, 256) and check the wrench reads at 16 px

## 2. Build

- [ ] 2.1 `make icon` writes `app_icon_dev.ico` too (`tool/icon.ps1 -Svg ... -Out ...`)
- [ ] 2.2 `Runner.rc` picks `app_icon_dev.ico` under `_DEBUG`
- [ ] 2.3 one debug and one release build: the wrench only on the debug exe, its window and taskbar
