## ADDED Requirements

### Requirement: One-step install
The config SHALL install its dependencies with one script per platform, safe to run again.

#### Scenario: Clean machine
- **WHEN** the user runs `bootstrap.ps1` on a Windows machine with only Git
- **THEN** nvim starts with the config and `:checkhealth` reports no missing tools

### Requirement: Tests in CI
Every push SHALL run the tests in CI.

#### Scenario: Broken test
- **WHEN** a push breaks a test
- **THEN** the workflow fails and the README badge shows it
