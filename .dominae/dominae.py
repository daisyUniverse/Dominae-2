#Screengrabbot by Ewi OwO

from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime
from pathlib import Path
from os import path
import subprocess
import discord
import asyncio

client = commands.Bot(command_prefix='>')

cwd = str(Path.home()) + "/.dominae"
img = cwd + "/img"
sh = cwd + "/sh"
txt = cwd + "/txt"

tokenfile = open(txt + '/token.txt','r')
token = tokenfile.read()
tokenfile.close()

@client.event
async def on_ready():
    print ("Bot Core Ready")
    print ('at {} \n'.format(str(datetime.now())))
    activity = discord.Game(name="ENABLED")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot: return

    channel = message.channel
    author  = message.author

    prefile = open(txt + '/pre.txt','r')
    pre = prefile.read().strip()

    tfile = open(txt + '/toggle.txt','r')
    toggle = tfile.read()

    if message.content.startswith('#OFF'):
        p = open(txt + '/toggle.txt','w')
        p.write("True")
        p.close

        await channel.send("Dominae is now OFF.")
        
        activity = discord.Game(name="DISABLED")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print ("Porn Mode " + toggle)
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('#ON'):
        n = open(txt + '/toggle.txt','w')
        n.write("False")
        n.close

        await channel.send("Dominae is now ON.")
        
        activity = discord.Game(name="ENABLED")
        await client.change_presence(status=discord.Status.online, activity=activity)
        print ("Porn Mode " + toggle)
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if toggle == "False":

        if message.content.startswith(pre + 'full'):

            subprocess.check_output(sh + "/sfull.sh")
            await channel.send(file=discord.File(img + "/sfull.png"))

            print ("Full Screenshot Uploaded ")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'window'):

            subprocess.check_output(sh + "/swindow.sh")
            await channel.send(file=discord.File(img + "/swindow.png"))

            print ("Window Screenshot Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'select'):

            subprocess.check_output(sh + "/sselect.sh")
            await channel.send(file=discord.File(img + "/sselect.png"))

            print ("Rectangle Select Screenshot Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'web'):

            subprocess.check_output(sh + "/sweb.sh")
            await channel.send(file=discord.File(img + "/sweb.png"))

            print ("Webshot Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'mov'):

            await channel.send("Recording...Please wait forever. (it takes a while.)")
            subprocess.check_output(sh + "/smov.sh")
            await channel.send(file=discord.File(img + "/smov.webm"))

            print ("Webm Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if '-ass' in message.content:

            ftfy = message.content.replace( "-ass " , " ass-" )
            await channel.send("\n Fixed that for you : \n" + '```' + "{}".format(author)[:-5] + ": " + ftfy + ' ```')
            await channel.send(file=discord.File(img + "/hyphen.jpg"))

            print ("Sweet-Ass Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'say'):

            f = open(txt + '/ssay.txt','w')
            f.write(message.content.replace("ssay ",""))
            f.close()

            subprocess.check_output(sh + "/ssay.sh")
            await channel.send(file=discord.File(img + '/ssay.png'))

            print ("Phrase Uploaded")
            print ("'" + message.content.replace("ssay ","") + "'")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'vox'):

            voxs = message.content.replace("svox ","")
            voxfn = voxs.replace(" ",".wav \n") + ".wav"
            voxfn += " svox.wav\n"
            voxfn = voxfn.lower()
            f = open(cwd + '/VOX/voxfn.txt','w')
            f.write(voxfn)
            f.close()

            subprocess.check_output(cwd + "/VOX/svox.sh")
            await channel.send(file=discord.File(cwd + '/VOX/svox.wav'))

            print ("Black Mesa Resarch Facility Notified")
            print ("'" + message.content.replace("svox ","") + "'")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith('#PREFIX'):

            f = open(txt + '/pre.txt','w')
            f.write(message.content.replace("#PREFIX ",""))
            with open(txt + '/pre.txt','r') as myfile:
                pre = myfile.read()
            f.close()

            print ("Prefix Changed to: " + "'" + message.content.replace("#PREFIX ","") + "'")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'server'):

            subprocess.check_output(sh + "/sremote.sh")
            await channel.send(file=discord.File(img + '/serversync.png'))

            print ("Server Scrot Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'servecam'):

            subprocess.check_output(sh + "/sremotecam.sh")
            await channel.send(file=discord.File(img + '/camsync.png'))

            print ("Server Webshot Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'pi'):

            subprocess.check_output(sh + "/spicam.sh")
            await channel.send(file=discord.File(img + '/pisync.png'))

            print ("Pi Shot Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'ibm'):

            subprocess.check_output(sh + "/spibm.sh")
            await channel.send(file=discord.File(img + '/ibmsync.png'))

            print ("IBM Shot Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))


        if message.content.startswith(pre + 'combo'):

            await channel.send("This will take a while...")
            subprocess.check_output(sh + "/scombo.sh")
            await channel.send(file=discord.File(img + '/result.png'))

            print ("Combo Shot Uploaded")
            print ('by {} at {} \n'.format(author, str(datetime.now())))


        if message.content.startswith(pre + 'help svox'):

            await channel.send("Here are the current VOX keywords.")
            await channel.send(file=discord.File(img + "/svox.png"))

            print ("Vox Keywords Shown")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

        if message.content.startswith(pre + 'help'):

            await channel.send("`" + pre + "help` shows this message. Who'd have thought? \n" + 
                                                     "`" + pre + "web` Takes a picture through my webcam \n" + 
                                                     "`" + pre + "mov` Takes a short clip through my webcam \n" + 
                                                     "`" + pre + "full` Takes a full screenshot of my monitors \n" + 
                                                     "`" + pre + "window` Takes a screenshot of the current window I'm using \n" + 
                                                     "`" + pre + "select` Forces me to select an area to screenshot \n" + 
                                                     "`" + pre + "server` Takes a screenshot of my server \n" + 
                                                     "`" + pre + "servecam` Takes a picture from my server camera \n" + 
                                                     "`" + pre + "say` Generates a text image out of some text \n" + 
                                                     "`" + pre + "vox` Generates an audio VOX sound. Use `" + pre + "vox help` for more info  \n" + 
                                                     "`#PREFIX` Sets the bot prefix. Default is s \n" + 
                                                     "`#ON / #OFF` Enables or Disables all bot functions")
            
            print ("Help Shown")
            print ('by {} at {} \n'.format(author, str(datetime.now())))

client.run(token.strip())
