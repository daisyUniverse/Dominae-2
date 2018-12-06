# Dominae

A BASH and Discord.py Rewrite based Discord bot (Linux only!)
Main use is for taking pictures through the webcam of the system running the bot, along with other fun bits and bobs

## Getting Started

To get started, you need to have .dominae in your home directory and you need to run the install script to get all the prerequisites installed and the scripts in the right places, then you can run `dominae -t <token>` to set your bot token. then just run dominae and you should up up and running!

```
git clone https://github.com/Evshaddock/Dominae-2.git
cp -r /Dominae/.dominae/ ~
cd ~/.dominae/sh
./install.sh
dominae -t <bot token>
dominae
```

To run the bot in logging mode (for example if you want to start it up with your machine) you need to run 
```
dominae -l
```
this will write all bot activity to ~/.dominae/txt/log.txt

### Prerequisites

If you'd rather install the prerequisites yourself, or the script isn't working on your system here are all the required packages

```
scrot
imagemagick
ffmpeg
libffi
sox
python3.5
```

You'll also need to install some python modules. you can do that by doing this

```
sudo python3.5 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
sudo python3.5 -m pip install -U aiohttp
sudo python3.5 -m pip install -U websockets
```

Once that's done you should copy my startup script to your bin to make launching easier, you can do that by running this

```
sudo cp ~/.dominae/sh/dominae /usr/bin
```

If you'd rather run it without the launch script, just remember to put your bot token in `~/.dominae/txt/token.txt`, if it doesn't exist, create it.
Run the bot with `python35 ~/.dominae/dominae.py`

### Bot Features

`shelp` shows this message. Who'd have thought? 

`sweb` Takes a picture through my webcam 

`smov` Takes a short clip through my webcam 

`sfull` Takes a full screenshot of my monitors 

`swindow` Takes a screenshot of the current window I'm using 

`sselect` Forces me to select an area to screenshot 

`sserver` Takes a screenshot of a remote system[Not working (for now!)]

`sservecam` Takes a picture from a remote systems camera [Not working (for now!)]

`ssay` Generates a text image out of some text 

`svox` Generates an audio VOX sound. Use svox help for more info

`#PREFIX` Sets the bot prefix. Default is `s`

`#ON` / `#OFF` Enables or Disables all bot functions

`scombo` This is meant to take every available image and stitch them together into one giant image to post. It's not functional without the new SSH system implemented so consider this a 'coming soon' type deal.

Note: You might notice there are some functions that connect to other machines. These use SSH and aren't ready to be implemented in my public release of this bot. I will have a system for setting this up eventually.

