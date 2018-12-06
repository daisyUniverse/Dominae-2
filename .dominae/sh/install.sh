#!/bin/sh

# Installer script for Dominae.

if grep ID /etc/os-release | grep -qE "fedora"; then
    echo "Fedora detected! Installing prerequisites..."
	sudo dnf install \
		scrot \
		imagemagick \
		epel-release \
		https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm \
		ffmpeg \
		ffmpeg-devel \
		libffi \
		sox \
		python35 
    echo "Installing python packages..."
    sudo python3.5 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
    sudo python3.5 -m pip install -U aiohttp
    sudo python3.5 -m pip install -U websockets
    sudo cp $HOME/.dominae/sh/dominae /usr/bin
    echo "Done."
    echo "Make sure you set your bot token by using [dominae -t <token>] before running!"
    
elif grep ID /etc/os-release | grep -qE 'debian|ubuntu'; then
	DEBIAN_FRONTEND=noninteractive
	DEBCONF_NONINTERACTIVE_SEEN=true
        export DEBIAN_FRONTEND DEBCONF_NONINTERACTIVE_SEEN
    echo "Debian / Ubuntu detected. Installing prerequisites..."
    sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt-get update
	sudo apt-get install \
		scrot \
		imagemagick \
		ffmpeg \
		ffmpeg-devel \
		libffi \
		sox \
		python3.5 
    echo "Installing python packages..."
    sudo python3.5 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
    sudo python3.5 -m pip install -U aiohttp
    sudo python3.5 -m pip install -U websockets
    sudo cp $HOME/.dominae/sh/dominae /usr/bin
    echo "Done."
    echo "Make sure you set your bot token by using [dominae -t <token>] before running!"
    
elif grep ID /etc/os-release | grep -q 'arch\|manjaro'; then
    echo "Arch / Manjaro detected. Installing prerequisites..."
	sudo pacman -S \
		scrot \
		imagemagick \
		ffmpeg \
		ffmpeg-devel \
		libffi \
		sox \
		python35 
    echo "Installing python packages..."
    sudo python3.5 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
    sudo python3.5 -m pip install -U aiohttp
    sudo python3.5 -m pip install -U websockets
    sudo cp $HOME/.dominae/sh/dominae /usr/bin
    echo "Done."
    echo "Make sure you set your bot token by using [dominae -t <token>] before running!"
    
else
	echo "Sorry, I haven't added support for your OS's package manager yet. You can find the list of prerequisites on my github and install them manually, then copy ~/.dominae/sh/dominae to your /usr/bin"
fi
