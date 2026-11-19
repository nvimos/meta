# the Ignore panes, closer to Purrage's

Tags: integrate-purrage
Status: In Progress, for TASK-191; the decisions are settled (see Decisions).

## Why

The Add and Ignore mode's Ignore pane (`p`) was ported from Purrage in a hurry and lost its shape.
Purrage showed every `.gitignore` of the project in a list, with the selected file's lines next to
it; Ops shows only the files around the cursor row, stacked in one column, and reads them again
after every cursor rest.

Both apps also carry a feature that can never show anything: the pane asks git which rule ignores
the row under the cursor (`git check-ignore -v`). Every row of the list is either untracked and
*not* ignored (git status would not list it otherwise) or tracked, and without `--no-index`
`check-ignore` never reports a tracked file. So the answer is always "no match". The test that
covers it (`test/ignore_test.dart`, "the pane shows the ignore files of the cursor row and moves
with the cursor") only passes because its fake lookup invents a match the app cannot produce. The
Ignore dialog has the same dead branch ("already ignored by … in file:line").

The deeper problem is the question itself. The cursor can only rest on a row the list shows, and
the list shows exactly the paths git did not ignore; an ignored untracked path is absent. A tracked
path can match a `.gitignore` pattern, but ignore rules do not apply to tracked files, and
`check-ignore` does not report one without `--no-index`. So "which rule ignores this row" has no
reachable answer: the pane asks why a visible row is ignored, about rows that are not ignored.

## The idea

Bring back Purrage's two panes, without the match lookup, and keep what Ops added.

The value is the ignore surface itself — seeing where the ignore files are and editing their rules
— not a verdict about the highlighted row. Purrage's two panes keep that value with the match
removed; there, the match is only a shortcut for choosing which file to show. Ops made it the
pane, so removing it leaves a path-scoped list with a gap where the reason for the pane used to be.

- Two panes side by side
  - left: the list of every `.gitignore` in the project, named by its folder; the top-most one is
    the "project .gitignore" (not "root"); 35 % of the pane's width, at least 80 px
  - right: every line of the selected `.gitignore` as it is, comments and blank lines too, without
    line numbers; the rest of the width, for the rules
- No `.git/info/exclude` and no global ignore file in the list: `.gitignore` files only.
- The list does not follow the cursor row: it starts on the project `.gitignore` when it exists,
  else the first file found, and keeps the file the user picked last for the session.
- No "which rule matches" verdict, no highlighted rule, no `check-ignore` per cursor rest.
- The files are read once when the panes open, and again only when the status reports a changed
  `.gitignore` path or after the app's own write; moving the cursor in the file list reads nothing
  (proportional work: a cursor move moves a highlight).
- Line actions, on every line (rules, comments and blank lines, so any line can be deleted)
  - the right-click menu: Delete, Dirname, Flip, Open
    - Dirname takes a rule one folder up, as in Purrage: disabled where there is no folder above
      (the tooltip says why), never a wildcard-only parent (`**/`, which matches everything below),
      and only removes the line when the parent rule is already in the file
      - not a rule (a comment or a blank line): not enabled; "dirname only works on positive rules"
      - a negation: not enabled; "please edit negation rules manually"
      - a wildcard-only parent: not enabled; "please edit wildcard rules manually"
      - no folder above (`*.log`, `/x.log`, `build/`): not enabled; "no folder above this rule"
    - Flip toggles the leading `!` on a rule, so a positive rule becomes a negation and back; it is
      disabled on comments and blank lines ("flip only works on rules")
    - Open opens the `.gitignore` in the editor at that line
  - the hover buttons stay, an exception to the rule that ported Purrage modes have no hover-only
    buttons; the "one folder up" button is renamed Dirname, the same word as in the menu
- Purrage's Open in editor (the selected `.gitignore`) and New here (a `.gitignore` in the cursor
  row's folder — inside the folder for a directory row, at the root for the project file; the new
  file shows up as an untracked row, tracked like anything else).
