# ops PDF preview

Status: To Do (backlog TASK-194)

## Why

Add and Ignore's preview can draw PDF pages through `pdfrx` (PDFium), ported from Purrage. The
library builds PDFium natively, which made every build slow, so it became an optional build
(`packages/ops_pdf_on` / `ops_pdf_off`, `make configure pdf=on|off`). Nothing tests the PDF build: on
2026-11-19 a release went out with PDF on that nobody had tried, and it was set back to a
prerelease. Until this change is done, PDF stays off everywhere: locally, in `make release`, and
in CI.

## What Changes

- a test that builds with PDF on and renders a page of a small sample PDF in the preview (the page
  is drawn, its size is right, no error pane)
- a CI job in `test.yml` that runs `tool/configure.ps1 -Pdf on`, then that test, on Windows; it fails the
  workflow when the PDF build breaks
- once that job is green: the CI release build (`release.yml`) always builds with PDF on
- local builds stay off: `make release` turns PDF off before it builds (done 2026-11-19);
  `make configure pdf=on` stays for trying PDF by hand
- the stub (`ops_pdf_off`) stays as the fallback for builds without PDF

## Scale

PDF is a small feature, one preview adapter among several. Its test is one test among the many CI
already runs, not a gate of its own: it goes into the normal test run (in its own job only because
it needs the PDF build), and a release waits on it the same way it waits on every other test.

## Decisions (2026-11-19)

- the CI test is the check; no manual checklist is required before PDF ships
- PDF is off in every build until this change is implemented, then always on in CI releases
- the promote flow is a separate change: `ops-release-promote`

## Impact

- `nvimos-poc-frontend/test/`: a PDF preview test and a sample PDF fixture (small, checked in)
- `nvimos-poc-frontend/.github/workflows/test.yml`: a PDF job
- `nvimos-poc-frontend/.github/workflows/release.yml`: pdf-on before the build
- open: the test must skip in the default (off) build, where `ops_pdf` is the stub; a tag or a
  separate test file run only by the PDF job
- open: CI time for the PDFium build, and whether `flutter-action`'s cache keeps it
