# planning from a remote repo when there is no local checkout

Status: Open proposal, not decided. Nothing is built for it yet.

## Why

Some projects keep their planning in a separate repo: the Backlog.md tasks and the OpenSpec changes
live in a meta repo, and each code repo has a committed `.nvimos` file whose `tracking` line points
to a local checkout of it (`tracking = ../nvimos-meta/`). That works on my machine, where both
repos sit side by side. It does not work for anyone else.

Someone who downloads Ops and clones only the code repo opens it and sees an empty Tasks mode. The
`.nvimos` file names a folder that isn't there, and nothing tells them where the planning actually
lives or how to get it. To see what is in progress they would have to know that a meta repo exists,
find it, clone it next to the code repo under exactly the right name, and reopen. Nobody does that.

The first case is a demo: I want to show Ops to someone on their machine or a fresh one, clone the
code repo, open it, and have the Tasks mode full of real tasks right away. But it is also a plain
useful feature: a contributor who only works on the code still wants to see what is planned and
what is being worked on, without setting up a second repo they will never write to.

## The idea

The `.nvimos` file gets a second line that names the planning repo on GitHub, next to the local
path:

```
tracking = ../nvimos-meta/
tracking_remote = nvimos/meta
project = frontend
```

When Ops opens a repo, it looks for the planning in this order:

1. the local `tracking` folder, if it exists: the normal case, nothing changes
2. otherwise, if `tracking_remote` is set, a snapshot of that repo's `main`, which Ops fetches as an
   archive and keeps in its own local state
3. otherwise, the repo root, as today

The snapshot is perishable. It lives in Ops's cache folder, not next to the code, nobody edits it,
and Ops may delete and fetch it again at any time. It is a read-only window on the planning as it
is on `main`: the tasks, their status, the OpenSpec changes, the progress of their boxes.

Because it is read-only, the Tasks mode shows it as such. A bar at the top says where the tasks come
from and how old the snapshot is ("snapshot of nvimos/meta main, fetched 12 minutes ago"), with a
Refresh button. Status changes, priority changes and ticking boxes are disabled with a tooltip that
says why: an edit to the snapshot would be lost on the next fetch and never reach the team. The bar
also offers to clone the planning repo to the `tracking` path for someone who does want to edit;
after the clone the local folder wins and the snapshot is no longer used.

Ops fetches the snapshot without being asked: the first time a repo with `tracking_remote` and no
local folder is opened, and again when it is opened later and the snapshot is older than an hour.
Opening never waits for the network: an existing snapshot shows at once and is replaced when the
new one arrives; with no snapshot yet, the Tasks mode shows a loading state. When the fetch fails
(offline, rate limit, a private repo without access) an old snapshot stays in use with its age in
the bar; with none, the Tasks mode says it could not fetch the planning and why, with a Retry.

## Use cases

**Showing Ops to someone.** I sit down at Kari's laptop, install Ops from the release page, and
clone `nvimos/ops`. I open it in Ops and switch to Tasks. For a second it says it is fetching the
planning from nvimos/meta, then the list fills: task 194 "ops PDF preview" in To Do, the ignore
panes in progress, the board change as a proposal. I click through them, open a change, show its
boxes. Nothing to configure. (The `tracking_remote` line and the snapshot do all of it.)

**A contributor who only codes.** Ola clones the frontend to fix a bug he found. He wants to know
whether someone is already on it. He opens the Tasks mode, filters on "frontend", and finds the
task, In Progress, with a branch name. He tries to change its priority and the control is greyed
out: "read-only snapshot of nvimos/meta; clone it to edit". He doesn't need to. (The read-only
snapshot and its bar.)

**Working offline.** On the train, Ola opens the repo again. The fetch fails; the bar says
"snapshot from yesterday 14:20, could not refresh: offline", and the tasks are there. (The old
snapshot stays until a new one arrives.)

**Becoming a planner.** Kari decides to help with the planning. She clicks "Clone to
../nvimos-meta/" in the bar. Ops clones the repo, the bar disappears, and her edits now go into
her checkout like mine do. The snapshot is deleted. (The local folder wins over the snapshot.)

## Technical notes

- `.nvimos` key
  - `tracking_remote = <owner>/<repo>` for GitHub; a full `https://github.com/<owner>/<repo>` is
    accepted too
  - optional `tracking_ref = <branch>` for a branch other than `main`; the default is the repo's
    `main`
  - unknown keys are already ignored by today's reader, so old Ops versions are unaffected
- fetch
  - `https://codeload.github.com/<owner>/<repo>/zip/refs/heads/<ref>` (what
    `github.com/<owner>/<repo>/archive/refs/heads/<ref>.zip` redirects to); no API token for a
    public repo
  - a private repo: if `gh auth token` gives a token, send it as `Authorization: Bearer` to the API
    zipball endpoint (`https://api.github.com/repos/<owner>/<repo>/zipball/<ref>`); otherwise the
    failure message says the repo is private or missing and suggests cloning it
  - keep the response's `ETag` and send `If-None-Match` on the next fetch, so an unchanged repo
    costs a 304 and no download
  - the first version only needs GitHub; the key's value is shaped so another host can be added
    later
- where it lives
  - `%LOCALAPPDATA%\nvimos\ops\tracking\<owner>\<repo>\<ref>\` with the extracted tree and a
    `snapshot.json` (fetched at, ETag, commit sha from the archive's top folder name)
  - extract into a new temp folder next to it, then swap the folders, so a crash mid-extract never
    leaves a half snapshot in use
  - it is a cache: deleting the folder is always safe
- the archive is untrusted data
  - extract only what the Tasks mode reads: `backlog/` and `openspec/` (`.md`, `.yml`, `.yaml`)
  - reject entries with `..`, absolute paths or links; cap the archive size and the file count
  - nothing in it is run
- reading
  - the snapshot folder is handed to the same task loader as a local tracking folder, with a
    read-only flag on the `Tracking` (`lib/tasks/workspace.dart`)
  - the workspace exposes the source (local folder or snapshot, its age, the last fetch error) for
    the bar
  - edit actions check the flag in the state class, not only in the widgets, so a key binding
    can't write to the snapshot either
  - with the relay backend, the backend's `tracking.lua` still resolves a local folder; the snapshot
    is an Ops-side fallback used only when that resolves to nothing
- clone
  - "Clone to <tracking>" runs `git clone https://github.com/<owner>/<repo> <tracking path>` and
    reloads the workspace; the snapshot folder is removed afterwards
- tests
  - a local zip served from a test HTTP server (no network in tests); the cache root goes through
    `keepForCleanup`
  - order of precedence, read-only edits refused, a 304 keeps the snapshot, a failed fetch keeps
    the old snapshot, a hostile archive (`..`, a link) extracts nothing outside the folder

## Out of scope

- writing back to the remote (issues, pull requests to the meta repo from the snapshot)
- other hosts than GitHub
- planning repos that need more than `backlog/` and `openspec/`
