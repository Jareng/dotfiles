import os
import subprocess
import asyncio
from libqtile import qtile, layout, hook, bar, extension
from libqtile.command import lazy
from libqtile.config import Key, Group, Match, Click, Drag, \
    Screen, ScratchPad, DropDown
# from libqtile.backend.wayland import InputConfig
from env import openweather_loc, openweather_coord, openweather_apikey, wttr_loc
from libqtile.widget import Spacer, GroupBox, CurrentLayoutIcon, \
    TextBox, Wttr, Net, WindowTabs, PulseVolume, HDDBusyGraph, \
    CPU, Memory, Clock, Systray, Mpris2, OpenWeather

# color scheme
from colors import theme

# mod
mod = "mod4"
alt = "mod1"

# Fonts
font_base = "NotoSans Nerd Font Bold"
font_icons = "Font Awesome 6 Free Solid"

# Apps
myTerminal = os.getenv("TERMINAL")
# myTerminal = "alacritty"
myBrowser = os.getenv("BROWSER")
myFileManagerTUI = os.getenv("FILE_MANAGER_TUI")
myFileManagerGUI = os.getenv("FILE_MANAGER_GUI")
myCodeEditor = os.getenv("CODE_EDITOR")
myMixer = "pavucontrol"
myCalendar = "gsimplecal"
myPasswordManager = "keepassxc"

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

# wl_input_rules = {
#     "type:keyboard": InputConfig(kb_layout="fr"),
# }

#######################
# HOOKS
#######################
# @hook.subscribe.startup_once
# def startup():
#     processes = [
#         ["easyeffects", "--gapplication-service"],
#     ]
#
#     for p in processes:
#         subprocess.Popen(p)

@hook.subscribe.startup
def autostart():
    subprocess.call([HOME + "/.config/qtile/autostart.sh"])

# # Launch all scratchpad at start
# @hook.subscribe.startup_complete
# def scratchpad_startup():
#     scratchpad: ScratchPad = qtile.groups_map["scratchpad"]
#     for dropdown_name, dropdown_config in scratchpad._dropdownconfig.items():
#         scratchpad._spawn(dropdown_config)
#         def wrapper(name):
#             def hide_dropdown(_):
#                 dropdown = scratchpad.dropdowns.get(name)
#                 if dropdown:
#                     dropdown.hide()
#                     hook.unsubscribe.client_managed(hide_dropdown)
#             return hide_dropdown
#
#         hook.subscribe.client_managed(wrapper(dropdown_name))

@hook.subscribe.client_new
async def move_client(client):
    await asyncio.sleep(0.01)
    # Move spotify to workspace 8
    if client.name == "Spotify":
        client.togroup("8")

