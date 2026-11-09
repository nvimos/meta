# voice input with whisper.cpp

Status: To Do (backlog TASK-65)

## Why

voice input with whisper.cpp

- local whisper.cpp, binaries and models in %LOCALAPPDATA%/whisper.cpp
- languages: English, Norwegian, Russian; -l auto
  - ggml-base.bin is weak on Norwegian: try ggml-small.bin
  - maybe a key to pin the language (en/no/ru/auto) when auto guesses wrong
- record with ffmpeg (on PATH): `-f dshow -i audio="<mic>"`; mic name from -list_devices
- `<M-v>` toggles in normal and insert: record, then stop -> transcribe -> insert at cursor
  - `<Esc>` while recording cancels; statusline shows recording
  - check `<M-v>` for clashes first; also in the `<leader>pC` / `<M-?>` prompt popup
- paths per machine in a gitignored lua/genja/local/voice.lua

## What Changes

- (to be worked out)

## Impact

- Source: `todo-2027.md`, section "new setup 2027"

## Original notes

```markdown
- [ ] voice input with whisper.cpp (todo-ideas #20, spec 2026-10-23)
  - local whisper.cpp, binaries and models in %LOCALAPPDATA%/whisper.cpp
  - languages: English, Norwegian, Russian; -l auto
    - ggml-base.bin is weak on Norwegian: try ggml-small.bin
    - maybe a key to pin the language (en/no/ru/auto) when auto guesses wrong
  - record with ffmpeg (on PATH): `-f dshow -i audio="<mic>"`; mic name from -list_devices
  - `<M-v>` toggles in normal and insert: record, then stop -> transcribe -> insert at cursor
    - `<Esc>` while recording cancels; statusline shows recording
    - check `<M-v>` for clashes first; also in the `<leader>pC` / `<M-?>` prompt popup
  - paths per machine in a gitignored lua/genja/local/voice.lua
```
