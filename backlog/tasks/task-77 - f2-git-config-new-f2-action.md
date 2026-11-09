---
id: TASK-77
title: 'f2 git config (new f2 action)'
status: To Do
assignee: []
created_date: '2026-11-10'
labels:
  - todo-2027
  - f2-git-config
dependencies: []
ordinal: 77000
---

## Description

f2 git config (new f2 action)

- spec
  - no global handling
    - just go to homedir and run it there to set global
  - look for .gitconfig and .git/config
    - these trigger adding this action to f2
- idea: consider generating an explorer
  - it's a sub-picker
    - displayed as path in the telescope pickers, value also seen
    - loads known values / parameters from git.exe or docs
    - custom map to add to your file e.g. `<m-a>`
  - ui behavior; show
    - unset config values in gray
    - problematic values in red
    - custom values in magenta
    - defaults in green
- sub-item: select from config values
  - items:
    - upstream origin / branch
- sub-item: append settings
  - items:
    - add this dir as trusted
    - new remote
- sub-item: set needed options for git
  - items
    - email
    - name
- sub-item: toggle-cycle options
  - selecting item selects next and keeps ui open
        (currently active is indicated)
  - items
    - main branch name
      - cycle: master -> main -> trunk
      - input: a custom name
    - item: switch line endings
      - cycle: crlf -> lf -> auto

From `todo-2027.md`, section "f2 git config".

## Original notes

```markdown
- [ ] f2 git config (new f2 action)
  - spec
    - no global handling
      - just go to homedir and run it there to set global
    - look for .gitconfig and .git/config
      - these trigger adding this action to f2
  - idea: consider generating an explorer
    - it's a sub-picker
      - displayed as path in the telescope pickers, value also seen
      - loads known values / parameters from git.exe or docs
      - custom map to add to your file e.g. `<m-a>`
    - ui behavior; show
      - unset config values in gray
      - problematic values in red
      - custom values in magenta
      - defaults in green
  - sub-item: select from config values
    - items:
      - upstream origin / branch
  - sub-item: append settings
    - items:
      - add this dir as trusted
      - new remote
  - sub-item: set needed options for git
    - items
      - email
      - name
  - sub-item: toggle-cycle options
    - selecting item selects next and keeps ui open
          (currently active is indicated)
    - items
      - main branch name
        - cycle: master -> main -> trunk
        - input: a custom name
      - item: switch line endings
        - cycle: crlf -> lf -> auto
```
