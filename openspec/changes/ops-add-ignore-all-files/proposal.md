# Add and Ignore: show every tracked file too

Tags: ops, ui
Status: In progress, for TASK-208.

## Why

Add and Ignore lists what git has something to say about: conflicts, staged, changed and untracked
files. With the preview beside it, it is also the quickest way to look through a repository's
files, except that only the changed ones are in the list. Browsing the rest means another tool.

This stretches the mode beyond its git-and-ignore purpose, knowingly: the use is worth it.

## The idea

- A toggle button in the list's header, left of the preview, ignore panes and reload buttons, and a
  key (`T`), shows **all files**: every file git tracks, not only the changed and untracked ones.
- The clean tracked files come in their own section, **Tracked**, under the others; a changed file
  stays in its own section and is not listed twice.
- A tracked row has the same tools as any tracked row: untrack (`−`), the eye that ignores and
  untracks it, Open and Delete in the right-click menu. It has no add button (there is nothing to
  stage).
- The preview, the filter and the selection work over the larger list unchanged: filter by name,
  highlight, read the file beside it.
- The choice is remembered. The button is lit while all files show.

## Use cases

- I want to read `lib/state/session.dart` without opening an editor. I press `T`, type `session` in
  the filter, and the preview shows it.
- I want to stop tracking a generated file that was committed by mistake. With all files shown, I
  find it in Tracked and press the eye: it is ignored and untracked in one step.
- I turn it off again, and the list is back to what needs my attention.

## Technical

- The tracked paths come from `git ls-files -z` (`Repo.trackedFiles`), through the repository the
  mode already opens for ignore and delete (`ensureRepo`, also when connected to Neovim).
- Proportional work: the list is read once when the toggle goes on and again after each status
  refresh (git hints, an action), and replaced only when it changed, so the rows cache (keyed on the
  identity of the status, the tracked list and the toggle) survives cursor moves and unchanged
  refreshes. Off, no `ls-files` runs.
- `AddIgnoreSection.tracked`, after `untracked`; a tracked row is a `StatusFile` with no flags; its
  letter is blank with a tooltip that says it is tracked and unchanged.
- A big repository gives a long list: the list is built lazily (`ListView.builder`), the rows are
  sorted once per change.
