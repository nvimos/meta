# make configure: build options in one place

Tags: ops, build
Status: In progress, for TASK-204.

## Why

ops has one build option so far, the PDF pages, with three targets of its own (`pdf-on`, `pdf-off`,
`pdf-status`). Rendered markdown is about to become the second. A pair of targets per option doesn't
scale, and there is no single place that says how the current checkout is configured.

## The idea

- One step, `make configure`, in the spirit of `./configure` from the autotools, without autotools.
- Options are set as make variables: `make configure pdf=on markdown=off`. An option left out keeps
  its current setting.
- `make configure` with no options prints how the checkout is configured, one line per option.
- The setting stays until it is changed again: every later `make live`, `make dev`, `make build` uses
  it.
- Each option has a default (PDF off, markdown on); a fresh clone builds with the defaults without
  running configure.
- `make release` configures what it ships first, so a release never depends on what was left
  configured locally.

## Use cases

- I want to check the PDF build still compiles: `make configure pdf=on`, `make dev`, then
  `make configure pdf=off` again.
- I'm not sure what this checkout builds: `make configure` prints `off pdf` and ` on markdown`.
- I run `make release` while PDF is on locally. It switches PDF off before building.

## Technical

- An option is a Dart package in two variants with the same name and API, `packages/<pkg>_on` and
  `packages/<pkg>_off` (as `ops_pdf` is today). `pubspec.yaml` depends on the default variant.
- `tool/configure.ps1` writes the git-ignored `pubspec_overrides.yaml`, with a
  `dependency_overrides` entry for each option that differs from its default, and runs `pub get`
  when anything changed. No entries left: the file is removed. The file is the configuration; there
  is no second state file to drift from it.
- The options are one table in the script (name, package, default); a new option is a line there and
  its two packages.
- Output follows the scripts' style: one line per option, the state right-aligned, nothing for an
  option that was already so; `-WhatIf` for a dry run.
- `pubspec.lock` is committed from the default configuration; another one shows it as modified.
- Replaces `tool/pdf.ps1` and the `pdf-on` / `pdf-off` / `pdf-status` targets.
