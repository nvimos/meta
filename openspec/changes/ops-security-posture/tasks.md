# Tasks

## 1. Build

- [ ] 1.1 link classification: `classifyLink(href)` allows `http`, `https`, `mailto`; every other
  scheme is text plus Copy; `file:` and local paths stay in the preview; UNC is refused; tests for
  `ms-msdt:`, `search-ms:`, `smb:`, `javascript:`, `data:`, `file://server/share`,
  `\\server\share`, `C:\…`, `..\..\…`, control characters and a fragment
- [ ] 1.2 one `ShellLauncher` seam over `ShellExecuteW`; remove every `cmd /c start` in
  `nvim_launcher.dart`, `repos.dart`, `editors.dart` and `terminals.dart`; a test with a folder named
  `a & b` starts only the editor
- [ ] 1.3 one `GitCommand` builder shared by `Repo` and `LocalBackend._git`: `core.fsmonitor=false`,
  `core.pager=cat`, `core.editor=false`, `sequence.editor=false`, `GIT_TERMINAL_PROMPT=0`,
  `--no-textconv` on patches; route the remaining `GitDir.runCommand` calls through it
- [ ] 1.4 write-op preflight: parse `git config --local --list -z`; refuse `add`, `commit`, `checkout`,
  `merge` and `rebase` when `filter.*.clean|smudge|process`, `core.fsmonitor`, `core.hooksPath`,
  `core.sshCommand` or `credential.helper` is set; the notice names the key
- [ ] 1.5 no hooks from the app: `core.hooksPath` to an empty temp dir, `--no-verify` on commit; a
  repo with hooks gets one notice, with "commit in Neovim or a terminal" as the way to run them
- [ ] 1.6 `resolveInside(root, path)` with link resolution and a case-insensitive Windows compare;
  use it for task files, ignore files, discard, rename and the relay's `repo.path()`
- [ ] 1.7 `.nvimos` tracking outside the repo: confirm once per repo, show the resolved path, and
  remember the answer for the session only
- [ ] 1.8 discard on an untracked row goes through `Trash` when `deleteToTrash` is on; recursive
  deletes check `isLink` and name the resolved target
- [ ] 1.9 **New change**: read-only draft (no `Write`/`Edit`, or plan mode); the app validates and
  writes only `openspec/changes/<id>/…` and the matching task file; `.git/**` refused; prompt and diff
  shown before writing; `acceptEdits` only after an explicit second confirmation and still confined
- [ ] 1.10 redact traces before storage: home directory to `~`, `user:pass@` out of URLs, capped
  detail; the copy button copies the redacted text
- [ ] 1.11 `SECURITY.md`: trusted vs untrusted, what runs, what is refused, the remote caveat; Help
  gains a Security group; README links it
- [ ] 1.12 hostile fixture under `test/fixtures/`: `.git/config` with `core.fsmonitor` and
  `filter.x.process`, a writing hook, the six link shapes, a junction to an outside dir, `a & b`, and
  a `.nvimos` pointing at a temp sibling
- [ ] 1.13 `findBackendDir` never searches the opened folder: `NVIMOS_BACKEND`, the exe's folder and
  `~/ws` only; a plugin path inside the opened repo is refused with a notice; the Log names the path
  it loads; a test with a fake `relay/plugin/nvimos.lua` in the repo asserts it is not used

## 2. Relay

- [ ] 2.1 `serve(addr)` refuses a non-loopback address unless called with `!`; the notice says
  "open to the network, unencrypted"; `test_05_nav.lua` covers accept and refuse
- [ ] 2.2 the app defaults to `127.0.0.1`, marks a non-loopback connection `remote, unencrypted` in
  the connect screen and the status bar, explains the exposure, and never stores it
- [ ] 2.3 docs: the supported remote path is SSH port forwarding; a token on `nvimos.attach` does not
  protect `nvim_exec_lua` and is not offered as if it did
- [ ] 2.4 `tracking.path` in the relay rejects a path that leaves the planning root, on the same
  rules as `resolveInside`

## 3. Verify

- [ ] 3.1 unit tests: link classifier, `resolveInside` (including a link and a `..`), the git
  preflight parser, redaction, and the shell launcher fake
- [ ] 3.2 hostile-fixture test: open, browse, diff, stage and commit; no marker file, no process from
  the repo, one notice per refusal
- [ ] 3.3 agent test: a prompt-injection fixture that asks for `.git/hooks/post-checkout` and a file
  outside the change dir writes neither; the diff shown matches what is written
- [ ] 3.4 manual: the six links in the app, `a & b` on this machine, `:NvimosServe 0.0.0.0:6666`,
  a remote address refused and then confirmed, discard to the trash, and a repo with a real hook
  (committed from a terminal still runs it)
- [ ] 3.5 `make test` and `flutter analyze` pass on Windows; the relay's `make test` passes
- [ ] 3.6 backend discovery: start Neovim from a folder that contains a fake `relay/plugin/nvimos.lua`;
  it is not loaded, and the Log says which real plugin was used
