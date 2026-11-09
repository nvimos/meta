# 17. publish the other plug-wip plugins (done 2026-11-05: 12 repos on...

Status: Done (backlog TASK-57)

## Why

17. publish the other plug-wip plugins (done 2026-11-05: 12 repos on...

each plug-wip folder is its own checkout, ignored by the nvim repo, 2492965)
- repos github.com/tox2ik/<folder name>, genja-util.nvim first; history kept with `git subtree split`
- genja-completion011.nvim keeps its name inside the config (unique, visible); only its repo is
  tox2ik/genja-completion.nvim (spec: name = the folder name, url = the repo)
- specs: local plug-wip dir when present, else the GitHub repo (as abdul-keymaps)
- gh 2.103.3 installed (winget); needs `gh auth login` before repos can be created

## What Changes

- (to be worked out)

## Impact

- Source: `todo-2026-neovim011.md`, section "release v2026"

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
