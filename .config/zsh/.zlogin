#!/bin/bash

if [ "$(tty)" = "/dev/tty1" ];then
  # exec startx
  # exec wl_qtile
  exec wl_hyprland
  # exec wl_sway
fi
