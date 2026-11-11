## ADDED Requirements

### Requirement: Layout per task
The config SHALL offer one zen layout per kind of work, each on its own key.

#### Scenario: Reading
- **WHEN** the user presses z1
- **THEN** only the text shows, centred, without signs or diagnostics

#### Scenario: Debugging
- **WHEN** the user presses z3 during a debug session
- **THEN** the window is maximized with numbers and all diagnostics, and the debug panes open as splits beside it

### Requirement: Leaving restores
Leaving a zen layout SHALL restore the window size, diagnostics and options from before it.

#### Scenario: z0 after z2
- **WHEN** the user presses z0 in z2
- **THEN** the window size and the diagnostics limit are as they were before z2
