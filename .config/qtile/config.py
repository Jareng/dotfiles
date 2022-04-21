import os
import subprocess
from libqtile import qtile, layout, hook, bar
from libqtile.command import lazy
from libqtile.config import Key, Group, Match, Click, Drag, Screen

# widgets
from libqtile.widget.spacer import Spacer
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayoutIcon
from libqtile.widget.textbox import TextBox
from libqtile.widget.wttr import Wttr
from libqtile.widget.net import Net
from libqtile.widget.windowtabs import WindowTabs
from libqtile.widget.pulse_volume import PulseVolume
from libqtile.widget.graph import HDDBusyGraph
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.clock import Clock
from libqtile.widget.systray import Systray

# color scheme
import colors

# color scheme
theme = colors.nord


# mod
mod = "mod4"
alt = "mod1"

# Fonts
font_base = "NotoSans Nerd Font Bold"
font_icons = "Font Awesome 6 Free Solid"

# Apps
terminal = "alacritty"
browser = "firefox"
pulse_app = "pavucontrol"

# widget settings
lang = "fr"
wttr_loc = {"50.5199,2.64781": "Béthune"}
spacer_length = 10
widget_defaults = dict(
    font=font_base,
    fontsize=14,
    padding=2,
    background=theme["bg"],
    foreground=theme["fg"]
)
extension_defaults = widget_defaults.copy()

# layout settings
layout_settings = {
    "border_width": 2,
    "margin": 5,
    "border_focus": theme["primary_dark"],
    "border_normal": theme["bg"],
    "font": font_base,
    "grow_amount": 4,
}
labels = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]

# bars settings
main_bar_height = 26
secondary_bar_height = 18

# general settings
home = os.path.expanduser("~")
wmname = "LG3D"
auto_fullscreen = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
auto_minimize = True


# functions
def open_calendar():  # spawn calendar widget
    qtile.cmd_spawn("gsimplecal")


def close_calendar():  # kill calendar widget
    qtile.cmd_spawn("killall -q gsimplecal")


def show_weather():
    qtile.cmd_spawn(f"{terminal} --hold -t 'Wttr-Weather' -e wttr {list(wttr_loc.values())[0]}")


#
# HOOKS
#
@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])

# Swallow ?
# import psutil

# @hook.subscribe.client_new
# def _swallow(window):
#     pid = window.window.get_net_wm_pid()
#     ppid = psutil.Process(pid).ppid()
#     cpids = {c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()}
#     for i in range(5):
#         if not ppid:
#             return
#         if ppid in cpids:
#             parent = window.qtile.windows_map.get(cpids[ppid])
#             parent.minimized = True
#             window.parent = parent
#             return
#         ppid = psutil.Process(ppid).ppid()

# @hook.subscribe.client_killed
# def _unswallow(window):
#     if hasattr(window, 'parent'):
#         window.parent.minimized = False


#
# KEYBINDS
#
keys = [
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="toggle Fullscreen"
    ),

    # LAYOUTS
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),
    Key([mod, "shift"], "space",
        lazy.layout.flip(),
        desc="Flip layout"
    ),
    Key([mod], "t",
        lazy.window.toggle_floating(),
        desc="Toggle Floating",
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
        desc="Move window to the left"
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

    Key([mod], "q",
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

    # APPLICATIONS
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
    ),
]


#
# MOUSE
#
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

