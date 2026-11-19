# Tasks

## 1. The Stack view

- [ ] 1.1 `lib/state/stack.dart`: branches, ancestry, trailers, worktrees and the task link, with unit tests on fixture git output
- [ ] 1.2 the rows: state, order, commits ahead, worktree, task Notes
- [ ] 1.3 review against the parent, with the base toggle (`m`)

## 2. The actions

- [ ] 2.1 merge next, fast-forward only
- [ ] 2.2 restack with `--update-refs`, tagging the old tips first, stopping at the first conflict

## 3. Live

- [ ] 3.1 follow the repository watcher's refs signal (TASK-186), no timer
