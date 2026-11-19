# Tasks

Draft: the open questions in `proposal.md` come first; these tasks change with the answers.

## 0. Decide

- [ ] 0.1 answer the open questions in `proposal.md`

## 1. Web entry point

- [ ] 1.1 `lib/main_web.dart`; `flutter build web -t lib/main_web.dart` builds
- [ ] 1.2 web-safe prefs, session and timing behind conditional imports
- [ ] 1.3 a check that the web entry's import graph has no `dart:io`
- [ ] 1.4 desktop-only modes and actions hidden; demo banner with Reset and a link to the releases

## 2. Fake repo

- [ ] 2.1 `DemoBackend` with HEAD, index and working tree; status, log, branches, checkout
- [ ] 2.2 line diff and hunks; stage, unstage, discard per file and per hunk; commit
- [ ] 2.3 three-way merge with conflicts in the `ConflictHunk` shape; the merge steps
- [ ] 2.4 `.gitignore` matching for Add and Ignore
- [ ] 2.5 `listFiles`, `readFiles`, `setLines`, `move`
- [ ] 2.6 the layer in browser storage, with a version and Reset

## 3. Data

- [ ] 3.1 `tool/demo_export.dart`: a git repo to the demo JSON
- [ ] 3.2 the planning snapshot from `nvimos/meta` as the demo repo's tracking folder

## 4. Publish

- [ ] 4.1 GitHub Action: build web, publish to Pages on push to main
- [ ] 4.2 rebuild when `nvimos/meta` changes (or nightly)

## 5. Verify

- [ ] 5.1 unit tests for every `DemoBackend` operation
- [ ] 5.2 open the published link in a fresh browser: Tasks shows the planning; stage, commit, merge
  with conflicts and ignore work; reload keeps them; Reset clears them
- [ ] 5.3 the app-wide keys checked in Chrome, Edge and Firefox
