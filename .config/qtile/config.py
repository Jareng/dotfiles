import os
import subprocess
import asyncio
from libqtile import layout, hook, bar
from libqtile.command import lazy
from libqtile.config import Key, Group, Match, Click, Drag, \
    Screen, ScratchPad, DropDown

# widgets
from libqtile.widget import Spacer, GroupBox, CurrentLayoutIcon, \
    TextBox, Wttr, Net, WindowTabs, PulseVolume, HDDBusyGraph, \
    CPU, Memory, Clock, Systray

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
files_browser = "pcmanfm"
# music_player = "com.spotify.Client"
music_player = "dev.alextren.Spot"
pulse_app = "pavucontrol"
calendar = "gsimplecal"

# layout settings
layout_settings = {
    "border_width": 2,
    "margin": 5,
    "border_focus": theme["primary_dark"],
    "border_normal": theme["bg"],
    "font": font_base,
    "grow_amount": 4,
}
# labels = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
# labels = ["", "", "", "", "", "", "阮", "", "", ""]
labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Keyboard layout
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
    "parenright",
    "equal",
]

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

# bars settings
main_bar_height = 26
secondary_bar_height = 20

# general settings
HOME = os.path.expanduser("~")
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


#
# HOOKS
#
@hook.subscribe.startup
def autostart():
    subprocess.call([HOME + "/.config/qtile/autostart.sh"])


@hook.subscribe.client_new
async def move_client(client):
    await asyncio.sleep(0.01)
    if client.name == "Spotify":
        client.togroup("8")


# # Move Gsimplecal under the clock widget
# @hook.subscribe.client_new
# def set_gsimplecal_floating(c):
#     # set floating immediately so it doesn't change tiling windows temporarily
#     if c.name == "gsimplecal":
#         c.cmd_enable_floating()
#
#
# @hook.subscribe.client_managed
# def set_gsimplecal_position(c):
#     if c.name == "gsimplecal":
#         c.cmd_set_size_floating(100, 100)
#         c.cmd_set_position_floating(2285, 26)


#
# KEYBINDS
#
keys = [
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
        desc="toggle Fullscreen"
    ),
    Key([mod], "t",
        lazy.window.toggle_floating(),
        desc="Toggle Floating",
    ),
    Key([mod], "m",
        lazy.window.toggle_maximize(),
        desc="Toggle Maximize",
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

#
# LAYOUTS
#
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

floating_layout = layout.Floating(
    **layout_settings,
    float_rules=[
        # Run the utility of `xprop`
        # to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Open File"),
        Match(title="Unlock Database - KeePassXC"),  # Wayland
        Match(title="File Operation Progress", wm_class="thunar"),  # Wayland
        Match(title="Friends List", wm_class="Steam"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="Arandr"),
        Match(wm_class="QjackCtl"),
        Match(wm_class="org.kde.ark"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="fiji-Main"),
        Match(wm_class="file_progress"),
        Match(wm_class="imv"),
        Match(wm_class="lxappearance"),
        Match(wm_class="mpv"),
        Match(wm_class="notification"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="Pinentry-gtk-2"),
        Match(wm_class="qt5ct"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="Dragon"),
        Match(wm_class="Dragon-drag-and-drop"),
        Match(wm_class="toolbar"),
        Match(wm_class="wlroots"),
        Match(wm_class="Xephyr"),
        Match(wm_class="yad"),
        Match(wm_class="nvidia-settings"),
        Match(wm_type='utility'),
        Match(wm_type='notification'),
        Match(wm_type='toolbar'),
        Match(wm_type='splash'),
        Match(wm_type='dialog'),
        Match(role="gimp-file-export"),
        Match(func=lambda c: c.has_fixed_size()),
        Match(func=lambda c: bool(c.is_transient_for())),
    ]
)


#
# GROUPS
#
groups = [
    Group("1",
          label=labels[0],
          layout="max",
          # matches=[Match(wm_class=[])]
    ),
    Group("2",
          label=labels[1],
          layout="max",
          # matches=[Match(wm_class=[])]
    ),
    Group("3",
          label=labels[2],
          layout="max",
          # matches=[Match(wm_class=[])]
    ),
    Group("4",
          label=labels[3],
          layout="max",
          matches=[Match(wm_class=["Steam", "Lutris", "Bottles"])]
    ),
    Group("5",
          label=labels[4],
          layout="monadtall",
          # matches=[Match(wm_class=[])]
    ),
    Group("6",
          label=labels[5],
          layout="monadtall",
          # matches=[Match(wm_class=[])]
    ),
    Group("7",
          label=labels[6],
          layout="monadtall",
          # matches=[Match(wm_class=[])]
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


#
# GROUPS BINDINGS
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

#
# SCRATCHPADS
#
groups.append(
    ScratchPad('scratchpad', [
        DropDown('calendar', calendar,
            # width=0.9, height=0,
            x=0.892, y=0,
            opacity=1
        ),
        DropDown('term', terminal,
            width=0.8, height=0.5,
            opacity=0.9,
        ),
        DropDown('mixer', pulse_app,
            width=0.4, height=0.6,
            x=0.59, y=0,
            on_focus_lost_hide=True,
            warp_pointer=True,
            opacity=1
        ),
        DropDown('music', music_player,
            width=0.8, height=0.8,
            match="Spotify"
            # x=0.4, y=0.2, opacity=1
        ),
        DropDown('files', files_browser,
            width=0.8, height=0.8,
            opacity=1,
        ),
        # DropDown('bitwarden', 'bitwarden-desktop',
        #     # width=0.4, height=0.6, x=0.3, y=0.1, opacity=1
        # ),
]))

keys.extend([
    Key(["control"], group_keys[0], # 1
        lazy.group['scratchpad'].dropdown_toggle('term')
    ),
    Key(["control"], group_keys[1], # 2
        lazy.group['scratchpad'].dropdown_toggle('mixer')
    ),
    Key(["control"], group_keys[2],
        lazy.group['scratchpad'].dropdown_toggle('music')
    ),
    Key(["control"], group_keys[3],
        lazy.group['scratchpad'].dropdown_toggle('files')
    ),
    # Key(["control"], group_keys[3],
    #     lazy.group['scratchpad'].dropdown_toggle('bitwarden')
    # ),
])

#
# WIDGETS
#
def widgets_bar(primary=False):
    widgets = [
        GroupBox(
            padding=1,
            margin_y=3,
            borderwidth=2,
            disable_drag=True,
            hide_unused=False,
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
        # WindowName(
        #     mouse_callbacks={"Button1": lazy.layout.next()}
        # ),
        # TaskList(
        #     borderwidth=0,
        # ),
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
                lazy.group['scratchpad'].dropdown_toggle('mixer')
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
        Wttr(
            lang=lang,
            location=wttr_loc,
            format="%c %t (%f)",
            units="m",
            update_interval=600,
        ),
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
                lazy.group['scratchpad'].dropdown_toggle('calendar')
            }
        ),
    ]
    if primary:
        widgets.append(Systray())

    widgets.append(Spacer(length=spacer_length))
    return widgets

#
# SCREENS
#
screens = [
    Screen(
        top=bar.Bar(
            widgets_bar(primary=True),
            size=main_bar_height
        )
    ),
    Screen(
        top=bar.Bar(
            widgets_bar(primary=False),
            size=secondary_bar_height
        )
    ),
]
