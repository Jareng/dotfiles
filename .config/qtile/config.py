import os
import re
import subprocess
import asyncio
from env import OPW_APIKEY, OPW_COORD, OPW_LOC
from utils import *
from libqtile import qtile, layout, hook, bar, extension
from libqtile.command import lazy
from libqtile.config import Key, Group, Match, Click, Drag, \
    Screen, ScratchPad, DropDown
from libqtile.backend.wayland import InputConfig
from libqtile.widget import Spacer, GroupBox, CurrentLayoutIcon, \
    TextBox, Net, WindowTabs, PulseVolume, HDDBusyGraph, \
    CPU, Memory, Clock, Mpris2, OpenWeather, WidgetBox, ThermalZone, \
    CPUGraph, DF, Load
from qtile_extras.widget import StatusNotifier

# color scheme
from themes.fjord import *

# general settings
HOME = os.path.expanduser("~")
wmname = "LG3D"
auto_fullscreen = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
auto_minimize = True

#######################
# WAYLAND
#######################
wl_input_rules = {
    "type:keyboard": InputConfig(
        kb_layout="fr",
        kb_variant="nodeadkeys"
    ),
}


#######################
# HOOKS
#######################
@hook.subscribe.startup
def autostart():
    subprocess.call([HOME + "/.config/qtile/autostart.sh"])


# Reload config on screen changes
@hook.subscribe.screens_reconfigured
async def outputs_changed():
    await asyncio.sleep(1)
    qtile.reload_config()


@hook.subscribe.client_new
async def move_client(client):
    # Center new floating window
    if client.floating:
        client.center()
    # wait for client name to be updated
    await asyncio.sleep(0.01)
    # Move spotify to workspace 9
    if client.name == "Spotify":
        client.togroup("9")


# Cycle through window including floating in max layout
@lazy.window.function
def float_to_front(client):
    if client.floating:
        client.bring_to_front()
    else:
        client.bring_to_front()
        client.disable_floating()

    # Key([MOD], "Tab",
    #     lazy.group.next_window(),
    #     float_to_front(),
    #     desc="move focus to next window"
    # ),

