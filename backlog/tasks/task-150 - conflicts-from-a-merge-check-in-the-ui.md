---
id: TASK-150
title: 'show the files that would conflict in the merge with another branch'
status: To Do
assignee: []
created_date: '2026-11-15'
labels:
  - frontend
dependencies: []
ordinal: 150000
---

## Description

Ops should show, in the UI, which files would conflict if the current branch merged another branch,
and keep those files out of the normal file lists (they cannot be staged or committed cleanly until
the merge is done). The check must not touch the working tree or the index: a real `git merge
--no-commit` changes the checkout, and its `--abort` path only runs on failure, so a clean merge
would be left in progress. Use `git merge-tree --write-tree --name-only --messages <base> <other>`
(read-only), and parse its conflicted-file output.

The check runs when the user picks the branch to merge (Changes or Pull request), and its result
is shown where the file lists are, as a separate "Conflicts" group that the stage and unstage keys
skip.

## Acceptance Criteria

- [ ] #1 the conflicting paths come from `git merge-tree --write-tree --name-only`, with no merge started
- [ ] #2 no working-tree or index change happens during the check
- [ ] #3 the conflicting files show in a "Conflicts" group, not in the STAGED or CHANGES lists
- [ ] #4 stage, unstage and discard keys skip the files in that group
- [ ] #5 the group is empty and hidden when the merge is clean
- [ ] #6 a failed check (no such branch, git error) shows the error text and leaves the lists as they were
