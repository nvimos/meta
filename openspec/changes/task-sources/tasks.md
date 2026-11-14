# Tasks

Only if the proposal is accepted.

## 1. Build

- [ ] 1.1 decide the open questions (OpenSpec box as task or checklist, where mappings live, remote edits, how the source shows)
- [ ] 1.2 the common task model: the fields, status kinds and priority scale above
- [ ] 1.3 the `TaskSource` interface with its capability flags and edits
- [ ] 1.4 `BacklogSource` from today's `Task` parsing and edits
- [ ] 1.5 `OpenSpecSource` from a change's tasks.md
- [ ] 1.6 the status-kind mapping next to `statuses` in the planning config, with the default table
- [ ] 1.7 the Tasks views, filters, sorting and auto status on the common model
- [ ] 1.8 a change lists the tasks that name it, not only the first `TASK-n` on its Status line
- [ ] 1.9 GitHub issues and Linear: fill the field table from their APIs on paper; note gaps
- [ ] 1.10 PLAN.md: the task model and the sources

## 2. Verify

- [ ] 2.1 the Tasks mode shows the same tasks, statuses and checklists as before the change
- [ ] 2.2 changing a status, a priority and ticking a box still write the same lines to the files
- [ ] 2.3 a source that can't set a status shows no status action
- [ ] 2.4 `merge-beside-checkout` lists TASK-143 to TASK-148
