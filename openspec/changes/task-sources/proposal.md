# tasks from several sources

Status: Open proposal, not decided. Nothing is built for it yet.

## Why

Ops's Tasks mode reads two kinds of files today, and each has its own model in the code. A
Backlog.md task (`Task` in `lib/tasks/model.dart`) has front matter with an id, a status, a priority,
labels, dependencies and a milestone, and sections with checkboxes: Acceptance Criteria, Definition
of Done, Verify. An OpenSpec change (`Change`) has a proposal with a `Status:` line and a tasks.md
whose checkboxes are grouped into Build and Verify. The views, the auto status after a tick and the
planned Board mode each know both shapes and handle them separately.

That is fine for two sources that live in the same folder. It does not stretch to the next ones. A
team (see `team-planning`) keeps its work in GitHub issues or in Linear, not in markdown files next
to the code, and I want to see those in the same list, with the same filters, and change a status
from the same place. Adding a third and a fourth model to every view is the wrong way to get there.

So the goal is one task model in the UI, with sources behind it. The views show tasks; where a task
comes from is a detail of the source.

## The idea

A task is what the UI shows and edits: a title, a status, a priority, some labels, a body, and
checklists. A source (a provider) turns its own records into tasks and turns the user's edits back
into its own writes. Backlog.md is the first source and the reference: the model is shaped after
it, because it is what the Tasks mode already does well. OpenSpec tasks.md is the second, already
read today. GitHub issues and Linear are kept in mind now, so the model doesn't have to be broken
open again when they arrive, but they are not built in this change.

Each source says what it can do. Backlog.md can do everything: read, change the status and the
priority, tick a box, create a task. An OpenSpec tasks.md has no status of its own, only boxes. A
read-only GitHub source would show issues and offer nothing to edit. The UI hides or disables an
action the source can't do, instead of failing on it.

Status is the field that differs most between sources. Every source has its own names (Backlog.md's
To Do, In Progress, Needs Test, Done, Dropped; Linear's workflow states; GitHub's open and closed).
The UI keeps the source's name for display, and every status also maps to a small fixed set of
kinds, which is what filters, sorting, the Board's lanes and the auto status work with:

| kind        | Backlog.md (this repo) | OpenSpec tasks.md        | GitHub issue                 | Linear state type    |
|-------------|------------------------|--------------------------|------------------------------|----------------------|
| backlog     | -                      | -                        | -                            | backlog, triage      |
| todo        | To Do                  | no box ticked            | open                         | unstarted            |
| in progress | In Progress            | some boxes ticked        | open, with an "in progress" project field or label | started |
| review      | Needs Test             | Build ticked, Verify open | -                           | started (named review) |
| done        | Done                   | every box ticked         | closed (completed)           | completed            |
| dropped     | Dropped                | -                        | closed (not planned)         | canceled             |

The statuses a project uses stay in its own config (Backlog.md's `statuses` in
`backlog/config.yml`); only the mapping to a kind is new. A status with no mapping counts as todo.

Overlap is out of scope. The same work can show up twice, for example a Backlog.md task and the
GitHub issue it was copied from, or a change and the tasks that name it. This change does not merge
or hide duplicates; it only makes sure each task knows its source, so a later change can.

## Fields

The model, with Backlog.md as the reference. "Required" means every source must fill it.

| field        | required | Backlog.md            | OpenSpec tasks.md            | GitHub issue              | Linear issue               |
|--------------|----------|-----------------------|------------------------------|---------------------------|----------------------------|
| source       | yes      | `backlog`             | `openspec`                   | `github`                  | `linear`                   |
| id           | yes      | `TASK-142`            | change id, plus box number   | `nvimos/ops#12`           | `OPS-12`                   |
| title        | yes      | `title`               | the box's text               | title                     | title                      |
| status       | yes      | `status`              | from the box marks           | state (+ state reason)    | workflow state             |
| status kind  | yes      | mapped                | mapped                       | mapped                    | the state's type           |
| priority     | no       | `priority` (high, medium, low) | -                   | a label or a project field | 0 to 4 (none, urgent, high, medium, low) |
| labels       | no       | `labels`              | -                            | labels                    | labels                     |
| assignees    | no       | `assignee`            | -                            | assignees                 | assignee (one)             |
| milestone    | no       | `milestone`           | -                            | milestone                 | project or cycle           |
| dependencies | no       | `dependencies`        | -                            | sub-issues, "blocked by"  | relations (blocks)         |
| parent       | no       | -                     | the change                   | parent issue              | parent issue               |
| order        | no       | `ordinal`             | line in tasks.md             | -                         | sort order                 |
| created      | no       | `created_date`        | file time                    | created at                | created at                 |
| updated      | no       | file time             | file time                    | updated at                | updated at                 |
| body         | no       | Description           | -                            | body (markdown)           | description (markdown)     |
| checklists   | no       | Acceptance Criteria, Definition of Done, Verify | the box itself | task lists in the body | -          |
| link         | yes      | the file path         | the file and line            | the issue URL             | the issue URL              |
| change       | no       | the OpenSpec change it names | the change            | -                         | -                          |

Priority is a small fixed scale too: none, low, medium, high, urgent. Backlog.md has the middle
three; Linear has all five; GitHub has none of its own, so a source config names the labels or the
project field that stand for it.

Checklists keep their marks (open, x, in progress, partly, will not do), as the Tasks mode already
shows them. A source without those marks shows open and x only.

## How it fits in Ops

Today `Workspace` (`lib/tasks/workspace.dart`) loads the planning folder and builds `Task` and
`Change` objects from the files. In this change:

- a `TaskSource` interface: list the tasks, watch for changes, and the edits it supports (set
  status, set priority, tick a box, create), each returning an error string the way `edit()` does
  now
- what a source can do, as flags the views read (`canSetStatus`, `canTick`, `canCreate`, ...)
- `BacklogSource` wraps today's `Task` parsing and edits; `OpenSpecSource` turns a change's tasks.md
  boxes into tasks whose parent is the change
- the views (list, detail, filters, sorting) and the auto status after a tick work on the common
  model; the change detail (proposal, specs, deltas) stays a change view
- the status-kind mapping for Backlog.md lives next to `statuses` in the planning config, with the
  table above as the default

GitHub and Linear are only checked against the model on paper here: their fields fill the table
above without a new required field. Building them is a later change each, with its own questions
(auth, rate limits, offline, how often to fetch).

Today's link from a change to its task reads the first `TASK-n` on the proposal's `Status:` line
(`Change.taskId`). With changes split into several tasks (as `merge-beside-checkout` is now), the
link goes the other way too: a task names its change, and the change lists the tasks that name it.

## Open questions

- Is an OpenSpec box a task of its own, or only a checklist item of its change? As a task it gets a
  status and shows in the list; as a checklist it stays as it is now.
- Where does the status-kind mapping for a GitHub repo or a Linear team live: in the planning config
  of the repo that shows them, or in Ops's own settings?
- Do edits to a remote source (GitHub, Linear) go out at once, or are they queued and shown as
  pending?
- Should the Tasks mode show the source as a column, a filter, or only an icon?

## Impact

Ops (`nvimos/ops`): `lib/tasks/model.dart`, `parse.dart`, `workspace.dart`, `auto_status.dart` and
the Tasks views move to the common model. The planned Board mode (`kanban-board-mode`) uses status
kinds for its lanes. No change to the files on disk: Backlog.md tasks and OpenSpec changes are read
and written as they are now.
