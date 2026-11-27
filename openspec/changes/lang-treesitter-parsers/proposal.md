# treesitter parsers per enabled language

Status: To Do (backlog TASK-212)

## Why

Languages are switched on in one place: the `enabled` table of genja-completion011, merged with the
machine's `lua/genja/lsp/local.lua`. Treesitter parsers are listed in another: a fixed list of about
forty names in the config's `lua/lazyp/my/load-treesitter.lua`. The two drift apart. Today the list
installs `vue`, `svelte`, `astro`, `angular`, `templ` and `blade` on a machine where none of those
languages is on, and it has no `c`, `cpp` or `python`, although `c_cpp` and `python` are language
modules and python is on here. The language modules already say this in comments ("treesitter vue
is in the config's load-treesitter.lua"), which is the sign that the list belongs with them.

Switching a language on should bring everything it needs, the parsers included, the same way it
already brings its servers and Mason tools. Switching one off should stop installing its parsers,
so a new machine only builds what it uses; every parser is a C build at first install.

## The idea

Each language module names its parsers next to its servers and tools:

```lua
-- lua/genja/lang/go.lua
return {
    servers = { gopls = { ... } },
    tools = { 'golangci-lint' },
    parsers = { 'go', 'gomod', 'gosum', 'gotmpl', 'templ', 'proto' },
}
```

Completion features that work on a filetype name theirs too (`gitcommit`: `gitcommit`, `git_rebase`,
`diff`; `gitignore`: `gitignore`, `gitattributes`; `sshconfig`: `ssh_config`). A short base list is
always installed, because Neovim itself and the config use it whatever is enabled: `lua`, `vim`,
`vimdoc`, `markdown`, `markdown_inline`, `regex`, `query`. Neovim ships most of these (and `c`), but
nvim-treesitter's queries expect its own builds of them, so they stay in the list.

genja-completion011 collects the parsers of the enabled languages and features the way it collects
servers and tools, and exposes the list as `require('genja.lsp').parsers()`. Treesitter itself stays
in the config's spec, which keeps loading at start so highlighting works on the first buffer; only
its scheduled `install_parsers()` changes. It installs `parsers()` plus a short list of the config's
own (`yaml` for `yaml.ansible`, `xml`), instead of the fixed list. The compiler check and the PATH
fix-ups stay where they are, after the first screen.

Nothing is uninstalled. A parser left over from a language that was switched off costs nothing at
start, and switching the language back on would mean another C build. Leftovers are listed instead:
`:checkhealth genja.lsp` gets a parsers section (wanted but not installed, installed but not
wanted), and the config's `make status` table gets a parsers column.

### Where the parsers come from

A first mapping, from today's list and the language modules; check each against LazyVim's language
extras and AstroCommunity's packs, as the plugin's CLAUDE.md says for any language work:

| language   | parsers                                                       |
|------------|---------------------------------------------------------------|
| bash       | bash                                                          |
| powershell | powershell                                                    |
| make       | make                                                          |
| gitconfig  | git_config                                                    |
| sshconfig  | ssh_config                                                    |
| json       | json                                                          |
| css        | css, scss                                                     |
| html       | html                                                          |
| php        | php, php_only, phpdoc, blade, twig, html                      |
| go         | go, gomod, gosum, gotmpl, templ, proto                        |
| typescript | typescript, javascript, tsx, jsdoc                            |
| vue        | vue                                                           |
| angular    | angular                                                       |
| svelte     | svelte                                                        |
| astro      | astro                                                         |
| c_cpp      | c, cpp                                                        |
| python     | python                                                        |
| lua, vim   | (base list)                                                   |

`blade` and `twig` stay with php for now, since there is no Laravel or Symfony language module.
`vue` is wanted by blade-nav.nvim too; that plugin's spec can add it to the config's own list if it
is used without the vue language.

## Impact

- genja-completion011: `parsers` field in `genja.Lang` and the language modules, feature parsers,
  `parsers()` in `lsp/init.lua`, a parsers section in `lsp/health.lua`, README (languages table) and
  CLAUDE.md
- config: `lua/lazyp/my/load-treesitter.lua` installs `parsers()` plus its own short list;
  `tests/` `make status` gets the column; CLAUDE.md "Filetypes and parsers" points to the language
  modules
- `parsers()` reads the language modules the same way `servers()` does, so it doesn't load mason or
  start anything; it runs in the scheduled install, after the first screen
