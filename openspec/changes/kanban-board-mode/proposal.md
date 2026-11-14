# a board mode for the changes

Status: Open proposal, not decided. There is no backlog task yet; one gets made if we go ahead.

## Why

The Tasks mode lists the OpenSpec changes and the Backlog.md tasks, grouped and sorted. A list
answers "what is there", but not "where is each change". To see that, I open a change and read its
checkboxes. With a handful of changes that is fine; with twenty, some drafted last week by an agent,
some half built, some waiting for a tasks file, I want one picture: which changes are only an idea,
which are ready to build, which are being built, which are done and waiting to be archived.

A Kanban board is that picture. The npm package `specdeck` shows one for OpenSpec projects, and it
is a good one. I do not want to run it or depend on it: it is a Node server with a browser page,
and this app already has everything such a board needs, in Dart, inside the window I work in. What I
want is the same kind of board as a mode of Ops, built by reading how `specdeck` decides things and
doing the same in our own code.

## What I learned from the specdeck source

I read the source of `specdeck` 0.4.1 (MIT) without running it. These are the parts that matter
here.

**Lanes are never stored.** A change has no status field. Its lane is worked out from the files
every time: which artifacts exist and how many task boxes are ticked. The board can therefore never
disagree with the repository, and an agent that ticks a box in `tasks.md` moves the card without
anyone telling the board. The lanes, in order: Draft, Proposed, Specified, Ready, In Progress, Done,
Archived.

**The rule that places a card** is short:

- in the archive folder: Archived;
- `tasks.md` exists: no boxes, or none ticked: Ready; all ticked: Done; some ticked: In Progress;
- no `tasks.md`, and no artifact at all: Draft;
- no `tasks.md`, and everything `tasks.md` depends on is written (proposal, design, specs): Specified;
- otherwise: Proposed.

It does not name `proposal.md` or `tasks.md` in the rule. It asks the workflow schema which artifact
tracks the implementation and what that artifact needs, so a project with its own schema still gets
sensible lanes.

**An artifact is done when its file exists.** There is no judgement of quality. A one-line proposal
counts. An artifact whose dependencies are missing is blocked, otherwise it is ready to write.

**Tasks are only checkboxes.** `- [ ] 1.1 text`, under `## 1. Heading`. Plain bullets are not
tracked, and a tasks file full of bullets with no boxes is reported as a problem instead of showing
an empty list. A checkbox before any heading still counts.

**A board never moves a card by hand.** Dragging a card between lanes is refused by design, because
the next read of the files would undo it. The one drag that exists is archiving, because that is a
real action.

**Writes are narrow.** The only thing it writes is a task checkbox, and the write is refused when the
file changed since it was read.

Everything else in `specdeck` (the server, the browser editor, approval by git trailers, handing work
to an agent, a registry of projects) is a product around that board, and is not part of this
proposal.

## Backlog.md's board, to analyze later

Backlog.md, whose task files the Tasks mode already reads, has a Kanban board of its own. It is not
analyzed here, and nothing in this proposal is based on it. Before anything is built, its source
gets the same treatment as `specdeck`'s: read, not run, and written down in this proposal the way
the section above does. The questions to take to it:

- how a task lands in a column: from its `status` field, so the board shows a stored state, unlike
  `specdeck`'s derived one;
- which columns there are, whether they come from `backlog/config.yml`, and how they are ordered;
- how cards are ordered inside a column (the `ordinal` field), and what moving a card writes;
- what a card shows, and how milestones, labels and filters work on the board;
- what it does with many tasks and with tasks from several projects.

The two boards answer different questions. Backlog.md's says where a task is, by what someone
recorded. `specdeck`'s says where a change is, by what its files show. This app has both kinds of
thing, tasks and changes, so the Board mode may need a switch between the two, or one board with the
change's lane and the task's status side by side. That is decided after both are understood.

## The idea

A new mode, the Board, between Tasks and Directories on the rail. It shows the changes of the Active
Directory's planning folder as columns, one per lane, left to right in the order above. Each change
is a card: its name, how many boxes are ticked out of how many, and the Backlog.md task it belongs to
when it has one. A lane with nothing in it stays visible but thin.

