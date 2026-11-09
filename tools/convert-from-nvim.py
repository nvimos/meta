# convert.py <nvim-config-dir> <meta-dir>: todo markdown -> Backlog.md tasks + OpenSpec changes.
# Every top-level checkbox item ("- [ ]", "-[x]", "-[n]", ...) of the todo files becomes one task and one
# change. Build steps and verify steps are kept apart; the original text is kept verbatim in both.
import io
import os
import re
import sys

SRC, DST = sys.argv[1], sys.argv[2]
FILES = ['todo-ideas.md', 'todo-2026-neovim011.md', 'todo-2027.md', 'todo-2028.md', 'C:/Users/jazzo/AppData/Local/Temp/claude/17f1b8d43c23617b/a7774b26-80f0-45a1-97aa-bdda65c32ea5/scratchpad/meta/todo-cleanup-release-2026.md']
TODAY = '2026-11-10'

ITEM = re.compile(r'^-\s?\[(.)\]\s?(.*)$')
SUB = re.compile(r'^(\s+)-\s?\[(.)\]\s?(.*)$')
DATE = re.compile(r'(20\d\d-\d\d-\d\d)')
VERIFY = re.compile(r'^(test|try|check)\b|untested|not tested|by hand', re.I)


def slug(text, words=6):
    text = re.sub(r'`[^`]*`', lambda m: m.group(0).strip('`'), text)
    parts = re.findall(r'[a-z0-9]+', text.lower())
    return '-'.join(parts[:words]) or 'item'


def title_of(first):
    t = re.sub(r'\s*\((?:[^()]*20\d\d-\d\d-\d\d[^()]*)\)\s*$', '', first).strip()
    t = t.rstrip(':').strip()
    if len(t) > 90:
        t = t[:87].rsplit(' ', 1)[0] + '...'
    return t or 'untitled'


def parse(path):
    items, section, cur = [], '', None
    for line in io.open(path, encoding='utf-8').read().splitlines():
        h = re.match(r'^(#{1,3})\s+(.*)$', line)
        m = ITEM.match(line)
        if h:
            section = h.group(2).strip()
            cur = None
            continue
        if m:
            cur = {'mark': m.group(1), 'first': m.group(2).strip(), 'lines': [line], 'section': section,
                   'file': os.path.basename(path)}
            items.append(cur)
            continue
        if cur is not None and (line.startswith((' ', '\t')) or line == ''):
            cur['lines'].append(line)
        elif cur is not None:
            cur = None  # prose at column 0 ends the item
    for it in items:
        while it['lines'] and it['lines'][-1].strip() == '':
            it['lines'].pop()
    return items


def classify(it):
    """Status, build steps, verify steps for one item."""
    build, verify = [], []
    first_cont = []
    for line in it['lines'][1:]:
        m = SUB.match(line)
        if m:
            done = m.group(2) in 'xX'
            text = m.group(3).strip()
            (verify if VERIFY.search(text) else build).append((done, text))
        elif line.strip():
            first_cont.append(line)
    block = '\n'.join(it['lines'])
    mark = it['mark']
    open_verify = [v for v in verify if not v[0]]
    untested = bool(re.search(r'untested|not tested', block, re.I))
    if mark in 'nN':
        status = 'Dropped'
    elif mark in 'xX':
        status = 'Needs Test' if (open_verify or untested) else 'Done'
    else:
        build_done = build and all(b[0] for b in build)
        if build_done and (open_verify or untested):
            status = 'Needs Test'
        elif any(b[0] for b in build) or mark not in ' ':
            status = 'In Progress'
        else:
            status = 'To Do'
    if untested and not open_verify and status == 'Needs Test':
        verify.append((False, 'try it by hand (marked untested in the notes)'))
    return status, build, verify, first_cont


def frontmatter(task_id, it, status, labels, date):
    q = it['first'] and title_of(it['first']).replace("'", "''")
    lines = ['---', f'id: TASK-{task_id}', f"title: '{q}'", f'status: {status}', 'assignee: []',
             f"created_date: '{date}'", 'labels:']
    lines += [f'  - {l}' for l in labels]
    lines += ['dependencies: []', f'ordinal: {task_id * 1000}', '---', '']
    return lines


