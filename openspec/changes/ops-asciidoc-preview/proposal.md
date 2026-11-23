# AsciiDoc in the preview, like markdown

Tags: ops, ui
Status: Proposed, for TASK-207. Not started.

## Why

Some repos write their docs in AsciiDoc (`.adoc`, `.asciidoc`) instead of markdown. The preview
renders markdown and HTML (`ops-markdown-preview`) but shows AsciiDoc as raw text.

## The idea

- An AsciiDoc file in the preview is rendered, exactly like a markdown file: the same Rendered /
  Text switch, the same remembered choice, selectable text.
- Links work the same: another AsciiDoc, markdown or HTML file shows in the preview, with the
  mouse's back and forward buttons; a web link goes to the browser; `xref:` and `<<id>>` cross
  references to another file open it, an anchor in the same file does nothing.
- A build option like the others: `make configure asciidoc=on|off`.

## Use cases

- I highlight `docs/manual.adoc`. The preview shows its title, sections, lists, admonitions
  (NOTE, TIP, WARNING) and source blocks.
- I click `xref:install.adoc[Install]`. The preview shows `install.adoc`; back returns.

## Technical

- There is no mature AsciiDoc renderer for Flutter. Options:
  - convert AsciiDoc to HTML in Dart and draw it with the HTML renderer the preview already has
    (`ops_html`). An AsciiDoc-to-HTML package on pub.dev, if one covers the common subset (sections,
    lists, tables, source blocks, admonitions, includes off); else a small converter of our own for
    that subset
  - call `asciidoctor` when it is installed (Ruby or the JS build): full fidelity, but an outside
    tool, slow to start, not on most Windows machines
  - recommended: the Dart conversion for the common subset, drawn by `ops_html`; nothing native
- Fit with what exists
  - `DocKind.asciidoc` and `.adoc` / `.asciidoc` in `DocumentAdapter.kindOf`; the switch and the
    pref (`previewRendered`) already cover every document kind
  - links: the converter turns `xref:` and `<<file#id>>` into `<a href>`; `resolveLink` and the
    back / forward trail take them as they are
  - `include::` directives are not followed (they read other files; the preview reads one)
- Effort: about a day with a usable package, two or three with our own converter for the subset.
