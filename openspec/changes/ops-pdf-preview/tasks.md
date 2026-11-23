# Tasks

## 1. Off until tested

- [x] 1.1 `make release` turns PDF off before it builds; PDF off locally
- [x] 1.2 the untested PDF release v2026-11-19 set back to a prerelease

## 2. Test

- [ ] 2.1 a sample PDF fixture in `test/`
- [ ] 2.2 a test that renders its first page in the preview with PDF on (skipped or not run with
  the stub)
- [ ] 2.3 a CI job that turns PDF on and runs that test on Windows

## 3. Ship

- [ ] 3.1 `release.yml` builds with PDF on, once 2.3 is green
- [ ] 3.2 `PLAN.md` and `CLAUDE.md` say PDF ships in CI releases
