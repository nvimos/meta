# Tasks

## 1. Build

- [x] 1.1 settle the open questions with the user; fold the answers into the proposal
- [x] 1.2 remove the dead match: `IgnoreInfo.match`, the verdict, the highlighted rule, the
  `checkIgnore` call, the debounce and the per-path cache
- [x] 1.3 remove the test that invents a match — a fake state the app cannot reach — and its
  "one lookup per resting place" assertion
- [x] 1.4 remove the Ignore dialog's "already ignored" branch (`already`, `alreadyIgnored()`,
  `checkIgnoreAll` in `forSelection`, the preview lines, the problem text); its target is named
  "project .gitignore"
- [x] 1.5 the two panes: the list (35 % of the width, at least 80 px) of every `.gitignore` (the top
  one "project .gitignore") and every line of the selected one, comments and blanks, no numbers;
  read once, again only on a changed `.gitignore` path or an own write
- [x] 1.6 the list starts on the project `.gitignore` when it exists, else the first file, and
  keeps the user's pick for the session; it does not follow the cursor row
- [x] 1.7 the line menu on every line: Delete, Dirname, Flip, Open; the hover buttons stay, "one
  folder up" renamed Dirname; each disabled action says why (the five notifications)
- [x] 1.8 Open in editor (through `EditorSession`) and New here (through the backend; inside the
  folder for a directory row, at the root for the project file)
- [x] 1.9 keys: two Tab stops, `j` / `k` in the list and the line cursor, Shift+wheel, Enter opens
  in the editor; Help, PLAN.md
- [x] 1.10 after the Ignore dialog writes: select the file, the line helper finds the new rule
  after a re-read, centre it in the lines pane, no animation
- [x] 1.11 the area: a remembered switch between the ignore panes and the preview; resizable by its
  left edge, width remembered, hidden by default under 600 px, where `p` or the switch still opens
  it for the session
- [x] 1.12 CLAUDE.md: the ignore lines are the exception to "no hover-only row buttons"
- [x] 1.13 reads: `loadIgnorePanes` returns the tracked list (plus the project `.gitignore` when it
  exists untracked) and the selected text in one call; the files are found again only on a changed
  `.gitignore` path or an own write; selecting another file reads only that file
- [x] 1.14 hidden idle: the ignore panes and the preview do nothing while the switch hides them, and
  load when shown
- [x] 1.15 one row height from the text style (`itemExtent`), lines cut, never wrapped
- [x] 1.16 discovery: tracked files at once, `untrackedIgnoreFiles` adds the rest when it arrives
- [x] 1.17 motion keys: Right / `l` and Left / `h` across the three panes, Ctrl+arrow, lowest visible
  item when coming up; `debugLabel` and `focusRoles` for the new nodes
- [x] 1.18 Undo button on the notice after Delete, Flip, Dirname; one at a time; `Delete` on the line
  cursor deletes the line; a removed line is restored with `insertIgnoreLine`
- [x] 1.19 the effect notice: rows back in the list / now ignored, from the status before and after
- [x] 1.20 the governing-file marker, as a trial: mark the `.gitignore` files that govern the cursor
  row's folder, without moving the selection
- [x] 1.21 empty state with "Create project .gitignore"

## 2. Backend

- [x] 2.1 `RepoBackend`: a gitignore API — `loadIgnorePanes` (tracked list, plus the project file
  when it exists untracked, and the selected text), `untrackedIgnoreFiles`, `readIgnoreFile`,
  `appendIgnoreLines`, `replaceIgnoreLine`, `insertIgnoreLine`, `createIgnoreFile`, and an
  `IgnoreFileRef` for a repo-relative `.gitignore` or the `.git/info/exclude` target; no local
  absolute path on the wire
- [x] 2.2 `LocalBackend` delegates the API to its `Repo`
- [x] 2.3 `NvimBackend` forwards it to a new relay module (`nvimos.gitignore`), so Neovim in a VM
  or over SSH works
- [x] 2.4 relay Lua tests: discovery, read, append, replace, insert, create, exclude, and the
  relative-path rules
- [x] 2.5 the pane and dialog use the backend for ignore I/O; no `ensureRepo()` or local repo path
  on that path; Open goes through `EditorSession`
- [x] 2.6 the relay reloads an open, unmodified buffer of a `.gitignore` after a write

## 3. Verify

- [x] 3.1 unit tests for the pure helpers: every dirname shape and refusal (leading spaces,
  escaped `\#` and `\!`, folder-only rules, bracket-only parents, `**/`), Flip on positive,
  negated, escaped (`\!`), leading-space and non-rule lines, and the line-after-write helper (CRLF,
  no final newline, several rules, duplicate)
- [x] 3.2 pane tests: the list starts on the project file and keeps a pick across cursor moves, a
  cursor move reads no file, a write selects its file and centres its line
- [x] 3.3 performance tests: a refresh without a changed `.gitignore` reads nothing; hidden panes
  read nothing until shown; one `loadIgnorePanes` call plus the later untracked call
- [x] 3.4 undo tests: Delete restores the line with `insertIgnoreLine`, Dirname-removal restores
  it, Flip restores the old line, and each refuses when the file changed meanwhile
- [x] 3.5 effect-notice and marker tests: rows gained/lost after a write with no extra git call;
  the governing files are marked and the selection does not move
- [x] 3.6 backend contract tests: a fake remote backend whose paths do not exist on this machine
  covers list, read, edit and create without touching the local filesystem; run the same contract
  against `LocalBackend`
- [ ] 3.7 in the app: open the panes, switch to the preview and back, resize and narrow the window,
  press `p` under 600 px, edit a rule and a comment from the menu and from a hover button, Flip a
  rule, Enter on a file and a line, create a nested `.gitignore` with New here and track it
- [ ] 3.8 remote check: with a Neovim whose cwd is not on this machine, list, read, edit, create
  and Open in editor work through the backend only