layouts = [
    layout.Max(),
    layout.MonadTall(
        **layout_settings,
        ratio=0.60,
        single_border_width=0,
        single_margin=0,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

# floating_layout = layout.Floating(
#     **layout_settings,
#     float_rules=[
#         # Run the utility of `xprop` to see the wm class and name of an X client.
#         *layout.Floating.default_float_rules,
#         Match(title="weather"),
#         Match(title="branchdialog"),  # gitk
#         Match(title="pinentry"),  # GPG key password entry
#         Match(title="Open File"),
#         Match(title="Unlock Database - KeePassXC"),  # Wayland
#         Match(title="File Operation Progress", wm_class="thunar"),  # Wayland
#         Match(title="Friends List", wm_class="Steam"),
#         Match(wm_class="confirmreset"),  # gitk
#         Match(wm_class="makebranch"),  # gitk
#         Match(wm_class="maketag"),  # gitk
#         Match(wm_class="ssh-askpass"),  # ssh-askpass
#         Match(wm_class="Arandr"),
#         Match(wm_class="QjackCtl"),
#         Match(wm_class="org.kde.ark"),
#         Match(wm_class="confirm"),
#         Match(wm_class="dialog"),
#         Match(wm_class="download"),
#         Match(wm_class="error"),
#         Match(wm_class="fiji-Main"),
#         Match(wm_class="file_progress"),
#         Match(wm_class="imv"),
#         Match(wm_class="lxappearance"),
#         Match(wm_class="mpv"),
#         Match(wm_class="notification"),
#         Match(wm_class="pavucontrol"),
#         Match(wm_class="Pinentry-gtk-2"),
#         Match(wm_class="qt5ct"),
#         Match(wm_class="ssh-askpass"),
#         Match(wm_class="Dragon"),
#         Match(wm_class="Dragon-drag-and-drop"),
#         Match(wm_class="toolbar"),
#         Match(wm_class="wlroots"),
#         Match(wm_class="Xephyr"),
#         Match(wm_class="yad"),
#         Match(wm_class="nvidia-settings"),
#         Match(wm_type='utility'),
#         Match(wm_type='notification'),
#         Match(wm_type='toolbar'),
#         Match(wm_type='splash'),
#         Match(wm_type='dialog'),
#         Match(role="gimp-file-export"),
#         Match(func=lambda c: c.has_fixed_size()),
#         Match(func=lambda c: bool(c.is_transient_for())),
#     ]
# )


floating_layout = layout.Floating(
    **layout_settings,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(title="Wttr-Weather"),
        # Match(wm_class="confirmreset"),  # gitk
        # Match(wm_class="makebranch"),  # gitk
        # Match(wm_class="maketag"),  # gitk
        # Match(wm_class="ssh-askpass"),  # ssh-askpass
        # Match(title="branchdialog"),  # gitk
        # Match(title="pinentry"),  # GPG key password entry
    ]
)


#
# GROUPS
#
groups = [
    Group("1",
        label=labels[0],
        layout="max"),
    Group("2",
        label=labels[1],
        layout="max"
    ),
    Group("3",
        label=labels[2],
        layout="max",
        matches=[Match(wm_class=["Geany"])]
    ),
    Group("4",
        label=labels[3],
        layout="monadtall"
    ),
    Group("5",
        label=labels[4],
        layout="monadtall"
    ),
    Group("6",
        label=labels[5],
        layout="monadtall"
    ),
    Group("7",
        label=labels[6],
        layout="monadtall"
    ),
    Group("8",
        label=labels[7],
        layout="max",
        matches=[Match(wm_class=["Guitarix"])]
    ),
    Group("9",
        label=labels[8],
        layout="max",
        matches=[Match(wm_class=["Spotify"])]
    ),
    Group("10",
        label=labels[9],
        layout="max",
        matches=[Match(wm_class=["jellyfinmediaplayer"])]
    ),
]

# QWERTY
# group_keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# AZERTY
group_keys = [
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
    # "parenright",
    # "equal",
]

#
# GROUPS BINDING
#
for k, group in zip(group_keys, groups):
    keys.append(
        # mod1 + letter of group = switch to group
        Key(
            [mod], (k),
            lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name),
        )
    )
    keys.append(
        # mod1 + shift + letter of group = move focused window to group
        Key(
            [mod, "shift"], (k),
            lazy.window.togroup(group.name),
            desc="Move focused window to group {}".format(group.name),
        )
    )


# # Append scratchpad with dropdowns to groups
# groups.append(ScratchPad('scratchpad', [
#     DropDown('term', 'kitty', width=0.4, height=0.5, x=0.3, y=0.1, opacity=1),
#     DropDown('mixer', 'pavucontrol', width=0.4,
#              height=0.6, x=0.3, y=0.1, opacity=1),
#     DropDown('pomo', 'pomotroid', x=0.4, y=0.2, opacity=1),
#     DropDown('bitwarden', 'bitwarden-desktop',
#              width=0.4, height=0.6, x=0.3, y=0.1, opacity=1),
# ]))
# # extend keys list with keybinding for scratchpad
# keys.extend([
#     Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
#     Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
#     Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('pomo')),
#     Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
# ])


def init_bar():
    return [
        GroupBox(
            padding=1,
            margin_y=3,
            borderwidth=2,
            disable_drag=True,
            rounded=False,
            highlight_method="line",
            active=theme["primary"],
            inactive=theme["grey"],
            highlight_color=theme["bg_light"],
            block_highlight_text_color=theme["primary"],
            this_current_screen_border=theme["primary"],
            this_screen_border=theme["bg_light"],
            other_current_screen_border=theme["bg"],
            other_screen_border=theme["bg_light"],
            urgent_border=theme["red"],
        ),
        Spacer(length=spacer_length),
        CurrentLayoutIcon(
            custom_icon_paths=[
                os.path.expanduser("~/.config/qtile/icons")
            ],
            scale=0.8,
        ),
        Spacer(length=spacer_length),
        TextBox(
            foreground=theme["primary"],
            text="",
            font=font_icons,
        ),
        Spacer(length=spacer_length),
        WindowTabs(),
        Spacer(length=spacer_length),
        Wttr(
            lang=lang,
            location=wttr_loc,
            format="%c %t (%f)",
            units="m",
            update_interval=600,
            mouse_callbacks={"Button1": show_weather}
        ),
        Spacer(length=spacer_length),
        HDDBusyGraph(
            border_width=0,
            graph_color=theme["primary"]
        ),
        Spacer(length=spacer_length),
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
            text="",
            font=font_icons,
        ),
        PulseVolume(
            limit_max_volume="True",
            update_interval=0.1,
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn(pulse_app)},
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
            format="{MemPercent: .0f} % {SwapUsed: .0f}{mm}",
            # format="{MemUsed: .0f}{mm}",
            measure_mem="G"
        ),
        Spacer(length=spacer_length),
        TextBox(
            foreground=theme["primary"],
            text="",
            font=font_icons,
        ),
        Clock(
            format="%a %d %b %H:%M:%S",
            mouse_callbacks={'Button1': open_calendar, 'Button2': close_calendar}
        ),
        Spacer(length=spacer_length),
        # Systray(),
        # Spacer(length=spacer_length),
    ]


systray = [
    Systray(),
    Spacer(length=spacer_length),
]

main_bar = init_bar() + systray
second_bar = init_bar()

screens = [
    Screen(
        top=bar.Bar(
            main_bar,
            size=main_bar_height
        )
    ),
    Screen(
        top=bar.Bar(
            second_bar,
            size=secondary_bar_height
        )
    ),
]