#######################
# KEYBINDS
#######################
keys = [
    Key([mod], "c",
        lazy.window.kill(),
        desc="Kill focused window"
    ),
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"
    ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),

    # Layouts
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),
    Key([mod, "shift"], "space",
        lazy.layout.flip(),
        desc="Flip layout"
    ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle Fullscreen"
    ),
    Key([mod, "shift"], "f",
        lazy.hide_show_bar(),
        desc="Hide/Show Bar"
    ),
    Key([mod], "t",
        lazy.window.toggle_floating(),
        desc="Toggle Floating",
    ),
    Key([mod], "m",
        lazy.window.toggle_minimize(),
        desc="Toggle Miniimize",
    ),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Grow window to the left",
    ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Grow window down",
    ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Grow window up",
    ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
    ),

    # MOVEMENTS
    Key([alt], "Tab",
        lazy.layout.next(),
        desc="Move window focus to other window"
    ),
    Key([alt, "control"], "Tab",
        lazy.next_screen(),
        desc="Toggle between screens"
    ),
    Key([mod], "Left",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key([mod], "Right",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key([mod], "Down",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key([mod], "Up",
        lazy.layout.up(),
        desc="Move focus up"
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key([mod, "shift"], "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key([mod, "shift"], "Up",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
    # Dmenu
    Key([mod, "shift"], "d",
        lazy.run_extension(
            extension.DmenuRun(
                font=font_base,
                fontsize="14",
                # dmenu_height=10,
                # dmenu_lines=15,
                background=theme["bg"],
                foreground=theme["fg"],
                selected_background=theme["bg_light"],
                selected_foreground=theme["primary"],
            )
        )
    ),
]

#######################
# MOUSE
#######################
mouse = [
    Drag([mod], "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position(),
    ),
    Drag([mod], "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()
    ),
    Click([mod], "Button2",
          lazy.window.bring_to_front()
    ),
]

#######################
# LAYOUTS
#######################
layout_settings = dict(
    border_width=1,
    margin=10,
    border_focus=theme["primary_dark"],
    border_normal=theme["bg"],
    font=font_base,
    grow_amount=4,
    single_border_width=0,
    single_margin=0,
)

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_settings),
]

floating_layout = layout.Floating(
    # **layout_settings,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        # Match(wm_class="yad"),
        Match(wm_class="mojosetup"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=1,
    border_focus=layout_settings["border_focus"],
    border_normal=layout_settings["border_normal"]
)

#######################
# GROUPS
#######################
# labels = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
# labels = ["", "", "", "", "", "", "阮", "", "", ""]
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
          matches=[Match(wm_class=["nemo", "thunar", "pcmanfm"])],
          spawn=[myFileManagerGUI]
    ),
    Group("4",
          label=groups_labels[3],
          layout="max",
          matches=[Match(wm_class=["Steam", "Lutris", "Bottles"])],
    ),
    Group("5",
          label=groups_labels[4],
          layout="monadtall",
          # matches=[Match(wm_class=[])],
          spawn=[myTerminal]
    ),
    Group("6",
          label=groups_labels[5],
          layout="monadtall",
          # matches=[Match(wm_class=[])],
    ),
    Group("7",
          label=groups_labels[6],
          layout="monadtall",
          matches=[Match(wm_class=["jellyfinmediaplayer"])],
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
        # mod + letter of group = switch to group
        Key(
            [mod], (key),
            lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name),
        )
    )
    keys.append(
        # mod + shift + letter of group = move focused window to group
        Key(
            [mod, "shift"], (key),
            lazy.window.togroup(group.name),
            desc="Move focused window to group {}".format(group.name),
        )
    )

#######################
# SCRATCHPADS
#######################
groups.append(
    ScratchPad("scratchpad", [
        DropDown("terminal", myTerminal,
            width=0.9, height=0.5,
            x=0.05,
        ),
        DropDown("easyeffects", "easyeffects",
            match=Match(title="EasyEffects"),
            width=0.9, height=0.9,
            x=0.05, y=0,
            opacity=1,
        ),
        DropDown("ranger", f"{myTerminal} -e {myFileManagerTUI}",
            width=0.8, height=0.8,
            x=0.1, y=0,
        ),
        DropDown("password_manager", myPasswordManager,
            match=Match(wm_class="KeePassXC"),
            width=0.9, height=0.9,
            x=0.05,
            opacity=1
        ),
        DropDown("calendar", myCalendar,
            # width=0.9, height=0,
            x=0.892, y=0,
        ),
        DropDown("mixer", myMixer,
            width=0.4, height=0.6,
            x=0.59, y=0,
            opacity=1,
        ),
]))

keys.extend([
    Key(["control"], groups_keys[0],
        lazy.group["scratchpad"].dropdown_toggle("terminal")
    ),
    Key(["control"], groups_keys[1],
        lazy.group["scratchpad"].dropdown_toggle("easyeffects")
    ),
    Key(["control"], groups_keys[2],
        lazy.group["scratchpad"].dropdown_toggle("ranger")
    ),
    Key(["control"], groups_keys[11],
        lazy.group["scratchpad"].dropdown_toggle("password_manager")
    ),
])

#######################
# WIDGETS
#######################
# widget settings
spacer_length = 10
widget_defaults = dict(
    font=font_base,
    fontsize=14,
    padding=2,
    background=theme["bg"],
    foreground=theme["fg"]
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
            active=theme["grey"],
            inactive=theme["grey"],
            highlight_color=theme["bg_light"],
            block_highlight_text_color=theme["primary"],
            this_current_screen_border=theme["green"],
            this_screen_border=theme["primary_dark"],
            other_current_screen_border=theme["grey"],
            other_screen_border=theme["grey"],
            urgent_border=theme["red"],
        ),
        Spacer(length=spacer_length),
        CurrentLayoutIcon(
            custom_icon_paths=[
                os.path.expanduser("~/.config/qtile/icons")
            ],
            scale=0.6,
        ),
        Spacer(length=spacer_length),
        # TextBox(
        #     foreground=theme["primary"],
        #     text="",
        #     font=font_icons,
        # ),
        # Spacer(length=spacer_length),
        WindowTabs(),
        # WindowName(
        #     mouse_callbacks={"Button1": lazy.layout.next()}
        # ),
        # TaskList(
        #     borderwidth=0,
        # ),
        TextBox(
            foreground=theme["primary"],
            text="",
            font=font_icons,
        ),
        Net(
            format="{down}"
        ),
        Spacer(length=spacer_length),
        TextBox(
            foreground=theme["primary"],
            text="",
            font=font_icons,
        ),
        Net(
            format="{up}"
        ),
        Spacer(length=spacer_length),
        TextBox(
            foreground=theme["primary"],
            text="",
            # font=font_icons,
        ),
        Mpris2(
            name="com.spotify.Client",
            scroll_interval=None,
            display_metadata=["xesam:title", "xesam:artist"],
            objname="org.mpris.MediaPlayer2.spotify",
        ),
        Spacer(length=spacer_length),
        HDDBusyGraph(
            border_width=0,
            graph_color=theme["primary"]
        ),
        Spacer(length=spacer_length),
        TextBox(
            foreground=theme["primary"],
            text="",
            font=font_icons,
        ),
        PulseVolume(
            limit_max_volume="True",
            update_interval=0.1,
            mouse_callbacks={
                "Button3":
                lazy.group["scratchpad"].dropdown_toggle("mixer")
            }
        ),
        Spacer(length=spacer_length),
        TextBox(
            foreground=theme["primary"],
            text="",
            font=font_icons,
        ),
        CPU(
            update_interval=1,
            format="{load_percent: .0f} %",
        ),
        Spacer(length=spacer_length),
        TextBox(
            text="",
            font=font_icons,
            foreground=theme["primary"],
        ),
        Memory(
            format="{MemPercent: .0f} %",
            measure_mem="G"
        ),
        Spacer(length=spacer_length),
        OpenWeather(
            app_key=openweather_apikey,
            coordinates=openweather_coord,
            dateformat="%Y-%m%d ",
            format="{icon} " \
                   "{temp:.1f}°{units_temperature} " \
                   "({main_feels_like:.1f}°{units_temperature}) " \
                   "{humidity}% " \
                   "{wind_speed:.1f}{units_wind_speed}",
            language="fr",
            location=openweather_loc,
            metric=True,
        ),
        # Wttr(
        #     lang="fr",
        #     location=wttr_loc,
        #     format="%c %t (%f)",
        #     units="m",
        #     update_interval=600,
        # ),
        Spacer(length=spacer_length),
        TextBox(
            foreground=theme["primary"],
            text="",
            font=font_icons,
        ),
        Clock(
            format="%a %d %b %H:%M:%S",
            mouse_callbacks={
                "Button1":
                lazy.group["scratchpad"].dropdown_toggle("calendar")
            }
        ),
        Spacer(length=spacer_length),
    ]

    if primary:
        # Clock mouse_callbacks doesn't work if i insert this before ??
        # pos = len(widgets) - 4
        # widgets[pos:pos] = [
        #     Systray(),
        #     Spacer(length=spacer_length),
        # ]
        widgets.extend([
            Systray(),
            Spacer(length=spacer_length),
        ])

    # widgets.extend([
    #     Spacer(length=spacer_length),
    # ])

    return widgets

# def widgets_monitor1():
#     widget_monitor1 = widgets_list(primary=True)
#     return widget_monitor1
#
# def widgets_monitor2():
#     widget_monitor2 = widgets_list(primary=False)
#     return widget_monitor2
#
# widgets_monitor1 = widgets_monitor1()
# widgets_monitor2 = widgets_monitor2()

#######################
# SCREENS
#######################
screens = [
    Screen(
        top=bar.Bar(
            # widgets_monitor1,
            widgets_list(primary=True),
            size=26
        )
    ),
    Screen(
        top=bar.Bar(
            # widgets_monitor2,
            widgets_list(primary=False),
            size=20
        )
    ),
]
