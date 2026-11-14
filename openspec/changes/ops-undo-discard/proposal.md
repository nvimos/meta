# undo a discard, instead of asking first

Status: Open proposal, not decided, not to be implemented yet. There is no backlog task yet; one gets
made if we go ahead.

## Why

In the Changes mode, discarding a file or a hunk asks "Discard changes? This can't be undone." every
time. I know what the discard button does. I pressed it because I want that hunk gone, and the
question only slows me down. When I clean up a file with six hunks I do not want six dialogs. I want
to click, see the hunk disappear, and go on.

The question is there for a good reason: a discard really is permanent today. Git has no copy of an
unstaged edit, so once Ops throws it away, it is gone. That is why the dialog exists, and it is why
simply deleting the dialog would be a bad trade. I would be one mis-click away from losing an hour
of work with no way back.

So the proposal swaps the question for a safety net. Ops stops asking and starts remembering. Every
file or hunk that gets discarded is first copied into a small collection that lives as long as the
app runs. Later, in the UI, I can look through what I discarded and put any of it back. The
discard becomes cheap to do and cheap to take back, which is what I actually want from a button
like this, instead of an expensive one that has to be guarded.

## The idea

A state object for the running session, the discard bin, that collects everything discarded:

- when I discard a hunk or a file, Ops first records what is about to be lost, as a patch (the same
  text `git apply` reads), together with when, which file, how many lines went, and a short preview
- then the discard runs, with no confirmation
- the recorded patches can be reapplied later from the UI, which puts the lines back into the work
  tree as unstaged changes, exactly where a discard took them from

Two rules shape how it behaves.

**It is kept per project and per branch.** A patch made against one branch's version of a file
usually does not apply to another branch's version, so a flat list of everything would mostly
offer things that cannot be put back. Each entry is filed under the project (the repository) and the
branch that was checked out when I discarded it. The Changes mode shows the entries of the project
and branch I am looking at; switching branch shows that branch's entries.

**It only lives for the session.** The bin is memory, not a file. When I close Ops, it is empty
again. That is on purpose: it is a short-term safety net for "oops, not that one", not an archive,
and nothing gets written to disk that I would later have to clean up or that could leak.

## Use cases

Each case is written from where I sit: what I do, what I see, and which part of the idea handles it.
The project is `webshop`. The main checkout is on `feature/cms-updates`, and `main` is another
branch of the same project.

### Cleaning up a file with several hunks

I have debug prints in `lib/cart.dart`, in six places, and I want them all gone. In the Changes mode
I select the file and click discard on the first hunk. The hunk disappears at once, with no dialog,
and I do the same for the other five.

I see each hunk vanish as I click. Behind the scenes, six entries were added to the bin for
`webshop` / `feature/cms-updates`. Nothing in the flow asked me anything.

### I discarded the wrong hunk

On the fourth click I notice that the hunk I just threw away was a real fix, not a debug print. I
open the discarded list in the Changes mode, find the newest entry for `lib/cart.dart`, with its
preview showing the lines, and press reapply. The lines are back in the work tree, unstaged,
at the place they came from, and the entry leaves the list (or is marked as reapplied).

This case needs the list to be easy to reach and to show enough of each entry that I can recognize it
at a glance: the file, the time, and the changed lines.

### I discarded a whole file's changes

I click discard on `config/dev.yaml`, meaning to drop my local tweak. A minute later I remember that
the tweak held a value I still needed. The bin has one entry for the file with all its hunks
together. I reapply it, and the file has my tweak again.

An untracked file is the harder variant: discarding it deletes the file. For this to be undoable,
the entry has to keep the whole content of the file, not just a diff. That is still small for text
files, and is one of the open questions below for large or binary ones.

### Switching branches

I discard a hunk on `feature/cms-updates`, then switch to `main` to look at something. The
discarded list now shows `main`'s entries, which are empty, so I do not see an entry that would not
apply here anyway. When I switch back to `feature/cms-updates`, the entry is there again.

### The file changed since the discard

I discarded a hunk in `lib/cart.dart`, then edited the file further, and now the old lines do not
fit where they were. I press reapply. Git's patch apply tolerates small shifts in line numbers, so
if the surroundings are still recognizable, the hunk goes back in at its new position. If not, Ops
says the patch no longer applies, the entry stays in the list, and the file is not touched. I can
still see the preview and copy the lines out by hand.

### I close the app

