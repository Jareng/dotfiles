-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

vim.filetype.add({
  extension = {
    conf = "config",
    rasi = "rasi",
  },
  pattern = {
    -- ["~/.config/hypr/.*%.conf"] = "hyprlang",
    [".*/hypr/.*%.conf"] = "hyprlang",
    [".*/kitty/.*%.conf"] = "kitty",
    [".*/hawck/.*%.hwk"] = "lua",
    [".*/Kvantum/.*%.kvconfig"] = "toml",
    [".*/rofi/.*%.rasi"] = "rasi",
    [".*/hooks/.*%.hook"] = "systemd",
  },
})

vim.opt.spelllang = { "en", "fr_FR" }

vim.g.autoformat = false
