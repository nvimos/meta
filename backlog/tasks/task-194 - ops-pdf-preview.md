---
id: TASK-194
title: 'ops PDF preview: test the PDF build, then ship it'
status: To Do
assignee: []
created_date: '2026-11-19'
labels:
  - ops
  - frontend
  - ci
dependencies: []
ordinal: 194000
---

## Description

ops: the PDF preview (pdfrx) is an optional build nobody tests. Keep PDF off in every build until a CI job builds it and renders a sample PDF page; then CI releases always build with PDF on.

Change: `openspec/changes/ops-pdf-preview/`

## Acceptance Criteria

- [x] #1 PDF off locally and in `make release`
- [ ] #2 a CI job builds with PDF on and renders a sample PDF page
- [ ] #3 the CI release builds with PDF on once that job is green
