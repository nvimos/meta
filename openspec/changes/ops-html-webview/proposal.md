# HTML pages in a real browser engine

Tags: ops, ui
Status: Proposed, for TASK-206. Not started; only if the light renderer is not enough.

## Why

The preview draws HTML without a browser (`ops-markdown-preview`, `flutter_widget_from_html_core`):
tags and basic CSS, no JavaScript. That is right for generated docs, reports and notes. A real web
page (a built site, a coverage report with scripts, a page laid out with flexbox or grid) comes out
broken, and the Open button is the only way to see it as it is.

## The idea

- An HTML file can be shown by the real engine, the one Edge uses, inside the preview.
- It is a third view next to Rendered and Text (Browser), or it replaces Rendered for HTML when the
  build has it; to be decided by trying both.
- Scripts are off by default; a local page never reaches the network unless I allow it for that page.
- A build option like PDF: `make configure webview=on`; without it the light renderer stays.

## Use cases

- I highlight `coverage/index.html`. The preview shows the report as Edge would, its tables and
  colours intact.
- I highlight a page from a static site build. Its layout is right; links to other pages of the site
  open in the preview as they do today.

## Technical

- Windows 11 ships the engine: WebView2 (Edge, Chromium). Nothing large is bundled; the
  `webview_windows` package (or `flutter_inappwebview`'s Windows support) wraps it.
- What makes it a few days, not one:
  - it is a native view drawn into a texture: it needs a fixed height, while the preview is a list
    of several files one under the other. Likely: a browser view only when a single HTML file is
    highlighted, filling the pane
  - keys and focus: the view takes the keyboard while focused, so the app's keys (pane motion,
    Alt+1..9) need a way out (Esc, or the shell's keys handled before it)
  - overlays: tooltips and menus over the view, and the text is not part of the app's selection
  - security: JavaScript off unless allowed, no network for `file:` pages, no downloads
  - the runtime: present on Windows 11; the stub shows the light renderer when it is missing
  - navigation inside the view: links handled by the app's history (back / forward), not by the
    view's own
- Like PDF, the build is slow to try and needs a test that builds it in CI before a release ships
  it on.
