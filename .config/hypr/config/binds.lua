-- ▄▄▄▄· ▪   ▐ ▄ ·▄▄▄▄  .▄▄ ·
-- ▐█ ▀█▪██ •█▌▐███▪ ██ ▐█ ▀.
-- ▐█▀▀█▄▐█·▐█▐▐▌▐█· ▐█▌▄▀▀▀█▄
-- ██▄▪▐█▐█▌██▐█▌██. ██ ▐█▄▪▐█
-- ·▀▀▀▀ ▀▀▀▀▀ █▪▀▀▀▀▀•  ▀▀▀▀
--
-- https://wiki.hypr.land/Configuring/Basics/Binds/

-- Writing hl.ds.exec_cmd() all the time is too long, here is a shortcut
local function run(cmd, window_rules)
	return hl.dsp.exec_cmd(cmd, window_rules)
end

-- Runs script with given name
local function run_script(script_name)
	return hl.dsp.exec_cmd(Scripts .. script_name)
end

-- Runs script with given name
local function hypr_script(script_name)
	return hl.dsp.exec_cmd(HyprScripts .. script_name)
end


-- Launch terminal
hl.bind("SUPER + RETURN", hl.dsp.exec_cmd(Terminal))
hl.bind("SUPER + SHIFT + RETURN", hl.dsp.exec_cmd(Terminal, { float = true }))

-- Launch some apps
-- hl.bind("SUPER + B", hl.dsp.exec_cmd(FileManagerGui))
-- hl.bind("SUPER + N", hl.dsp.exec_cmd(Browser))

-- Launcher
hl.bind("SUPER + R", hl.dsp.exec_cmd("vicinae toggle"))
hl.bind("SUPER + V", hl.dsp.exec_cmd("vicinae 'vicinae://launch/clipboard/history?toggle=true'"))
hl.bind("SUPER + E", hl.dsp.exec_cmd("vicinae 'vicinae://launch/core/search-emojis?toggle=true'"))
-- hl.bind("SUPER + R", hl.dsp.exec_cmd("pkill rofi || rofi -show drun -show-icons -run-command 'uwsm app -- {cmd}'"))
hl.bind("SUPER + SHIFT + V", hl.dsp.exec_cmd("pkill rofi || cliphist list | rofi -dmenu | cliphist decode | wl-copy"))
hl.bind("SUPER + SHIFT + P", hl.dsp.exec_cmd("pkill rofi || $HOME/.config/rofi/powermenu/powermenu.sh"))
hl.bind("SUPER + N", hl.dsp.exec_cmd("swaync-client -t -sw"))

-- dmenu
hl.bind("SUPER + D", hl.dsp.exec_cmd("dmenu -i -h 30 -b -fn 'Hack Nerd Font 16'"))

-- Hyprcap
hl.bind("SUPER + Print",                hl.dsp.exec_cmd("hyprcap shot -wzcnA"))
-- Screenshot a window
hl.bind("Print",                        hl.dsp.exec_cmd("hyprcap shot window:active -wzcnA"))
-- Screenshot a monitor
hl.bind("SHIFT + Print",                hl.dsp.exec_cmd("hyprcap shot monitor:active -wzcnA"))
-- Screenshot a region
hl.bind("SUPER + SHIFT + Print",        hl.dsp.exec_cmd("hyprcap shot region -wzcnA"))

hl.bind("SUPER + Scroll_Lock",          hl.dsp.exec_cmd("hyprcap rec -wzcnA"))
-- Record a window
hl.bind("Scroll_Lock",                  hl.dsp.exec_cmd("hyprcap rec window:active -wzcnA"))
-- Record a monitor
hl.bind("SHIFT + Scroll_Lock",          hl.dsp.exec_cmd("hyprcap rec monitor:active -wzcnA"))
-- Record a region
hl.bind("SUPER + SHIFT + Scroll_Lock",  hl.dsp.exec_cmd("hyprcap rec region -wzcnA"))

