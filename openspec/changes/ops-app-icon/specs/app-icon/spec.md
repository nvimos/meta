## ADDED Requirements

### Requirement: Own app icon
The front end SHALL ship its own icon, built from one source drawing in the repo, in place of the
default Flutter icon.

#### Scenario: Taskbar
- **WHEN** `ops.exe` runs
- **THEN** the taskbar, the title bar and Alt+Tab show the Ops icon, not the Flutter one

#### Scenario: Small sizes
- **WHEN** the icon shows at 16 px on a light or a dark taskbar
- **THEN** its shape is still recognizable
