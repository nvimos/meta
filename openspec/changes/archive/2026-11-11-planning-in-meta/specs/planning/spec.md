## ADDED Requirements

### Requirement: Planning lives in nvimos-meta
The config's todos, ideas and solved issues SHALL live in nvimos-meta, not in the config repo.

#### Scenario: A solved issue
- **WHEN** `/close-issues` closes an issue in the config
- **THEN** it writes a Backlog.md task in nvimos-meta and commits it there; the config gets no todo file

### Requirement: Backlog.md first, OpenSpec for design
Every item SHALL be a Backlog.md task; work that needs a proposal or specs also gets an OpenSpec change
that names its task (`Status: X (backlog TASK-n)`). No item is copied into both formats.

#### Scenario: A small fix
- **WHEN** a fix needs no design
- **THEN** it is a Backlog.md task only
