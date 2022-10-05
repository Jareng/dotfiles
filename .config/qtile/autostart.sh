#!/bin/bash

# Load env
source ~/.env.zsh

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

# List the apps you wish to run on startup below preceded with "run"

# Policy kit (needed for GUI apps to ask for password)
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# xrandr layout
run ~/.screenlayout/monitor.sh &
# # kanshi
# run kanshi &
# Start compositor
run picom &
# Start dunst
run dunst &
# sxhkd Hotkeys
run sxhkd &
# Nitrogen
run nitrogen --restore &
# Unclutter - (hides mouse pointer after 2 seconds of inactivity)
run unclutter --timeout 2 &
# Start Volume Control applet
run volctl &
# Start Network Manager Applet
run nm-applet &
# Udiskie
run udiskie -A --notify --smart-tray &
# Easyeffects
run easyeffects --gapplication-service &
# KDE Connect
run kdeconnect-indicator &
# # Screensaver
# run xscreensaver -no-splash &
# # Bluetooth
# run blueman-tray &
# # MPD
# run mpd ~/.config/mpd/mpd.conf &

# function is_running {
#   # grab the first word of a string
#   set -- $1
#   # if process is not running
#   if ! pgrep -x $1 > /dev/null; then
#     echo "$1 is not running"
#     $*
#   fi
#   return 0
# }
#
# apps=(
#   "dunst &"
#   "sxhkd &"
#   "nitrogen --restore"
#   "unclutter --timeout 2 &"
#   "picom -b --config /home/$(whoami)/.config/picom/picom.conf"
# )
#
# # Need "" around ${apps[@]} so it take the full string
# for app in "${apps[@]}"; do
#   is_running "$app"
# done
