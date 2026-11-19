# project discovery from a directory crawler

Tags: integrate-purrage
Status: Open proposal, not decided, not to be implemented yet. Part 4 of 5 in the Purrage integration.
Tasks: TASK-171, TASK-172, TASK-173, TASK-174.

## Why

Ops' Directories mode is built from the genja-startdirs plugin: the backend asks the plugin for its
frecency list, or falls back to the directories of Neovim's recent files. That is useful, but it is a
list of hints, not a map of the repositories on the machine. A fresh folder, a checkout the plugin
has never seen, or a machine without the plugin produces a thin or empty list.

Purrage's Browse mode already has the better foundation: it walks a starting directory, recognises a
repository by its `.git` (folder or file), skips the trees that should never be walked, records what
it scanned, and lists the repositories it found. It does not need a plugin, and it works with no
editor running.

## The idea

Make the directory crawler the source of truth for project discovery, and demote start-dirs to a
hint source.

The crawler:

- starts from the connected Neovim's working directory; with no Neovim, from the last folder the
  user browsed, or home on a first run
- walks to a configurable depth, never following links
- treats a directory with a `.git` as a repository and does not walk into that repository's own
  subfolders looking for more
- has a skip list for build, cache and system trees, with a shallower rule for `AppData`
- reports visited, found, skipped, elapsed and the slowest/widest directories, for the console
- can be stopped and replaced by a newer scan

The hints:

- genja-startdirs' frecency list, when a Neovim backend is connected
- Neovim's recent-file directories as the fallback, as today
- the user's own recent projects from `Prefs` when no Neovim is connected
- the currently connected repository and the active directory, shown first

Hints do not replace the walk. They seed it, order its results, and put the likely repositories at
the top. A hint that is not a repository, or no longer exists, is shown greyed with a Remove button;
it is never dropped behind the user's back.

The existing Directories mode becomes the **Repos** mode, and its state a view over the crawler plus
the hints. Purrage's Browse view is folded into it: one view, not two. “Active Directory”,
“Open project” and the picker behaviour stay as they are.

## Scope

- Port Purrage's `RepoBrowser` and its scan report, skip list and depth setting.
- Add a hint layer over it: start-dirs/oldfiles when connected, `Prefs` when not, and the active
  repository.
- Merge the source of the Directories list: crawl results first, hints as ordering and seed.
- Keep the crawler in the state layer, testable with a fake directory lister.
- Keep the Neovim backend able to supply hints; it is not required for the crawl.

## Out of scope

- The Browse or Directories view. The UI is part 5.
- The local git backend and actions; parts 2 and 3.
- Fetching, cloning or creating repositories.
- Watching the filesystem for new repositories; a rescan is enough for now.

## Done when

- The crawler finds repositories under a folder with no Neovim running.
- Start-dirs and oldfiles order or seed the list when connected, but are not required.
- The active and connected repositories appear first.
- The Directories state can be driven by a fake lister in tests.
- A scan reports what it did, and a second scan replaces a running one cleanly.

## Decided (2026-11-19, the user)

| question | answer |
|---|---|
| Mode name | **Repos** |
| Browse view | **folded into Repos**: one view |
| Stale hint | **shown greyed** with a Remove button |
| Start directory | **the Neovim cwd** when connected; otherwise the last folder used, home on a first run |

## Open questions

None left for this part.
