# Tasks

## 1. Config

- [ ] 1.1 `.nvimos` reader takes `tracking_remote` (`owner/repo` or a GitHub URL) and
  `tracking_ref` (default `main`)
- [ ] 1.2 `tracking_remote = nvimos/meta` added to the `.nvimos` of the ops and relay repos

## 2. Snapshot

- [ ] 2.1 fetch the archive (codeload, `gh auth token` for a private repo), with ETag /
  `If-None-Match`
- [ ] 2.2 extract only `backlog/` and `openspec/` into a temp folder, refuse `..`, absolute paths
  and links, cap size and file count; swap into the cache folder with `snapshot.json`
- [ ] 2.3 resolve the planning: local folder, else snapshot, else repo root
- [ ] 2.4 fetch on open when there is no snapshot or it is older than an hour, without blocking the
  open

## 3. UI

- [ ] 3.1 Tasks mode bar: source, age, last fetch error, Refresh, Clone to `<tracking>`
- [ ] 3.2 edits disabled on a snapshot (state class refuses, controls greyed with a tooltip)
- [ ] 3.3 loading and failed states when there is no snapshot yet
- [ ] 3.4 Clone runs `git clone` to the tracking path, reloads, removes the snapshot

## 4. Docs

- [ ] 4.1 `PLAN.md`: the `.nvimos` keys, the snapshot, the bar
- [ ] 4.2 README: a fresh clone shows the planning without setup

## 5. Verify

- [ ] 5.1 tests against a local HTTP server serving a zip: precedence, read-only, 304, failed fetch
  keeps the old snapshot, hostile archive
- [ ] 5.2 on a machine without `nvimos-meta`: clone `nvimos/ops`, open it, the Tasks mode fills
- [ ] 5.3 offline after a fetch: the old snapshot shows with its age
