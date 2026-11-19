# Tasks

## 1. Build

- [ ] 1.1 pick the task id format; new tasks use it, old numbers stay
- [ ] 1.2 generate `index.tsv` from the task headers, or drop it and update the scan tools
- [ ] 1.3 backend: pull, commit and push in the planning folder
- [ ] 1.4 frontend: sync action and the ahead/behind status
- [ ] 1.5 frontend: take a task (assignee, In Progress, commit, push); a rejected push pulls and says who
- [ ] 1.6 frontend: assignee on the row and in the detail panel, "mine" filter
- [ ] 1.7 status edits go to the planning repo's default branch only
- [ ] 1.8 README: setting up a teammate on a stock Neovim

## 2. Verify

- [ ] 2.1 two clones each create a task offline, then both sync: two different ids, no conflict
- [ ] 2.2 two clones change the status of different tasks, then both sync: no conflict
- [ ] 2.3 two clones take the same task: the second sees who has it
- [ ] 2.4 a teammate's edit shows on the other board after one sync
