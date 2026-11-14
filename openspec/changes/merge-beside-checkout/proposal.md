# merge beside the checkout

Status: To Do (backlog TASK-143). The open questions were answered on 2026-11-14 (see Decisions).
The work is in backlog tasks, not in a tasks.md: TASK-143 clean merge without a checkout, TASK-144
bring the checkout forward, TASK-145 refuse on unsaved buffers, TASK-146 merge worktree for
conflicts, TASK-147 dialogs and notes in Ops, TASK-148 merge rules in PLAN.md.

## Why

The PR mode has a Merge button. It merges the head branch into the base branch with a merge commit,
and nothing is pushed. To do that today, it uses the main checkout: the folder where I normally
work and where Neovim has my files open. If base is not the branch checked out there, Merge
checks it out first. Merge also refuses to start while there are unsaved buffers or uncommitted
changes to tracked files. A merge in a dirty folder can mix my unfinished edits into the merge, or
fail halfway and leave both tangled together.

That rule is safe, but it gets in the way of the most common case. Most days, the main checkout is
on `main` and has something in progress: a half-written README section, a config value I am trying
out, or files an agent is editing. Meanwhile a finished branch is waiting, say
`feature/api-integration`, which an agent built in its own worktree. All I want is to put that
branch into `main`. Today I first have to commit or stash my unrelated work, merge, and then get my
work back. The merge has nothing to do with the files I am editing, but the folder is dirty, so I
am stopped.

The other case is just as awkward. Say I am working on `feature/cms-updates` in the main checkout,
and I want to merge `feature/api-integration` into `main`. Merge would switch the main checkout to
`main`, right where Neovim has my `feature/cms-updates` files open. Even if that works, it is not
what I asked for. I wanted `main` to move forward, not to be taken off my own branch.

So the goal is this: merging a finished branch into `main` should not need the main checkout to be
clean, and it should not switch branches or leave conflict markers there. The main checkout belongs
to me while I work. The merge should happen somewhere else.

## The idea

Most merges are clean: the two branches changed different files, or different parts of the same
file. Git can work out such a merge entirely by itself, without writing a single file on disk. It
does the merge in its own storage, makes the merge commit there, and then moves `main` to point at
it. No folder has to be checked out and no files are written, so nobody's work is in the way. When
Ops moves `main`, it first checks that `main` is still where it was when the merge started. If
someone else committed to `main` in the meantime, the merge is not saved, nothing is lost, and Ops
asks me to merge again.

Some merges have conflicts: both branches changed the same lines. Those can't be finished without a
place to resolve them, where someone opens the files with conflict markers, fixes them and commits.
That place should not be my main checkout. So Ops makes a merge worktree of its own, one per PR
branch, in the temp folder: `%TEMP%\nvimos-ops\merge.<repo>.<branch>`, for example
`merge.nvimos-poc-frontend.feature-api-integration`. The names start with `merge` so they are easy
to spot as a group. The conflicted merge waits there for me. `main` does not move until the
conflict is resolved and committed, and my main checkout never sees a conflict marker. Once the
merge is committed or thrown away, Ops removes the worktree.

One step is left when `main` is the branch checked out in my main checkout. Moving the branch does
not change the files on disk. Right after the merge, my folder still shows the old `main`, and git
would think I had undone everything the merge brought in. So Ops brings the folder forward to the
new `main`, the same way git does when switching between two commits: it rewrites the files the
merge changed and leaves every other file alone, including my uncommitted edits. After that, Neovim
reloads any open buffer whose file changed, so I see the merged text.

The tricky part is a file that the merge changed and that I am also editing. Then the merged
version and my unfinished version would have to be mixed in my folder, which is exactly what we
want to avoid. Ops asks me first, in a dialog that lists those files; the use cases below describe
it. A buffer with unsaved changes on such a file is different: Merge refuses before anything
happens.

This is the fallback, not a replacement. When the main checkout is already on the base branch and
clean, Merge works as it does today. The new path takes over only where today's Merge would
refuse or switch my branch.

In short: a clean merge happens without a folder, a merge with conflicts happens in Ops's own
merge folder, and the main checkout is never switched to another branch. At most, it is brought
forward to the new `main` when that is the branch it is on.

## Use cases

Each case is written from where I sit: what I do, what I see, and which part of the idea handles
it. The branches are an ordinary week's work: `main`; two finished branches, `feature/api-integration`
and `fix/login-timeout`; and `feature/cms-updates`, which I am still writing.

### Merging into main while I have unrelated work in progress

The main checkout is on `main`. I have uncommitted edits in `README.md` and `config/dev.yaml`. An
agent has finished `feature/api-integration`, which adds files under `lib/api/` and changes
`lib/client.dart`. In the PR mode I pick base `main` and head `feature/api-integration`, look at the
diff, press Merge and confirm.

