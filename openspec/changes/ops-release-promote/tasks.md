# Tasks

## 1. Prerelease first

- [ ] 1.1 `release.yml` publishes with `--prerelease`
- [ ] 1.2 `make release` publishes with `--prerelease`
- [ ] 1.3 the weekly gate's handling of unpromoted prereleases decided and done

## 2. Promote

- [ ] 2.1 `promote.yml`: `workflow_dispatch` with a tag (default the newest prerelease), runs
  `gh release edit <tag> --prerelease=false --latest`
- [ ] 2.2 `make promote TAG=` does the same locally
- [ ] 2.3 promote refuses a tag that is not a prerelease

## 3. Verify

- [ ] 3.1 a dispatched release run ends as a prerelease; promote makes it Latest
- [ ] 3.2 `PLAN.md` / `CLAUDE.md` describe the flow
