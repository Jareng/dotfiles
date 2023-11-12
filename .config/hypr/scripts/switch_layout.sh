#!/bin/sh

hyprctl switchxkblayout holtek-usb-hid-keyboard next

devices=$(hyprctl devices -j)
devices_tmp=/tmp/hypr/devices

# echo $devices
# layout=$(grep -A 2 -E "(^|\s)holtek-usb-hid-keyboard($|\s)" "$devices" | awk 'NR==3 {print $3}')
layout_full=$(echo "$devices" | jaq -r '.keyboards[] | select(.name=="holtek-usb-hid-keyboard") | .active_keymap')
echo $layout_full

if [ "$layout_full" = "English (US)" ]; then
	layout="us"
else
	layout="fr"
fi

setxkbmap $layout

notify-send "Hyprland" "Layout $layout\n$layout_full"

exit 0
