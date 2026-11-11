## ADDED Requirements

### Requirement: One conversation per buffer
A chat buffer SHALL hold one running conversation: each answer is appended below its question.

#### Scenario: Follow-up
- **WHEN** the user types a follow-up below an answer and sends it
- **THEN** the next answer is appended below it, with the earlier turns as context

### Requirement: Folded questions
Questions SHALL fold by themselves once answered.

#### Scenario: Long chat
- **WHEN** a chat has many turns
- **THEN** each question is a closed fold above its answer
