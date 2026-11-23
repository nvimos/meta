---
id: TASK-205
title: 'security posture for untrusted repositories'
status: To Do
assignee: []
created_date: '2026-11-23'
labels:
  - ops
  - security
dependencies: []
ordinal: 205000
---

## Description

ops: make the app safe on input it does not own. A repository is data plus prose plus a `.git`
directory, and today the app can execute from all three: the New change agent writes with
`acceptEdits` after reading repo prose, rendered markdown hands any URI scheme to Explorer, four call
sites start through `cmd /c start`, git reads hooks and exec-capable config, and the relay is an
unauthenticated TCP API that reaches `nvim_exec_lua`. The change defines the threat model, hardens
the git and shell doors, contains paths, makes the agent draft instead of write, and refuses a
non-loopback relay unless the user says so out loud. P1 findings (release signing, log retention,
PDF sandboxing, named pipe) are named follow-ups, not this task.

Change: `openspec/changes/ops-security-posture/`

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 a hostile fixture (exec-capable `.git/config`, a hook, six link shapes, a junction, `a & b`, an outside `.nvimos`) is opened, diffed and committed without running its code or touching outside the repo
- [ ] #2 rendered links: only `http`, `https` and `mailto` reach the shell; unknown schemes and UNC paths do not
- [ ] #3 no `cmd /c start` remains; a folder named `a & b` starts only the editor
- [ ] #4 the agent drafts read-only and the app writes only the change directory and its task file; `.git/**` is refused
- [ ] #5 `:NvimosServe 0.0.0.0:6666` refuses without `!`; the app will not store a remote address and says it is unencrypted
- [ ] #6 discard honours the trash setting; writes and deletes are contained by `resolveInside`
- [ ] #7 `SECURITY.md` and a Help Security group exist; `make test` and `flutter analyze` pass
<!-- AC:END -->
