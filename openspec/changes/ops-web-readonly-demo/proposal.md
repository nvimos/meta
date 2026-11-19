# Ops on the web: a demo that runs in the browser

Status: Open proposal, not decided. Draft for discussion; the open questions at the end need
answers before anything is built.

## Why

Showing Ops to someone today means they install a Windows app, clone a repo and maybe start
Neovim. That is a lot to ask from someone who only wants to see what it looks like. A link they
can open in a browser, with no install and nothing to set up, is a much easier first step.

Flutter builds for the web, and the app is already split where it needs to be: every mode talks to
git through one interface, `RepoBackend`, and the Tasks mode gets its files through it too. The
desktop app implements that interface by running `git`. A web build can implement it a second
time, as a fake repo that lives in the browser.

The web version is a demo, not a second product. It does not need to be perfect, and it never
touches a real repo. It shows the real UI, with real planning data, and lets a visitor click
through everything: stage a hunk, commit, merge a branch with conflicts, ignore a folder, tick a
box on a task. All of that is mocked: the changes are kept in the browser's storage and go nowhere
else.

## The idea

The demo is a static website: the Ops web build plus its data, served from GitHub Pages or any
other static host. There is no server.

It starts from two things baked into the site when it is built:

- a small demo repo, exported to JSON: its files, commits and branches, with one branch that
  conflicts on purpose so the Merge view has something to show
- a snapshot of this project's planning (`backlog/` and `openspec/` from `nvimos/meta`), so the
  Tasks mode shows the real tasks and changes

Whatever the visitor does goes into a layer on top of that starting point, saved in the browser's
`localStorage`. Reloading the page keeps it; a "Reset demo" button throws it away and starts over.
Nothing is ever written to GitHub or any other remote, and the "read-only" in the name means
exactly that: the real repos are only read, never changed.

The modes that need a real computer are left out of the web build: Neovim, the terminals, the file
manager, the external editors, "open in editor". The modes that work on a repo (Pull request,
Changes, Add and Ignore, Repos, Tasks, History, Help) all run against the fake repo.

A banner (or a mark in the status bar) says this is a demo whose changes stay in this browser, and
links to the release page for the real app.

Later, the same build could open other repos: a visitor pastes a GitHub URL and the demo reads
that repo's planning and files instead of the baked-in ones. That is a second step and not part of
the first version; see the open questions.

## Use cases

**A link in a message.** I send Erik a link. He opens it on his work laptop, where he can't
install anything. Ops appears in the browser with the Tasks mode open: our real backlog, task 196
in To Do, the ignore panes in progress. He opens a change and reads its proposal. (The baked-in
planning snapshot.)

**Trying the git modes.** Erik switches to Changes. There are a few modified files in the demo
repo. He stages one hunk, writes a commit message and commits. The commit shows up in Pull
request's commit list. (The fake repo and its browser layer.)

**A merge with conflicts.** He picks the `feature/rename` branch and merges it. Two files
conflict; the Merge view lights up, he picks a side for each hunk and finishes the merge. (The
three-way merge in Dart, and the branch that conflicts on purpose.)

**Starting over.** Erik's colleague Nora opens the same link in the same browser the next day and
sees Erik's commit. She clicks Reset demo and gets the repo as it was. (The layer in
`localStorage`, and the reset.)

**What isn't there.** Nora looks for the Neovim connection. The web build doesn't show it; the
banner says the full app has it and links to the download. (Desktop-only parts left out.)

## Technical notes

### What the code allows today

- `lib/tasks/` uses no `dart:io`: the Tasks workspace already reads through `RepoBackend.listFiles`
  and `readFiles`
- 26 files under `lib/` import `dart:io`: all of `lib/local/`, `lib/rpc/client.dart`,
  `lib/main.dart`, and in the shell's path `state/session.dart`, `state/prefs.dart`,
  `state/repos.dart`, `state/preview.dart`, `state/nvim_launcher.dart`, `timing/ui_timing.dart`,
  `ui/preview_pane.dart` and a few more
- `RepoBackend` (`lib/backend/repo_backend.dart`) has 47 methods: branches, log, diff, status,
  stage / unstage / discard per file and per hunk, checkout, merge, rebase, commit, the merge
  steps (`mergePreflight`, `mergeStart`, `mergeHunks`, `mergePick`, `mergeFinish`, `mergeAbort`),
  `listFiles`, `readFiles`, `setLines`, `move`, and more
- the local backend runs `git` and parses its output (`lib/local/local_backend.dart`,
  `diff_parse.dart`, `git_repo.dart`); Add and Ignore uses `git check-ignore -v`
- the `git` package in `pubspec.yaml` runs processes and must not be imported by the web build

### The web entry point

- `lib/main_web.dart`, built with `flutter build web -t lib/main_web.dart`
- it never imports `lib/local/` or `lib/rpc/`; a test (or an analyzer rule) checks that nothing in
  its import graph pulls in `dart:io`
- the shell parts that touch `dart:io` get web-safe versions behind conditional imports
  (`if (dart.library.js_interop)`): prefs in `localStorage`, `UiTiming` without files, a session
  that has no Neovim
- the mode list is filtered: modes that only make sense on a desktop are not shown
- PDF stays off (it is off by default already)

### The fake repo (`DemoBackend`)

- implements `RepoBackend` in plain Dart, so it also runs on the desktop and in tests
- the repo state: a map of files for HEAD, the index and the working tree; commits are snapshots
  (a parent, a message, an author, a time, the file map); branches are names pointing at commits
- status: compare working tree with index, index with HEAD
- diffs: a line diff (Myers) gives the hunks; staging a hunk applies it to the index, discarding
  it applies it backwards to the working tree