#######################
# KEYBINDS
#######################
keys = [
    # Keys_base
    Key([MOD], "c",
        lazy.window.kill(),
        desc="Kill focused window"
    ),
    Key([MOD, CTRL], "r",
        lazy.reload_config(),
        desc="Restart Qtile"
    ),
    Key([MOD, CTRL], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),

    # Keys_layouts
    Key([MOD, CTRL], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts",
    ),
    Key([MOD, SHIFT], "space",
        lazy.layout.flip(),
        desc="Flip layout"
    ),
    Key([MOD], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle Fullscreen"
    ),
    Key([MOD, SHIFT], "f",
        lazy.hide_show_bar(),
        desc="Hide/Show Bar"
    ),
    Key([MOD], "t",
        lazy.window.toggle_floating(),
        lazy.window.center(),
        desc="Toggle Floating",
    ),
    Key([MOD], "m",
        lazy.window.toggle_minimize(),
        desc="Toggle Miniimize",
    ),
    Key([MOD], "left",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key([MOD], "right",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key([MOD], "down",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key([MOD], "up",
        lazy.layout.up(),
        desc="Move focus up"
    ),
    # Key([MOD], "space",
    #     lazy.layout.next(),
    #     desc="Move window focus to other window"
    # ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD, SHIFT], "left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key([MOD, SHIFT], "right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key([MOD, SHIFT], "down",
        lazy.layout.shuffle_down(), 
        desc="Move window down"
    ),
    Key([MOD, SHIFT], "up",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([MOD, CTRL], "left",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
    ),
    Key([MOD, CTRL], "right",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
    ),
    Key([MOD, CTRL], "down",
        lazy.layout.grow_down(),
        desc="Grow window down"
    ),
    Key([MOD, CTRL], "up",
        lazy.layout.grow_up(),
        desc="Grow window up"
    ),
    Key([MOD], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
    ),

    # Keys_move
    Key([ALT], "Tab",
        # lazy.layout.next(),
        lazy.group.next_window(),
        float_to_front(),
        desc="Move window focus to other window"
    ),
    Key([MOD], "Tab",
        lazy.screen.toggle_group(),
        desc="Switch to Previous Group",
    ),
    Key([MOD], "twosuperior",
        lazy.next_screen(),
        desc="Toggle between screens"
    ),

    # Keys_apps
    Key([MOD], "Return",
        lazy.spawn(TERMINAL),
        desc="Terminal",
    ),
    Key([MOD], "r",
        lazy.spawn(APP_LAUNCHER),
        desc="Rofi",
    ),
    Key([MOD, SHIFT], "e",
        lazy.spawn(EMOJI_SELECTOR),
        desc="Rofi Emoji",
    ),
    Key([MOD, SHIFT], "p",
        lazy.spawn(POWERMENU),
        desc="Rofi Powermenu",
    ),
    # Dmenu
    Key([MOD, SHIFT], "d",
        lazy.run_extension(
            extension.DmenuRun(
                font=FONTS,
                fontsize=FONT_SIZE,
                background=BACKGROUND,
                foreground=FOREGROUND,
                selected_background=BACKGROUND_ALT,
                selected_foreground=PRIMARY,
            )
        )
    ),
]

#######################
# MOUSE
#######################
mouse = [
    Drag([MOD], "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position(),
    ),
    Drag([MOD], "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()
    ),
    Click([MOD], "Button2",
          lazy.window.bring_to_front()
    ),
]

#######################
# LAYOUTS
#######################
layout_settings = dict(
    border_width=2,
    margin=10,
    border_focus=PRIMARY_ALT,
    border_normal=BACKGROUND,
    font=FONTS,
    grow_amount=4,
    single_border_width=0,
    single_margin=0,
)

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_settings),
]

#######################
# FLOATING_RULES
#######################
floating_layout = layout.Floating(
    **layout_settings,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # Match(title=WM_NAME, wm_class=WM_CLASS, role=WM_WINDOW_ROLE)
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        # Match(wm_class="yad"),
        Match(wm_class="mojosetup"),
        Match(wm_class="thunar", title="File Operation Progress"),
        Match(wm_class="file-roller"),
        # Steam
        # Match(title="Friends List"),
        # Match(title="Steam - News"),
        Match(title=re.compile("Steam - News")),
        Match(wm_class="Steam", title=re.compile("Friends List")),
        # The following Match` will float all windows that are transient windows for a parent window:
        Match(func=lambda c: bool(c.is_transient_for())),
    ],
)

#######################
# GROUPS
#######################
# groups_labels = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
# groups_labels = ["", "", "", "", "", "", "阮", "", "", ""]
groups_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Keyboard layout
# QWERTY
# groups_keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# AZERTY
groups_keys = [
    "ampersand",
    "eacute",
    "quotedbl",
    "apostrophe",
    "parenleft",
    "minus",
    "egrave",
    "underscore",
    "ccedilla",
    "agrave",
    "parenright",
    "equal",
]

groups = [
    Group("1",
          label=groups_labels[0],
          layout="max",
          # matches=[Match(wm_class=[])],
    ),
    Group("2",
          label=groups_labels[1],
          layout="max",
          # matches=[Match(wm_class=[])],
    ),
    Group("3",
          label=groups_labels[2],
          layout="max",
          # matches=[Match(wm_class=["nemo", "thunar", "pcmanfm"])],
          matches=[Match(wm_class=re.compile('^Nemo.*|^Thunar.*', re.IGNORECASE))],
          spawn=[FILEMANAGER_GUI]
    ),
    Group("4",
          label=groups_labels[3],
          layout="max",
          # matches=[Match(wm_class=["Steam", "Lutris", "com.usebottles.bottles"])],
          matches=[Match(wm_class=re.compile('^Steam.*|^Lutris.*|^Bottles.*', re.IGNORECASE))],
    ),
    Group("5",
          label=groups_labels[4],
          layout="monadtall",
          # matches=[Match(wm_class=[])],
          spawn=[TERMINAL]
    ),
    Group("6",
          label=groups_labels[5],
          layout="monadtall",
          # matches=[Match(wm_class=[])],
    ),
    Group("7",
          label=groups_labels[6],
          layout="monadtall",
          matches=[Match(wm_class=["Jellyfin Media Player"])],
    ),
    Group("8",
          label=groups_labels[7],
          layout="max",
          matches=[Match(wm_class=["Guitarix"])],
    ),
    Group("9",
          label=groups_labels[8],
          layout="max",
          matches=[Match(wm_class=["Spotify"])],
    ),
    Group("10",
          label=groups_labels[9],
          layout="max",
          matches=[Match(wm_class=["easyeffects"])],
          # spawn=["easyeffects"]
    ),
]

