#!/bin/bash

#    Swytch is a script providing a window switcher for sway using rofi, awk and jq.
#    The script is based on:
#    https://www.reddit.com/r/swaywm/comments/aolf3u/quick_script_for_rofi_alttabbing_window_switcher/
#    Copyright (C) 2019  Björn Sonnenschein
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# todo: first, query all existing workspaces and build color dict, so that
#   all workspaces always get the same color, even if no windows at some workspace in between exists.
#   remark: not possible at least for hyprland, because hyprctl workspace only return actually used workspaces
#   and not all workspaces that are defined in config

# TODO: performance
# TODO: make icons optional for performance

blue="#5E81AC"
green="#A3BE8C"
orange="#D08770"
red="#BF616A"
magenta="#B48EAD"

# obtain command to execute with swaymsg for selected window
if [ -z "$1" ]; then
	command_=focus
else
	command_=$1
fi

# TODO: is XDG_CURRENT_DESKTOP the appropriate variable?
# TODO: style and DRY
if [ "$XDG_CURRENT_DESKTOP" == "Sway" ]; then
	# Obtain the avaliable windows' workspaces, names and IDs as strings
	#mapfile -t windows < <(
	# TODO: fix sway
	function make_array_windows {
		declare -A result=(
			$(
				swaymsg -t get_tree | jq -r '[
    	    recurse(.nodes[]?)
    	    |recurse(.floating_nodes[]?)
    	    |select(.type=="workspace")
    	    | . as $workspace | recurse(.nodes[]?)
    	    |select(.type=="con" and .name!=null)
    	    |sort_by($workspace.name, .name)[]
    	    |."'"$1"
			))
		return result
	}

elif [ "$XDG_CURRENT_DESKTOP" == "Hyprland" ]; then
	id_active=$(hyprctl activewindow -j | grep -oP '(?<="address": ")(.*)(?=",)')

	# TODO: instead of calling jq for each variable, build some array of dicts
	# Remark: I do not understand why hyprctl clients returns some emtpy clients sometimes (with class=""),
	#   but they must be excluded.
	json=$(hyprctl clients -j | jq -r 'sort_by(.workspace.name)[] | select(.workspace.id != -1 and .class != "")')

	# Use grep instead of jq for performance
	mapfile -t names < <(echo "$json" | grep -oP '(?<="title": ")(.*)(?=",)')
	mapfile -t classes < <(echo "$json" | grep -oP '(?<="class": ")(.*)(?=",)')
	mapfile -t ids < <(echo "$json" | grep -oP '(?<="address": ")(.*)(?=",)')
	mapfile -t workspaces < <(echo "$json" | grep -oP '(?<="name": ")(.*)(?=")')

#  end_time=$(date +%s.%3N)
#
#  elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
#  echo time get windows: $elapsed

fi

# get window list to display
windows_separators=()
colors=("$blue" "$green" "$orange" "$red" "$magenta")
workspace_previous=''
index_workspace_active=0
index_window_last_active=0
num_separators=0
index_color=0
bold=1

#start_time=$(date +%s.%3N)

for index_window in "${!ids[@]}"; do
	# todo: consider arbitraty workspace name length by separating by space instead of simply taking first argument.
	workspace=${workspaces[$index_window]}
	title=${names[$index_window]}
	class=${classes[$index_window]}
	id=${ids[$index_window]}

	if [ "${id}" == "${id_active}" ]; then
		index_window_last_active=("${index_window}")
	fi

	# obtain index of the active window
	if [ "${id}" == "${id_active}" ]; then
		index_workspace_active=$(($workspace))
	fi

	window=("$workspace£$class£$title")

	# escape problematic characters
	# for now, simply delete them.
	# TODO: escape
	# TODO: add all possible problematic characters
	window=$(echo "$window" | tr -d '%&')
	#      has_char=$(echo "$window" | grep '&')
	#    window=$(echo "$window" | sed 's/h//g')

	windows_separators+=("${window}")
done
#
#end_time=$(date +%s.%3N)
#elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
#echo time make array windows with separator: $elapsed

## column spacing
#start_time=$(date +%s.%3N)
mapfile -t windows_separators_spaced < <(printf '%s\n' "${windows_separators[@]}" | column -s "£" -t)
#end_time=$(date +%s.%3N)
#elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
#echo time make windows with columns: $elapsed

