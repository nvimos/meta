# the commit field keeps the keyboard while you type

Tags: bug, accessibility, keys
Status: Approved, for TASK-211. The fix is in and verified in the running app (2026-11-23).

## Why

In Changes, `cc` puts the keyboard in the commit message field. Typing a burst there, like the first
letters of a summary, kept only the first letter: the rest went nowhere. The field had lost the
keyboard after one character, and the later keys reached no widget at all.

It made the commit field unusable for anyone who types quickly, which is everyone writing a commit
message.

## The cause

The field's buttons on the right, inside the field, are the large-window button and an X that
clears the message. The X only exists while there is text, so the first letter adds it. Adding it
reshapes the field's semantics: the editable text moves into a new semantics node, with a new id,
and that node carries the "focused" flag.

The Windows accessibility bridge in the Flutter engine (`accessibility_bridge.cc`) follows the
focused flag. When the focused node changes, it tells the node it had before that it "lost
accessibility focus" (`SetLastFocusedId`). The old node still belongs to the text field, and a
Material `TextField` on Windows unfocuses itself when it loses accessibility focus
(`handleDidLoseAccessibilityFocus` in `text_field.dart`). So the first frame after the first letter
took the keyboard away.

It only happens while Windows accessibility is active for the app, which is also why the
`Failed to update ui::AXTree` errors show up at all (change `ops-tooltip-semantics`). Something on
this machine keeps it active.

## The fix

The buttons in a field are one semantics node of their own, `Semantics(container: true)` around
them. The X can come and go inside it without touching the field's node, so the focused node keeps
its id and the bridge has nothing to report.

- the commit field's buttons (`_FieldButtons`, `lib/ui/changes_view.dart`)
- the shared X of the filter and picker fields (`ClearButton`, `lib/ui/widgets.dart`); every
  other text field with an X uses it (Add and Ignore, Directories, Help, the rev pickers, the Tasks
  filter, the command palette)

## How it was found

The steps, the dead ends and the navigation-key question are in [debugging.md](debugging.md).
The technique that found it, a temporary trace in the running app, with the code to add it again,
is in [trace-technique.md](trace-technique.md).

## Technical notes

- `test/support/semantics_focus.dart`: `focusedSemanticsIds` lists the nodes flagged focused,
  `expectStableFocusWhileTyping` types the first letter and expects the same focused node and the
  keyboard still in the field. Tests that use it run as Windows
  (`TargetPlatformVariant.only(TargetPlatform.windows)`); only there does the text field have the
  unfocus handler.
- `commit_message_test.dart` "the first letter keeps the keyboard in the field": fails without the
  fix, passes with it.
- `widgets_test.dart` "a filter field keeps the keyboard when its x appears": a guard; a plain
  field with only the `ClearButton` kept its node even before the fix, but any button added next
  to the X would bring the problem back.
- `commit_message_test.dart` "hjkl and wasd type into the empty field": pins that the navigation
  letters type and only the arrows step out (see debugging.md).
- The temporary commit trace in `changes_view.dart` (`[commit-trace]` lines in `out/live.log`,
  `_TracedFocusNode`) confirmed the fix in a `make live` run and is removed.
- Upstream: a Flutter issue is worth filing. The bridge sending "lost accessibility focus" when a
  node's own semantics are split is a framework or engine bug, and a text field that unfocuses
  on it turns an accessibility detail into lost typing.
