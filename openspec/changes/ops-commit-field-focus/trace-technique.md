# The technique: a temporary trace in the running app

How the lost commit keys were tracked down once tests could not reproduce them, written so it can be
done again for the next bug of this kind: keys, text or focus that behave differently in `make live`
than in a widget test.

## When to reach for it

- widget tests replay the steps and the bug doesn't show
- the bug lives in what tests replace with fakes: the Windows engine, real timing, the accessibility
  layer, the IME, the mouse resting somewhere
- guessing would mean changing code without knowing which change matters

A trace turns "something takes the keyboard" into a timeline you can read, one run of the real
steps at a time.

## The idea

Four questions, each answered by one probe that writes a line to `out/live.log`:

| question                                | probe                                                         |
|-----------------------------------------|---------------------------------------------------------------|
| did the key reach the app, and where?   | a `HardwareKeyboard` handler that logs every key down         |
| did the text arrive?                    | a listener on the field's `TextEditingController`             |
| when did the field gain or lose focus?  | a listener on the field's `FocusNode`                         |
| who took the focus?                     | a `FocusNode` subclass that prints a stack trace on `unfocus` |

Every line carries the milliseconds since the view started and a fixed tag (`[commit-trace]`), so
`grep` picks them out of the log and the times can be compared. The gaps matter: a key handler
moves focus within a millisecond of its key, while a frame is about 16-50 ms; a change that comes
one frame after a key is the frame's doing, not the key's.

## How to add it

In the view's `State`, debug builds only (`kDebugMode`), so it can never ship:

```dart
import 'package:flutter/foundation.dart' show kDebugMode;

// TEMPORARY (<date>): trace of <field>, to find <symptom>. Remove once found.
final _messageFocus = kDebugMode ? _TracedFocusNode(debugLabel: 'commit message') : FocusNode(debugLabel: 'commit message');
final _traceClock = Stopwatch()..start();
void _trace(String what) => debugPrint('[commit-trace] ${_traceClock.elapsedMilliseconds.toString().padLeft(7)} ms  $what');

bool _traceKey(KeyEvent e) {
  if (e is KeyDownEvent || e is KeyRepeatEvent) {
    final focus = FocusManager.instance.primaryFocus?.debugLabel ?? '${FocusManager.instance.primaryFocus}';
    _trace('key ${e.logicalKey.keyLabel} char=${e.character} focus=$focus');
  }
  return false; // never claims the key: the app still sees it
}

@override
void initState() {
  super.initState();
  if (kDebugMode) {
    HardwareKeyboard.instance.addHandler(_traceKey);
    _message.addListener(() => _trace('text "${_message.text}" sel=${_message.selection.baseOffset}'));
    _messageFocus.addListener(() => _trace('field focus=${_messageFocus.hasFocus} '
        'attached=${_messageFocus.context?.mounted ?? false} '
        'primary=${FocusManager.instance.primaryFocus?.debugLabel}'));
  }
}

@override
void dispose() {
  if (kDebugMode) HardwareKeyboard.instance.removeHandler(_traceKey);
  super.dispose();
}
```

And the focus node that names the caller:

```dart
/// TEMPORARY: says who takes the keyboard from the field.
class _TracedFocusNode extends FocusNode {
  _TracedFocusNode({super.debugLabel});

  @override
  void unfocus({UnfocusDisposition disposition = UnfocusDisposition.scope}) {
    if (hasFocus) debugPrint('[commit-trace] unfocus($disposition) called from:\n${StackTrace.current}');
    super.unfocus(disposition: disposition);
  }
}
```

Notes:

- the `HardwareKeyboard` handler runs before every `Focus` handler, so it sees each key even when
  something else claims it; it returns `false` so it never changes what the app does
- `primaryFocus?.debugLabel` names the node that has the keyboard; give new `FocusNode`s a
  `debugLabel` (the project does already, for the debug bar)
- a node is created in a field initializer, so swapping it in needs a hot restart (`R`), not a hot
  reload (`r`)
- `attached` tells the two ways to lose focus apart: `unfocus()` was called (a stack trace appears)
  or the field's element was rebuilt and its node detached (`attached=false`, no stack trace)

## How to run it

1. Add the probes, `make analyze`.
2. `R` in `make live`.
3. Do the steps once, as the bug happens (here: `Alt+]` to Changes, `cc`, a quick burst).
4. Read the trace:
   `grep "commit-trace" out/live.log | grep -v "Alt Left"` (held Alt repeats flood it), and the
   lines after `unfocus(` for the stack trace.

## Reading it, this time

Round one gave the timeline: the first letter landed, the field lost focus 49 ms later, and the next
keys found the page's focus scope. That ruled out a key command (it would have moved focus at once,
and to the rail) and pointed at something on the next frame.

Round two added the stack trace on `unfocus`. It named the caller outright: the text field's "lost
accessibility focus" handler, called by the Windows accessibility bridge while the frame sent its
semantics update. From there, a widget test running as Windows could list the focused semantics
node before and after the letter and show its id changing: a reproduction without the real
machine, and the test that now guards the fix.

The verification run used the same trace: the keyboard stayed in the field through `hello`, held
keys and backspaces, and no `unfocus` stack trace appeared.

## Taking it out

Remove the probes, the `_TracedFocusNode` class and the `kDebugMode` import in the same change as
the fix, once a run of the real steps shows the fix working. `grep -n "commit-trace\|_trace"` on the
file must come back empty.
