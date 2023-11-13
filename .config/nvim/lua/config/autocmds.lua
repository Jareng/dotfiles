-- Autocmds are automatically loaded on the VeryLazy event
-- Default autocmds that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/autocmds.lua
-- Add any additional autocmds here

-- Remove whitespace on save
vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = "*",
  command = ":%s/\\s\\+$//e",
})

-- -- Don't auto commenting new lines
-- vim.api.nvim_create_autocmd("BufEnter", {
--   pattern = "*",
--   command = "set fo-=c fo-=r fo-=o",
-- })

-- start terminal in insert mode
vim.api.nvim_create_autocmd("TermOpen", {
  -- group = "bufcheck",
  pattern = "*",
  command = "startinsert | set winfixheight",
})

-- start git messages in insert mode
vim.api.nvim_create_autocmd("FileType", {
  -- group = "bufcheck",
  pattern = { "gitcommit", "gitrebase" },
  command = "startinsert | 1",
})
