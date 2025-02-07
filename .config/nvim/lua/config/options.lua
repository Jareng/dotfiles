-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

vim.filetype.add({
  extension = { conf = "config", rasi = "rasi", wofi = "rasi" },
  filename = {
    ["vifmrc"] = "vim",
  },
  pattern = {
    -- ["~/.config/hypr/.*%.conf"] = "hyprlang",
    -- [".*/waybar/.*"] = "jsonc",
    [".*/hypr/.*%.conf"] = "hyprlang",
    [".*/kitty/.*%.conf"] = "kitty",
    [".*/hawck/.*%.hwk"] = "lua",
    [".*/Kvantum/.*%.kvconfig"] = "toml",
    [".*/rofi/.*%.rasi"] = "rasi",
    [".*/hooks/.*%.hook"] = "systemd",
    -- ["%.env%.[%w_.-]+"] = "sh",
  },
})

vim.opt.spelllang = { "en", "fr_FR" }

vim.g.autoformat = false

-- Enable the option to require a Prettier config file
-- If no prettier config file is found, the formatter will not be used
vim.g.lazyvim_prettier_needs_config = false