The lanes are derived in Dart from the files the Tasks mode already loads (`Workspace`): the
proposal, design, spec deltas and tasks of each change, and whether it sits in the archive. Nothing
new is stored and nothing new is read from disk. When a file changes, in Neovim or outside it, the
workspace reloads and the card moves, the way every other mode follows the backend.

The board does not invent a status. It also does not replace the status of the Backlog.md task: a
task's To Do, In Progress and Done stay where they are, in the Tasks mode. A card can show its
task's status as a small mark, but the lane comes from the change's files alone. Where the two
disagree, for instance a task marked Done whose change is still In Progress, the card says so; that
disagreement is useful to see.

Clicking a card opens the same change detail as in the Tasks mode, in a panel from the right.
Ticking a box there already works and already refuses a stale file, so a card moves in front of me
when I tick the last box.

## Use cases

Each case is written from where I sit.

### Where is everything

I switch to the Board. Seven columns. Draft has two cards an agent started last night: a proposal
and nothing else. Specified has one: proposal, design and specs are written, but no task list yet.
Ready has three, In Progress two, Done one, and Archived is folded to a thin strip because I rarely
want it. I see that three changes are ready to build and nobody has started them, which is the thing
I came to find out.

### A card moves by itself

An agent works through `tasks.md` of a change that is In Progress. I leave the Board open. As the
last box is ticked, the card moves from In Progress to Done. Nobody pressed anything on the board.

### Why is this card here

A change sits in Proposed although I think I wrote everything. I open it and see that the design
is missing; the card shows that the lane is Proposed because `design.md` does not exist yet, not
because someone decided so. I write the file in Neovim and the card moves to Specified.

### A tasks file with no boxes

An agent wrote `tasks.md` with plain bullets. The card sits in Ready and shows a warning: the file
has bullets but no checkboxes, so none of it counts as progress. This is better than a card that
claims nothing has been started.

### Dragging

I try to drag a card from Ready to Done. Nothing moves, and a short note says lanes come from the
files. Dragging a Done card to Archived is the exception and asks first, like archiving in the Tasks
mode does today.

## How it could fit the app

This section is the technical side, and is a first guess.

- `lib/tasks/lanes.dart`: a pure function from a change's artifacts and task counts to a lane,
  with the rule above, and unit tests. The artifacts and the task counts are in the model already
  (`parse.dart`, `model.dart`).
- `lib/ui/board_view.dart`: the mode. The columns are a horizontal list of lists built from data,
  with named sub-widgets for the lane and the card, following `declarative_ui_guidelines.md`.
- The rail gets a sixth mode, so `M-1` to `M-5` become `M-1` to `M-6`; the Keys table, the Help
  mode and the debug bar's role table get the new entries.
- Keys, in the pane and list vocabulary of the other modes: Left and Right (`h`, `l`) between lanes,
  Up and Down (`j`, `k`) between cards, past the last lane Right goes nowhere, Left from the first
  lane goes to the rail, Enter opens the detail, Esc closes it, `gg` and `G` first and last card.
  The Tab cycle: the rail, then the lanes, then the detail.
- The workflow schema: OpenSpec projects can have their own. A first version assumes the default
  (`tasks.md` tracks the work, and needs the proposal, design and specs). Reading the schema file
  to find the tracked artifact is a second step.
- Performance: the lanes are derived when the workspace loads or reloads, not in `build`. Moving a
  card is a re-derivation of that one change.

Taking ideas from `specdeck` is fine under its MIT licence. We write our own code, and the
proposal's text names it as the source of the lane rule and the "nothing is stored" principle.

## Open questions

- Should the Archived lane exist at all, or is archiving a change in the Tasks mode enough?
- Should a card show its Backlog.md task's status, or only the change's own progress?
- The lane names: `specdeck` uses Draft, Proposed, Specified, Ready, In Progress, Done, Archived.
  Ours could be closer to the Tasks mode's words (To Do, In Progress, Needs Test, Done). The
  derivation does not depend on the names.
- One board for the whole planning folder, or a project filter like the Tasks mode has (`a` toggles
  every project's changes).
- Whether to look at git as well: a change that exists on another branch only, or has uncommitted
  edits, is something `specdeck` marks on the card. The Pull request and Changes modes already know
  git, so this could come later.
