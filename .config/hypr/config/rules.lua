-- ▄▄▌ ▐ ▄▌▪   ▐ ▄ ·▄▄▄▄  ▄▄▌ ▐ ▄▌    ▄▄▄  ▄• ▄▌▄▄▌  ▄▄▄ ..▄▄ ·
-- ██· █▌▐███ •█▌▐███▪ ██ ██· █▌▐█    ▀▄ █·█▪██▌██•  ▀▄.▀·▐█ ▀.
-- ██▪▐█▐▐▌▐█·▐█▐▐▌▐█· ▐█▌██▪▐█▐▐▌    ▐▀▀▄ █▌▐█▌██▪  ▐▀▀▪▄▄▀▀▀█▄
-- ▐█▌██▐█▌▐█▌██▐█▌██. ██ ▐█▌██▐█▌    ▐█•█▌▐█▄█▌▐█▌▐▌▐█▄▄▌▐█▄▪▐█
--  ▀▀▀▀ ▀▪▀▀▀▀▀ █▪▀▀▀▀▀•  ▀▀▀▀ ▀▪    .▀  ▀ ▀▀▀ .▀▀▀  ▀▀▀  ▀▀▀▀
--
-- https://wiki.hyprland.org/Configuring/Window-Rules/

-- Workspace rules
hl.workspace_rule({ workspace = 1,  monitor = "DP-1", default = true })
hl.workspace_rule({ workspace = 2,  monitor = "DP-1" })
hl.workspace_rule({ workspace = 3,  monitor = "DP-1", on_created_empty = FileManagerGui })
hl.workspace_rule({ workspace = 4,  monitor = "DP-1" })
hl.workspace_rule({ workspace = 5,  monitor = "DP-1" })
hl.workspace_rule({ workspace = 6,  monitor = "DP-1" })
hl.workspace_rule({ workspace = 7,  monitor = "DP-1" })
hl.workspace_rule({ workspace = 8,  monitor = "DP-1" })
hl.workspace_rule({ workspace = 9,  monitor = "DP-1" })
hl.workspace_rule({ workspace = 10, monitor = "DP-1" })

hl.workspace_rule({ workspace = 11, monitor = "DP-2", default = true })
hl.workspace_rule({ workspace = 12, monitor = "DP-2" })
hl.workspace_rule({ workspace = 13, monitor = "DP-2" })
hl.workspace_rule({ workspace = 14, monitor = "DP-2" })
hl.workspace_rule({ workspace = 15, monitor = "DP-2" })
hl.workspace_rule({ workspace = 16, monitor = "DP-2" })
hl.workspace_rule({ workspace = 17, monitor = "DP-2" })
hl.workspace_rule({ workspace = 18, monitor = "DP-2" })
hl.workspace_rule({ workspace = 19, monitor = "DP-2" })
hl.workspace_rule({ workspace = 20, monitor = "DP-2" })

-- Special Workspace rules
hl.workspace_rule({
	workspace = "special:filemanager",
	on_created_empty = Terminal .. " --class='".. FileManagerTui .."' -e " .. FileManagerTui,
})
hl.workspace_rule({ workspace = "special:mousai",       on_created_empty = "flatpak run io.github.seadve.Mousai" })
hl.workspace_rule({ workspace = "special:easyeffects",  on_created_empty = "easyeffects" })
hl.workspace_rule({ workspace = "special:term",         on_created_empty = Terminal .. " --title term" })
hl.workspace_rule({ workspace = "special:term2",        on_created_empty = Terminal .. " --title term" })
hl.workspace_rule({ workspace = "special:term3",        on_created_empty = Terminal .. " --title term" })
hl.workspace_rule({ workspace = "special:term4",        on_created_empty = Terminal .. " --title term" })

-- Smart Gaps
hl.workspace_rule({ workspace = "w[tv1]s[false]", gaps_out = 0, gaps_in = 0 })
-- hl.workspace_rule({ workspace = "f[1]s[false]", gaps_out = 0, gaps_in = 0 })
hl.workspace_rule({ workspace = "s[false]", gaps_out = 0, gaps_in = 0 })
hl.window_rule({ match = { float = false, workspace = "w[tv1]s[false]" }, border_size = 0 })
hl.window_rule({ match = { float = false, workspace = "w[tv1]s[false]" }, rounding = 0 })
-- hl.window_rule({ match = { float = false, workspace = "f[1]s[false]" }, border_size = 0 })
-- hl.window_rule({ match = { float = false, workspace = "f[1]s[false]" }, rounding = 0 })
hl.window_rule({ match = { float = false, workspace = "s[false]" }, border_size = 0 })
hl.window_rule({ match = { float = false, workspace = "s[false]" }, rounding = 0 })

