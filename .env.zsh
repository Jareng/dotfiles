# unset LC_ALL

## Path
export PATH="$PATH:$CARGO_HOME/bin:$GOPATH/bin:$HOME/.scripts"

## Theme
export GTK_THEME_VARIANT="dark"
export QT_STYLE_OVERRIDE="kvantum"
export GTK_THEME="Flat-Remix-GTK-Blue-Dark-Solid"
# export XCURSOR_THEME="Vimix-white-cursors"
export XCURSOR_THEME="Nordzy-cursors"
export XCURSOR_SIZE=30

export XKB_DEFAULT_LAYOUT="fr"
export XKB_DEFAULT_VARIANT="nodeadkeys"


## Config files

# General
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"
export XDG_CACHE_HOME="$HOME/.cache"

# Folders
export XDG_DESKTOP_DIR="$HOME/Desktop"
export XDG_DOWNLOAD_DIR="$HOME/Downloads"
export XDG_DOCUMENTS_DIR="$HOME/Documents"
export XDG_MUSIC_DIR="$HOME/Music"
export XDG_PICTURES_DIR="$HOME/Pictures"
export XDG_VIDEOS_DIR="$HOME/Videos"
export XDG_TEMPLATES_DIR="$HOME/Templates"
export XDG_PUBLICSHARE_DIR="$HOME/Public"

export XDG_DATA_DIRS="$HOME/.local/share/flatpak/exports/share:$XDG_DATA_DIRS"

# Zsh
# export HISTSIZE=1000
# export SAVEHIST="$HISTSIZE"

# Electron
export ELECTRON_OZONE_PLATFORM_HINT="wayland"

# Android
export ANDROID_USER_HOME="$XDG_DATA_HOME/android"

# Shell
export HISTFILE="${XDG_STATE_HOME}/zsh/history"

# dotnet
export DOTNET_CLI_HOME="$XDG_DATA_HOME/dotnet"

# Hyprshot
export HYPRSHOT_DIR="$XDG_PICTURES_DIR/Hyprshot"

# cargo
export CARGO_HOME="$XDG_DATA_HOME/cargo"
export CARGO_NET_GIT_FETCH_WITH_CLI=true

# cuda
export CUDA_CACHE_PATH="$XDG_CACHE_HOME/nv"

# gnupg
export GNUPGHOME="$XDG_DATA_HOME/gnupg"

# go
export GOPATH="$XDG_DATA_HOME/go"

# gtk-2.
export GTK2_RC_FILES="$XDG_CONFIG_HOME/gtk-2.0/gtkrc"

# icons
export XCURSOR_PATH=/usr/share/icons:"$XDG_DATA_HOME/icons"

# Java
# _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=gasp'

# less
export LESSHISTFILE="$XDG_STATE_HOME/less/history"
export LESSKEY="$XDG_CONFIG_HOME/less/keys"

# mypy
export MYPY_CACHE_DIR="$XDG_CACHE_HOME/mypy"

# ncurses
export TERMINFO="$XDG_DATA_HOME/terminfo"
export TERMINFO_DIRS="$XDG_DATA_HOME/terminfo":/usr/share/terminfo

# nvm
export NVM_DIR="$XDG_DATA_HOME/nvm"

# Python
export PYTHON_HISTORY="$XDG_DATA_HOME/python/history"

# rustup
export RUSTUP_HOME="$XDG_DATA_HOME/rustup"

# Rust
export RUSTC_WRAPPER="sccache"

# wget
export WGETRC="$XDG_CONFIG_HOME/wget/wgetrc"

# Wine
export WINEPREFIX="$XDG_DATA_HOME/wine"
# Stop wine setting its own applications as defaults
export WINEDLLOVERRIDES="winemenubuilder.exe=d"

## Variables
export TERM="xterm-256color"
export EDITOR="nvim"
export VISUAL="nvim"
export TERMINAL="kitty"
export BROWSER="firefox"
export FILE_MANAGER="thunar"
export FILE_MANAGER_GUI="thunar"
export FILE_MANAGER_TUI="yazi"
export CODE_EDITOR="vscode"
export OPENER="xdg-open"
# export PAGER="less"
# export PAGER="nvim"
# export WM="qtile"
# Neovim Manpager
export MANPAGER='nvim +Man!'
# Neovim Pacdiff
export DIFFPROG="nvim -d"

# Pipewire
export PIPEWIRE_LATENCY="256/48000"

export KEYB_DEVICE_NAME="holtek-usb-hid-keyboard"

# Steam
export STEAM_FORCE_DESKTOPUI_SCALING=1.5
