# Untrusted repositories: the security posture

Tags: security, ops
Status: Proposed, for TASK-205. The P0 fixes below are in scope; the remaining findings are
follow-ups named at the end.

## Why

Ops is a local app, so it is tempting to assume it runs on local trust. That assumption is wrong in
one specific way: the app's input is a repository, and a repository is not just data. It is a tree of
files chosen by someone else, a `.git` directory that can carry configuration and hooks, prose the
app renders, and prose an agent reads.

Local trust holds for the files the user wrote. It does not hold for a branch from a fork reviewed as
a pull request, a take-home exercise, a sample repo downloaded as a zip, a repo an agent created or
edited, or a Neovim the user connected to over the network. "The app runs locally" says where the
process runs, not who controls its input.

The risks are not exotic. Each one is a normal feature doing what it was told:

- Mara reviews a contributor's branch. The README has `[Check the build](ms-msdt:...)`. She clicks it.
- She opens a sample project from a zip. Its `.git/config` sets `core.fsmonitor`, or its
  `.git/hooks/pre-commit` exists. She stages a file and commits a typo fix.
- She presses **New change** in a repo whose `openspec/config.yaml` says, in prose, to append a line
  to `.git/hooks/post-checkout` first. The agent is told to follow that file, and may write.
- She runs `:NvimosServe 0.0.0.0:6666` to reach the app from a laptop, and the cafe Wi-Fi gets the
  same power her shell has.
- The repo folder is named `acme & calc`, and the app starts Neovim through `cmd /c start`.

## The model

Three rules, in order:

1. **Repository content is data, never instructions.** It may be rendered, diffed and read. It does
   not get to direct a tool with more power than the pane that shows it.
2. **Opening, browsing and reviewing must not execute code from the repo.** Staging, committing,
   merging and checking out may run the user's own tooling, and only after the app says so.
3. **Everything that leaves the process goes through one named door with a test:** a shell, a URL, a
   socket, an agent. No second path, no `cmd /c` shortcut.

## Findings

In scope here: S1–S6, S8 and S12. S7 and S9–S11 are the named follow-ups at the end.

| # | Risk | Where | How it happens | Severity |
|---|------|-------|----------------|----------|
| S1 | An auto-approving agent follows repo prose | `lib/tasks/workspace.dart` (`newChange`) | `claude -p --permission-mode acceptEdits --allowedTools Read,Write,Edit,Glob,Grep`; the prompt says to follow `openspec/config.yaml` and the existing changes | High |
| S2 | The relay is unauthenticated remote code execution | `nvimos-relay` (`serve`), `lib/rpc/client.dart` | any client that reaches the port can call `nvim_exec_lua` and `nvimos.files.*` (absolute paths); `serve` accepts `0.0.0.0`; the app connects to any host in cleartext | High |
| S3 | Git runs repository config and hooks | `lib/local/repo.dart`, `local_backend.dart` | `status` runs `core.fsmonitor`; `diff` runs textconv drivers; `commit`, `checkout`, `merge` and `rebase` run hooks and filters | Medium |
| S4 | Rendered markdown hands URLs and files to the Windows shell | `lib/state/preview_links.dart`, `local/file_manager.dart` | any non-`file` scheme becomes a `WebLink`; any local path becomes a `FileLink`; both end at `explorer.exe` | High |
| S5 | `cmd /c start` re-parses arguments | `nvim_launcher.dart`, `repos.dart`, `editors.dart`, `terminals.dart` | a directory or file name with `&`, `\|`, `^`, `%` can start another command | High |
| S6 | Paths are joined, not contained | `local/paths.dart`, `files.dart`, `local_backend.dart`, relay `tracking.lua` | `.nvimos`, `readFiles`, ignore writes and the relay's `repo.path()` accept absolute paths and `..`; discard deletes untracked paths for good | Medium |
| S7 | Native parsers read repo files in-process | `packages/ops_pdf_on` (PDFium), image previews | a malformed PDF or image can exercise a memory-safety bug | Low |
| S8 | Logs and traces keep more than they should | `log_state.dart`, `action_failure.dart`, `_git`'s `detail` | command lines, home paths, credentials in remote URLs, and whatever a failure quotes (a path, a diff line) are copyable | Medium |
| S9 | Releases are unsigned and packed | `.github/workflows/release.yml`, `dist/` | no Authenticode, no checksum, Enigma Virtual Box packing; AV heuristics and SmartScreen | Medium |
| S10 | CI actions float on tags | `.github/workflows/*.yml` | `actions/checkout@v4` and friends can move under the build | Low |
| S11 | The RPC decoder has no frame cap | `lib/rpc/msgpack.dart` | a peer can make the app allocate without bound | Low |
| S12 | Backend discovery can load a repo's Neovim plugin | `lib/state/nvim_launcher.dart` (`findBackendDir`) | it walks up from `Directory.current`, so a repo containing `relay/plugin/nvimos.lua` is added to Neovim's runtimepath and `:runtime` executes it | Medium |

