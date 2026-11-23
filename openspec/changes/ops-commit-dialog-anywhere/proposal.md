# the commit message as a dialog from any mode

Tags: ops, ui
Status: Proposed, for TASK-209. Not started; an idea to try, not a settled design.

## Why

The commit message lives in Changes: its field under the file lists, and a large dialog
(`CommitMessageDialog`) opened from there. Staging often happens elsewhere (Add and Ignore, the
Pull request view, Neovim), and writing the message means switching to Changes first. A message
started and left half done is easy to lose.

Whether a modal is the right shape is an open question; the proposal is to try it.

## The idea

- One key, from any mode, brings up the commit message as a dialog over the app, like a dialog on a
  web page: the app dims behind it.
- Inside, a text area about 90 characters wide and 6 lines tall by default, with room around it; it
  can be resized (a grip at its lower right corner), and the dialog grows with it.
- Three buttons at the bottom:
  - **Accept**: commit with the message; the dialog closes and the draft is cleared
  - **Hide**: close and keep the text; it is there again the next time the dialog comes up
  - **Cancel**: close and throw the text away
- An **X** in the upper right corner, **Esc**, and a click outside the dialog also close it. They
  keep the text, like Hide, so nothing typed is lost by a stray click or key (to be confirmed: the
  alternative is that they act like Cancel).
- The draft is one: the same text as the commit field in Changes, so starting in one and finishing
  in the other works.

## Use cases

- I stage two files in Add and Ignore, press the key, write `add-ignore: all files toggle` and the
  body, and Accept. The commit is made without leaving Add and Ignore.
- Halfway through the body I want to check a diff. I press Hide (or Esc), look at Pull request,
  bring the dialog back: the text is still there, the caret where I left it.
- I started a message for the wrong change. Cancel clears it.

## Technical

- `showDialog` with `barrierDismissible: true` (a click outside), `barrierColor` for the dimmed
  app; a `Dialog` with a title row (the X as an `IconButton`, tooltip, pointer cursor) and the
  buttons in its actions row, each with a tooltip and the pointer cursor.
- The text area: a `TextField` (`maxLines: null`, `expands: true`) in a box sized in characters and
  lines from the code font (`TextPainter` for one character's width and the line height): 90 × 6 by
  default, plus padding. Resizing: a drag grip at the corner, anchored to the pointer as the side
  pane's edge is (start size + pointer travel), clamped to the window; the size is remembered.
- The draft: moved out of the Changes view into a `CommitDraft` `ChangeNotifier` on the session, so
  both the Changes field and the dialog edit the same text and selection. Hide, X, Esc and the
  barrier pop without touching it; Cancel clears it; Accept commits through the action queue (as
  Changes does) and clears it on success, keeping it on failure with the error shown.
- Keys: the shell owns the key (it is app-wide), so it goes into the shell's handler, `keyTable`
  and the Keys table. Candidates: `Ctrl+Shift+C`, or `cc` as Fugitive has it (a plain key is
  ignored while typing in a field anyway). Ctrl+Enter accepts inside the dialog, as today.
- The existing `CommitMessageDialog` (Neovim's `git commit` look with the commented template) is
  either replaced by this dialog or becomes its "full" form; to decide when building.
- The shell dismisses tooltips on a mode switch; the dialog is a route above every mode, so a mode
  switch is not possible while it is up.
