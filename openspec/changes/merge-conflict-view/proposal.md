# merge conflict view

Status: In Progress (backlog TASK-151 to TASK-153). Builds on `merge-beside-checkout` (TASK-143 to TASK-146)
and TASK-150. Drafted 2026-11-15. Rescanned 2026-11-19: the merge-tree pre-flight, the
conflict-marker checks and finishing in the merge worktree are in the relay's `merge.lua`, the
conflict view is `conflict_view.dart` in Ops; the backlog tasks still say To Do and need checking
against the code and a test.

## Why

Clicking Merge in the pull request view today either merges cleanly or, when the two branches changed
the same lines, undoes the merge and shows an error that names the files. The error tells me what
went wrong but nothing about how to fix it. To finish the merge I have to leave Ops, open each
conflicted file in another tool, fix the lines, come back, and commit somewhere else. The part of
the job that needs the most care is the part Ops does least for me.

The goal is that a conflict becomes something Ops shows and helps me resolve, in the same place where
I started the merge, with the same kind of view I already use for diffs.

## The idea

Merge starts with a pre-flight. Before anything changes, Ops asks git whether the two branches would
conflict, and it does this without writing anything to the repo. A conflict costs nothing to find
out. If there is no conflict, the merge runs as it does now, as described in `merge-beside-checkout`.
If there are conflicts, Ops does not run the merge at all. It opens a third diff mode, the conflict
view, beside the unified and side-by-side modes. The view lists the conflicted files and lets me
resolve them.

The conflict view works on the merge worktree from TASK-146, a separate working folder that Ops keeps
for the merge, not on my main checkout. So my main checkout never sees a conflict marker, and `main`
does not move until the merge is committed.

Within a conflicted file, each hunk shows the two sides, ours and theirs, and I pick one of them for
that hunk. The idea follows Meld, an open source diff tool, which lets the user take either side of a
conflict block. A conflicted file can also be opened in nvim, in a new nvim-qt window on that file
and not in diff mode, for anything the two picks do not cover.

Two guards keep a half-resolved file from getting through. Adding a file, with the add button that
also marks a conflict as resolved, is refused while the file still has conflict markers at the start
of a line. And before the commit that completes the merge, a verify step checks that no conflicted
path is left and that no staged file has a marker. Tests and analysis are optional, not a gate.

When everything passes, the commit completes the merge on `main`.

In short: a conflict is found before anything changes, shown in its own diff mode, resolved per hunk
or in nvim, guarded at add and again at commit, and finished by a merge commit on the base branch.

## Use cases

The cast: I am a developer working on Ops. `feature/api-integration` is a finished branch that an
agent built in its own worktree. `main` is the base. The conflicts I meet are in `config/routes.yaml`
and `PLAN.md`, where both branches changed the same lines.

### Merge with a conflict

I click Merge in the pull request view with `main` as base and `feature/api-integration` as head. The
pre-flight finds two conflicted files, and the conflict view opens on the first one. Nothing asks me
first, the same as a plain merge. Today the same click would have ended in an error that undoes the
merge. The part of the idea that handles it is the pre-flight, and the view it opens.

### Pick a side for one hunk

In `config/routes.yaml` there is one hunk where my branch renamed a route and `main` changed its
timeout. I pick theirs for the rename and ours for the timeout, and the file's preview shows the
combined result. The other hunks stay as they are until I pick them too.

### Open a file in nvim

One hunk in `PLAN.md` needs a real edit that neither side has. I open the file in nvim, in a new
nvim-qt window, edit it, save, and come back to Ops. The conflict view reads the file again, so
what I saved is what I see.

### Try to add a file with markers

I click add on `PLAN.md` while a `<<<<<<<` line is still in it. Ops refuses, names the file and the
line, and the file stays unresolved. The check is the reason the add button is safe to use in a hurry.

### Everything resolved

I add both files. The verify step passes, nothing is left unmerged and no marker is staged, and the
commit completes the merge on `main`. The view says so, and the lists refresh.

### Main moved while I was resolving