What is already right, and should stay:

- every process starts with `runInShell: false`, and git gets `--` before paths;
- `diff` and `diffFile` already pass `--no-ext-diff`;
- deletes in Add and Ignore go to the Recycle Bin by default, and `HiddenWrite` restores attributes;
- the hot-reload VM-service path is guarded by `kDebugMode`;
- `pubspec.lock` is committed;
- git's own `safe.directory` refusal is not bypassed.

## What this change fixes

### S1. The agent drafts; the app writes

- Default to a read-only draft. The agent runs with no `Write`/`Edit` tools (or `--permission-mode
  plan`) and returns the proposed files; the app validates and writes only
  `openspec/changes/<id>/…` and the matching `backlog/tasks/task-<n> - <slug>.md`.
- Never write `.git/**`. Refuse a `tracking` root outside the repo unless the user confirms it for
  this change.
- Show the prompt and the resulting diff before anything is written. `acceptEdits` is not a default;
  it is an explicit second confirmation, and still limited to the change directory.
- Treat quoted repository prose as data in the prompt. The sandbox, not the wording, is the defense.

### S2. The relay is loopback, and remote is said out loud

- `:NvimosServe` refuses a non-loopback address unless called with `!`; the notice says the port is
  open to the network and unencrypted. Loopback is not a per-user boundary on Windows either: another
  account on the machine can connect to `127.0.0.1`, which is why the named pipe is the real local fix.
- The app defaults to `127.0.0.1`, marks a non-loopback connection `remote, unencrypted`, explains
  that anyone on the path can read and change the session, and does not remember it.
- Document the supported remote path: SSH port forwarding, or a Neovim on the same machine.
- Do not pretend a token fixes this. A token on `nvimos.attach` cannot protect `nvim_exec_lua`:
  Neovim answers every client on that address with its full API. Only binding and transport do.

### S3. Git is told to ignore repository tooling

A clean `git clone` does not copy hooks or `.git/config`, so this is not "every clone is remote code
execution". It is every repository that arrives with its `.git` directory: a zip, a shared folder, a
VM snapshot, a repo an agent created. The app's own agent can write `.git` today, which is how S1
turns into S3.

- One wrapper for every git call (replace `GitDir.runCommand` where it is used) that adds:
  `-c core.fsmonitor=false -c core.pager=cat -c core.editor=false -c sequence.editor=false`,
  `GIT_TERMINAL_PROMPT=0`, and `--no-textconv` on patch-producing calls (`--no-ext-diff` stays).
- For write operations (`add`, `commit`, `checkout`, `merge`, `rebase`), preflight with
  `git config --local --list`: when the repo defines `filter.*.clean|smudge|process`,
  `core.fsmonitor`, `core.hooksPath`, `core.sshCommand`, or `credential.helper`, refuse with one
  notice that names the key and says to commit in a terminal if the user trusts it.