- Ignore-file I/O goes through the backend, never a local path:
  - `RepoBackend` gains `loadIgnorePanes` (tracked `.gitignore` list plus the selected file's text
    in one call), `untrackedIgnoreFiles` (added later), `readIgnoreFile`, `appendIgnoreLines`,
    `replaceIgnoreLine`, `insertIgnoreLine`, `createIgnoreFile`, and an `IgnoreFileRef` that names
    either a repo-relative `.gitignore` or the `.git/info/exclude` target
  - `LocalBackend` delegates to `Repo`; `NvimBackend` calls a new relay module, so Neovim in a VM or
    over SSH works
  - Open in editor uses `EditorSession` (`session.editor`), not a local repository root
  - after a write, the file is read again and the new rule's line is found by a helper (not by
    guessing from the append result)
- Keys as in Purrage, plus Enter
  - the `.gitignore` list and the lines are two Tab stops; `j` / `k` pick a file in the list and
    move the line cursor; Shift+wheel scrolls the lines
  - Enter opens in the editor: the selected `.gitignore` from the list, the file at the line cursor
    from the lines
- After the Ignore dialog writes a rule, the list selects the `.gitignore` it went into, and the new
  line is put in the middle of the lines pane at once, without an animated scroll.
- The area is shared with the preview, one at a time: a switch above it chooses the ignore panes
  or the preview, as Purrage's Git lists / Preview, and is remembered.
- The area is resizable by its left edge, as in Purrage: the width is remembered, and the area is
  hidden by default when the window is narrower than 600 px; `p` or the switch still opens it.

## Performance

