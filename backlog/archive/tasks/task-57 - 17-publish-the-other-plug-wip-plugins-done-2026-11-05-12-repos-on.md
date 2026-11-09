---
id: TASK-57
title: '17. publish the other plug-wip plugins (done 2026-11-05: 12 repos on...'
status: Done
assignee: []
created_date: '2026-11-05'
labels:
  - todo-2026-neovim011
  - release-v2026
dependencies: []
ordinal: 57000
---

## Description

17. publish the other plug-wip plugins (done 2026-11-05: 12 repos on...

each plug-wip folder is its own checkout, ignored by the nvim repo, 2492965)
- repos github.com/tox2ik/<folder name>, genja-util.nvim first; history kept with `git subtree split`
- genja-completion011.nvim keeps its name inside the config (unique, visible); only its repo is
  tox2ik/genja-completion.nvim (spec: name = the folder name, url = the repo)
- specs: local plug-wip dir when present, else the GitHub repo (as abdul-keymaps)
- gh 2.103.3 installed (winget); needs `gh auth login` before repos can be created

From `todo-2026-neovim011.md`, section "release v2026".

## Original notes

```markdown
- [x] 17. publish the other plug-wip plugins (done 2026-11-05: 12 repos on github.com/tox2ik, MIT, READMEs with lazy install;
          each plug-wip folder is its own checkout, ignored by the nvim repo, 2492965)
          - repos github.com/tox2ik/<folder name>, genja-util.nvim first; history kept with `git subtree split`
          - genja-completion011.nvim keeps its name inside the config (unique, visible); only its repo is
            tox2ik/genja-completion.nvim (spec: name = the folder name, url = the repo)
          - specs: local plug-wip dir when present, else the GitHub repo (as abdul-keymaps)
          - gh 2.103.3 installed (winget); needs `gh auth login` before repos can be created
```
