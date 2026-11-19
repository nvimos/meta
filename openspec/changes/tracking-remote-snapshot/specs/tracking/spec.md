## ADDED Requirements

### Requirement: Remote planning repo in .nvimos
The `.nvimos` file SHALL accept a `tracking_remote` key naming the planning repo on GitHub
(`owner/repo` or its URL), and an optional `tracking_ref` (default `main`).

#### Scenario: Old reader
- **WHEN** an Ops version without this change reads a `.nvimos` with `tracking_remote`
- **THEN** it ignores the key and behaves as before

### Requirement: Snapshot when there is no local checkout
When the local `tracking` folder does not exist and `tracking_remote` is set, Ops SHALL fetch an
archive of the remote ref into its cache folder and show the planning from it. A local `tracking`
folder SHALL always win over the snapshot.

#### Scenario: Fresh clone
- **WHEN** a repo whose `.nvimos` has `tracking_remote` is opened and the `tracking` folder is
  missing
- **THEN** Ops fetches the snapshot without being asked and the Tasks mode shows its tasks and
  changes

#### Scenario: Local checkout present
- **WHEN** the `tracking` folder exists
- **THEN** Ops reads it and fetches nothing

#### Scenario: Stale snapshot
- **WHEN** the repo is opened and the snapshot is older than an hour
- **THEN** the old snapshot shows at once and is replaced when the new fetch arrives

#### Scenario: Fetch fails
- **WHEN** the fetch fails
- **THEN** an existing snapshot stays in use with its age and the error in the Tasks bar; with no
  snapshot the Tasks mode shows the error and a Retry

### Requirement: Snapshot is read-only
A snapshot SHALL NOT be edited. Status, priority and checkbox changes SHALL be refused by the state
and shown disabled with a tooltip that says why.

#### Scenario: Edit attempt
- **WHEN** the user tries to change a task's status in a snapshot, by click or key
- **THEN** nothing is written and the control says the tasks are a read-only snapshot

### Requirement: Archive is untrusted
Ops SHALL extract only `backlog/` and `openspec/` text files from the archive, SHALL NOT write
outside the snapshot folder, and SHALL NOT run anything from it.

#### Scenario: Hostile entry
- **WHEN** the archive holds an entry with `..`, an absolute path or a link
- **THEN** that entry is skipped and nothing is written outside the snapshot folder
