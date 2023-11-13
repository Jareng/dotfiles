-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

vim.filetype.add({
  extension = {
    conf = "config",
    rasi = "rasi",
  },
  pattern = {
    ["~/.config/hypr/.*%.conf"] = "hypr",
    ["~/.config/Kvantum/.*%.kvconfig"] = "toml",
    -- ["~/.config/rofi/.*%.rasi"] = "rasi",
    ["/etc/pacman.d/hooks/.*%.hook"] = "systemd",
  },
})
