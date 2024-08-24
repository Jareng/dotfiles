#!/bin/sh

# magnify_value_float="$(hyprctl -j getoption misc:cursor_zoom_factor | jaq '.float')"
# magnify_value=${magnify_value_float%%.*}
#
# echo $magnify_value_float
# echo $magnify_value
# echo $1
# if [[ $1 == $magnify_value ]]; then
#   magnify_value="1"
# else
#   magnify_value="$1"
# fi
#
# hyprctl keyword misc:cursor_zoom_factor $magnify_value

magnify_value="$(hyprctl -j getoption cursor:zoom_factor | jaq '.float')"
incr="0.1"

if [ "$1" == false ]; then
	magnify_value="1"
else
	magnify_value="$(echo $magnify_value + $incr | bc)"
fi

hyprctl keyword cursor:zoom_factor "$magnify_value"
