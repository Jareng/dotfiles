#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

eval $(gnome-keyring-daemon --start)
export SSH_AUTH_SOCK

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile

exec qtile start
#exec bspwm

# Sway Test
# export __GL_GSYNC_ALLOWED=0
# export __GL_VRR_ALLOWED=0
# export WLR_DRM_NO_ATOMIC=1
# export QT_AUTO_SCREEN_SCALE_FACTOR=1 
# export QT_QPA_PLATFORM=wayland
# export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
# export GDK_BACKEND=wayland
# export XDG_CURRENT_DESKTOP=sway 
# export GBM_BACKEND=nvidia-drm
# export __GLX_VENDOR_LIBRARY_NAME=nvidia 
# export MOZ_ENABLE_WAYLAND=1
# export WLR_NO_HARDWARE_CURSORS=1 
# exec sway --unsupported-gpu
# exec /home/jareng/sway.sh
