---
id: TASK-142
title: 'ops: the text of every modal is selectable'
status: To Do
assignee: []
created_date: '2026-11-14'
labels:
  - ops
  - frontend
dependencies: []
ordinal: 142000
---

## Description

ops: the text a modal shows can't be selected, so a warning or an error can't be copied or quoted.
Make the title and the text of every modal selectable, the discard warning first.

The modals today:

- "Discard changes?" and its text, from a click on discard (a file or a hunk) in Changes
- "Merge head into base?" in Pull request
- "Archive this change?" in Tasks
- the error details (already selectable)
- the forms: new task, new change

What to build:

- one shared confirm modal (title, text, Cancel and an action button, `danger` for discard), used by
  the discard, merge and archive questions, so the rule lives in one place
- the title and the text in it selectable, across both with one drag; the buttons stay buttons, a
  click on them does what it did
- the form modals (`DialogFrame`) get the same, with their text fields still typing and selecting normally
- the rule goes into PLAN.md: every modal's text is selectable; a new modal uses the shared one

## Acceptance Criteria

- [ ] #1 the title and the text of the discard, merge and archive modals can be selected and copied
- [ ] #2 the discard, merge and archive questions use one shared confirm modal
- [ ] #3 the form modals (new task, new change) show selectable text and their fields still work
- [ ] #4 the buttons of every modal still click (Cancel, the action) and Esc still closes
- [ ] #5 PLAN.md states the rule for modals

## Verify

- [ ] test: the title and the text of the confirm modal are selectable (a SelectionArea around them, not the buttons)
- [ ] test: Cancel returns false and the action returns true, the text being selectable
- [ ] manual: Changes, discard a hunk; drag over "Discard changes?" and the text below it; Ctrl+C; paste elsewhere shows both
- [ ] manual: the same drag-and-copy on the merge modal (Pull request) and the archive modal (Tasks)
- [ ] manual: in the discard modal click Cancel, then discard again and click Discard; both buttons work as before
- [ ] manual: New task and New change: type in the field, then select the dialog's own text; neither disturbs the other
- [ ] manual: Esc closes each modal

## Notes

- the manual steps are for the user to run after the change is in; the work goes on from what they find
- the error details modal already uses a SelectionArea (`ErrorPane`); keep it as it is
