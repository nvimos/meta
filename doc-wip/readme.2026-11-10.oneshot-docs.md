# Where the POC projects' state, decisions and look and feel are recorded

Each POC project has a one-shot v1 note in its own `doc-wip/`. It records everything needed to
pick the work up again later. Both notes are committed in their repos.

| Project  | Note                                                             | Commit  |
|----------|------------------------------------------------------------------|---------|
| backend  | `~/es/nvimos-poc-backend/doc-wip/oneshot.nvimos-poc-backend.v1.md`   | 5ca3ba0 |
| frontend | `~/es/nvimos-poc-frontend/doc-wip/oneshot.nvimos-poc-frontend.v1.md` | ab711dc |

The app name in the file names is the folder name.

## What each note holds

- **What it is**, with links to the original prompts in `poc-nvim-backend/`.
- **State:** what's done, the test counts, and how it was checked: screenshots, a scratch clone,
  a real agent run, and the run on the real Neovim on 2026-11-10.
- **Decisions:** the setup wizard answers, and the design choices made along the way, each with
  its reason.
- **Look and feel** (frontend):
  - every color with its hex value and what it's used for;
  - fonts and text sizes;
  - the pixel layout of each screen;
  - status and priority icons, the parts of the detail panel, keys, and the inbox groups.
- **Style and conventions:** code style, Makefile, line endings, commit style, and the rules for
  working in the POC folders.
- **Lessons and gotchas:** for example lazy.nvim dropping the plugin at startup, and Flutter on the
  exFAT drive.
- **Gaps against the prompts, and ideas for v2.**

## Gaps found while writing the frontend note

- There's no board view, though the README says there is.
- There are no saved views, such as "agent tonight".
- The change detail shows its parts stacked instead of as tabs.
- The OpenSpec CLI summaries (`openspec list` and the like) are never read.
