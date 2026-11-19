# time relay requests

Status: To Do (backlog TASK-149)

## Why

Ops feels slow in places, and I don't know yet where the time goes. Ops already measures its own
side: every backend call is timed as `rpc <module>.<fn>` and summarized per session into
`%APPDATA%\nvimos\ui-timing.json`. That number is the whole round trip: msgpack over the socket,
Neovim getting round to the request, the Lua, the git it runs, and the way back. It says
`changes.refresh` takes 650 ms, but not whether that is git, the Lua around it, or waiting in line.

The relay should measure its own side the same way: how long each request takes inside Neovim, and
how much of that is git. Put next to Ops's file, the difference is the transport and the queue.
With both, I can decide what to optimize from numbers instead of guesses.

## The idea

The relay times every request it serves. A request is one API endpoint, the `<module>.<fn>` that Ops
calls through `nvim_exec_lua` (`nvimos.attach`, `nvimos.git.status`, `nvimos.files.diff`, ...), not
the internal functions those call. The names are the same as Ops's `rpc` keys, so the two files can
be read side by side.

For each request it records the time from entry to return, whether it raised an error, and how much
of that time was spent in git commands (every git call goes through `repo.run`, so one hook there
covers them all). It keeps the raw times in memory for the session, which is the life of the Neovim
process.

When Neovim exits (`VimLeavePre`), the relay writes the session's summary into a stats file, and
every few minutes in between, so a crash loses little. The file keeps the last 30 sessions and
totals across them. It works quietly: no messages, no notifications, and a failure to write is
swallowed. Timing can be turned off with `NVIMOS_TIMING=0`, the same switch Ops uses; it is on by
default, since the relay has no release build.

The file lives in local app data, not the roaming one: `%LOCALAPPDATA%\nvimos\relay-timing.json` on
Windows, `~/.local/state/nvimos/relay-timing.json` elsewhere. Several Neovims may run at once; each
reads the file, adds its session, and writes it back in one go, so the last one to exit wins for
the totals, and no session is dropped as long as two don't exit in the same instant.

### What the file shows

Per session: when it started and ended, and per endpoint:

- `n`: how many calls
- `avg`, `p50`, `p95`, `max`: the call's time in ms
- `total`: all its calls together, in ms, which is what ranks the endpoints by cost
- `git`: the time in git, as `avg` and `total`
- `errors`: how many calls raised

Across the kept sessions (`totals`), per endpoint: the total count, the overall average, the worst
`p95` and `max`, the total time, and its share of all time spent serving requests. The totals are
sorted by total time, so the first entries are the ones to look at.

The format follows Ops's `ui-timing.json`, with the added `avg`, `total`, `git` and `errors`.

An endpoint that only starts work and returns (a job in `nvimos.jobs`) is timed to its return, not
to the job's end. The job's own run time is a later question.

## Impact

Relay (`nvimos/relay`): a new `lua/nvimos/timing.lua`. The public functions of the modules Ops calls
are wrapped once, when the module is loaded, so no endpoint knows about the timing; `repo.run` adds
its time to the request in progress. A `VimLeavePre` autocmd and a timer write the file. A test
calls a few endpoints and reads back the summary. The README names the file and the switch.
