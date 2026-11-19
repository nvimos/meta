---
id: TASK-152
title: 'add refuses files with conflict markers; verify before the merge commit'
status: To Do
assignee: []
created_date: '2026-11-15'
labels:
  - backend
  - frontend
dependencies:
  - TASK-151
ordinal: 152000
---

## Description

The add action in the conflict view refuses a file that still has a line starting with `<<<<<<<`,
`=======` or `>>>>>>>`. The error names the file and the first marker line, and the file stays
unresolved. Before the commit that completes the merge, a verify step checks that no unmerged path
remains (`git diff --name-only --diff-filter=U` is empty) and that no staged file has a marker. Tests
and analysis are optional, not a gate. A failed verify refuses the commit, names the files, and leaves
base where it is.

Change: `openspec/changes/merge-conflict-view/` ("Add refuses a file with conflict markers", "The verify
step before the commit").

## Acceptance Criteria

- [ ] #1 add on a file with a marker line at its start is refused; the error names the file and line
- [ ] #2 a marker in the middle of a line (not at its start) does not block add
- [ ] #3 verify refuses the commit while an unmerged path or a marker is left; base does not move
- [ ] #4 a CRLF file with markers is detected the same way as an LF file

## Verify (by hand)

- [ ] #V1 leave `<<<<<<<` in `PLAN.md`, click add: refused, error names `PLAN.md` and the line
- [ ] #V2 remove the marker, click add: accepted; verify passes when the last file is added
- [ ] #V3 with one file still unresolved, the commit is refused and `main` has not moved
