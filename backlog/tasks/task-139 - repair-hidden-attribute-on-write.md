---
id: TASK-139
title: 'write: repair the Windows Hidden attribute before a write'
status: Needs Test
assignee: []
created_date: '2026-11-12'
labels:
  - nvim-config
  - issue
  - windows
dependencies: []
ordinal: 139000
---

## Description

write: a file with the Windows Hidden attribute made `:w` fail with E212. `plugin/hidden-write.lua` clears
the attribute, writes, and sets it again; only a failed repair is reported.
Commits: config cda1a33. Found in another session; filed here with its commit.

## Acceptance Criteria

- [x] #1 `plugin/hidden-write.lua`: reads the attribute with GetFileAttributesW, `attrib -H` before the
  write, `attrib +H` after it (also when the write fails)
- [x] #2 `CLAUDE.md`: `### No useless messages`: repair at the point of use, notify only when it fails

## Verify

- [ ] test: `attrib +H` on a file, edit and `:w` it in nvim: the write works, the file is Hidden again after
- [ ] test: a normal file: `:w` is as fast as before and prints nothing extra

## Notes

- Not written in this session; the verify steps come from the plugin's header.
