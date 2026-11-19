## ADDED Requirements

Draft, for discussion; nothing here is decided.

### Requirement: A conflict opens the conflict view
A merge whose pre-flight finds conflicts SHALL open the conflict view and SHALL NOT run the merge.

#### Scenario: Conflict found by the pre-flight
- **WHEN** the user clicks Merge and `git merge-tree --write-tree` reports conflicted files
- **THEN** the conflict view opens listing those files, base has not moved, and the main checkout is unchanged

#### Scenario: Clean pre-flight
- **WHEN** the pre-flight reports no conflict
- **THEN** the merge runs as a plain merge, with no view

### Requirement: Pick either side per hunk
The conflict view SHALL let the user pick ours or theirs for each conflict hunk of a file.

#### Scenario: Pick a hunk
- **WHEN** the user picks theirs for a hunk
- **THEN** the file's preview shows theirs for that hunk and the other hunks are unchanged

### Requirement: Open a conflicted file in nvim
The conflict view SHALL open the conflicted file in a new nvim-qt instance, not in diff mode.

#### Scenario: Open in nvim
- **WHEN** the user chooses to open a conflicted file in nvim
- **THEN** nvim-qt starts a new instance on that file

### Requirement: Add refuses a file with conflict markers
Add SHALL refuse a file that has a conflict marker at the start of a line.

#### Scenario: File still has markers
- **WHEN** the user adds a file containing a line starting with `<<<<<<<`, `=======` or `>>>>>>>`
- **THEN** Ops refuses, names the file and the first marker line, and the file stays unresolved

### Requirement: The verify step before the commit
The commit that completes the merge SHALL run a verify step first.

#### Scenario: Verify passes
- **WHEN** no unmerged paths remain and no staged file has a marker
- **THEN** the commit completes the merge on base

#### Scenario: Verify fails
- **WHEN** an unmerged path or a marker remains
- **THEN** the commit is refused, the files are named, and base has not moved

### Requirement: Re-check on Resolve
Resolve SHALL run the pre-flight again before it opens the view.

#### Scenario: Conflict gone since the dialog
- **WHEN** base or head moved after the pre-flight and the conflict no longer exists
- **THEN** the merge runs as a plain merge and the view says so