Today, Merge refuses because the folder is dirty. With this proposal, the merge is clean, so git
does it without a folder, `main` moves, and my main checkout is brought forward. I see the short
note "Merged feature/api-integration into main", and the lists refresh. `lib/api/` and the new
`lib/client.dart` are on disk, and if I had `lib/client.dart` open in Neovim, the buffer now shows
the merged text. My README and config edits are still there, uncommitted and untouched.

### Merging into main while I work on another branch

The main checkout is on `feature/cms-updates`, my own branch, with open buffers and some unsaved
work. `fix/login-timeout` is done, and I want it in `main`. I pick base `main` and head
`fix/login-timeout`, and press Merge.

Today, Merge would switch my folder to `main` and take me off my branch. With this proposal, `main`
is not checked out anywhere, so no files need to change at all. The merge happens without a
folder, and `main` moves. My checkout, my branch and my buffers are left completely alone. I see the
same short note, and `main` in the pickers now contains the fix.

### The merge changes a file I am editing

As in the first case, but this time my uncommitted edits are in `lib/client.dart`, the same file
`feature/api-integration` changes. The merge itself is clean, but bringing my folder forward would
have to mix the merged `lib/client.dart` with my unfinished edits.

Before anything happens, Ops shows a dialog. It lists the affected files, here `lib/client.dart`,
and offers four ways on:

- **Stash, apply, pop** (the default): my edits to those files go into a stash, the folder is
  brought forward, and the stash is applied on top. If it applies cleanly, the stash is dropped.
  If my edits and the merge touched the same lines, the file gets conflict markers and the stash
  is kept, so nothing is lost.
- **Discard modified files**: my edits to those files are thrown away and the folder is brought
  forward.
- **Move main only**: `main` moves, my folder stays behind with a note, and I bring it forward
  when my edit is done.
- **Refuse**: nothing happens.

My other uncommitted edits, in `README.md` and `config/dev.yaml`, are left alone in every case.

### The merge changes a file with unsaved changes in Neovim

As above, but I have `lib/client.dart` open in Neovim with unsaved changes. Ops never overwrites
such a buffer, so Merge refuses up front. The note names the path and the buffer number, for
example "lib/client.dart (buffer 7) has unsaved changes, and the merge changes it", and has a
button that opens that buffer in a new tab, so I can save or drop the changes and merge again.

### The merge has conflicts

`feature/cms-updates` and `feature/api-integration` both changed `config/routes.yaml`. The API
branch was merged yesterday. Today I merge `feature/cms-updates` into `main`, and the two changes to
the routes file overlap.

Today, Merge undoes the merge, lists the files, and that is the end of it. With this proposal, Ops
finds out about the conflict without having touched anything, then runs the merge in its own merge
folder and leaves it there. I see a note that the merge stopped on a conflict in
`config/routes.yaml`, with a way to open it or throw it away. My main checkout and `main` itself
are exactly as before. Once I have fixed the file in the merge folder and committed, `main` moves to
the merge commit. If my main checkout is on `main`, it is brought forward as in the first case.

### Main moved while I was deciding

I opened the merge question for `fix/login-timeout`, and while it was open, an agent committed a
small fix straight to `main`. I press Yes.

The merge was worked out against the old `main`, so Ops does not save it. Nothing is lost: the
agent's commit stays on `main`, and no merge commit is stored. I see a note that `main` changed
during the merge and the merge should be run again, and the diff refreshes to the new `main`.

### Nothing in progress

The main checkout is clean and on `main`. Merge works exactly as it does today; the new path is
not used. That keeps the risk low while the new path is young.

## How it works in git

This section is the technical side of the idea above. The git here is 2.46. `merge-tree
--write-tree` needs 2.38 or later.

### A clean merge, without a work tree

`git merge-tree --write-tree` merges two commits in the object database. It writes no files and
uses no index. On success it prints the id of the merged tree and exits 0. On a conflict it exits 1,
and the output lists the conflicted files.

```sh
old=$(git rev-parse refs/heads/main)
head=$(git rev-parse refs/heads/feature/api-integration)

tree=$(git merge-tree --write-tree "$old" "$head")      # exit 1: conflict, see below
commit=$(git commit-tree "$tree" -p "$old" -p "$head" \
         -m "Merge branch 'feature/api-integration'")
git update-ref -m "ops: merge feature/api-integration" refs/heads/main "$commit" "$old"
```

The last argument of `update-ref` is the value `main` must still have. If someone moved `main`
in the meantime, `update-ref` fails, and the new commit is simply an unreferenced object that `gc`
cleans up later. That is the "Main moved while I was deciding" case.

