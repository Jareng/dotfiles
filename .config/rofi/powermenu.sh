#!/usr/bin/env bash

rofi \
	-show p \
	-modi p:'~/.config/rofi/scripts/rofi-power-menu' \
	-theme-str '@import "powermenu.rasi"'

# chosen="$(printf "  Power Off\n  Restart\n  Logout" | rofi -dmenu -i -theme-str '@import "powermenu.rasi"')"
# poweroff="systemctl poweroff"
# reboot="systemctl reboot"
# logout="$LOGOUT_CMD"
#
# case "$chosen" in
# "  Power Off")
# 	"$poweroff"
# 	;;
# "  Restart")
# 	"$reboot"
# 	;;
# "  Logout")
# 	"$logout"
# 	;;
# *)
# 	exit 1
# 	;;
# esac
