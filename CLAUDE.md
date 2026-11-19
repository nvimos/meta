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

## How to name tasks

A title says what the task is about, in a few words. Someone scanning the backlog should know the
topic and the action without opening the task.

1. **Start with the action or the topic, in plain words.** "evaluate vint", "lookup kubernetes spec",
   "adjust colorcolumn visibility", "drop map-jolemak", "move or document alma vimrc". A short verb
   comes first where one fits, a noun when the task is a whole area ("golang full support").
2. **Keep the one thing that identifies the task, drop the rest.** "Alma vimrc" stands in for
   `lua/genja/vimrc.almalinux.vim`. Paths, extensions and "the zero-byte stub" are detail for the
   body, not the title.
3. **Name the goal, not the current state or how to get there.** "colorcolumn stripe is the background
   plus a little gray" became "adjust colorcolumn visibility". Reasons ("same feel as PHP", "heavy
   vimscript editing") belong in the description.
4. **Drop context that other fields already carry.** Prefixes like "colors:" and "vint:" and asides
   like "started before 2027, alongside..." go; labels and the description hold that.
5. **A short phrase can say the decision.** "delete or fill" becomes "drop"; "write manifests with
   the spec at hand" becomes "lookup ... spec". Take the shorter word that keeps the meaning.
6. Aim for 3-5 words or 50-60 chars, lowercase, no trailing punctuation.
   Not a sentence; a phrase that scans well in a list.
7. Aim for clarity over brevity.
8. **Titles must differ by more than one word.** A shared template word ("finished work") is not a name;
   put the part that sets the task apart first and let the rest go. Statuses and labels already say
   what kind of task it is.
9. **Name what the work was about, not the bucket it sits in.** "look finished work" had a vague area
   word ("look") plus the shared tag; "color adjustments" says what was actually done. Pick the
   concrete subject (colors) and the kind of change (adjustments, tweaking), and leave the area label
   and the tag out.
10. **Rename in two passes.** When renaming a badly named task, apply these rules once and consider the
    result. Then apply them one more time to that result and judge whether the new proposal is better
    than the first; use whichever you prefer.

In one line: the topic plus what is wanted done to it, in plain words, with everything else pushed
down into the description.
