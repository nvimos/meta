Project: Nvim-backed GitHub Desktop clone for solo agent-review workflows

A Flutter desktop app (Windows first; Linux, Android and macOS later) that feels like GitHub Desktop
for reviewing and navigating code changes. A running Neovim is its backend: the app talks to it
over msgpack-RPC and stays in sync with it all the time.

Core use case

I'm reviewing work agents did overnight. I have two branches (e.g. main and agent/feature-xyz). I
want a clean, GitHub-like view of what changed between them, click around with the mouse, inspect
files, and jump into Neovim at the spot I'm looking at. No real GitHub PR required, just two local
revisions. Then I look at my own uncommitted work the same way and stage and commit it.

Modes

- Pull request: two revisions as base and head, their commits and the changed files, the diff of
  the selected file like GitHub's "Files changed" tab. Unified first, side-by-side later.
- Changes: the working tree against HEAD; stage, unstage and discard files or hunks; commit.
- Tasks: a Linear-style workspace over the repo's planning files (see `flutter-project-man.md`).
- Directories: pick which repo the other modes work on, from my usual start dirs.

Main ideas

- Neovim is the single source of truth. All git and file work goes through it; the app runs no
  git itself and never edits text. Editing happens in Neovim.
- Bidirectional and live: what I do in the app shows in Neovim, and what happens in Neovim (edits,
  buffer switches, cursor, git state) shows in the app within a second or two.
- Switching directories moves the connected Neovim there, or, if I want, starts a new Neovim per
  directory.
- Clicking a line opens it in Neovim, without stepping on unsaved work and without showing the
  wrong version of a file.
- Errors replace the thing that failed and can be read and copied in full.
- Mouse first, keyboard for everything too, in the spirit of vim.
- Dense, calm and polished, not a terminal.

Non-goals for the first version

- Real GitHub API / actual pull requests.
- Team features.
- Editing inside the app.
- Mobile or web.

`~/es/nvimos-poc-frontend/PLAN.md` holds the details and wins where it disagrees with this file.
