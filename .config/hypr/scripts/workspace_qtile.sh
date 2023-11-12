#!/bin/sh

monitors="$(hyprctl monitors -j)"

prevworkspace_temp="/tmp/hypr/prevworkspace_temp"
prevworkspace="$(cat "$prevworkspace_temp")"
currworkspace="$(echo "$monitors" | jq '.[] | select(.focused==true) | .activeWorkspace.id')"

# Save current workspace before switching to new
if [ "$1" != "$currworkspace" ]; then
	echo "$currworkspace" >"$prevworkspace_temp"
fi

# Switch to previous workspace and quit
if [[ "$1" == "prev" ]]; then
	hyprctl dispatch workspace "$prevworkspace"
	exit 0
fi

activemonitor="$(echo "$monitors" | jq '.[] | select(.focused==true) | .id')"
passivemonitor="$(echo "$monitors" | jq '.[] | select(.focused==false) | .id')"
passivews="$(echo "$monitors" | jq '.[] | select(.focused==false) | .activeWorkspace.id')"

# Swap
if [ "$1" = "" ]; then
	workspace="$(echo "$monitors" | jq '.[] | select(.focused==false) | .activeWorkspace.id')"
	exit 0
else
	workspace="$1"
fi

if [ "$workspace" = "$passivews" ] && [ "$activemonitor" != "$passivemonitor" ]; then
	hyprctl dispatch swapactiveworkspaces "$activemonitor" "$passivemonitor"
else
	hyprctl keyword general:no_cursor_warps 1
	hyprctl dispatch moveworkspacetomonitor "$workspace" "$activemonitor"
	hyprctl dispatch workspace "$workspace"
	hyprctl keyword general:no_cursor_warps 0
fi

exit 0
