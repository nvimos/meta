# a history mode with stacked branches

Status: Open proposal, decided in part (see Decided). Project: frontend (Ops). There is no backlog task yet.

## Why

Agents now build work as **stacked branches**: one branch per task, each started from the one
before it, several stacks in parallel worktrees, joined and merged in a fixed order later. In
Purrage on 2026-11-17 that was 21 branches in four stacks (A, B, C built in parallel, D after the
join), with the order kept by hand in an ASCII tree, in the task files and in commit trailers.

Ops can show one pair of branches as a pull request, but nothing shows the *shape*: which branch
sits on which, which one is next to merge, which stack still needs a rebase, which agent is still
building, and what each one reported. The user had to ask for the tree again and again while the
agents worked, and the merge order lived in a hand-written note
(`Purrage/doc-wip/readme.2026-11-17.merge-order.md`, where this idea started).

## What Changes

A new **History** mode on the rail (4th, after Pull request, Changes and Add and Ignore; the rail is Alt+1 … Alt+9, see
`purrage-mode-and-ui`). This proposal
specifies its first view, **Stack**; a commit log view can follow in the same mode.

### Where the stack comes from

Everything is read from the active directory's repository; nothing new has to be recorded.

- **Ancestry** draws the tree: each local branch hangs under the nearest other local branch that
  is its ancestor (`git merge-base --is-ancestor`), and the root is the default branch.
- **Intent** comes from the `Stacked-On:` commit trailer (and `Task:`), read from the branch's
  commits. When ancestry and intent disagree (a parent was rewritten, a stack is not rebased
  yet) the row is marked and shows both, e.g. "trailer: PR-keys-every-mode · ancestry: main".
- **Order**: the merge position from the task file's `Merge N of M` line, when there is one;
  otherwise the order of ancestry.
- **Worktrees**: `git worktree list --porcelain`: where a branch is checked out, locked or not;
  `git status` there: dirty or clean.
- **Agent information**: the task linked by the `Task:` trailer, read through the Tasks mode's
  Backlog reader: status, ACs ticked (`5/7`), and the `## Notes` section.

All **local** branches are shown; a `PR-*` prefix is not special.

### What a row shows

```
History ▸ Stack                                            watching refs ●
 main @ v2-solidify
 ├─ ✔ 1  PR-background-work-handle   task-19  Done 3/3          merged
 ├─ ▶ 2  PR-process-env-seams        task-15  Done 3/3   +4 −0  next  [merge]
 │  └─ ○ 3  PR-workspace-out-of-shell task-14 Done 3/3   +9      waiting
 │     └─ ⚠ 7 PR-time-the-actions     task-1   Done 4/4          trailer: PR-keys-every-mode,
 │                                                                ancestry: main  [restack]
 └─ ⟳ 13 PR-design-tokens             task-20  In Progress 5/7   dirty · stack-b
 Enter: review against parent   m: base ↔ main   M: merge next   R: restack
```

- merge position, branch, task id and title, task status and ACs;
- state, each with an icon and a word, never colour alone: **merged** into the default branch ·
  **next** (merging it is a fast-forward) · **waiting** · **needs restack** (its parent moved, or
  ancestry and trailer disagree) · **being built** (its worktree is dirty, or it has no commit
  of its own yet);
- commits and files ahead of its parent;
- worktree: folder name, locked, dirty;
- the task's Notes expand under the row (a disclosure, closed by default).

### What it does

- **Review**: `Enter` opens the Pull request mode with *base = the row's parent, head = the
  branch*, so the diff is only that task's change. `m` toggles the base between the parent and
  the default branch, there and back.
- **Merge next** (`M`): fast-forwards the default branch to the next branch in order. Offered only
  when it is a fast-forward, so it cannot conflict. Local only; nothing is pushed.
- **Restack** (`R`): rebases the children of a parent that moved onto it, one branch at a time in
  stack order, with `--update-refs`. It stops at the first conflict and hands it to the conflict
  layout the Pull request merge already uses; a stopped restack can be continued or aborted there.
  Before it starts, Ops tags the old tips (`pre-restack-<branch>`), so nothing can be lost.
- Every action answers with a short note, as the Pull request actions do.

### How live

The view **watches refs**: a file watcher on `.git/HEAD`, `.git/refs/`, `.git/packed-refs` and each
worktree's `HEAD` and `index`. When an agent commits, switches branch or rebases, the view
re-reads (debounced) and redraws only the rows that changed. No timer, no polling. The watcher is
the local backend's repository watcher (TASK-186), not a second one.

## Decided (2026-11-17, the user)

| question | answer |
|---|---|
| Where | a view in a new **History** mode, not a mode of its own and not inside Pull request |
| Source of the order | **both** ancestry and the `Stacked-On:` trailer; disagreement is shown |
| Which branches | **all local** branches |
| Review base | **toggle**: parent by default, `m` switches to the default branch |
| Actions | **merge next** (fast-forward only) and **restack** (stop at the first conflict) |
| Liveness | **watch refs** (file watcher), no timer |
| Agent information | **yes**, from the task file: status, ACs, Notes |

## Open questions

- The History mode's other view: a commit log (graph or flat), and which is shown first.
- Branches without a task or trailer (plain feature branches): one flat group, or by ancestry
  like the rest.
- Merging a whole stack at once (fast-forward to its tip) as well as "next".
- Whether restack also updates the `Stacked-On:` trailer of a commit whose parent changed
  (that rewrites the message; today the trailer keeps saying where it was built).
- Keys: `m` / `M` / `R` against the existing table (`M-…` is Alt); check for clashes.

## Impact

- New: `lib/ui/history_view.dart` (mode), `lib/ui/stack_view.dart`; `lib/state/stack.dart`
  (the model: branches, ancestry, trailers, worktrees, task link) with unit tests on fixture git
  output; ref changes from the repository watcher (TASK-186).
- Changed: mode rail and Alt+1 … Alt+9, Help key table, the Pull request mode (open with a given
  base and head, base toggle), the Tasks reader (look a task up by id).
- Git commands used: `for-each-ref`, `merge-base --is-ancestor`, `log --format=%(trailers…)`,
  `worktree list --porcelain`, `status --porcelain`, `merge --ff-only`, `rebase --update-refs`,
  `tag`. Nothing pushes.
- PLAN.md: a "History" section under Views (Modes), and the rail order.
