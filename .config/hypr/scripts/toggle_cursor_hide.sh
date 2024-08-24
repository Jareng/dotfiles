#!/bin/sh

cursor_timeout="$(hyprctl -j getoption cursor:inactive_timeout | jq '.int')"

echo $cursor_timeout

if [ $cursor_timeout = 0 ]; then
	timeout="3"
	notify-send "Hyprland" "Cusor Auto-Hide\nEnabled (3s)"
else
	timeout="0"
	notify-send "Hyprland" "Cusor Auto-Hide\nDisabled"
fi

hyprctl keyword cursor:inactive_timeout $timeout
