# How the lost commit keys were found

Notes for the next bug of this kind: what was tried, what each step showed, and why the obvious
suspect was not it.

## 1. The report

Alt+] to Changes, stage a file with "add", `cc` to the commit field, type a burst: only the first
letter stayed in the field.

## 2. Tests that did not reproduce it

Widget tests replayed the steps: the Changes view alone, then the whole shell on a real local
repository with the file watcher running, with a click on the field and with `cc`, and with the
refresh after the stage landing in the middle of the burst. In every run the keyboard stayed in the
field, no key handler claimed a letter, and the text input connection opened once.

So the cause was in what the tests don't have: the real Windows engine, real timing, the real
accessibility layer.

## 3. A trace in the running app

A temporary trace in `changes_view.dart` wrote `[commit-trace]` lines to `out/live.log`: every key
with its character and the focused node, every change of the field's text, every focus change of
the field. One run showed:

```
50596 ms  key down C            pending=true    (cc completes)
50597 ms  field focus=true
51002 ms  key down H  char=h    focus=commit message
51007 ms  text "h"
51056 ms  field focus=false                     (49 ms after the first letter)
51112 ms  key down K  char=e    focus=_ModalScopeState Focus Scope
```

The first letter landed. About one frame later the field lost the keyboard to the page's
top-level focus scope, and the following keys went nowhere.

## 4. The navigation-key question

The first idea was the rule that makes an arrow key at the edge of the commit field step out of
it (Left to the rail, Up to the list above), with H being Left in hjkl, and the same for the other
direction letters `j k l` and `w a s d`. An exception for those letters in the field seemed to be
the fix.

It wasn't the cause:

- the rule only looks at the real arrow keys (`final nav = arrow ? navKey(e) : null; // letters
  type into the field` in `CommitBox`), so a letter never reaches it
- a key handler moves the focus within a millisecond of the key: after `cc` the field had the
  keyboard 1 ms after the second `c`; here the focus left 54 ms after the `h` went down, a frame
  later, not on the key
- the Left rule sends the keyboard to the rail, and the trace would have said `focus=rail`; it said
  the page's focus scope, which is where focus falls when a node is unfocused
- the `h` itself landed as text (`text "h"`), so it was typing, not a command

The letters do belong in the field, so the suggestion became a test that pins it: `h j k l w a s d`
(including the D-position key the layout reads as Right) type into the empty field and keep the
keyboard there, and only the arrows step out.

## 5. Who called unfocus

The trace's focus node (`_TracedFocusNode`) printed a stack trace whenever `unfocus()` was called on
it. The next run named the caller:

```
_TracedFocusNode.unfocus
_TextFieldState.build.<closure>            (material_ui text_field.dart: handleDidLoseAccessibilityFocus)
SemanticsAnnotationsMixin._performDidLoseAccessibilityFocus
SemanticsOwner.performAction
FlutterView.updateSemantics … PipelineOwner.flushSemantics … drawFrame
```

Not app code and not a key: the accessibility bridge, while the frame sent its semantics update.

## 6. Why the bridge thought the focus moved

In the engine, the Windows bridge takes the node flagged focused as its focus and, when that node
changes, sends the previous one "lost accessibility focus". A widget test running as Windows listed
the focused nodes in the shell:

```
after cc:       #55 textField=true label="Commit message  (cc, Ctrl+Enter commits)" value=""
after h:        #55 …                                                               value="h"
a frame later:  #74 textField=true label=""                                          value="h"
```

The field's focused node changed from #55 to #74 one frame after the first letter. Narrowed down
with plain text fields:

- a field with only a hint: the node stays
- a field with a fixed suffix of two buttons: the node stays
- a field whose suffix gains a button with the text (the X): a new node
- the same growing suffix inside `Semantics(container: true)`: the node stays

## 7. The fix and its check

`Semantics(container: true)` around the commit field's buttons and around `ClearButton`. A test
running as Windows types the first letter and expects the same focused node and the keyboard still
in the field; it fails without the fix.

## What to take from it

- When tests can't reproduce a focus bug, trace it in the running app: keys, text, focus changes,
  and a stack trace on `unfocus`.
- On Windows, a text field's focus is tied to its semantics node. Anything that reshapes that node
  while you type (a button that appears inside the field) can unfocus it, but only while the
  accessibility layer is active, so it may never show on another machine.
