#!/bin/sh

active_window="$(hyprctl activewindow -j | jq -r ".class")"

if [ "$active_window" != "firefox" ]; then
	hyprctl dispatch killactive ""
fi