-- Cycle current workspace layout
hl.bind("ALT + Tab", function()
	hl.dispatch(hl.dsp.layout("cyclenext"))
	hl.dispatch(hl.dsp.window.cycle_next()) -- Change focus to another window
	hl.dispatch(hl.dsp.window.bring_to_top()) -- Bring it to the top
end)
hl.bind("ALT + SHIFT + Tab", function()
	hl.dispatch(hl.dsp.layout("cycleprev"))
	hl.dispatch(hl.dsp.window.cycle_prev()) -- Change focus to another window
	hl.dispatch(hl.dsp.window.bring_to_top()) -- Bring it to the top
end)

hl.bind("SUPER + Tab", hl.dsp.focus({ last = "+1" }))
hl.bind("SUPER + twosuperior", hl.dsp.focus({ monitor = "+1" }))
hl.bind("SUPER + CTRL + Left", hl.dsp.focus({ monitor = "0" }))
hl.bind("SUPER + CTRL + Right", hl.dsp.focus({ monitor = "1" }))
hl.bind("SUPER + CTRL + twosuperior", hl.dsp.workspace.swap_monitors({ monitor1 = "DP-1", monitor2 = "DP-2" }))

-- Restart Waybar
hl.bind("SUPER + CTRL + R", hl.dsp.exec_cmd("systemctl restart --user waybar.service"))

hl.bind("SUPER + L", hypr_script("switch_kb_layout"))
hl.bind("SUPER + M", hypr_script("switch_monitor_hz"))

-- Window actions
hl.bind("SUPER + Q", hl.dsp.window.close()) -- Close window
hl.bind("SUPER + SHIFT + Q", hl.dsp.window.kill()) -- Kill window
hl.bind("SUPER + P", hl.dsp.window.pseudo()) -- Pseudotiles window
hl.bind("SUPER + Z", hl.dsp.window.center()) -- Centers window if it is floating
hl.bind("SUPER + U", hl.dsp.window.pin()) -- Pins floating window
hl.bind("SUPER + X", hl.dsp.window.resize({ x = -80, y = -75, relative = true })) -- Make window x-80 y-75 smaller
hl.bind("SUPER + C", hl.dsp.window.resize({ x = 80, y = 75, relative = true })) -- Make window x+80 y+75 bigger
hl.bind("SUPER + F", hl.dsp.window.fullscreen({ action = "toggle" }))
hl.bind("SUPER + SHIFT + F", hl.dsp.window.fullscreen_state({ internal = "2", client = "0", action = "toggle" }))
hl.bind("SUPER + T", function()
	-- Toggle window floating state and center it.
	hl.dispatch(hl.dsp.window.float({ action = "toggle" }))
	hl.dispatch(hl.dsp.window.center())
end)

-- hl.bind("SUPER + Q", function ()
--   local w = hl.get_active_window()
--   if w ~= nil and w.class == "firefox" then
--     hl.notification.create({ text = "Protected", timeout = 5000 })
--   else
--     hl.notification.create({ text = "Not Protected", timeout = 5000 })
--   end
-- end)

hl.bind("SUPER + I", function()
  local windowInfo = hl.get_active_window()
  hl.notification.create({ text = "Class: " .. windowInfo.class, timeout = 5000, icon = "ok" })
  hl.notification.create({ text = "Title: " .. windowInfo.title, timeout = 5000, icon = "ok" })
end)


