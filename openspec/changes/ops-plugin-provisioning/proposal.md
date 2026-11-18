# provision the relay plugin on first run

Status: Open proposal, not decided, not to be implemented yet. There is no backlog task yet; one gets
made if we go ahead.

## Why

Ops offers to start Neovim from the Connect screen, but the offer only works when relay can be found.
Today `findBackendDir` checks `NVIMOS_BACKEND`, then a `relay` or `nvimos-poc-backend` checkout next
to the app, and otherwise starts Neovim with `-c NvimosServe` and trusts the user's own config to
provide relay. A default Neovim install has no relay, and plain `nvim` does not put it on
`runtimepath`. So on a machine without the author's setup, ops starts Neovim and then cannot attach:
the first experience is a Connect screen that promises something it cannot deliver.

There is a second inconsistency behind the same gap. The Connect screen resolves the plugin from the
filesystem, while Directories' New Neovim per directory asks an already-connected Neovim for
`plugin_root()` and then calls a separate launcher in `dirs.dart`. That path cannot bootstrap; it only
works because another Neovim is already running with the plugin.

## The idea

Give ops its own copy of relay, and make every start go through one resolver and one launcher.

The round on 2026-11-18 settled these choices:

- when no local plugin can be found, download relay into `%APPDATA%/nvimos/plugin` and start Neovim
  with that copy
- search order: `NVIMOS_BACKEND`, then a local checkout, then the managed download; the user's own
  config is the last fallback, not the first
- download the archive of `nvimos/relay` `main`, newest first
- refresh the managed copy when it is older than six hours; if the refresh fails, keep the existing
  copy
- if no managed copy exists and the download fails, fall back to `:NvimosServe` in the user's config
- ship a known relay plugin inside the installer, so an offline first run has something to seed the
  managed folder with, and refresh it from downloads afterwards
- when `nvim` is not on PATH either, offer to download a portable Neovim into the app state folder
- unify the Connect-screen launcher and the Directories launcher into one implementation

The state folder would hold the managed plugin, the portable Neovim and the fetch metadata:

```
%APPDATA%/nvimos/
  state.json
  plugin/       relay checkout: plugin/nvimos.lua, lua/nvimos/...
  nvim/         portable Neovim (bin/nvim.exe, runtime/...)
  plugin.json   fetchedAt, source, revision, API version
```

The resolution order becomes:

```
NVIMOS_BACKEND
  > local checkout (relay or nvimos-poc-backend next to the app)
    > %APPDATA%/nvimos/plugin (managed download)
      > NvimosServe in the user's config
        > error with setup steps
```

The bundled plugin seeds the managed folder on first start if it is missing, so first run needs no
network. A stale managed copy is refreshed atomically: fetch into a sibling temp folder, check for
`plugin/nvimos.lua`, rename into place, and keep the old copy on any failure.

One function then owns the whole start: resolve the plugin, choose the executable (system Neovim or
the portable one), build the command line for console, nvim-qt or headless, set the working
directory, launch, and poll the address. The Connect screen calls it with an address; Directories
calls it with a directory and a fresh port. `DirsState.launch` can stay as the test seam but should
delegate to the same implementation.

First run, in order: no `nvim` gets the portable download offer; no plugin gets the bundled seed or
the download; Neovim starts with the resolved plugin on `runtimepath`; the app connects and shows the
opening mode; the managed copy is refreshed in the background when it turns six hours old.

## A simpler shape (added later, not decided)

Most of the complexity above comes from treating the plugin as something the app acquires at runtime.
Relay is about 126 KB of Lua across 33 files, and its API is coupled to the app (`Backend.apiVersion`
is `1`). It is not a large third-party dependency; it is part of the product, so its lifecycle could
match the app's lifecycle.

That would replace the download, refresh, bundle/seed and API-skew decisions with:

- embed relay in ops as Flutter assets; copy them to a state folder on startup, overwriting every
  time (126 KB is nothing), with no `plugin.json`, timestamps or version folders
- resolve the plugin in two cases only: `NVIMOS_BACKEND` when set (the developer override), otherwise
  the embedded copy
- drop the GitHub download and the archive of `main`, the six-hour refresh, the bundle-vs-download
  split and the seeding step, the checksums and atomic replace, the stale-copy handling, the
  `NvimosServe` fallback, and the sibling checkout search
- drop the portable Neovim download for now: show that Neovim is missing, link to an install, and
  retry. The people this app is for already run Neovim; bundling or downloading an editor is a
  bigger decision and a larger maintenance surface, and can be revisited if first-run feedback says
  missing `nvim` is common
- keep the one-launcher refactor: it is independent of provisioning and small

The trade-off is that plugin fixes ship with an ops release instead of instantly. Given the API
handshake, that is arguably correct: a newer `main` plugin can break an older app, which is the risk
the download design spends the most words on. The installer would grow by about 126 KB.

The state-folder path and the resolution order in the two ideas above are not settled; the simpler
shape would make most of those paths unnecessary. In short: embedded plugin, system Neovim, one
launcher, no downloader.

## Open questions

- `main` can bump the plugin API before the app expects it. The handshake already rejects a
  mismatch; should the app then prefer the bundled or previous known-good copy instead of retrying
  the same broken download? Otherwise a bad download can strand the app.
- the portable Neovim needs a source and a version policy (stable, latest, pinned per ops release),
  and it must not silently override a working system Neovim
- the archive of `main` has no release-level checksum; is recording the resolved commit and refusing
  to replace a working copy with one that fails to load enough?
- how the bundled plugin is wired into the installer, and whether it makes the installer too large
- the Connect screen currently shows commands to start Neovim by hand; should it say which plugin
  copy will be used and whether a refresh is in flight?

## Checkout path (done)

The launcher now recognizes the current relay repo name first when it searches for a checkout:
`nvimos-relay`, then the older `relay` and `nvimos-poc-backend` names. The folder still has to be a
sibling of the app or one of its parents and contain `plugin/nvimos.lua`; `NVIMOS_BACKEND` still wins
over all of them. This applies to every start kind (console, nvim-qt, headless) and to the test
helpers' backend lookup. The state-folder paths in the two ideas above are still undecided.
