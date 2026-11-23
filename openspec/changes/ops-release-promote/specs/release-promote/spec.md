## ADDED Requirements

### Requirement: Builds publish as prereleases
A release build, from CI or from `make release`, SHALL publish as a prerelease, never as Latest.

#### Scenario: Weekly build
- **WHEN** the scheduled release workflow builds and publishes
- **THEN** the new GitHub release is a prerelease, and the previous Latest stays Latest

### Requirement: Promote a tested build
A manual promote step SHALL turn a chosen prerelease into the Latest release without building
again.

#### Scenario: Promote
- **WHEN** promote runs with a prerelease's tag
- **THEN** that release is no longer a prerelease and is marked Latest, with the same files

#### Scenario: Wrong tag
- **WHEN** promote runs with a tag that is not a prerelease
- **THEN** it fails and changes nothing
