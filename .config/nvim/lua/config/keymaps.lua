-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

local map = vim.keymap.set

-- map("x", "p", [["_dP]], { desc = "Paste without overwrite" })
map("x", "s", [["_c]], { desc = "Smart substitute" })
map("n", "s", [["_cl]], { desc = "Smart substitute" })
