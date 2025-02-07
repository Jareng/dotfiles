return {
	-- {
	--   "navarasu/onedark.nvim",
	--   opts = {
	--     transparent = true,
	--     style = "darker",
	--     -- styles = {
	--     --   sidebars = "transparent",
	--     --   floats = "transparent",
	--     -- },
	--   },
	-- },
	{
		"EdenEast/nightfox.nvim",
		opts = {
			options = {
				transparent = true,
			},
		},
	},
	{
		"folke/tokyonight.nvim",
		opts = {
			transparent = true,
			style = "storm", -- "storm", "night", "moon"
			styles = {
				-- comments = { italic = true },
				-- keywords = { italic = true },
				sidebars = "transparent",
				floats = "transparent",
			},
		},
	},
	{
		"olimorris/onedarkpro.nvim",
		priority = 1000, -- Ensure it loads first
		opts = {
			options = {
				transparency = true,
			},
		},
	},

	{
		"LazyVim/LazyVim",
		opts = {
			colorscheme = "tokyonight",
		},
	},
}
