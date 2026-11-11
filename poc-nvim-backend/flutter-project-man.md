Project: Folio, a Linear-style workspace for OpenSpec and Backlog.md, inside the Nvim-backed review app

The Tasks mode of the review app from `flutter.md` (`~/es/nvimos-poc-frontend`). It turns a repo's
planning files into something that feels like Linear: dense, calm, everything clickable, nothing
that looks like Markdown. Same app, same Neovim connection, same backend plugin
(`~/es/nvimos-poc-backend`). "Folio" is the working name from the mock-up.

Why

OpenSpec has each change agreed on before code is written (proposal, spec deltas, design, tasks),
then archived into a living spec. Backlog.md is the lighter cousin: one Markdown file per task.
Both are cumbersome to drive by hand. They have different jobs and work well side by side:
- Backlog.md tracks what to do.
- OpenSpec records what a change does to the system. The living spec is what I trust when I come
  back to a project months later, instead of chat history or thousands of lines of config.

Core use case

In the evening I triage: pick tasks for agents tonight, approve the drafted proposals. In the
morning the inbox shows what moved; I open each task, review its agent branch in the Pull request
mode, try it by hand from its Verify list, and move it on. Finished changes get archived into the
living spec. Anything I want to edit opens in Neovim.

Main ideas

- Linear's ideas, not its name or assets: a sidebar, a list, a detail panel from the right; dark,
  dense and calm with one accent color.
- An inbox first: what changed since I last looked, and what needs attention.
- Everything is a record I can open: tasks, changes, requirements, milestones, specs, old notes.
- No Markdown look: requirements as cards, tasks as checklists, statuses as badges.
- A spec browser that shows every change that ever touched a requirement.
- The old notes (`legacy/`) stay readable, and any of them can become a task.
- Milestones come from the files (dates or archive points); no database.
- Reviewing a task's branch opens the Pull request mode with its Verify list beside the diff.
- An agent can draft a whole change from one sentence; I approve it in the app.

Data

- The files in the repo are the database, written back the way a human or the CLIs would write
  them. A repo may have only Backlog.md or only OpenSpec; when both exist they are linked.
- All reading and writing goes through Neovim, so unsaved edits show and changes made by me or an
  agent appear within a second or two. The CLIs are used when installed, never required.

Non-goals for the first version

- Our own task format, a database or a server; sync with GitHub Issues, Jira or Linear.
- Editing prose inside the app; that happens in Neovim.
- Multiple users, time tracking, sprint planning.
- Agent orchestration beyond "start one for this change".

Source: Grok conversation "OpenSpec Inquiry"
<https://grok.com/share/bGVnYWN5_08dd64e6-2dfd-4a0a-a318-3707097cdc52> (full text in the print
`poc-project-man.pdf`), including its HTML prototype and the "Folio" mock-up, neither of which is
saved here.

`~/es/nvimos-poc-frontend/PLAN.md` holds the details and wins where it disagrees with this file.
