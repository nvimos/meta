# completion Specification

## Purpose

How completion behaves in buffers and on the command line.

## Requirements

### Requirement: blink.cmp completion
Completion SHALL come from blink.cmp, with the config's own sources built on one source builder.

#### Scenario: Insert mode
- **WHEN** the user types in a buffer with an LSP attached
- **THEN** the menu offers LSP, buffer-word and path items

### Requirement: Command-line completion like plain Vim
On the command line `<Up>`/`<Down>` SHALL recall history; the menu moves on `<M-j>`/`<M-k>`.

#### Scenario: History
- **WHEN** the user presses `<Up>` on an empty `:` line
- **THEN** the previous command is recalled, not a menu item