- log and checkout follow commit parents and swap the file maps
- merge: a line-based three-way merge (diff3) against the common ancestor; overlapping changes
  become conflicts in the `ConflictHunk` shape the Merge view already reads
- rebase: replay commits one by one with the same merge, or leave it out at first
- Add and Ignore: `.gitignore` matching in Dart (a pub package if a good one exists, else about 150
  lines), returning what `git check-ignore -v` returns: the file, the rule, its line
- `setLines` and `move` change the working tree, so task edits and file renames work
- the layer: every change is a small event or a new state saved under one key in `localStorage`
  (JSON); the starting point comes from the baked-in JSON; Reset deletes the key
- `localStorage` holds about 5 MB per site; the demo repo must stay well under it, or the layer
  moves to IndexedDB

### Baking the data

- a tool (`tool/demo_export.dart`, run in CI) exports a real git repo to the JSON the fake reads:
  the commits of chosen branches, their file maps (deduplicated by content hash), the authors
- the planning snapshot: `backlog/` and `openspec/` from `nvimos/meta` `main`, the same files the
  `tracking-remote-snapshot` change fetches, stored as the tracking folder of the demo repo
- both are assets of the web build, loaded at start

### Hosting

- static files only: `index.html`, `main.dart.js` or the wasm build, the renderer, the assets
- GitHub Pages is enough: build with `--base-href /<repo>/` when served from a subpath; use hash
  URLs so no 404 routing is needed
- GitHub Pages can't set response headers; the multithreaded wasm renderer needs COOP/COEP, so it
  runs single-threaded there. Cloudflare Pages or Netlify can set the headers if that matters
- first load is about 2 to 3 MB for the renderer and the app, plus the data
- a GitHub Action builds and publishes on every push to `main` of ops, and on a push to
  `nvimos/meta` (or nightly) for fresh planning

### Tests

- `DemoBackend` gets unit tests per operation, the same way the local backend has them
- the existing widget tests could run against `DemoBackend` instead of real git where they only
  need a repo; that would make them faster and keep them inside the fake clock
- one smoke test builds the web target in CI

## Relation to other changes

- `tracking-remote-snapshot`: same planning data, same read-only view of a remote repo; the web
  demo bakes in what the desktop app would fetch
- `purrage-backend-seam` and `purrage-local-git-backend`: the backend seam the fake plugs into
- `bootstrap-and-ci`: the CI the web build and its publishing go into

## Open questions

1. **Read-only or mocked writes?** The name says read-only; the plan above mocks every write in
   the browser. Is "read-only" about the real repos only, or should the first version really be
   read-only (Tasks and diffs to look at, no stage, commit or merge) and the mocked writes come
   second?
2. **Which repo is the demo repo?** ops itself (big, real history, real meta), a slice of it, or a
   small made-up repo with a story (a few commits, a feature branch, a conflict)? A made-up one is
   predictable and small; ops itself is more convincing.
3. **Whose planning?** This project's real `nvimos/meta`, or a made-up backlog that matches the
   demo repo? The real one shows real work but has nothing to do with a made-up demo repo.
4. **Any GitHub URL, when?** Should a visitor be able to paste a GitHub URL in the first version?
   Reading a repo from the browser: one GitHub API call
   (`/repos/<o>/<r>/git/trees/<ref>?recursive=1`) lists the files, each file comes from
   `raw.githubusercontent.com`; both allow requests from other sites. The zip download
   (`codeload.github.com`) probably doesn't. Without a login the API allows 60 calls an hour per
   visitor. Git history (commits, branches) for the git modes would need many more calls; is the
   URL feature Tasks-only?
5. **Other git hosts.** A browser can't speak the git protocol to an arbitrary server without a
   CORS proxy (what isomorphic-git uses). That means running a server. Later, or never?
6. **Dart fake or isomorphic-git?** The plan uses a fake written in Dart (deterministic, no
   JavaScript bridge, doubles as a test fake). isomorphic-git would be real git in the browser,
   but has no `check-ignore -v`, limited conflict handling, and needs its own adapter to our
   models anyway. Agreed on Dart?
7. **How much of git is faked?** Rebase, stash, discard of untracked files, renames: which are in
   the first version, and which buttons are hidden or show "not in the demo"?
8. **Which modes are in?** Pull request, Changes, Add and Ignore, Repos, Tasks, History, Help seem
   to fit. Does Repos make sense with one demo repo, or should the demo ship two or three repos?
9. **localStorage or sessionStorage?** localStorage keeps a visitor's work across reloads and
   visits; sessionStorage forgets it when the tab closes, so every visit starts clean. Which is the
   better demo? Should the layer have a version, so a new site build drops an old layer that no
   longer fits the new starting point?
10. **Where is it hosted, and under what address?** GitHub Pages of `nvimos/ops`
    (`nvimos.github.io/ops`), a separate `nvimos/demo` repo, or an own domain? Wasm or the JS
    build?
11. **Is the web entry point worth the shell changes?** The conditional imports touch session,
    prefs and timing. Is that acceptable in the main code, or should the web shell be a separate
    thin app that reuses the views?
12. **Banner and links.** What does the demo banner say, and where does it link (releases page,
    README, a landing page)?
13. **Analytics.** Do we want to know how many people open the demo? GitHub Pages has none; adding
    a tracker brings a cookie banner. Probably no.
14. **Keys in the browser.** Some app-wide keys (Alt+1..9, Ctrl+B) may be taken by the browser.
    Which ones collide, and do they need web alternatives?
15. **Size of the work.** Rough guess: one to two weeks, most of it the three-way merge and the
    ignore matching. Is that worth it now, or after the release and CI work?
