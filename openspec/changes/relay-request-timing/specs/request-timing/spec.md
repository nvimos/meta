## ADDED Requirements

### Requirement: Every request is timed
The relay SHALL time every call Ops makes to a public function of its modules, keyed by
`<module>.<fn>`, from entry to return, with the time spent in git commands during the call and
whether it raised an error.

#### Scenario: A git request
- **WHEN** Ops calls `nvimos.git.status`
- **THEN** the session records one `nvimos.git.status` call with its time in ms and its git time

#### Scenario: A failing request
- **WHEN** a request raises an error
- **THEN** it is recorded with its time and counted under `errors`, and the error reaches Ops as before

### Requirement: Stats are written quietly when the session ends
The relay SHALL write the session's summary to `relay-timing.json` in the local app data folder
(`%LOCALAPPDATA%\nvimos\` on Windows) when Neovim exits and every few minutes before that, keeping
the last 30 sessions and totals across them. Writing SHALL show no message and a failure SHALL not
disturb Neovim.

#### Scenario: Neovim exits
- **WHEN** Neovim exits after serving requests
- **THEN** the file holds this session with, per endpoint, `n`, `avg`, `p50`, `p95`, `max`, `total`,
  `git` and `errors`, and the totals are updated

#### Scenario: Ranking the slow parts
- **WHEN** the file is read
- **THEN** the totals list each endpoint with its count, average, worst p95, max, total time and share
  of all request time, sorted by total time

#### Scenario: The folder can't be written
- **WHEN** the stats file can't be written
- **THEN** nothing is shown and Neovim exits normally

### Requirement: Timing can be turned off
The relay SHALL skip all timing when `NVIMOS_TIMING=0` is set, and time by default otherwise.

#### Scenario: Off
- **WHEN** Neovim starts with `NVIMOS_TIMING=0`
- **THEN** no request is timed and no file is written
