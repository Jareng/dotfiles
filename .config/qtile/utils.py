import os

MOD = "mod4"
ALT = "mod1"
CTRL = "control"
SHIFT = "shift"

FONTS = "NotoSans Nerd Font Bold"
FONTS_ICONS = "Font Awesome 6 Free Solid"
FONT_SIZE = 15
ICONS_THEME = "/usr/share/icons/Flat-Remix-Blue-Dark/"

TERMINAL = os.getenv("TERMINAL")
FILEMANAGER_GUI = os.getenv("FILE_MANAGER_GUI")
FILEMANAGER_TUI = os.getenv("FILE_MANAGER_TUI")
BROWSER = os.getenv("BROWSER")
CODE_EDITOR = os.getenv("CODE_EDITOR")
CALENDAR = "gsimplecal"
MIXER = "pavucontrol"
APP_LAUNCHER = "rofi -show drun -show-icons"
EMOJI_SELECTOR = "rofi -show emoji -theme-str '#element-icon { enabled: false; }'"
POWERMENU = "powermenu"

KEYBOARD_LAYOUT = "fr"
KEYBOARD_VARITAN = "nodeadkeys"

SPACER_LENGTH = 10

CPU_TEMP = "/sys/class/thermal/thermal_zone2/temp"

PRIMARY_MONITOR_BAR_HEIGHT = 26
SECONDARY_MONITOR_BAR_HEIGHT = 20


# COMMANDS
GET_SPEAKERS_VOLUME = '''
    pactl get-sink-volume @DEFAULT_SINK@ \
    | grep -i Volume \
    | awk '{print $5}' \
    | sed 's/%//'
'''
RAISE_SPEAKERS_VOLUME = '''
    pactl set-sink-mute @DEFAULT_SINK@ 0 && \
    pactl set-sink-volume @DEFAULT_SINK@ +5%
'''
LOWER_SPEAKERS_VOLUME = 'pactl set-sink-volume @DEFAULT_SINK@ -5%'

ARE_SPEAKERS_MUTED = '''
    pactl get-sink-mute @DEFAULT_SINK@ \
        | grep -q 'no' \
        && echo 0 \
        || echo 1
'''
TOGGLE_SPEAKERS_MUTE = 'pactl set-sink-mute @DEFAULT_SINK@ toggle'

GET_MICROPHONE_VOLUME = '''
    pactl get-source-volume @DEFAULT_SOURCE@ \
    | grep -i Volume \
    | awk '{print $5}' \
    | sed 's/%//'
'''
IS_MICROPHONE_MUTED = '''
    pactl get-source-mute @DEFAULT_SOURCE@ \
        | grep -q 'no' \
        && echo 0 \
        || echo 1
'''
TOGGLE_MICROPHONE_MUTE = '''
    pactl set-source-mute @DEFAULT_SOURCE@ toggle
'''
