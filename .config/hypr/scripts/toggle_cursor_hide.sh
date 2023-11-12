#!/bin/sh

cursor_timeout="$(hyprctl -j getoption general:cursor_inactive_timeout | jq '.int')"

echo $cursor_timeout

if [ $cursor_timeout = 0 ]; then
	timeout="3"
	notify-send "Hyprland" "Cusor Auto-Hide\nEnabled (3s)"
else
	timeout="0"
	notify-send "Hyprland" "Cusor Auto-Hide\nDisabled"
fi

hyprctl keyword general:cursor_inactive_timeout $timeout