def checklist(steps, numbered_ac=False):
    out = []
    for n, (done, text) in enumerate(steps, 1):
        box = 'x' if done else ' '
        out.append(f'- [{box}] #{n} {text}' if numbered_ac else f'- [{box}] {text}')
    return out


def notes(cont):
    """The item's plain sub-lines (not checkboxes), dedented, as they were written."""
    if not cont:
        return []
    indent = min(len(l) - len(l.lstrip()) for l in cont)
    return [l[indent:] for l in cont] + ['']


def main():
    tasks_dir = os.path.join(DST, 'backlog', 'tasks')
    archive_dir = os.path.join(DST, 'backlog', 'archive', 'tasks')
    changes = os.path.join(DST, 'openspec', 'changes')
    for d in (tasks_dir, archive_dir, os.path.join(changes, 'archive')):
        os.makedirs(d, exist_ok=True)
    n = 0
    seen = set()
    index = []
    for f in FILES:
        for it in parse(os.path.join(SRC, f)):
            n += 1
            status, build, verify, cont = classify(it)
            title = title_of(it['first'])
            m = DATE.search('\n'.join(it['lines']))
            date = m.group(1) if m else TODAY
            labels = [slug(f.replace('.md', ''), 3)]
            if it['section']:
                labels.append(slug(it['section'], 4))
            original = ['```markdown'] + it['lines'] + ['```']
            src = f"`{f}`" + (f", section \"{it['section']}\"" if it['section'] else '')

            # Backlog.md task
            fname = f"task-{n} - {re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-')[:70]}.md"
            body = frontmatter(n, it, status, labels, date)
            body += ['## Description', '', title, ''] + notes(cont) + [f'From {src}.', '']
            if build:
                body += ['## Acceptance Criteria', ''] + checklist(build, True) + ['']
            if verify:
                body += ['## Verify', '', 'Hands-on checks, kept apart from the build steps.', ''] + checklist(verify) + ['']
            body += ['## Original notes', ''] + original + ['']
            folder = archive_dir if status in ('Done', 'Dropped') else tasks_dir
            io.open(os.path.join(folder, fname), 'w', encoding='utf-8', newline='\n').write('\n'.join(body))

            # OpenSpec change
            cid = slug(title)
            while cid in seen:
                cid += '-' + str(n)
            seen.add(cid)
            if status in ('Done', 'Dropped'):
                cdir = os.path.join(changes, 'archive', f'{date}-{cid}')
            else:
                cdir = os.path.join(changes, cid)
            os.makedirs(cdir, exist_ok=True)
            prop = [f'# {title}', '', f'Status: {status} (backlog TASK-{n})', '', '## Why', '',
                    title, ''] + notes(cont) + ['## What Changes', '']
            prop += [f'- {t}' for _, t in build] or ['- (to be worked out)']
            prop += ['', '## Impact', '', f'- Source: {src}', '', '## Original notes', ''] + original + ['']
            io.open(os.path.join(cdir, 'proposal.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(prop))
            tasks = ['# Tasks', '', '## 1. Build', '']
            tasks += [f"- [{'x' if d else ' '}] 1.{i} {t}" for i, (d, t) in enumerate(build, 1)] or [
                f"- [{'x' if status in ('Done', 'Needs Test') else ' '}] 1.1 {title}"]
            tasks += ['', '## 2. Verify', '']
            tasks += [f"- [{'x' if d else ' '}] 2.{i} {t}" for i, (d, t) in enumerate(verify, 1)] or [
                f"- [{'x' if status == 'Done' else ' '}] 2.1 tried by hand"]
            io.open(os.path.join(cdir, 'tasks.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(tasks) + '\n')
            index.append((n, status, cid, title, f))
    io.open(os.path.join(DST, 'index.tsv'), 'w', encoding='utf-8', newline='\n').write(
        'task\tstatus\tchange\ttitle\tfile\n' + ''.join(f'TASK-{a}\t{b}\t{c}\t{d}\t{e}\n' for a, b, c, d, e in index))
    counts = {}
    for _, s, *_ in index:
        counts[s] = counts.get(s, 0) + 1
    print(n, counts)


main()
