# scan.py [status ...] [--details]: the Backlog.md tasks by status, one line each.
#   scan.py                       every open task (not Done / Dropped), grouped by status
#   scan.py "Needs Test"          only those waiting to be tried by hand
#   scan.py "In Progress" --details   with description, open steps and verify steps
# Reads backlog/tasks/*.md (frontmatter + sections); no Backlog.md CLI needed.
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ['In Progress', 'Needs Test', 'To Do', 'Done', 'Dropped']


def read(path):
    text = io.open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.S)
    if not m:
        return None
    meta = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'^(\w+):\s*(.*)$', line)
        if kv:
            meta[kv.group(1)] = kv.group(2).strip().strip("'")
    sections = {}
    for part in re.split(r'^## ', m.group(2), flags=re.M)[1:]:
        head, _, body = part.partition('\n')
        sections[head.strip()] = body.strip()
    meta['sections'] = sections
    return meta


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    details = '--details' in sys.argv
    wanted = args or ['In Progress', 'Needs Test', 'To Do']
    tasks = []
    for path in glob.glob(os.path.join(ROOT, 'backlog', 'tasks', '*.md')) + \
            glob.glob(os.path.join(ROOT, 'backlog', 'archive', 'tasks', '*.md')):
        t = read(path)
        if t and t.get('status') in wanted:
            tasks.append(t)
    tasks.sort(key=lambda t: (ORDER.index(t['status']) if t['status'] in ORDER else 9,
                              int(t['id'].split('-')[1])))
    width = max([len(t['status']) for t in tasks] + [0])
    for t in tasks:
        print(f"{t['status']:>{width}} {t['id']:<9} {t['title']}")
        if details:
            for name in ('Description', 'Acceptance Criteria', 'Verify'):
                body = t['sections'].get(name)
                if body:
                    open_lines = [l for l in body.splitlines() if l.strip() and not l.startswith('- [x]')]
                    if not open_lines:
                        continue
                    print('    ' + name + ':')
                    for line in open_lines:
                        if line.strip():
                            print('      ' + line)
            print()


main()
