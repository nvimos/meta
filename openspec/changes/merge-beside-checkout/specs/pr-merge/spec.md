## ADDED Requirements

Draft, for discussion; nothing here is decided.

### Requirement: Merge leaves the main checkout alone
A merge of head into base SHALL NOT switch branches or write conflict markers in the main checkout.

#### Scenario: Base is checked out and dirty
- **WHEN** base is checked out in the main checkout, which has uncommitted changes in files the merge
  does not touch, and the user merges head into base
- **THEN** base gets the merge commit, the main checkout is on the new commit, and the uncommitted
  changes are still there

#### Scenario: Base moved meanwhile
- **WHEN** base gets a new commit while the merge runs
- **THEN** the merge fails and base keeps the new commit

### Requirement: Conflicts are resolved beside the checkout
A merge with conflicts SHALL stop in the merge worktree, not in the main checkout.

#### Scenario: Conflict
- **WHEN** head and base change the same lines
- **THEN** Ops names the conflicted files, the main checkout has no conflict markers, and base has
  not moved
