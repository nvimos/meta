# Tasks

- [x] 1 `Repo.trackedFiles` (`git ls-files -z`)
- [x] 2 `AddIgnoreState.showTracked`: the Tracked section, read on toggle and after each refresh,
  replaced only when changed; remembered in `Prefs` (`addIgnoreAllFiles`)
- [x] 3 the toggle button left of the preview button (tooltip, lit while on) and the key `T`
- [x] 4 tracked rows: untrack and the eye, no add; a muted `·` letter with a tooltip
- [x] 5 tests: the section shows and hides, no duplicates, a cursor move keeps the rows, a refresh
  with the same files keeps them, a real repo's `ls-files`
- [x] 6 `PLAN.md`, Help, the Keys table
- [ ] 7 try it in the app on a big repository (thousands of files): the toggle and a refresh stay quick
