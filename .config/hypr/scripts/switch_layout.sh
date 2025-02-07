#!/bin/sh

hyprctl switchxkblayout all next

devices=$(hyprctl devices -j)
# devices_tmp=/tmp/hypr/devices

# echo $devices
# layout=$(grep -A 2 -E "(^|\s)holtek-usb-hid-keyboard($|\s)" "$devices" | awk 'NR==3 {print $3}')
layout_full=$(echo "$devices" | jaq -r '.keyboards[] | select(.name=="holtek-usb-hid-keyboard") | .active_keymap')

if [ "$layout_full" = "English (US)" ]; then
	layout="us"
else
	layout="fr"
fi

etxkbmap "$layout"

notify-send "Hyprland" "Layout $layout\n$layout_full"

exit 0