-- Layer rules
hl.layer_rule({
  match = { namespace = "viciane", },
  blur = true,
  ignore_alpha = 0,
  -- no_anim = true,
})

hl.layer_rule({
	match = {
		namespace = "swaync-control-center|swaync-notification-window",
	},
	blur = true,
	ignore_alpha = 0.5,

	animation = "slide right",
})

hl.layer_rule({
	match = {
		namespace = "awww-daemon|selection",
	},

	no_anim = true,
})

-- Workspaces Assignment
-- Games workspace
hl.window_rule({ match = { class = "steam_app_.*" }, fullscreen = true, workspace = "4 silent" })
hl.window_rule({ match = { tag = "proton-game" }, fullscreen = true, workspace = "4 silent" })
hl.window_rule({ match = { content = "game" }, fullscreen = true, workspace = "4 silent" })

-- Games Launcher
hl.window_rule({
  match = {
    class = "net.lutris.Lutris|heroic|[Ss]team|omikuji|com.usebottles.bottles"
  },
  workspace = "4 silent",
})

-- Media Player
hl.window_rule({
  match = {
    class = "Jellyfin Media Player|org.jellyfin.jellyfinmediaplayer|com.github.iwalton3.jellyfin-media-player|nl.jknaapen.fladder|[Ff]ladder"
  },
  workspace = "6 silent",
})

-- Guitarix
hl.window_rule({ match = { class = "guitarix" }, workspace = "9 silent" })

-- Music Player
hl.window_rule({
  match = {
    class = "[Ss]potify|[Ff]eishin"
  },
  workspace = "12 silent",
})

hl.window_rule({ match = { class = "org.gnome.FileRoller" },          workspace = "special:fileroller" })
hl.window_rule({ match = { class = "com.github.wwmm.easyeffects" },   workspace = "special:easyeffects silent" })
hl.window_rule({ match = { class = "io.github.seadve.Mousai" },       workspace = "special:mousai silent" })

-- Window rules
-- Disable blur for firefox
hl.window_rule({ match = { class = "firefox" }, no_blur = true })

-- Ignore maximize requests
hl.window_rule({ match = { class = ".*" }, suppress_event = "maximize" })

-- Floats
hl.window_rule({
  match = {
    title = "file_progress|eog|blueman-manager|nm-appler|nm-connection-editor|Rename.*|File Operation Progress|\
             Select a directory|Select folder|Browse for Folder"
  },
  float = true,
  center = true
})
hl.window_rule({
  match = {
    title = "Enter name of file to save to.*"
  },
  size = { "(monitor_w*0.7)", "(monitor_h*0.7)" },
  float = true,
  center = true
})

-- Winetricks
hl.window_rule({
  match = {
    class = "zenity", title = "^(Winetricks -)(.*)|winetricks|ProtonFixes"
  },
  float = true,
  center = true,
})

-- Pavucontrol
hl.window_rule({
  match = {
    class = "org.pulseaudio.pavucontrol"
  },
  size = { "(monitor_w*0.7)", "(monitor_h*0.8)" },
  float = true,
  center = true,
})

-- Gnome Calculator
hl.window_rule({
  match = {
    class = "org.gnome.Calculator"
  },
  size = { "500", "700" },
  float = true,
  center = true,
})

-- Faugus
hl.window_rule({
  match = {
    class = "faugus-run",
	  title = "Winetricks Logs"
  },
  size = { "(monitor_w*0.6)", "(monitor_h*0.7)" },
  float = true,
  center = true,
})

-- Firefox
hl.window_rule({
  match = {
    class = "firefox",
    title = "opening|extension:|firefox - choose user profile"
  },
  float = true,
  center = true,
})
hl.window_rule({
  match = {
    class = "firefox",
    title = "Library|Enter name of file to save to… -.*|Export Bookmarks File"
  },
  size = { "(monitor_w*0.7)", "(monitor_h*0.7)" },
  float = true,
  center = true,
})

-- Musicbrainz Picard
hl.window_rule({
  match = {
    class = "org.musicbrainz.Picard",
	  title = "Track Search Results|Album Search Results"
  },
  size = { "(monitor_w*0.9)", "(monitor_h*0.7)" },
  float = true,
  center = true
})

