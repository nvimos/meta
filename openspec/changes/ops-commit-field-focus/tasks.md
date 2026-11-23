# Tasks

## 1. Debug

- [x] 1.1 replay the steps in widget tests: the Changes view, the full shell on a local repo, `cc`
  and a click, the stage refresh during the burst (no repro)
- [x] 1.2 a temporary trace in the running app: keys, text, focus changes of the field
- [x] 1.3 rule out the navigation keys (hjkl, wasd) and pin them with a test
- [x] 1.4 a stack trace on `unfocus`: the Windows accessibility bridge, via the text field's
  "lost accessibility focus" handler
- [x] 1.5 find why the bridge saw the focus move: the X appearing gives the field a new semantics node

## 2. Fix

- [x] 2.1 `Semantics(container: true)` around the commit field's buttons and around `ClearButton`
- [x] 2.2 tests running as Windows: the commit field and a filter field keep their focused node and
  the keyboard after the first letter
- [x] 2.3 verify in `make live`: `cc`, type a burst, every letter in the field (2026-11-23: `hello`,
  held keys and backspaces kept the keyboard; no `unfocus` in the trace); a filter field not
  checked by hand yet
- [x] 2.4 remove the temporary commit trace (`[commit-trace]`, `_TracedFocusNode`)
- [x] 2.5a write the trace technique down, with the code to add it (`trace-technique.md`)
- [ ] 2.5 CLAUDE.md: the cause and the rule for buttons inside a text field
- [ ] 2.6 file the Flutter issue