I quit Ops at the end of the day. The next day the bin is empty. Anything I discarded yesterday and
did not reapply is gone, as it is today. Nothing was written to disk.

## How it works

### Where the patch comes from

The backend already builds the patch for a hunk when it discards one (`hunk_patch` in
`git.lua`, applied in reverse). The simplest, safest capture is to let the backend return that patch
from `discard_hunk`, so the copy and the discard are the same step and cannot drift apart. For a
whole file, `discard` would return the unstaged diff of the file (`git diff -- path`) before it runs
`git restore`; for an untracked file it would return the file's content, since the discard deletes
it.

The frontend then files what came back under the project and the branch:

- **project**: the repository root, which the session already knows (`RepoInfo.root`)
- **branch**: the current branch name at the moment of the discard; on a detached HEAD, the short
  commit id, so a detached session still has a key

### The state object

A `ChangeNotifier` under `lib/state/`, like the other state objects, so tests can drive it without
widgets:

- an entry holds: an id, the time, project, branch, the file path, whether it was a hunk, a whole
  file, or a deleted untracked file, the patch text, and the counts of added and removed lines
- `record(entry)` is called by the Changes state right before the discard goes to the backend
- `entriesFor(project, branch)` is what the UI lists, newest first
- `reapply(entry)` asks the backend to apply the patch to the work tree (not to the index), and on
  success drops the entry
- it is created with the session and dropped with it, never saved

The Changes state's `discardFile` and `discardHunk` call it, and `confirmDiscard` disappears from
those two paths. The shared `ConfirmDialog` stays; the merge and archive questions keep using it.

### Reapplying

The backend gets a call that applies a stored patch to the work tree, with `git apply`, not
`--cached`, so the lines come back as unstaged changes, as before. The same checks a discard
already has apply: a file with unsaved changes in Neovim is refused, so Ops never writes under a
buffer that has newer text. A patch that no longer applies is reported with git's own message, and
the entry stays. For a deleted untracked file the call writes the stored content back, and refuses
if a file now exists at that path.

### Where it shows up in the UI

Not decided. The candidates, from least to most room:

- **A note with Undo, right after the discard.** Ops already has a short note with an Undo button
  that stays 3 seconds, or while the mouse is over it. It fits "oops, not that one" with no
  navigation at all. It is not enough alone, because it is gone after a few seconds, but it
  covers the most common case for free.
- **A "Discarded" button in the Changes header, with a count.** It opens a popover or a panel with
  the list for this project and branch. Small, always in the same place, and empty most of the
  time.
- **A third list in the Changes mode**, next to STAGED and CHANGES, shown only when the bin has
  entries for this project and branch. More visible, but it takes room from the file lists and
  brings its own keys and focus rules.

My lean is the first two together: the note for the immediate case, the header button for the
rest. That is still to be decided.

## Open questions

- Where the list lives (above), and whether reapply has a key. Any key is a separate decision, since
  keys can conflict with the existing ones.
- How many entries to keep. Entries are small text, but a session can run for days. A cap per
  project and branch (say the newest 200), or a total size cap, dropping the oldest first, would keep
  memory bounded. Which one, and what number.
- Large and binary files. A discarded binary file, or a very large text file, cannot sensibly be
  held as text. Options: keep the confirmation for those, and only those; or refuse to discard them
  without the dialog; or store the bytes up to a limit.
- Whole-file discard of a file with both staged and unstaged parts: only the unstaged part is
  discarded today, and only that part would be recorded.
- Whether a reapplied entry is removed or kept and marked, so the list shows that it was put back.
- Whether the discarded list can show other branches of the same project, with a switch, since a
  patch may still apply after a branch is rebased or a hunk is cherry-picked.
- A bulk discard ("discard all", if it ever exists) should be one entry group, not hundreds.

## Impact

- `nvimos-poc-frontend`: a new state object under `lib/state/`, `ChangesState.discardFile` and
  `discardHunk` record first, `confirmDiscard` removed from those two paths, a UI place for the list,
  PLAN.md (Changes mode, and the "General requirements" note about confirmations)
- `nvimos-poc-backend`: `discard` and `discard_hunk` return what they removed, and a new call
  applies a stored patch to the work tree
- tests: the state object (record, per project and branch, reapply, no longer applies), the backend
  calls (capture, reapply, refusing a buffer with unsaved changes), and a widget test that a
  discard no longer opens a dialog
- no change to the merge and archive confirmations