- Never run hooks from the app: point `core.hooksPath` at an empty temp directory (that disables all
  hooks, including `post-checkout`), and still pass `--no-verify` to commit. A repo that has hooks
  gets the notice instead.
- Make the notice name the file and key, not a generic "unsafe repository".

### S4. Links are classified, not forwarded

- A pure `classifyLink(href)` returns `openWeb(url)` only for `http`, `https` and `mailto`.
- Every other scheme (`ms-msdt:`, `search-ms:`, `smb:`, `javascript:`, `data:`, unknown) is shown as
  text with a **Copy** button. It never reaches ShellExecute.
- `file:` and local paths resolve inside the preview. Opening one is a second, explicit click that
  names the resolved absolute path; a UNC path (`\\server\share`, `file://server/share`) is refused,
  because passing it to Explorer leaks an NTLM hash.
- `Run` on an executable stays the only path to executing a repo file, and the button shows the
  absolute target.

### S5. No `cmd /c start`

- Replace the four call sites with `ShellExecuteW` through FFI (as `shell_delete.dart` already does),
  or with a direct `Process.start` plus `CREATE_NEW_CONSOLE` for console programs. On macOS and Linux
  the same `ShellLauncher` wraps `open` and `xdg-open`; the allowlist and the no-shell rule are
  identical, and the UNC refusal is Windows-only.
- A `.cmd`/`.bat` shim is opened with ShellExecute, which handles the association without a shell.
- If any `cmd` use survives, quote and reject `& | ^ < > ( ) % ! "` in the argument it carries. A
  test uses a folder named `a & b` and asserts that only Neovim starts.

### S6. Writes and deletes are contained

- Add `resolveInside(root, path)`: canonicalize, resolve links, compare case-insensitively with the
  root prefix, and reject `..` and absolute paths that leave it. Use it for task files, ignore files,
  discard, rename and the relay's `repo.path()`.
- `.nvimos tracking` may point outside the repo (it is the point of the file), but the app asks once
  per repo before writing there, and says the resolved path.
- `discard()` on an untracked row goes to the trash when `deleteToTrash` is on, like Add and Ignore.
- Never recurse through a link: check `FileSystemEntity.isLink` before a recursive delete, and name
  the resolved target in the confirmation.

### S8. Traces are redacted

- Before an error or a log row is stored, replace the home directory with `~`, strip `user:pass@`
  from URLs, and cap the detail. The copy button copies the same redacted text.

### S12. Only the app's own relay may be loaded

- `findBackendDir` searches `NVIMOS_BACKEND`, the exe's folder and `~/ws`, never the folder being
  opened. The resolved plugin path is printed in the Log, and a path inside the opened repo is
  refused with a notice.
- The search stops at the first match; it does not walk to the drive root through a checkout.

## Out of scope, named

- `ops-release-integrity`: Authenticode signing or a published `SHA256SUMS`, a version display, and
  pinned action SHAs. The Enigma Virtual Box single-file build should at least say what it is.
- `ops-preview-sandbox`: PDF and image parsing out of process, or PDF off by default in releases.
- `relay-local-socket`: a Windows named pipe or Unix socket for the relay, so the OS can scope access
  to the user. This is the real fix for S2's local-process case; it needs a Neovim-side design.
- RPC frame caps (S11) go with the relay work.

## Decisions

Settled defaults; the alternative is named where it matters.

- **Untrusted by default.** No trust prompt on open. The app is safe to browse first; the notice
  appears only when a repo actually carries the thing being refused.
- **The app never runs repo hooks.** Not behind a flag, not after a trust dialog. If the user wants
  hooks, they commit in Neovim or a terminal. A "trust this repo" switch is not worth the risk it
  implies.
- **The agent never holds the pen by default.** It drafts, the app writes the two places a change
  owns. This removes S1 rather than moderating it.
