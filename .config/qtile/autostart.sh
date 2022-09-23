#!/bin/bash

function is_running {
  # grab the first word of a string
  set -- $1
  # if process is not running
  if ! pgrep -x $1 > /dev/null; then
    echo "$1 is not running"
    $*
  fi
  return 0
}

apps=(
  "dunst &"
  "sxhkd &"
  "nitrogen --restore"
  "unclutter --timeout 2 &"
  "picom -b --config /home/$(whoami)/.config/picom/picom.conf"
)

# Need "" around ${apps[@]} so it take the full string
for app in "${apps[@]}"; do
  is_running "$app"
done
