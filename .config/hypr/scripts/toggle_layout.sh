#!/bin/sh

layout="$(hyprctl -j getoption general:layout | jaq -r '.str')"

if [ "$layout" = "master" ]; then
	hyprctl keyword general:layout "dwindle"
else
	hyprctl keyword general:layout "master"
fi
