#!/bin/sh

wsmonitor="$(hyprctl -j workspaces | jq -r ".[] | select(.id == $1) | .monitor")"

if [ "$wsmonitor" = "DP-3" ]; then
	monitor="DP-2"
else
	monitor="DP-3"
fi

hyprctl dispatch moveworkspacetomonitor "$1 $monitor"