The merge commit gets the usual author and committer from `user.name` and `user.email`. Hooks do
not run (`commit-tree` is plumbing), which matches today's Merge closely enough, since it runs no
hooks of its own either. That is worth checking.

### Bringing the main checkout forward

When `main` is checked out in the main checkout (`git symbolic-ref HEAD` is `refs/heads/main`
there), the files on disk still match `$old` after `update-ref`. A two-tree read moves the index
and the work tree from `$old` to `$commit`, changing only the paths that differ between the two,
which is what `git checkout` does:

```sh
git read-tree -m -u "$old" "$commit"
```

It refuses, and changes nothing, if a path that differs between the two trees also has changes in
the index or the work tree. That is the "file I am editing" case. To ask before anything moves,
check first:

```sh
git diff --name-only "$old" "$commit"         # files the merge changes
git status --porcelain=v1 -z                  # files I have touched
# overlap -> the dialog, listing the files
```

The dialog's choices, with `$files` the overlapping paths:

```sh
# stash, apply, pop (default)
git stash push -m "ops: merge feature/api-integration" -- $files
git update-ref refs/heads/main "$commit" "$old"
git read-tree -m -u "$old" "$commit"
git stash apply --index && git stash drop     # conflict: markers in $files, stash kept

# discard modified files
git checkout "$old" -- $files                 # back to the committed text, then as usual

# move main only: update-ref, no read-tree; the note says the folder is behind
# refuse: nothing
```

The stash list is shared by all worktrees; the message `ops: merge <branch>` makes Ops's entry
easy to recognise.

`main` being checked out in some other worktree (an agent's) is found with
`git worktree list --porcelain`. That worktree is left alone: bringing it forward is its owner's
business.

The unsaved-buffer check and the reload happen in Neovim: refuse if a modified buffer's file is in
the `git diff --name-only` list, naming the path and the buffer number, and run `:checktime` after
`read-tree`. Opening the buffer in a new tab is `:tab sbuffer <nr>`.

### A merge with conflicts, in the merge worktree

`main` may not be checked out twice, so the merge worktree uses a detached HEAD:

```sh
repo=$(basename "$(git rev-parse --show-toplevel)")
wt="$TEMP/nvimos-ops/merge.$repo.feature-api-integration"   # '/' and other unsafe chars -> '-'
git worktree add --detach "$wt" "$old"
git -C "$wt" merge --no-ff --no-commit feature/api-integration
# conflicted files: git -C "$wt" diff --name-only --diff-filter=U
```

After I resolve and stage the files there:

```sh
git -C "$wt" commit --no-edit
git update-ref refs/heads/main "$(git -C "$wt" rev-parse HEAD)" "$old"
git worktree remove "$wt"
# then bring the main checkout forward, as above
```

Throwing the conflict away is `git -C "$wt" merge --abort` and `git worktree remove "$wt"`. The
temp folder can be cleaned out by Windows or a cleanup tool; then `git worktree prune` forgets the
worktree and Ops makes it again. A half-resolved conflict is lost with it, which is a known risk.

### Later actions

A fast-forward is `git merge-base --is-ancestor "$old" "$head"` followed by `update-ref` to `$head`
and the same bringing forward. A squash is `merge-tree` and `commit-tree` with one parent (`-p
"$old"` only). A rebase really needs a work tree and would be the merge worktree's second job.

## Decisions

Answered on 2026-11-14:

- **The merge worktree stays.** A conflict is one click in Ops, not a trip to the terminal.
- **It lives in the temp folder**, one per PR branch: `%TEMP%\nvimos-ops\merge.<repo>.<branch>`,
  removed once the merge is committed or thrown away.
- **A merge that changes a file I am editing** opens a dialog listing the files: stash, apply, pop
  (default), discard modified files, move main only, or refuse.
- **An unsaved buffer on a merged file** makes Merge refuse up front, naming the path and the
  buffer number, with a button that opens the buffer in a new tab.
- **`main` checked out in an agent's worktree** is left alone.
- **The new path is the fallback**, used only where today's Merge would refuse or switch my
  branch. A clean main checkout on base merges as today.
- **The backend runs the git commands** (`git.merge` in relay), next to the buffer check and the
  reload.

Still to check: the merge commit made with `commit-tree` runs no hooks.

## Impact

In the backend, `git.merge` (relay, branch `PR-merge-action`) gains the folder-less merge, the
guarded branch move, bringing the main checkout forward with the stash and discard choices, the
unsaved-buffer refusal with buffer numbers, and the merge worktree. In the frontend,
`PrState.canMerge` and `PrState.merge` in `lib/state/pr.dart` stop refusing a dirty folder as a
whole, `lib/ui/pr_view.dart` gains the affected-files dialog, the "open buffer in a new tab"
button, and the conflict and "main moved" notes. The merge rules in `PLAN.md` are rewritten to match.
