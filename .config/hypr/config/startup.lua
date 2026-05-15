-- .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄  ▄▄▄▄▄▄• ▄▌ ▄▄▄·
-- ▐█ ▀. •██  ▐█ ▀█ ▀▄ █·•██  █▪██▌▐█ ▄█
-- ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄  ▐█.▪█▌▐█▌ ██▀·
-- ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌ ▐█▌·▐█▄█▌▐█▪·•
--  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀ .▀
--
-- https://wiki.hypr.land/Configuring/Basics/Autostart/

-- exec-once
hl.on("hyprland.start", function()
  local exec_onces = {
    "dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",  -- Update some dbus variables
    -- "wl-paste --watch cliphist store",
    "udiskie --appindicator",
    "nm-applet --indicator",
    "blueman-applet",
    "kdeconnect-indicator",
    -- "easyeffects --service-mode",
    "flatpak run io.github.seadve.Mousai",
    "flatpak run com.protonvpn.www --start-minimized",
    "easyeffects",
  }

  for i = 1, #exec_onces do
    local cmd = exec_onces[i]
    hl.exec_cmd(cmd)
  end
end)

-- exec
local execs = {
  "$HOME/.local/bin/import-gsettings",
}

for i = 1, #execs do
  local cmd = execs[i]
  hl.exec_cmd(cmd)
end

