## ADDED Requirements

### Requirement: PDF build is tested before it ships
The PDF preview (pdfrx) SHALL ship in a release only from a build whose PDF test passed in CI.
Until that test exists, every build SHALL be made with PDF off.

#### Scenario: Release before the test exists
- **WHEN** `make release` or the CI release runs before this change is implemented
- **THEN** the build has PDF off, and a PDF in the preview shows its facts and the Open button

#### Scenario: CI test
- **WHEN** CI runs the PDF job
- **THEN** it builds with PDF on and renders the first page of a sample PDF in the preview, and a
  failure fails the workflow

#### Scenario: Release after the test exists
- **WHEN** the CI release builds after the PDF job is in place
- **THEN** it builds with PDF on

### Requirement: Local builds stay quick
Local builds SHALL have PDF off unless the developer turns it on with `make configure pdf=on`.

#### Scenario: Local release
- **WHEN** `make release` runs locally
- **THEN** it turns PDF off before it builds, and PDF is still off afterwards