-- Magnify
-- local zoomLevels = { 1, 2, 3 }
local zoomLevels = { 1, 2 }
local zoomIndex = 1
hl.bind("SUPER + SHIFT + Z", function()
	zoomIndex = (zoomIndex % #zoomLevels) + 1
	hl.config({ cursor = { zoom_factor = zoomLevels[zoomIndex] } })
end)

-- Move focus with mainMod + arrow keys
hl.bind("SUPER + left", hl.dsp.focus({ direction = "left" }))
hl.bind("SUPER + right", hl.dsp.focus({ direction = "right" }))
hl.bind("SUPER + up", hl.dsp.focus({ direction = "up" }))
hl.bind("SUPER + down", hl.dsp.focus({ direction = "down" }))

-- French AZERTY layout
local frenchKeys = {
	[1] = "ampersand",
	[2] = "eacute",
	[3] = "quotedbl",
	[4] = "apostrophe",
	[5] = "parenleft",
	[6] = "minus",
	[7] = "egrave",
	[8] = "underscore",
	[9] = "ccedilla",
	[10] = "agrave",
}
local workspaces = 10

for i = 1, workspaces do
	local key = frenchKeys[i]
	-- hl.bind("SUPER + " .. key,                  hl.dsp.workspace.toggle_special("_TEMP"))
	-- hl.bind("SUPER + " .. key,                  hl.dsp.workspace.toggle_special("_TEMP"))
	hl.bind("SUPER + " .. key, hl.dsp.focus({ workspace = i }))
	hl.bind("SUPER + SHIFT + " .. key, hl.dsp.window.move({ workspace = i }))

	-- hl.bind("SUPER + CTRL + " .. key,           hl.dsp.workspace.toggle_special("_TEMP"))
	-- hl.bind("SUPER + CTRL + " .. key,           hl.dsp.workspace.toggle_special("_TEMP"))
	hl.bind("SUPER + CTRL + " .. key, hl.dsp.focus({ workspace = i + 10 }))
	hl.bind("SUPER + CTRL + SHIFT + " .. key, hl.dsp.window.move({ workspace = i + 10 }))
end

-- Special workspaces
hl.bind("SUPER + Space", hl.dsp.workspace.toggle_special("term"))
hl.bind("SUPER + SHIFT + Space", hl.dsp.window.move({ workspace = "special:term" }))

hl.bind("CTRL + twosuperior", hl.dsp.workspace.toggle_special("fileroller"))
hl.bind("CTRL + SHIFT + twosuperior", hl.dsp.window.move({ workspace = "special:fileroller" }))

hl.bind("CTRL + " .. frenchKeys[1], hl.dsp.workspace.toggle_special("filemanager"))
hl.bind("CTRL + SHIFT + " .. frenchKeys[1], hl.dsp.window.move({ workspace = "special:filemanager" }))

hl.bind("CTRL + " .. frenchKeys[2], hl.dsp.workspace.toggle_special("term2"))
hl.bind("CTRL + SHIFT + " .. frenchKeys[2], hl.dsp.window.move({ workspace = "special:term2" }))

hl.bind("CTRL + " .. frenchKeys[3], hl.dsp.workspace.toggle_special("term3"))
hl.bind("CTRL + SHIFT + " .. frenchKeys[3], hl.dsp.window.move({ workspace = "special:term3" }))

hl.bind("CTRL + " .. frenchKeys[4], hl.dsp.workspace.toggle_special("term4"))
hl.bind("CTRL + SHIFT + " .. frenchKeys[4], hl.dsp.window.move({ workspace = "special:term4" }))

hl.bind("CTRL + " .. frenchKeys[7], hl.dsp.workspace.toggle_special("mousai"))
hl.bind("CTRL + SHIFT + " .. frenchKeys[7], hl.dsp.window.move({ workspace = "special:mousai" }))

hl.bind("CTRL + " .. frenchKeys[8], hl.dsp.workspace.toggle_special("easyeffects"))
hl.bind("CTRL + SHIFT + " .. frenchKeys[8], hl.dsp.window.move({ workspace = "special:easyeffects" }))

-- Scroll through existing workspaces with mainMod + scroll
hl.bind("SUPER + mouse_down", hl.dsp.focus({ workspace = "e+1" }))
hl.bind("SUPER + mouse_up", hl.dsp.focus({ workspace = "e-1" }))

-- Move/resize windows with mainMod + LMB/RMB and dragging
hl.bind("SUPER + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind("SUPER + mouse:273", hl.dsp.window.resize(), { mouse = true })

-- Laptop multimedia keys for volume and LCD brightness
hl.bind(
	"XF86AudioRaiseVolume",
	hl.dsp.exec_cmd("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+"),
	{ locked = true, repeating = true }
)
hl.bind(
	"XF86AudioLowerVolume",
	hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),
	{ locked = true, repeating = true }
)
hl.bind(
	"XF86AudioMute",
	hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
	{ locked = true, repeating = true }
)
hl.bind(
	"XF86AudioMicMute",
	hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"),
	{ locked = true, repeating = true }
)
hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%+"), { locked = true, repeating = true })
hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%-"), { locked = true, repeating = true })

-- Requires playerctl
hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"), { locked = true })
hl.bind("XF86AudioPause", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"), { locked = true })
