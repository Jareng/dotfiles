#!/bin/sh

ACTIVE_WINDOW="$(hyprctl activewindow -j | jq -r ".class")"

if [ "$ACTIVE_WINDOW" != "firefox" ]; then
  hyprctl dispatch 'hl.window.close()'
fi
