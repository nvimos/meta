## ADDED Requirements

### Requirement: Task ids don't collide
A new task SHALL get an id that no other clone of the planning repo can give at the same time.

#### Scenario: Two people create a task offline
- **WHEN** two clones each create a task before pulling, then both sync
- **THEN** the two tasks have different ids and the merge has no conflict

### Requirement: No shared file per status change
A status change SHALL write only the task's own files; `index.tsv`, if kept, is generated.

#### Scenario: Status changes on different tasks
- **WHEN** two people change the status of two different tasks and both sync
- **THEN** git merges both without a conflict

### Requirement: Sync from the app
The Tasks mode SHALL pull, commit its own edits and push the planning folder, and show how far it is
behind or ahead.

#### Scenario: A teammate moved a task
- **WHEN** a teammate pushed a status change
- **THEN** it shows on the board after one sync

### Requirement: Taking a task
Taking a task SHALL set its assignee and status In Progress and push at once; a rejected push means
someone else took it first.

#### Scenario: Two people take the same task
- **WHEN** two people take one task at about the same time
- **THEN** the second push is rejected, the app pulls and shows who has the task
