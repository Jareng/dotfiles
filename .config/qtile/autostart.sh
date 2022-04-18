#!/bin/bash

check_if_running () {
    if ! pgrep -x $1 > /dev/null
    then
        echo "> $1"
        case $1 in

            picom)
                $1 -b --config ~/.config/picom/picom.conf &
                ;;

            *)
                $1 &
                ;;
        esac
    fi
}

allApps=(
    "dunst"
    "sxhkd"
    "picom"
)

for APP in ${allApps[@]}
do
    check_if_running "$APP"
done