While I was resolving, a support engineer committed a fix to `main`. When I click Resolve, Ops runs
the pre-flight again. If the conflict is still there, the view opens with the current files. If the
conflict is gone, the merge goes through as a plain merge and the view says that it did.

### Nothing special

I merge `feature/api-integration` into `main` and there is no conflict. The pre-flight passes, the
merge runs as a plain merge, and no view opens. That case keeps working exactly as it does today.

## How it works in git

The pre-flight reads both branches without changing the repo, and the resolution happens in the merge
worktree, never in the main checkout. Each block below is one part of the idea.

### The pre-flight

    git merge-tree --write-tree --name-only --messages <base> <head>

This writes objects to git's store but does not change the working tree, the index or any branch. It
lists the conflicted paths by name. It needs git 2.38 or newer, which this machine has; an older git
needs the three-argument form, which prints its output in a different shape and has to be parsed.
Its result decides the dialog, and the same call runs again when Resolve is clicked, so a commit that
landed in the meantime is not missed.

### Resolving in the merge worktree

    git -C "$wt" add <file>          # only after the marker check passes
    git -C "$wt" commit              # completes the merge on the detached base

The merge worktree is the one from TASK-146, at `%TEMP%\nvimos-ops\merge.<repo>.<branch>`, detached
at the old base. Add is the git step that marks a conflicted file as resolved. The commit in that
worktree makes the merge commit, which is the point where the merge stops being pending.

### The marker check

    # refuse the add when the file still has a conflict marker at the start of a line
    grep -nE '^(<{7}|={7}|>{7})' "$wt/$file"

The check runs before every add, and the first matching line is reported with the file name. It reads
the file as it is in the merge worktree, so an edit made in nvim is seen.

### Moving main

    git update-ref refs/heads/main <merge-sha> <old-main>

The update uses the old value as a guard: if `main` has moved since the merge started, the update
fails and nothing is lost, and Ops asks me to merge again. This is the step from TASK-146 and the
merge-beside-checkout proposal, repeated here because the verify step runs just before it.

Versions: `merge-tree --write-tree` needs git 2.38 or newer (checked: 2.46.2 here). The marker check
is a plain pattern match, and it should be tested on files with CRLF line endings, which Windows
writes.

## Open questions

Whether the merge commit should land directly on `main`, or first on the branch being merged, is the
open point. If a resolution is wrong, `main` is broken as soon as the commit lands, which is the
concern I raised. The alternative of an extra commit on `feature/api-integration`, so the resolution
can be reviewed on the pull request first, costs one more step and a commit that is not on `main`.
The other alternative is to produce the resolution as a diff, apply it to the branch, and leave
`main` untouched until the result is known to be clean. That keeps `main` safe and costs the most
work. For now the outcome is a merge on `main`, and both alternatives are written in PLAN.md.

Where the resolution happens is also worth a note. The earlier idea was to run the merge with
`--no-commit` in the main checkout, which would leave the conflict markers in the folder I work in.
The merge-beside-checkout proposal decided against that, so this change follows the merge worktree.
If that decision is reversed, the verify and add guards still apply, but the main checkout would
see markers while the merge is open.

## Decisions

- Entry: the conflict view opens automatically when the pre-flight finds a conflict. There is no key
  and no entry in the rail.
- Mode: a third diff mode, beside unified and side-by-side.
- Resolve: per hunk, either side, modeled on Meld. nvim opens the conflicted file, not in diff mode.
- Add: refuses a file that still has conflict markers.
- Finish: the commit completes the merge on the base branch, after the verify step.
- No confirm dialog on Merge (decided 2026-11-15).
- Resolve re-runs the pre-flight before it opens the view.

## Impact

The conflict view is a third diff mode in `lib/ui/`, and the pre-flight and the resolve step sit in
`lib/state/pr.dart`. `lib/backend/backend.dart` gets the `merge-tree` call and the marker check. PLAN.md
already has the merge rules, the conflict view and the credit to Meld. The plain merge without a
conflict is unchanged.
