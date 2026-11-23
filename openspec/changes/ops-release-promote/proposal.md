# ops release promote

Status: To Do (backlog TASK-195)

## Why

The weekly CI release (`release.yml`, Wednesdays) builds and publishes straight to a release, and
GitHub marks it Latest. Nobody has tried that build first. On 2026-11-19 an untested build became
Latest and had to be set back to a prerelease by hand. A build should be tested before it becomes
the release people download.

## What Changes

- the scheduled release publishes a **prerelease** (`vYYYY-MM-DD`, not Latest), as today's gate and
  build already do, only the flag changes
- a new manual workflow, **promote** (`workflow_dispatch`, input: the tag, default the newest
  prerelease): it turns that prerelease into the release and marks it Latest
- promote only takes a prerelease that exists; it builds nothing, so the promoted files are exactly
  the ones that were tested
- `make release` (local) publishes a prerelease too, so a local upload also waits for promote
- a local `make promote TAG=` runs the same `gh release edit` for when CI is not at hand

## Decisions (2026-11-19)

- flow: build, then promote (not artifact-only, not the automatic weekly Latest)
- separate from the PDF change (`ops-pdf-preview`)

## Impact

- `nvimos-poc-frontend/.github/workflows/release.yml`: `gh release create --prerelease`
- new `nvimos-poc-frontend/.github/workflows/promote.yml`
- `nvimos-poc-frontend/Makefile`: `release` adds `--prerelease`; a new `promote` target
- the weekly gate counts prereleases as releases, so an unpromoted build doesn't start a new one
  every week (open: or it should, and older prereleases get pruned)
