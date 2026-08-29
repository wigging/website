---
date: July 12, 2026
description: My configuration settings for the LazyVim terminal editor
tags: terminal
---

## LazyVim Configuration

LazyVim is a great Neovim setup that is pre-configured with reasonable features. It's better than starting from scratch. Here are my configuration settings that focus on Python, HTML, CSS, and JavaScript. Configuration files for LazyVim must be located in the `~/.config/nvim` directory. More info about LazyVim is available at <https://www.lazyvim.org>.

### Config

Files located in the ` ~/.config/nvim/lua/config` directory.

```lua
-- config/autocmds.lua

-- Trim trailing white space when a file is saved
vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = "*",
  command = [[%s/\s\+$//e]],
})

-- Detect Jinja filetypes, use .html and html so HTML LSP and Jinja LSP can coexist
vim.filetype.add({
  extension = {
    jinja = "jinja",
    jinja2 = "jinja",
    j2 = "jinja",
  },
  pattern = {
    [".*%.html"] = "html",
  },
})
```

```lua
-- config/keymaps.lua

vim.keymap.set("i", "jj", "<Esc>", { silent = true, desc = "Escape insert mode with jj" })

vim.keymap.set({ "n", "i" }, "<C-a>", "<Esc>ggVG", { desc = "Select all text with Ctrl-a" })
```

```lua
-- config/options.lua

-- Turn off relative line numbers in the editor
vim.opt.relativenumber = false

-- Turn off concealing code block and other syntax in Markdown files
vim.opt.conceallevel = 0

-- Automatically format the file when it is saved
vim.g.autoformat = true

-- Use ty and ruff for Python programming
vim.g.lazyvim_python_lsp = "ty"
vim.g.lazyvim_python_ruff = "ruff"

-- Use prettier formatter without config file
vim.g.lazyvim_prettier_needs_config = false
```

### Plugins

Files located in the ` ~/.config/nvim/lua/plugins` directory.

```lua
-- plugins/colorscheme.lua

return {
  "LazyVim/LazyVim",
  opts = {
    colorscheme = "catppuccin-nvim",
  },
}
```

```lua
-- plugins/lspconfig.lua
-- In ruff, F821 overlaps ty unresolved-reference

return {
  "neovim/nvim-lspconfig",
  opts = {
    inlay_hints = { enabled = false },
    servers = {
      ruff = {
        init_options = {
          settings = {
            lint = {
              ignore = { "F821" },
            },
          },
        },
      },
    },
  },
}
```

```lua
-- plugins/noice.lua

return {
  "folke/noice.nvim",
  opts = {
    presets = {
      lsp_doc_border = true,  -- Add a border to LSP hover and docs
    },
  },
}
```

```lua
-- plugins/snacks.lua

return {
  "snacks.nvim",
  opts = {
    indent = {
      scope = {
        enabled = false,
      },
    },
    picker = {
      sources = {
        explorer = {
          hidden = true,
          ignored = true,
          exclude = { ".git", ".venv", ".DS_Store" },
        },
        grep = {
          exclude = { "uv.lock" },
        }
      },
    },
  },
}
```

```lua
-- plugins/treesitter.lua

return {
  "nvim-treesitter/nvim-treesitter",
  opts = function(_, opts)
    vim.list_extend(opts.ensure_installed, {
      "css",
      "jinja",
      "swift",
    })
  end,
}
```