#######################
# GROUPS BINDINGS
#######################
for key, group in zip(groups_keys, groups):
    keys.append(
        # MOD + letter of group = switch to group
        Key(
            [MOD], (key),
            lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name),
        )
    )
    keys.append(
        # MOD + shift + letter of group = move focused window to group
        Key(
            [MOD, SHIFT], (key),
            lazy.window.togroup(group.name),
            desc="Move focused window to group {}".format(group.name),
        )
    )

#######################
# SCRATCHPADS
#######################
groups.append(
    ScratchPad("scratchpad", [
        DropDown(TERMINAL, TERMINAL,
            width=0.8, height=0.8,
            x=0.1, y=0.1,
            opacity=1.1,
            on_focus_lost_hide=False,
        ),
        DropDown(FILEMANAGER_TUI, f"{TERMINAL} -e {FILEMANAGER_TUI}",
            width=0.8, height=0.8,
            x=0.1, y=0.1,
            opacity=1.1,
        ),
        DropDown(CALENDAR, CALENDAR,
            x=0.892, y=0,
        ),
        DropDown(MIXER, MIXER,
            width=0.4, height=0.6,
            x=0.59, y=0,
            opacity=1,
        ),
    ],
    single = False,
    )
)

keys.extend([
    Key([MOD], "Space",
        lazy.group["scratchpad"].dropdown_toggle(TERMINAL)
    ),
    Key([CTRL], groups_keys[0],
        lazy.group["scratchpad"].dropdown_toggle(FILEMANAGER_TUI)
    ),
])

#######################
# WIDGETS
#######################
widget_defaults = dict(
    font=FONTS,
    fontsize=FONT_SIZE,
    padding=4,
    background=BACKGROUND,
    foreground=FOREGROUND,
)
extension_defaults = widget_defaults.copy()