- Not on every refresh. A refresh comes with nearly every git hint (each save in Neovim); the panes
  do not read again then.
  - the `.gitignore` files are found again only when the status lists a changed `.gitignore` path,
    or after the app's own write
  - only the selected file's text is read; the list needs names, not contents
  - one `loadIgnorePanes` call answers both (the tracked list and the selected file's text), not one
    call per file: over the relay every call is a round trip; `untrackedIgnoreFiles` adds the rest
    after the tracked ones are on screen
  - the first call also includes the project `.gitignore` when it exists but is untracked, so the
    default selection and its text are there on open; the later call adds the nested untracked ones
- Nothing while hidden. With the switch on Preview, the ignore panes neither listen nor read: they
  mark themselves stale and load when they are shown again. The same for the preview while the
  ignore panes are shown. This round does it for these two panes only; the rest of the app is the
  change `ops-hidden-panes-idle`.
- Every line has the same height (`itemExtent`), so centring a line is one `jumpTo` with no layout
  pass to measure first. A line is one line, cut with an ellipsis, never wrapped. The height
  follows the text style, not a constant, so it stays right when custom font sizes come.
- Discovery off the UI thread, in two steps: the tracked `.gitignore` files (`ls-files --cached`)
  show at once; the untracked ones (`--others`, which walks every untracked folder and can take
  seconds in a repo with an unignored `node_modules`) are added when they arrive.

## Usability

- Keys follow the motion rules of the rest of the app (CLAUDE.md, Keys)
  - Right / `l` goes from the file list to the `.gitignore` list, then to the lines; Left / `h`
    back the same way
  - going up into a list from below lands on its lowest visible item; Ctrl+arrow jumps between
    the panes
  - new focus nodes get a `debugLabel` and an entry in the debug bar's `focusRoles`
- Undo: Delete, Flip and Dirname act at once; the notice after one has an Undo button. One undo at
  a time: the next edit replaces it. Undo writes the old line back, with the same check that the
  file did not change meanwhile.
- `Delete` on the line cursor deletes that line, with the same Undo.
- The effect of an edit is said: after the refresh that follows, a short notice counts the rows that
  came back or left the list ("3 files back in the list", "2 files now ignored"), from the status
  before and after, with no extra git call.
- Which files apply to the row (a trial): the `.gitignore` list marks the files that govern the
  cursor row's folder, its own and those above it. It only marks; the selection stays where the
  user put it. A string-prefix check per file, no git. Kept if it helps, dropped if it is noise.
- Empty: a project without any `.gitignore` shows that, with a "Create project .gitignore" button.
- Narrow: under 600 px of window width the area is hidden by default, but `p` (or the switch)
  still opens it, as in Purrage. An explicit open stays open until `p` closes it; a later window
  resize does not undo the user's choice.
- Open in Neovim: after a write, a `.gitignore` that is open in a Neovim buffer without unsaved
  changes is reloaded there (the relay, like `:checktime` for that buffer), so Neovim shows the
  change at once. A buffer with unsaved changes is left alone: the app writes the file, and
  Neovim's own "changed on disk" warning is enough.

## Adjustments to Purrage

- No match lookup, no "not ignored" verdict, no Open line for a match in `exclude` or the global
  file (all dead, see Why).
- The panes explain the ignore surface, not the row's ignore state: a visible row is never ignored,
  and a match on a tracked row has no effect on it.
- The list does not follow the cursor row (Purrage followed the match).
- The project `.gitignore`, not `root`; `.gitignore` files only.
- Every line is shown and can be deleted, comments and blank lines too; no line numbers.
- Hover buttons on the lines, in addition to the menu; the menu also has Flip and Open.
- Enter opens in the editor; the lines have a cursor to open from.
- Ignore I/O goes through the backend, so a Neovim in a VM or over SSH is supported.
- Hidden under 600 px of window width (Purrage: 900 px).

## Cleanups that go with it

- Remove the test that invents a match (`test/ignore_test.dart`, "the pane shows the ignore files
  of the cursor row and moves with the cursor") and its "one lookup per resting place" assertion;
  a fake match is not a regression test for a reachable feature. Replace it with tests of what the
  panes do: the list starts on the project `.gitignore` and keeps a pick across cursor moves, a
  cursor move reads no file, a written rule selects its file and centres its line.
- Remove the match from the pane state (`IgnoreInfo.match`, `isMatch`, the verdict line, the
  highlighted rule, the `checkIgnore` call, the debounce timer and the per-path cache).
- Remove the Ignore dialog's dead "already ignored" branch: `IgnoreChoice.already`, the
  `checkIgnoreAll` call in `forSelection`, `AddIgnoreState.alreadyIgnored()`, the preview lines
  and the "git already ignores it" problem.
- The Ignore dialog's target names follow the panes: "project .gitignore", not "root .gitignore".
- Ignore I/O moves off the local `Repo` and onto `RepoBackend`; `ensureRepo()` and the Neovim-root
  reopen stay only for the actions that still need a local repository (delete), not for the pane.
- Unit tests for the pure helpers: every dirname rule shape and refusal (leading spaces, escaped
  `\#` and `\!`, folder-only rules, bracket-only parents, `**/`), Flip on positive, negated,
  escaped (`\!`), leading-space and non-rule lines, and the line-after-write helper (CRLF, no final
  newline, several rules, duplicate).
- Relay tests for the new ignore module: discovery, read, append, replace, insert, create, exclude,
  and the relative-path rules; an open unmodified buffer reloads after a write.
- Backend contract tests through a fake remote backend whose paths do not exist on this machine:
  listing, reading, editing and creating never touch the local filesystem; run the same contract
  against `LocalBackend`.
- Pane tests for Undo (Delete, Dirname-removal, Flip, refusal when the file changed), the effect
  notice, and the governing-file marker.
- CLAUDE.md: the ignore lines are the named exception to "no hover-only row buttons".

## Decisions

Settled with the user on 2026-11-19 (a question round); folded into the sections above.

- the list: every `.gitignore` of the project, the top one named "project .gitignore"; not
  `exclude`, not the global file
- the words: the left pane is the list of `.gitignore` files, the right pane the selected file's
  lines; "rail" is not used for them
- two panes side by side; the list takes 35 % of the pane, at least 80 px, the rules the rest
- the area: resizable, width remembered, hidden by default under 600 px (where `p` still opens it);
  shared with the preview through a switch
- the line menu: Delete, Dirname, Flip, Open; the hover button is renamed Dirname
- the refusals have their own words: "dirname only works on positive rules", "please edit negation
  rules manually", "please edit wildcard rules manually", "no folder above this rule", and "flip
  only works on rules"
- the lines have a cursor: `j` / `k` move it, Enter opens at it
- the list does not follow the cursor row; it starts on the project file (else the first file) and
  keeps a pick for the session
- every line shown, comments and blank lines too, no numbers; the menu and the hover buttons on
  every line
- keys: Purrage's, plus Enter to open in the editor
- after a write: select the file, the new line in the middle of the lines pane, no animation
- ignore I/O goes through `RepoBackend`, with repo-relative paths, so a remote Neovim works
- Purrage is left as it is (frozen); only Ops and the relay backend change
- second round (same day): read only on a `.gitignore` change or an own write, and only the
  selected file; hidden panes idle (here only, the app-wide part is its own change); one row height
  from the text style (custom font sizes will come); discovery in two steps; the motion keys;
  Undo as a button, one at a time; `Delete` deletes a line; the effect of an edit counted; the
  marker for files that apply to the row, as a trial; the empty state; `p` under 600 px
- third round: the backend loads the tracked list and selected text in one call, untracked files
  later; Undo of a removed line uses a dedicated `insertIgnoreLine`; the governing-file marker is
  implemented as a trial in this change; a remote backend must be usable through a fake backend
  contract test as well as the manual check
- a `.gitignore` open in Neovim: reload the buffer after a write when it has no unsaved changes;
  with unsaved changes, nothing special (the user does not edit them in both at once)

## Ideas for later

- Open in editor, one key everywhere: whatever opens something in the editor (a file row, a
  `.gitignore`, a line) uses the same key across the app; Enter here is the first step. Check the
  other modes and make them agree.
- A stacked layout as a second choice next to the switch (tiny, low priority): the ignore panes and
  the preview both open, the ignore panes above or below the preview, chosen in Settings.
- Dead rules marked: a negation (`!…`) under an excluded folder can never re-include anything. A
  separate change: `ops-dead-ignore-rules`.

## Technical notes

- Discovery happens in the backend, as in Purrage: `git ls-files --cached --others
  --exclude-standard -- ':(glob)**/.gitignore'` (the root file included); nested untracked files
  included, ignored ones skipped.
- `RepoBackend` gains the ignore-file API: `loadIgnorePanes` (tracked list and selected text in one
  call), `untrackedIgnoreFiles`, `readIgnoreFile`, `appendIgnoreLines`, `replaceIgnoreLine`,
  `insertIgnoreLine`, `createIgnoreFile`, and an `IgnoreFileRef` for a repo-relative `.gitignore`
  or the `.git/info/exclude` target. Paths are repo-relative; the backend resolves them and returns
  text/lines, never a local absolute path.
- `LocalBackend` delegates to `Repo`; `NvimBackend` calls a new relay module
  (`nvimos-relay/lua/nvimos/gitignore.lua`) with its own Lua tests.
- State: `lib/state/ignore_pane.dart` becomes a loaded-once list of files plus the selected one
  and the line cursor; tests drive it without widgets.
- The edits reuse `Repo.replaceIgnoreLine`'s semantics (one read, one write, refused when the line
  changed), through the backend so it works remotely too; Undo of a removed line uses
  `insertIgnoreLine` with the same "line unchanged" check on its neighbours.
- The line-after-write helper is pure and unit-tested: re-read the file, then find the exact rule
  line; a duplicate write selects the file without scrolling; several new rules centre the first.
- Open in editor uses `EditorSession.open(relativePath, line)`, not the local editors' root.
- The width and the switch are kept in prefs, like the other remembered sizes; an explicit `p` open
  under 600 px is a session override, not a prefs value.
- Purrage reference: `lib/ui/ignore_pane.dart` and `lib/state/ignore_files.dart` in
  `~/ws/Purrage`, its `PLAN.md` sections "Where a rule lives" and "The right-hand pane".
- Notes: `nvimos-ops/doc-wip/readme.2026-11-19.ignore-pane.md`.
