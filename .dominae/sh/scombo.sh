#! /bin/bash
$HOME/.dominae/sh/sweb.sh
$HOME/.dominae/sh/spicam.sh
$HOME/.dominae/sh/sremotecam.sh
$HOME/.dominae/sh/sfull.sh
$HOME/.dominae/sh/sremote.sh
$HOME/.dominae/sh/spibm.sh
ffmpeg -i $HOME/.dominae/img/ibmsync.png -s 640x480 $HOME/.dominae/img/presult-1.png -y
ffmpeg -i $HOME/.dominae/img/sfull.png -s 1920x400 $HOME/.dominae/img/presult-1-1.png -y
convert $HOME/.dominae/img/pisync.png $HOME/.dominae/img/camsync.png $HOME/.dominae/img/presult-1.png +append $HOME/.dominae/img/presult-2.png
convert $HOME/.dominae/img/sweb.png $HOME/.dominae/img/presult-2.png $HOME/.dominae/img/presult-1-1.png -append $HOME/.dominae/img/result.png
