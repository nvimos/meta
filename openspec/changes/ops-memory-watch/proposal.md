# watch ops' memory over time

Status: Open proposal, not decided, not to be implemented yet. There is no backlog task yet; one gets
made if we go ahead.

## Why

After a while of use, Ops feels slow. A look at the machine on 2026-11-14 found test leftovers (84 git
fsmonitor daemons and 20 orphaned test Neovims, about 880 MB, now cleaned up and stopped at the
source), but that does not settle whether Ops itself leaks. One reading is not enough to tell:
`ops.exe` (the live debug build) was at about 500 MB, and 15 minutes later at about 660 MB, with
hot reloads in between. A debug build under hot reload grows for ordinary reasons (old code and
objects stay around after each reload), so the number alone says little.

## The idea

Measure it over time, in a build where the number means something.

- sample the app's memory (working set) and handle count once a minute while it is in use, and keep
  the samples in a small log, so growth over an hour of normal use can be read off as a line
- do it in a profile or release build, not under `make live`, since hot reload skews the numbers
- if the line keeps rising without the work changing (same repo, same mode), it is a leak; if it
  rises and levels off, it is the app's normal footprint

Two ways to take the samples, which can also be used together:

- from outside: a small script that reads `ops.exe`'s working set and handle count every minute
  (`Get-Process`) into a CSV
- from inside: the app reads its own resident memory (`ProcessInfo.currentRss`) and shows it in the
  debug bar, next to the last key and mouse event, plus a line in the log; the debug bar already
  exists, so it costs little
- Flutter DevTools' memory tab can show what the Dart heap holds, for the second step: finding what
  is growing once it is known that something is

If a leak shows, the first places to look are the ones that keep things alive for the whole session:
the listeners on the session and the state objects, timers (the auto-pick, the Done note, the
retry timer), subscriptions to the backend's git change events, and the per-click records the
timing helper keeps (`UiTiming.instance.samples`).

## Open questions

- profile build or release build for the long run, and how to start it next to the usual
  `make live`
- whether the in-app readout is worth keeping, or the outside script is enough
- how long to run it, and what use counts as "normal"
- whether the backend's Neovim (the plugin's watchers and the git event stream) is sampled too
