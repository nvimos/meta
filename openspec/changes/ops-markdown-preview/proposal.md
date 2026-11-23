# rendered markdown in the preview

Tags: ops, ui
Status: Proposed, for TASK-202. Built after `ops-configure` (TASK-204), which makes it a build option.

## Why

The preview pane shows a markdown file as its raw text. A README, a task or a proposal reads better
rendered: headings, lists, tables, code blocks. Sometimes the source is what I want (to check the
markup, to copy a line), so both views are needed.

## The idea

- A markdown file in the preview is shown rendered by default.
- A switch next to the pane's Preview label toggles between Rendered and Text. It is only there for
  markdown files and remembers the last choice.
- Rendered markdown stays selectable and copyable, like the text view.
- Code blocks use the same syntax highlighting as the text view; images that point into the repo
  resolve against the file's folder.
- Links work like a small browser:
  - a local link to another markdown file, followed in the rendered view, opens that file in the
    preview
  - the mouse's back button goes back to the file I came from, and its forward button goes forward
    again, as in a browser; following a new link drops the forward trail
  - a web link (`http://`, `https://`) is handed to the system, which opens it the way it opens any
    link (the default browser)
  - other local links (a file that isn't markdown) open the file the way the preview's Open button
    does
- Rendering is a build option: `make configure markdown=off` builds the app without the markdown
  package; the preview then shows the text only and has no switch.

## Use cases

- I select `README.md` in Add and Ignore. The preview shows the headings and the table rendered.
- I click `[the plan](PLAN.md)` in it. The preview shows `PLAN.md`; the mouse's back button brings
  `README.md` back, the forward button `PLAN.md` again.
- I click `https://docs.flutter.dev/...`. My browser opens the page; the preview stays where it was.
- I want to see why a list breaks. I flip the switch to Text, read the source, flip it back.
- The next markdown file I select opens in the view I left the switch in.

## Technical

- The renderer: `flutter_markdown_plus`, the maintained community fork of `flutter_markdown`, which
  flutter.dev discontinued. A `MarkdownBody` widget, built on the pure-Dart `markdown` parser; GFM
  tables, task lists, a `syntaxHighlighter` hook for `re_highlight`, `selectable`, an `onTapLink`
  callback and an image builder for relative paths.
  - others looked at: `markdown_widget` (its own table of contents and theming); the `markdown`
    parser with our own widgets (full control, several times the work)
- A build option, like PDF: the package `ops_markdown` in two variants, `packages/ops_markdown_on`
  (the renderer) and `packages/ops_markdown_off` (a stub, `markdownBuiltIn = false`); on by default,
  since it builds nothing native. `make configure markdown=off` points the dependency at the stub.
- Links
  - `onTapLink` gets the href; resolve it against the shown file's folder
  - `.md` (and `.markdown`): show that file in the preview, pushing the current one on the history
  - `http` / `https` / `mailto`: hand to the system (`ShellExecute` through `cmd /c start ""` or
    `explorer.exe`, the same way the Open button launches files; no `url_launcher` needed)
  - the app's back stack (`NavHistory`, `lib/ui/nav_history.dart`) only goes back today; it gets a
    forward stack: `back()` moves the place it leaves onto forward, `forward()` moves it back, a new
    `push` clears forward. The shell maps the mouse's forward button (`kForwardMouseButton`) to it.
    That makes forward work for every jump, not only links
- Fit with the project rules
  - parse once per file content, not per build (proportional work); a toggle only swaps the shown
    child
  - the switch is a small atom with tooltips and the pointer cursor; inside the `SelectionArea` its
    labels need `SelectionContainer.disabled`; links show the pointer cursor and their target as a
    tooltip
  - the choice goes into `Prefs`
  - check the new package for deprecated APIs and for tooltip semantics (`expectTooltipsInSemantics`)
- Effort: about a day with `flutter_markdown_plus`, plus a few hours for links and the forward
  history.
