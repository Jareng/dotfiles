#!/usr/bin/env bash

chosen="$(printf "  Power Off\n  Restart\n  Logout" | rofi -dmenu -i -theme-str '@import "powermenu.rasi"')"
poweroff=systemctl poweroff
reboot=systemctl reboot
logout="$LOGOUT_CMD"

case "$chosen" in
"  Power Off") "$poweroff" ;;
"  Restart") "$reboot" ;;
"  Logout") "$logout" ;;
*) exit 1 ;;
esac
