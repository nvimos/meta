# Tasks

- [x] 1 `tool/configure.ps1`: an option table, reads the state from `pubspec_overrides.yaml`, writes
  the overrides that differ from the defaults, `pub get` on a change, `-WhatIf`
- [x] 2 `make configure` (`pdf=`, `markdown=`); with no options it prints the configuration
- [x] 3 `make release` configures `release_config` (`-Pdf off -Markdown on`) first; drop `pdf-on`,
  `pdf-off`, `pdf-status` and `tool/pdf.ps1`
- [x] 4 the stub's message, `CLAUDE.md`, `analysis_options.yaml` and the `ops-pdf-preview` proposal
  name `make configure pdf=on`
- [x] 5 add `markdown` with the `ops-markdown-preview` packages
- [x] 6 Makefile variables lowercase (`pdf=on`, `test_timeout=`, `version=`); only the exported
  `PUB_CACHE` and `CMAKE_BUILD_PARALLEL_LEVEL` keep their names
