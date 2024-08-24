alias clear="z4h-clear-screen-soft-bottom"

alias color_table="for i in {0..255}; do print -Pn '%K{$i}  %k%F{$i}${(l:3::0:)i}%f ' ${${(M)$((i%6)):#3}:+$\'\n\'}; done"

# Trash
alias rm='"Use trash/trashy instead or \rm if your really want rm"; false'
alias trash="trashy put"

# pacman and yay
alias unlock='sudo rm /var/lib/pacman/db.lck'    # remove pacman lock
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)' # remove orphaned packages
alias pac_remove_unused="sudo pacman -Qtdq | sudo pacman -Rns -"
alias pac_list_installed="pacman -Qe"
alias pac_browse_installed="pacman -Qq | fzf --preview 'pacman -Qil {}' --layout=reverse --bind 'enter:execute(pacman -Qil {} | less)'"
alias pac_browse_exp_installed="pacman -Qqe | fzf --preview 'pacman -Qil {}' --layout=reverse --bind 'enter:execute(pacman -Qil {} | less)'"

# adb
alias adb='HOME="$XDG_DATA_HOME"/android adb'

# vim
# alias nvim="lvim"
alias vim="nvim"
alias sunvim="sudo -E nvim"
alias nvim-kickstart='NVIM_APPNAME="nvim-kickstart" nvim'
alias nvim-lazy='NVIM_APPNAME="nvim-lazy" nvim'
alias nvchad='NVIM_APPNAME="nvchad" nvim'

# diff
alias diff="nvim -d"
alias vimdiff="nvim -d"
alias nvimdiff="nvim -d"

# Disable some console warnings likes GTK
alias bottles-cli="hide-warnings bottles-cli"

# move config files
alias svn="svn --config-dir $XDG_CONFIG_HOME/subversion"
alias nvnvidia-settings="nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings"
alias wget="wget --hsts-file=$XDG_DATA_HOME/wget-hsts"

#sudo
alias sudo="sudo "
alias sudoe="sudo -E"
# alias sudo='sudo -v; sudo '

alias ls="eza --group-directories-first --icons -Hlg"
alias ll="ls -a --git"
alias lt="ls -aT"
alias lss="eza -Hlgr --sort=size --icons --no-permissions"
alias lls="lss -ar --sort=size --git"
alias lts="lss -aTr --sort=size"
alias lsa="eza -Hlg --sort=age --icons --no-permissions"
alias lla="lsa -a --sort=age --git"
alias lta="lsa -aT --sort=age"
# alias lt="exa -aT --group-directories-first --icons"
# alias l.="exa -a | grep -E '^\.'"
alias ltree='ll --tree --level=2'


# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# confirm before overwriting something
# alias cp="cp -i"
# alias mv='mv -i'
# alias rm='rm -i'

# adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB
alias lynx='lynx -cfg=~/.lynx/lynx.cfg -lss=~/.lynx/lynx.lss -vikeys'
alias vifm='~/.config/vifm/scripts/vifmrun'
alias ncmpcpp='ncmpcpp ncmpcpp_directory=$HOME/.config/ncmpcpp/'
alias mocp='mocp -M "$XDG_CONFIG_HOME"/moc -O MOCDir="$XDG_CONFIG_HOME"/moc'

# ps
alias psa="ps auxf"
alias psgrep="ps aux | grep -v grep | grep -i -e VSZ -e"
alias psmem='ps auxf | sort -nr -k 4'
alias pscpu='ps auxf | sort -nr -k 3'

# get error messages from journalctl
alias jctl="journalctl -p 3 -xb"

# gpg encryption
# verify signature for isos
alias gpg-check="gpg2 --keyserver-options auto-key-retrieve --verify"
# receive the key of a developer
alias gpg-retrieve="gpg2 --keyserver-options auto-key-retrieve --receive-keys"

# alias upgrade-tools="z4h update"

# transition sudo to doas
# alias sudo="doas"
# alias sudoedit="doasedit"

# check qtile config
alias checkqtile="python3 ~/.config/qtile/config.py && qtile cmd-obj -o cmd -f validate_config"

# compile dxvk
alias updx="cd ~/Games/dxvk-tools/; git pull; ./updxvk build; ./updxvk lutris; ./updxvk proton-dist; ./upvkd3d-proton build; ./upvkd3d-proton lutris; ./upvkd3d-proton proton-dist"

