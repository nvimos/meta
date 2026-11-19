# mark dead ignore rules

Tags: integrate-purrage
Status: Draft, for TASK-193. Follows `ops-ignore-pane`.

## Why

Some lines in a `.gitignore` can never have an effect, and nothing says so. The Ignore panes'
Flip (turn a rule into a `!` negation and back) makes it easy to write one.

How git reads the rules, in short:

- a file's rules are read top to bottom; the last rule that matches a path decides
- a `.gitignore` in a folder adds its rules for that folder and below, after the ones above it
- `!pattern` re-includes what an earlier rule excluded
- the catch: when a *folder* is excluded, git does not look inside it at all, so no rule can bring
  back a file in it. `build/` followed by `!build/keep.txt` does nothing; the negation is dead. (It
  works only when the folder itself is not excluded, e.g. `build/*` then `!build/keep.txt`.)

## The idea

The lines pane marks the dead lines (muted, struck through) with a tooltip saying why:

- a negation whose path lies inside a folder an earlier rule excludes, in the same file or in a
  `.gitignore` above: "git never looks inside build/, so this cannot re-include anything"
- a negation that re-includes nothing because no earlier rule excludes it: "nothing above
  excludes this"
- a duplicate of an earlier line in the same file: "the same rule is on line 4"

Only the shapes that can be decided with certainty are marked; a rule the check cannot decide is
left alone, never marked wrongly.

## Cost

- No git call: the check works on the rules the pane already read, in memory.
- It runs when a file is read or edited, not per frame or per cursor move: a few hundred lines at
  most, cheap.
- The work is in the matching: a negation against the folder rules above it. Literal folders
  (`/build/`, `build/`) are a string check; wildcards (`*/cache/`, `**/out/`) need a gitignore
  pattern matcher (pure Dart, unit-tested, or reused from a package).

## Technical notes

- A pure `deadRules(fileRules, rulesAbove)` returning per line the reason or null; unit tests per
  shape, including the cases it must leave alone.
- The pane asks it after each load; nothing else changes.
