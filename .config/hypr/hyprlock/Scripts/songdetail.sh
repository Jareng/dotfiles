#!/bin/bash

# song_info=$(playerctl metadata --format '{{title}}  {{artist}}')
#
# echo "$song_info"

if [[ $(playerctl -p spotify status 2>/dev/null) == "Playing" ]]; then
  status='▷  '
else
  status='  '
fi

song_info=$(playerctl -p spotify metadata --format "$status {{title}} - {{artist}}")

echo "$song_info"
