# nvimos-meta

Planning repo for On-Screen Nvim (see README.md). The two proof-of-concept projects are steered from
here: the user gives instructions in this repo, the code goes in their own folders.

## POC projects

| Folder                       | What                                                                 | Prompt                         |
|------------------------------|----------------------------------------------------------------------|--------------------------------|
| `~/es/nvimos-poc-backend`    | relay (`nvimos/relay`): Lua plugin for Neovim that streams typed, ordered state events (buffers, cursor, git) to an RPC client, in place of a C patch to Neovim | `poc-nvim-backend/nvim-patch.md` |
| `~/es/nvimos-poc-frontend`   | Ops (`nvimos/ops`): Flutter desktop app: GitHub Desktop-style review of two branches and of the working tree, kept in sync with a running Neovim over msgpack-RPC; later a Tasks mode for OpenSpec / Backlog.md | `poc-nvim-backend/flutter.md`, `poc-nvim-backend/flutter-project-man.md` |

The prompts in `poc-nvim-backend/` are the original requirements. The Lua plugin comes first; the C
patch (`nvim_attach_ui_stream`) is planned in parallel, for what the plugin can't do (marks, signs,
extmarks, pushing events to clients as they connect). The frontend is a
native Windows app: Flutter for Windows is in `H:\flutter` (Visual Studio 2022 has the C++ tools).
The WSL distro `alma` also has a Flutter, which the POC doesn't use.

### Rules for work in the POC folders

These apply only inside the two folders above, not to this repo.

- Each project is its own git repo on branch `main`, public on GitHub: relay is `nvimos/relay`,
  Ops is `nvimos/ops`. Push only when the user asks.
- Commit as you go: one commit per feature, one per fix. Plan the steps before writing code.
  Don't ask before committing; commit and move on.
- Work directly in the main checkout on `main`. No worktrees or branches unless the user asks; Claude
  works alone there, the user only makes small changes now and then.
- Code for a POC goes only in its folder, never in this repo.

## Proposals

- An open proposal is something the user wants to do sometimes, not a fixed format. There is no house
  style for proposals: `openspec/changes/merge-beside-checkout` was a one-off, so don't use it as a
  template.
- When the user says to add a proposal, do your best with what was said. Don't overinterpret the
  request: no extra structure, sections or follow-up work that wasn't asked for.
