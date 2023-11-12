#!/bin/bash

if ! pgrep -af polkit-gnome > /dev/null; then
  echo "Starting polkit-gnome"
  /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
else
  echo "polkit-gnome is running"
fi

function run {
  service="$1"

  if [ $service = "/usr/lib/kdeconnectd" ]; then
    service="kdeconnectd"
  elif [ $service = "kdeconnect-indicator" ]; then
    service="kdeconnect-indi"
  fi
  # echo "$service"
  if ! pgrep -x $service > /dev/null; then
    echo "> Starting $@"
    $@ &
  else
    echo "$@ is running"
  fi
}

# List the apps you wish to run on startup below preceded with "run"

# Policy kit (needed for GUI apps to ask for password)
# run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
# dbus
# run dbus-update-activation-environment --systemd DISPLAY WAYLAND_DISPLAY SWAYSOCK
# exec dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
# Clipman
# run wl-paste -p -t text --watch clipman store -P
# xrandr layout
# kanshi
run kanshi
# Swayidle
run swayidle
# Hyprpaper
run hyprpaper
# dunst
run dunst
# Network Manager Applet
run nm-applet
# Udiskie
run udiskie --appindicator
# Easyeffects
run easyeffects --gapplication-service
# KDE Connect
run /usr/lib/kdeconnectd
run kdeconnect-indicator
