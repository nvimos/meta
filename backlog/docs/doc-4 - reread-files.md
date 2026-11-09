---
id: doc-4
title: 'reread-files'
type: other
created_date: '2026-11-10'
---

## autoreread

- check if i have something like this:
    vim.o.autoread = true
    vim.api.nvim_create_autocmd({ "FocusGained", "BufEnter", "CursorHold", "TermLeave" }, {
      command = "silent! checktime",
    })

- consider formalizing my config-auto-reread plugin