def widgets_list(primary=False):
    widgets = [
        GroupBox(
            padding=3,
            margin_y=3,
            borderwidth=2,
            disable_drag=True,
            hide_unused=True,
            rounded=False,
            highlight_method="line",
            active=GREY,
            inactive=GREY,
            highlight_color=BACKGROUND_ALT,
            block_highlight_text_color=PRIMARY,
            this_current_screen_border=GREEN,
            this_screen_border=PRIMARY_ALT,
            other_current_screen_border=GREY,
            other_screen_border=GREY,
            urgent_border=RED,
        ),
        Spacer(length=SPACER_LENGTH),
        CurrentLayoutIcon(
            custom_icon_paths=[
                os.path.expanduser("~/.config/qtile/icons"),
            ],
            scale=0.7,
        ),
        Spacer(length=SPACER_LENGTH),
        WindowTabs(
            # selected=(f"<span underline='single' underline-color='{PRIMARY}' font-size='105%'>", "</span>"),
            selected=(f"<span underline='single' underline-color='{PRIMARY}' font_weight='ultrabold'>", "</span>"),
            # selected=(f"<span overline='single' overline-color='{PRIMARY}' font_weight='ultrabold'>", "</span>"),
            # selected=("<u>", "</u>"),
            # selected=(f"<span foreground='{PRIMARY}'>", "</span>")
        ),
        Spacer(length=SPACER_LENGTH),
        Mpris2(
            # objname="org.mpris.MediaPlayer2.spotify",
            # scroll_interval=None,
            # # fmt=f"<span foreground='{GREEN}'></span> " + " {}",
            # # format=f"<span foreground='{PRIMARY}'></span> "+" {xesam:title} - {xesam:artist}",
            # format="{xesam:title} - {xesam:artist}",
            # playing_text="{track}",
            # # paused_text=f"<span foreground='{ORANGE}'></span> "+" {track}",
            # scroll=False,
        ),
        Spacer(length=SPACER_LENGTH),
        TextBox(
            foreground=PRIMARY,
            text="",
            font=FONTS_ICONS,
        ),
        PulseVolume(
            # get_volume_command=GET_SPEAKERS_VOLUME,
            # mute_command=TOGGLE_SPEAKERS_MUTE,
            limit_max_volume="True",
            update_interval=0.1,
            step=1,
            volume_app="pactl",
            mouse_callbacks={
                "Button3":
                lazy.group["scratchpad"].dropdown_toggle(MIXER)
            },
        ),
        Spacer(length=SPACER_LENGTH),
        WidgetBox(
            widgets=[
                CPU(
                    format="{freq_current}GHz {load_percent:.0f}% "
                ),
                TextBox(
                    foreground=PRIMARY,
                    text="",
                    font=FONTS_ICONS,
                ),
                ThermalZone(
                    fgcolor_normal=FOREGROUND,
                    fgcolor_high=ORANGE,
                    fgcolor_crit=RED,
                    crit=90,
                    zone=CPU_TEMP,
                ),
                CPUGraph(
                    border_width=2,
                    border_color=BACKGROUND,
                    graph_color=PRIMARY,
                    fill_color=PRIMARY_ALT,
                ),
                TextBox(
                    text="",
                    foreground=PRIMARY,
                    font=FONTS_ICONS,
                ),
                Memory(
                    format="{MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}",
                    measure_mem="G",
                ),
            ],
            foreground=PRIMARY,
            font=FONTS_ICONS,
            text_closed="",
            text_open="",
        ),
        # CPU(format="{load_percent:.0f}% "),
        Load(
            format="{load:.2f}"
        ),
        Spacer(length=SPACER_LENGTH),
        WidgetBox(
            widgets=[
                HDDBusyGraph(
                    border_width=2,
                    border_color=BACKGROUND,
                    graph_color=PRIMARY,
                    fill_color=PRIMARY_ALT,

                ),
                DF(
                    partition="/",
                    visible_on_warn=False,
                ),
                DF(
                    partition="/home",
                    visible_on_warn=False,
                ),
            ],
            foreground=PRIMARY,
            font=FONTS_ICONS,
            text_closed="",
            text_open="",
        ),
        DF(
            partition="/",
            visible_on_warn=True,
        ),
        DF(
            partition="/home",
            visible_on_warn=True,
        ),
        Spacer(length=SPACER_LENGTH),
        WidgetBox(
            widgets=[
                Net(
                    format=f"<span foreground='{GREEN}' size='large'> </span>" \
                            "{up:.1f}{up_suffix}",
                ),
                Net(
                    format=f"<span foreground='{GREEN}' size='large'> </span>" \
                            "{down:.1f}{down_suffix}",
                ),
            ],
            foreground=PRIMARY,
            text_closed="",
            text_open="",
            font=FONTS_ICONS,
        ),
        Spacer(length=SPACER_LENGTH),
        OpenWeather(
            app_key=OPW_APIKEY,
            coordinates=OPW_COORD,
            dateformat="%Y-%m%d ",
            format="{icon} " \
                   "{temp:.1f}°{units_temperature} " \
                   "({main_feels_like:.1f}°{units_temperature}) " \
                   "{humidity}% " \
                   "{wind_speed:.1f}{units_wind_speed}",
            language="fr",
            location=OPW_LOC,
            metric=True,
        ),
        Spacer(length=SPACER_LENGTH),
        WidgetBox(
            widgets=[
                Clock(
                    format="%A %d %B",
                    mouse_callbacks={
                        "Button1":
                        lazy.group["scratchpad"].dropdown_toggle(CALENDAR),
                    },
                ),
            ],
            foreground=PRIMARY,
            text_closed="",
            text_open="",
            font=FONTS_ICONS,
        ),
        Clock(
            format="%H:%M",
            mouse_callbacks={
                "Button1":
                lazy.group["scratchpad"].dropdown_toggle(CALENDAR),
            },
        ),
        Spacer(length=SPACER_LENGTH),
    ]

    if primary:
        widgets.extend([
            StatusNotifier(
                icon_theme=ICONS_THEME,
            ),
            Spacer(length=SPACER_LENGTH),
        ]),

    return widgets

#######################
# SCREENS
#######################
screens = [
    Screen(
        top=bar.Bar(
            widgets_list(primary=True),
            size=PRIMARY_MONITOR_BAR_HEIGHT,
        )
    ),
    Screen(
        top=bar.Bar(
            widgets_list(primary=False),
            size=SECONDARY_MONITOR_BAR_HEIGHT,
        )
    ),
]
