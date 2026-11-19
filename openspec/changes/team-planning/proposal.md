# team planning for 5-7 people

Status: To Do (backlog TASK-122)

## Why

The Tasks mode and the planning folder are built for one person: "Multiple users" is a non-goal of
the first version (`poc-nvim-backend/flutter-project-man.md`). A team of 5 to 7 sharing one planning
repo over git would hit these, worst first:

- duplicate task numbers: a new task takes the highest local number plus one, so two people who
  create a task before pulling both get the same number; the file names differ by slug, git merges
  both without a conflict, and two tasks share one id
- `index.tsv`: every status change writes a row in this one shared file, and edits to nearby rows
  land in the same merge hunk; it repeats what the task headers already hold
- no sync: the app writes through Neovim buffers, `auto_commit` is off and nothing pulls or pushes
  the planning repo, so each person's board is as old as their last manual pull
- the "file changed meanwhile" check in the edits only sees local changes, not a teammate's
- no ownership: `assignee` is written as `[]` and never shown or set, so two people can start the
  same task without knowing
- task status edited on agent branches only shows on the board after the branch is merged

Editing the same task is the smallest of these: a status is one header line and checkboxes on
different lines merge cleanly.

## What Changes

- task ids that can't collide between clones, readable in a list (a short random or time-based
  suffix, or the author's initials), the existing numbers kept as they are
- `index.tsv` generated from the task headers, or dropped; never edited by hand or by the app
- sync of the planning folder from the app: pull with rebase, commit the app's own edits, push;
  a status that shows how far behind or ahead the planning repo is
- taking a task: assignee from `git config user.name`, status In Progress, committed and pushed
  at once; a rejected push means someone was first, so the app pulls and shows who
- the assignee on the list row and in the detail panel; a "mine" filter
- task status always written in the planning repo on its default branch, never on a code branch
- a start for a teammate: the backend plugin on a stock Neovim, a clean planning repo without this
  config's history

## Impact

- frontend: `lib/tasks/workspace.dart` (task ids, the index, sync, take), `lib/tasks/edits.dart`,
  `lib/ui/tasks/` (assignee, "mine" filter, sync status), the keys in `PLAN.md`
- backend: git commands in the planning folder (`tracking.lua`), pull and push
- nvimos-meta: the task id format, `index.tsv`, `README.md`, the `planning` spec