windows_separators_formatted=()

#start_time=$(date +%s.%3N)

# store icons to avoid searching icons for known applications
declare -A icons

for index_window in "${!ids[@]}"; do
	# todo: consider arbitraty workspace name length by separating by space instead of simply taking first argument.
	window=${windows_separators_spaced[$index_window]}
	workspace=${workspaces[$index_window]}
	class=${classes[$index_window]}

	# if window has different workspace than previous, use next color. Cycle through colors
	if [ "$workspace" != "$workspace_previous" ] && [ ! -z "$workspace_previous" ]; then
		index_color=$index_color+1
	fi

	if (($index_color == ${#colors[@]})); then
		index_color=0
	fi

	if (($bold == 1)); then
		window_formatted=("<b><span foreground=\"${colors[$index_color]}\">${window}</span></b>")
	else
		window_formatted=("${window}")
	fi

	if [[ ${icons[$class]+exists} ]]; then
		icon="${icons[$class]}"
	else
		# try to find icon by desktop name and class
		icon=$(find /usr/share/applications ${HOME}/.local/share/applications/ -name "*${class}.desktop" -exec grep -oP '(?<=Icon=).*' {} \; | head -1)
		if [ -z "$icon" ]; then
			icon=$(grep -ir StartupWMClass=${class} /usr/share/applications/*.desktop ${HOME}/.local/share/applications/*.desktop -l | xargs grep -oP '(?<=Icon=).*' | head -1)
		fi
		icons[$class]=$icon
	fi

	icon="\0icon\x1f${icon}\n"
	window_formatted_w_icon="${window_formatted}${icon}"
	windows_separators_formatted+=("${window_formatted_w_icon}")
	workspace_previous=$workspace
done

#end_time=$(date +%s.%3N)
#elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
#echo time make array windows formatted: $elapsed

if [ -z "$monitor_id" ]; then
	idx_selected=$(printf '%b' "${windows_separators_formatted[@]}" | rofi -dmenu -i -p "$command_" -a "$index_workspace_active" -format i -selected-row "$index_window_last_active" -no-custom -s -width 80 -lines 30 -markup-rows -show-icons)
else
	idx_selected=$(printf '%b' "${windows_separators_formatted[@]}" | rofi -monitor $monitor_id -dmenu -i -p "$command_" -a "$index_workspace_active" -format i -selected-row "$index_window_last_active" -no-custom -s -width 80 -lines 30 -markup-rows -show-icons)
fi

# if no entry selected (e.g. user exitted with escape), end
if [ -z "$idx_selected" ]; then
	exit 1
fi
id_selected=${ids[$idx_selected]}
workspace_selected=${workspaces[$idx_selected]}

if [ "$XDG_CURRENT_DESKTOP" == "Sway" ]; then
	### unmaximize all maximized windows on the workspace of the selected window
	# Obtain the avaliable windows' workspaces, names and IDs as strings
	# TODO: FIX this for current code!
	mapfile -t ids_windows_maximized < <(
		swaymsg -t get_tree | jq -r '[
      recurse(.nodes[]?)
      |recurse(.floating_nodes[]?)
      |select(.type=="workspace")
      | . as $workspace | recurse(.nodes[]?)
      |select(.type=="con" and .name!=null and .fullscreen_mode==1 and $workspace.name=="'"$workspace_selected"'")
      |{workspace: $workspace.name, name: .name, id: .id, focused: .focused, app_id: .app_id}]
      |sort_by(.workspace, .name)[]
      |(.id|tostring)'
	)

	# unmaximize the maximized windows that are not the selected one
	for id_window_maximized in "${ids_windows_maximized[@]}"; do
		if [ "$id_window_maximized" != "$id_selected" ]; then
			swaymsg "[con_id=$id_window_maximized] fullscreen disable"
		fi
	done

	# Tell sway to focus said window
	if [ ! -z "$id_selected" ]; then
		swaymsg "[con_id=$id_selected] $command_"
	fi
elif [ "$XDG_CURRENT_DESKTOP" == "Hyprland" ]; then
	# TODO: also handle maximized windows?
	hyprctl dispatch focuswindow address:$id_selected
fi