-- Steam
hl.window_rule({
  match = {
    class = "[Ss]team",
    title = "Steam Settings|Recordings & Screenshots|Players|Game Servers",
  },
  size = { "(monitor_w*0.9)", "(monitor_h*0.9)" },
  float = true,
  center = true,
})
hl.window_rule({
  match = {
    class = "[Ss]team",
    title = "Special Offers"
  },
  size = { "(monitor_w*0.5)", "(monitor_h*0.7)" },
  float = true,
  center = true
})
hl.window_rule({
  match = {
    class = "[Ss]team",
    title = "Friends List"
  },
  size = { "(monitor_w*0.3)", "(monitor_h*0.8)" },
  float = true,
  center = true,
})

-- Lutris
hl.window_rule({
  match = {
    class = "net.lutris.Lutris",
    title = "Configure.*|Add a new game|Lutris settings"
  },
  size = { "(monitor_w*0.6)", "(monitor_h*0.9)" },
  float = true,
  center = true,
})

-- Bottles
hl.window_rule({
  match = {
    class = "bottles",
    title = "Preferences"
  },
  size = { "(monitor_w*0.7)", "(monitor_h*0.8)" },
  float = true,
  center = true,
})

hl.window_rule({ stay_focused = true, match = { class = "xfce-polkit" } })
hl.window_rule({ stay_focused = true, match = { title = "^(Rename device)$", class = "blueman-manager" } })

-- Tags
hl.window_rule({ float = true, match = { tag = "float" } })
hl.window_rule({ opacity = 1, match = { tag = "opaque" } })
hl.window_rule({ border_size = 2, match = { tag = "bordered" } })

hl.window_rule({
	name = "Float by title",
	match = {
		title = "Font Manager|Volume Control|Qalculate!|Library|Add bookmark",
	},

	float = true,
	center = true,
	persistent_size = true,
})

hl.window_rule({
	name = "Float by class",
	match = {
		class = "blueman-manager|blueman-services|nwg-look|rog-control-center|org.qbittorrent.qBittorrent|kvantummanager|\
             org.gnome.seahorse.Application|xfce-polkit|org.polymc.PolyMC|engrampa|nm-connection-editor|system-config-printer|hyprland-share-picker|\
             org.bleachbit.BleachBit|vlc|exo-desktop-item-edit|xdg-desktop-portal-gtk|org.gnome.eog|qt6ct|spotify|Spotify|xfce-polkit",
	},

	float = true,
	center = true,
	persistent_size = true,
})

hl.window_rule({
	name = "Thunar dialogs",
	match = {
		class = "thunar|Thunar",
		title = 'Rename "*.*"|File Operation Progress|Confirm to replace files|Attention',
	},

	float = true,
	persistent_size = true,
})

hl.window_rule({
	name = "Thunar stayfocused",
	match = {
		class = "thunar|Thunar",
		title = 'Attention|Rename "*.*"|Create Document from .*|New .* ...|Create New Folder',
	},

	stay_focused = true,
})

hl.window_rule({
	name = "Thunar move right bottom",
	match = {
		title = "^(File Operation Progress)$",
		class = "(thunar|Thunar)",
	},

	focus_on_activate = false,
	move = "1460 970",
})

hl.window_rule({
	name = "Thunar menu force center",
	match = {
		title = "^(Confirm to replace files)$",
		class = "(thunar|Thunar)",
	},

	center = true,
})

hl.window_rule({
	name = "Firefox Picture in Picture",
	match = {
		title = "Picture-in-Picture",
		class = "^(firefox)(.*)$",
	},

	size = "250 140",
	move = "1650 50",
	border_size = 2,
	pin = true,
	float = true,
	no_initial_focus = true,
	focus_on_activate = true,
	keep_aspect_ratio = true,
})


hl.window_rule({
	name = "peaclock terminal",
	match = {
		class = "peaclock",
	},

	float = true,
	pin = true,
	size = "500 260",
	move = "711 60",
})

hl.window_rule({
	name = "Dev-tools",
	match = {
		title = "^(DevToolsApp)$",
	},

	float = true,
	move = "50% 15%",
	size = "900 600",
})

hl.window_rule({
	name = "Flameshot",
	match = {
		class = "flameshot",
	},
	float = true,
	fullscreen = true,
})

hl.window_rule({
	name = "Uzerburg",
	match = {
		class = "ueberzugpp(.*)",
	},

	float = true,
	no_initial_focus = true,
})
