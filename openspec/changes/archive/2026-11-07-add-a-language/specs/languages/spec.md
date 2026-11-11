## ADDED Requirements

### Requirement: Adding a language is one documented step
Adding a language SHALL follow one checklist (`readme.add-a-language.md`): parsers, LSP, linters,
formatter, test runner, debug adapter, each in its lang module.

#### Scenario: A new language
- **WHEN** the user follows the checklist for a language
- **THEN** opening a file of that language gives highlighting, completion and diagnostics without other edits

### Requirement: Only the languages in use
Only languages a spec turns on SHALL be installed, with a conservative set of defaults.

#### Scenario: Unused language
- **WHEN** a language is not turned on in the spec
- **THEN** none of its servers or parsers are installed
