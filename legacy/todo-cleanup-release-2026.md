# cleanup for the 2026 release (from todo-ideas/cleanup-release-2026.md, an outside review 2026-11-08)

## cleanup release 2026

- [ ] verify a clean-machine install on Linux, not just Windows (2026-11-08)
  - tests/startup covers a clean clone on Windows only
- [ ] delete or fill the zero-byte `lua/genja/map-jolemak.lua` stub (2026-11-08)
- [ ] collapse the `lua/lazyp/unused-*` folders (2026-11-08)
  - specs marked `-- not used: 2026-10` keep their comment; decide which folder they live in
- [ ] move or document `lua/genja/vimrc.almalinux.vim` (2026-11-08)
  - CLAUDE.md "Alma vimrc split" says what it is; the README doesn't
- [ ] give the empty `lua/genja/ui` directory real code or remove it (2026-11-08)
  - check: gui-func-state lives in lua/genja/ui/gui-func-state/, so it may not be empty any more
- [ ] trim the F2 subsystem readmes (2026-11-08)
- [ ] experimental `zexp-*` files: keep, move or delete (2026-11-08)
- [ ] alternate readmes and `do.not.readme.md`: merge or remove (2026-11-08)
- [ ] todo files out of the config repo into nvimos/meta (2026-11-10)
  - [x] nvimos/meta with Backlog.md and OpenSpec side by side (2026-11-10)
  - [ ] todo-ideas.md, todo-202x.md, squash files, todo-ideas/ removed from the config, pointer left
  - [ ] skills (auto-todo, update-todo, close-issues) and CLAUDE.md point at meta
