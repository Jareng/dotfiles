#/bin/bash

isFloating="$(hyprctl activewindow -j | jq -r '.floating')"
fullscreenMode="$(hyprctl activewindow -j | jq -r '.fullscreenmode')"
window="$(hyprctl activewindow -j | jq -r '.address')"
workspace="$1"

hyprctl dispatch movetoworkspacesilent $workspace

if [ $isFloating = "false" && $fullscreenMode != "0" ]; then
	hyprctl dispatch fullscreen "1, address:$window"
fi
