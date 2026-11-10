Project: Nvim-backed GitHub Desktop clone for solo agent-review workflows
Build a Flutter desktop app (Windows first) that acts as a mouse-friendly GitHub Desktop–style UI for reviewing and navigating code changes. It talks to a running Neovim instance over msgpack-RPC and keeps a bidirectional sync with it.
Core use case

I’m reviewing work agents did overnight. I have two branches (e.g. main and agent/feature-xyz). I want to open a clean, GitHub-like view of the diff between them, click around with the mouse, inspect files, stage/unstage, and see the same state reflected live in my Neovim session (and vice versa). No real GitHub PR required — just two local branches.
Key requirements

Connect to Neovim
Attach to an existing Neovim instance via its msgpack-RPC socket (or spawn one).
Prefer a streaming structured-update API if available (see earlier nvim_ui_stream design); fall back to careful polling + autocommands for the POC.
Bidirectional: changes made in the Flutter UI (stage, discard, checkout, open file) are applied in Neovim; changes made in Neovim (edits, buffer switches, cursor moves) appear in the UI without manual refresh.

GitHub Desktop–style UI (minimal but polished)
Left sidebar: repository, branch selector, commit list / changed files.
Main area: file tree of the diff + side-by-side or unified diff viewer for the selected file.
“Pull request” view: treat two branches as base and head. Show the commit range and the aggregate file changes, styled like GitHub’s PR Files changed tab.
Mouse-first: clickable files, clickable hunks, buttons for stage/unstage/discard, drag-and-drop where it feels natural.
Keyboard optional, not required.

Most important features only
Open repo / switch branches.
View diff between two branches (or working tree vs HEAD).
Stage / unstage / discard individual files or hunks.
Open a file at a specific line in the connected Neovim instance.
Live refresh when the Neovim buffers or git state change.
Simple commit message + commit (optional for POC).

Architecture notes
Flutter desktop (Windows). Use the existing dart_nvim_api package or write a thin msgpack-RPC client.
Keep a local model of: open buffers, current buffer/cursor, git status, diff between the two selected branches.
On startup, snapshot the needed domains from Neovim, then subscribe to updates (or poll at a sensible rate for the POC).
All mutations go through Neovim (or through git commands executed in Neovim’s context) so there is a single source of truth.

Non-goals for the first version
Real GitHub API / actual pull requests.
Multi-repo or team features.
Full IDE editing inside Flutter (editing happens in Neovim).
Mobile or web.


Deliverable for the POC

A runnable Flutter Windows app that:

Connects to a Neovim instance that already has a repo open,
Lets me pick two branches,
Shows a GitHub-like file list + diff view,
Reflects buffer and git changes from Neovim within a second or two,
Lets me click a file/hunk and have Neovim jump to it.

Start with the connection + diff-between-two-branches view. Make the UI feel like a simplified GitHub PR Files tab, not a terminal.
