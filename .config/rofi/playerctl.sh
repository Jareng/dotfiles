#!/usr/bin/env bash

status_function() {
	if playerctl status >/dev/null; then
		echo "$(playerctl metadata -f "{{trunc(default(title, \"[Unknown]\"), 25)}}")"
		echo "$(playerctl metadata -f "{{trunc(default(artist, \"[Unknown]\"), 25)}} - {{trunc(default(album, \"[Unknown]\"), 25)}}")"
		echo "$(playerctl status -f "{{playerName}}")"
	else
		echo "Nothing is playing"
	fi
}
status=$(status_function)

# Options
toggle="⏯️ Play/Pause"
next="⏭️ Next"
prev="⏮ Previous"
seekminus="⏪ Go back 15 seconds"
seekplus="⏩ Go ahead 15 seconds"
switch="🔄 Change selected player"

# Variable passed to rofi
options="$toggle\n$next\n$prev\n$seekplus\n$seekminus\n$switch"

chosen="$(echo -e "$options" | rofi -show -p "${status^}" -dmenu -selected-row 0 -theme-str '@import "playerctl.rasi"')"
case $chosen in
$toggle)
	playerctl play-pause
	;;
$next)
	playerctl next
	;;
$prev)
	playerctl previous
	;;
$seekminus)
	playerctl position 15-
	;;
$seekplus)
	playerctl position 15+
	;;
$switch)
	playerctld shift
	;;
esac
