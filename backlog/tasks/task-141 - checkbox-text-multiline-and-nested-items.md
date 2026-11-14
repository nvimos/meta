---
id: TASK-141
title: 'ops: checkbox text on more than one line, and items nested under a checkbox'
status: To Do
assignee: []
created_date: '2026-11-13'
labels:
  - ops
  - issue
dependencies: []
ordinal: 141000
---

## Description

ops reads a checklist item (Acceptance Criteria, Verify, Definition of Done) from its first line only.
`checksIn` in `lib/tasks/markdown.dart` goes line by line, and `parseCheck` matches one `- [ ] text` line.
Everything that is not such a line is skipped, so:

- text that continues on the next line (an indented wrap) is dropped; only the first line shows
- plain bullets and numbered steps nested under a checkbox are dropped, so a Verify item written as a
  topic line with `1.` `2.` steps under it shows as the topic alone
- nested checkboxes show, but flat: they are separate rows with an indent, not children of the item

Found while reformatting Verify items into a topic line with steps: that shape loses its steps in ops.

Decide what an item is, then parse it that way. Questions:

- what belongs to an item: indented continuation lines, nested bullets, numbered steps, nested checkboxes,
  fenced code under it
- how it is shown: the wrapped text as one paragraph, the steps as a list under the topic line
- what ticking means for an item with nested checkboxes (the topic follows its children, or stays its own)
- how to edit one: the toggle and the auto status go by the item's line, which must still hold when the
  item spans lines
- how to parse: the line scan and regexes in `markdown.dart` do not scale to nesting. Try tree-sitter
  (markdown grammar) or another real Markdown parser, and compare with fixing the line scan

## Acceptance Criteria

- [ ] #1 a checkbox whose text wraps onto indented lines shows all of its text
- [ ] #2 bullets, numbered steps and nested checkboxes under a checkbox show under it, in order
- [ ] #3 the checkbox marks (`x`, `.`, `~`, `n`) and the toggle still work on the topic line and on nested
  checkboxes
- [ ] #4 the parser choice is written down in PLAN.md with the reason (tree-sitter or not)
- [ ] #5 tests cover a wrapped item, a nested list, a nested checkbox and a fenced block under an item

## Verify

- [ ] test: a Verify item with `1.` `2.` steps under it shows the steps
- [ ] test: an Acceptance Criteria item that wraps onto a second line shows both lines
- [ ] test: tick a nested checkbox; the file changes on that line only

## Notes

- Do not reformat existing Verify items into topic and steps until this is done: ops would drop the steps.