- **Links: http, https, mailto only.** `file:` links stay inside the preview. Unknown schemes are
  text plus Copy.
- **Remote relay is a session choice, never a stored default.** Saying it is unencrypted is part of
  the connect flow, not a tooltip.
- **Discard is reversible when the setting says so.** The trash setting applies to every delete,
  including discard.
- **No security theatre.** No token that does not cover `nvim_exec_lua`; no warning that fires on
  every open.

## Usability

- Browsing a normal, clean repository changes nothing on screen. The notices are for repos that carry
  hooks, exec-capable config, a tracking root outside the checkout, or a repo-born link.
- A refusal is one sentence plus the key or path that caused it, with Details in the Log, in the
  same voice as the rest of the app.
- `Help` gains a `Security` group: what the app runs, what it refuses, and the remote caveat.
- The connect screen shows `local` or `remote, unencrypted` next to the address, and the status bar
  keeps the badge for the session.

## Technical notes

- Link classification is pure and lives beside `preview_links.dart`: `classifyLink(href)`, with tests
  for every scheme above, control characters, `\\server\share`, `C:\…`, `..\..\…`, and a fragment.
- Shell launching goes through one `ShellLauncher` seam with a fake, like `ProcessRunner`; the Windows
  call is `ShellExecuteW(NULL, "open", path, NULL, cwd, SW_SHOWNORMAL)`, with `open` / `xdg-open` on
  macOS and Linux behind the same interface. The fixes here must not add new Windows-only code to the
  paths that already have platform branches (`editors.dart`, `terminals.dart`, `trash.dart`).
- Git hardening lives in one place: `Repo`'s runner and `LocalBackend._git` share a `GitCommand`
  builder, so no call site can forget the flags. The preflight parses
  `git config --local --list -z` into a set of keys and refuses by key.
- `resolveInside` uses `FileSystemEntity.resolveSymbolicLinks` where the path exists, and the
  canonical root otherwise; both sides are lowercased on Windows only.
- The relay's `serve(addr)` gains a loopback check (`127.0.0.1`, `::1`, `localhost`); `serve!` or a
  second confirmation is the only way past it. `test_05_nav.lua` covers both.
- The hostile fixture is a checked-in directory that the test copies to a temp dir: a `.git/config`
  with `core.fsmonitor` and `filter.x.process`, a hook that writes a marker, a README with the six
  link shapes, a junction to an outside dir, a file named `a & b`, and a `.nvimos` pointing at a temp
  sibling.
- `SECURITY.md` states the threat model in one page: what is trusted (the user, the machine, the
  editor), what is not (the repo, its config, its prose, the network), and what the app does about
  each.

## Done means

1. The hostile fixture is opened, browsed, diffed and committed in a test. No marker file appears, no
   command from its config or hooks runs, and one notice names each refusal.
2. The six link shapes are classified by unit test; `ms-msdt:`, `search-ms:`, `smb:`,
   `javascript:`, `data:` and `file://server/share` reach no shell; `http`/`https`/`mailto` do.
3. A repo folder named `a & b` opens Neovim and starts nothing else.
4. `:NvimosServe 0.0.0.0:6666` refuses without `!`; the app refuses a non-loopback address without
   the explicit remote confirmation, and does not persist it.
5. **New change** on a repo whose prose asks for `.git/hooks/post-checkout` writes only inside the
   change directory and the task file.
6. Discard on an untracked row lands in the trash when the setting is on.
7. Starting Neovim from inside a repo with a fake `relay/plugin/nvimos.lua` does not load it, and the
   Log names the plugin that was loaded.
8. `make test` and `flutter analyze` pass; `SECURITY.md` and the Help group exist.

## Ideas for later

- A per-repo "trusted" flag that unlocks hooks and agent writes, if the refusals prove too blunt.
- Open-with on a file link could go through the preview's own viewer first, for every type.
- A signed update check, once there is a certificate decision.
