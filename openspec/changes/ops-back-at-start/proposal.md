# the back button and the automatic open

Status: Draft, for later. The current behavior (keep the entry) is what the app does now; this
proposal records the argument and the alternatives, not a decision to change it.

## Why

When Ops connects to a repository, `_openProject` asks the backend what the project is for and
shows the first mode with something to do: Pull request when there is a branch, else Changes when
the checkout is dirty, else Tasks. That call goes through `_setMode`, which is also the place where
a mode switch records where the user came from. So the automatic open leaves a place on the back
stack: pressing the mouse's back button right after launch returns to the mode that was shown
before the auto-open — in practice the top/start mode, Pull request.

Is that right? The user did not click anything to make that jump, so the entry is not a place they
navigate back to in the browser sense. On the other hand, the auto-open *does* replace what is on
screen, and the back button is described as "the previous place", not "the previous click". The
current decision is to keep it: back undoes the automatic jump and returns to the start mode. This
proposal is a place to decide whether that stays.

## What happens today

- The shell starts on Pull request (`_mode = Mode.pullRequest`), so the startup place is Pull
  request unless the saved rail hides it, in which case the shell shows the nearest visible mode.
- On connect, a post-frame callback calls `_openProject`. `_dirs.openingTarget()` answers Pull
  request, Changes or Tasks.
- `_openProject` calls `_setMode(target)` with the default `record: true`. The previous mode is
  pushed as `Back to <label>`; the target mode is shown.
- If the target is already the shown mode, `_setMode` records nothing. Back then has no entry from
  the auto-open.
- Pressing the back button pops that place and calls `_setMode(previous, record: false)`. The
  current behavior with a hidden previous mode is to show it: hiding means "off the rail", not
  "cannot be shown" (see PLAN.md, Back).
- The auto-open also happens once per backend generation (`_openedProject`), so a reconnect can
  add another entry. A project opened from Repos goes through the same `_openProject` and records
  a place too, but that one is a user action.

## The argument for keeping it

- **Back means "the previous place", not "the previous click".** The auto-open changed the place;
  undo returns to where the app was before it. A browser also keeps the page it started on, even if
  the session opened it for you.
- **It gives the app a home.** After the automatic open, one press of the back button is always
  "the top of the app". That is easy to explain and easy to reach when the project opened into
  Changes or Tasks and the user wanted the start mode.
- **One rule, one code path.** The alternative is a special case inside `_openProject`; the current
  behavior is what every `_setMode` does. A single rule is easier to keep correct as more jumps
  are added.
- **The history is already shallow at launch.** The auto-open entry is the oldest; the 50-place
  cap cannot push anything important out at startup.

## The argument against

- The user made no choice, so a back button that "undoes launch" can feel wrong: on a fresh start,
  back should arguably do nothing until the user navigates.
- The label is odd. The debug bar would say `Back: Back to Pull request` while the user has not
  been anywhere; "Back to Connect" might describe the mental model better, but the Connect screen
  is not a mode.
- If the auto-open lands on Pull request (already the start mode), nothing is recorded; the
  behavior then differs depending on what the project contains. That is consistent with "no
  change, no place", but it makes the first back press unpredictable from the user's seat.
- A user who connects, is auto-opened into Changes, and presses back lands in Pull request, not on
  the Connect screen. If their intent was "leave this project", back is the wrong affordance and
  the result may surprise them.

## Options

1. **Keep it (current).** The auto-open records a place; back returns to the start/top mode. Add a
   shell test and a sentence in PLAN.md. This is the current decision.
2. **Do not record the automatic open.** `_openProject` gets a `record` flag; the connect path
   passes `false`, a Repos click keeps `true`. Back after launch does nothing until the user
   navigates. The code becomes one special case, but the user model is cleaner.
3. **Record only when the auto-open actually moves the user.** Already true: if the target is the
   shown mode, nothing is recorded. This is an invariant to state, not a separate option.
4. **A separate "home" place.** Back after launch goes to a synthetic Start place (Pull request),
   not to a history entry. This is the current observable behavior but with a different stack:
   home is always there, and the auto-open is not an entry. It would also let a future "Home"
   button reuse the place. More code for the same first-press result.
5. **Clear the history on connect/project open.** A fresh project starts with no back places; a
   task link after the open is the first. This matches "a project is a context"; it also means the
   auto-open can never be undone, which is arguably best if the user picked the project. The
   downside: the history is also cleared for an automatic reconnect in the same project, losing
   useful task-link places.
6. **Record the Connect screen as a place.** Back would leave the project and return to the
   connect screen. That is a bigger product question: does back navigate between projects? It
   would need a "disconnect" restore and a different label. Not recommended without a separate
   proposal.

## Edge cases to settle if this changes

- **A hidden start mode.** With a saved rail that hides Pull request, the startup mode is the
  nearest visible one (Changes). The history label must name the mode actually shown, not Pull
  request.
- **The target equals the start mode.** No entry; back does nothing. Keep this, and say so in the
  test.
- **Reconnects.** `_openedProject` resets for a new backend generation, so a reconnect can
  auto-open again and add another entry. Is that a new place or a refresh of the same one? A
  dedupe (skip if the top place has the same label and restore) may be wanted.
- **User-opened project after an automatic one.** Two entries with the same label; back walks
  through both, which is correct but noisy. The debug bar makes it visible.
- **A user-opened project that lands in the shown mode.** No entry, same as the auto-open.
- **A hidden previous mode.** The current decision is to show it; a back restore must not silently
  switch to a different mode.
- **Alt+[ / Alt+] and the wheel.** They are steps, not places, and do not record. Back after
  stepping returns to the last recorded place, not the previous step. This is deliberate and
  documented in PLAN.md.
- **The debug bar.** If the label is shown, it should read `Back: Back to Pull request` or
  `Back: none`; the auto-open entry should not look like a user action. A future refinement could
  label it `Back to the start` or `Back to <mode>` without changing the restore.
- **Task links and reviews.** They push entries above the auto-open. Back from a task link returns
  to the auto-opened mode; a second back returns to the start mode. That is the history working as
  a stack, not a special case.
- **Dialogs and context menus.** They are routes above the shell; the back button should not pop
  the history while a modal is open. The root listener is below the overlay, so it does not.

## Tests this would need

- A shell test with a fake `openingTarget` and no Neovim: connect in a dirty checkout, assert the
  auto-open shows Changes, press `kBackMouseButton`, assert Pull request and the rail selection.
- The same with Pull request hidden in the saved rail: the start place is the nearest visible
  mode, not Pull request.
- The target already shown: back does nothing.
- A user-opened project from Repos: back returns to the mode that was shown before the click.
- The debug bar line: `Back: none` before any jump, the label after a jump, `none` after the
  stack is exhausted.
- An auto-open followed by a task link and a review: back walks review → task → auto-open target
  → start mode.

## Recommendation

Keep the current behavior for now. It is one rule, it gives a predictable first back press, and it
matches the "previous place" wording. Revisit only if the back button starts reading as "undo the
project I chose": then option 2 (do not record the automatic open) is the smallest change, and
option 5 (clear on connect) is the stronger statement. Whatever is chosen, record it in PLAN.md and
cover the hidden-start-mode and target-equals-start cases with tests.
