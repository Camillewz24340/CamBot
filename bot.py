import atexit
from dis import disco
from platform import platform
import random
import re
from socket import MsgFlag
import discord
from discord.ext import tasks
import os
import time
import platform
from datetime import datetime
from termcolor import colored as col3
from utils import botstatus, consoledebug as Debug
from uptime import uptime
import sys
import math
import stopwatch

botstatus.clear_console_output()

if platform.system() == "Windows":
    os.system("cmd /c title CamBot - Starting")
Debug.DuringOperation("Starting...")

token = open("./token.txt", "r")
OwnerID = 660631616074547224
client = discord.Client()
uptime = stopwatch.Stopwatch()
uptime.start()
startupTime = datetime.now()
upSince = f"{str(startupTime.weekday)} {str(startupTime.day)}/{str(startupTime.month)} at {str(startupTime.hour)}:{str(startupTime.minute)} !"



def set_status():
    status = discord.Status.online
    if(datetime.now().hour < 7 or datetime.now().hour > 18):
        status = discord.Status.idle
    return status

@tasks.loop(seconds=2)
async def change_activity():
    activityList = [
    f"Im up since {upSince} !",
    "I'm cool !",
    f"I'm in {str(len(client.guilds))} servers !",
    f"Today is {datetime.now().day}/{datetime.now().month}/{datetime.now().year}",
    f"{datetime.now().hour}:{datetime.now().minute}",
    "Hi ! :D",
    ""
    ]

    await client.change_presence(status=set_status(),activity= discord.Activity(name=activityList[random.randint(0, len(activityList) - 1)],type=1))

    

@client.event
async def on_ready():
    botstatus.clear_console_output()
    Debug.Success(f"Ready, Connected as {client.user} in {str(len(client.guilds))} servers")
    if platform.system() == "Windows":
        os.system("cmd /c title CamBot - Ready")
    

    change_activity.start()

@client.event
async def on_message(message):
 
    if message.author == client.user:
        return
    msg = message.content.lower()
    send = message.channel.send
    edit = message.channel.edit

    if msg == "hi" or msg == "hello" or msg == "cam hello" or msg == "cam hi" or msg == "hey" or msg == "cam hey":
        messages = ["Hi !","Hi there !","Hey ! how it's going ?","Yo ! Whats up ?","Hey !","Hello !","Oh, hi !"]
        randMessage = random.randint(0,len(messages) - 1)
        await send(messages[randMessage])

    if re.match("bye|goodbye|cam bye|cam goodbye|i gtg",msg):
        messages = ["See ya !", "Bye !", "See you soon !", "Oh, see you later !", "Goodbye !", "See ya bud !"]
        randMessage = random.randint(0,len(messages) - 1)
        await send(messages[randMessage])

    if msg.startswith("hm"):
        await send(":thinking:_ _")

    if f"<@{str(client.user.id)}>" in message.content or msg == "cam ping":
        swtime = stopwatch.Stopwatch()
        swtime.start()
        await message.add_reaction("🏓")
        swtime.stop()
        elapsed = swtime.elapsed
        await send(f"Pong ! took {math.floor(elapsed*1000)} ms.")
    
    if re.match("lol|lmao|xd", msg):
        await send(":joy:_ _")
        
    if re.match("a+h+", msg):
        await send(":scream:_ _")

    if re.match("a+u+g+h", msg):
        await send(":weary:_ _") 
    
    if msg == "afk" or msg == "back" or msg == "im back" or msg == "i'm back":
        await message.add_reaction("👍")

    if re.match("cam say ", msg):
        txt = msg.replace("cam say ", "")
        if message.author.id == OwnerID:
            await message.delete()
            await send(txt)

    if re.match("^cam wiki", msg):
        query = message.content.replace("cam wiki", "")
        if query == "" or query == "_ _":
            await send("Search something, not the void ! :joy:")
            return
        from commands.internet import wikisearch
        await send(wikisearch.main(query))

    if msg == "cam wake up":
        await send("You can't wake me up, coz i already woke up :D")

    if re.match("cam removelast",msg):
        await message.delete()
        await message.channel.purge(limit=1)
        

    if msg == "cam lines":
        
        l = 0
        from pathlib import Path
        pathlist = Path("./").rglob('*.py')
        for path in pathlist:
            with open(str(path), "r", encoding="utf-8") as lines:
                for count, line in enumerate(lines):
                        pass
                        
            l += count + 1
        
        await send(f"In all my files, i have {str(l)} lines of code")

    if re.match("^cam qrcode",msg):
        from commands.internet import qrcodemake
        QRText = message.content.replace("cam qrcode","")
        if QRText == "":
            await send("You didn't precise data ! I'm gonna use my invitation link !", file=qrcodemake.makeqr("https://discord.com/api/oauth2/authorize?client_id=991796518904414218&permissions=8&scope=bot"))
            return    

        await send(file=qrcodemake.makeqr(QRText))
    
    if re.match("^cam user", msg):
        from commands.discordrelated import userinfo
        search = re.search("\d+", message.content).group()
        user = await client.fetch_user(int(search))
        await send(embed=userinfo.main(user))

    if re.match("^cam pycode ",msg):
        try:
            code = message.content.replace("cam pycode ","")
            print(code)
            from commands.dev import pycode
            await send(pycode.pycode(str(code)))
            
        except Exception as e:
            await send("An error occured:" + "`" + str(e) + "`")
            return "An error occured:" + str(e)


    if msg == "cam stop":
        Debug.DuringOperation("Restart Request Detected, checking if owner...")
        if not message.author.id == OwnerID:
            Debug.Error("Author ID doesn\'t match, not restarting")
            return
        await message.delete()
        Debug.Success("Author ID matches !")
        Debug.DuringOperation("Stopping...")
        if platform.system() == "Windows":
            os.system("cmd /c title CamBot - Stopping")
        time.sleep(1)
        sys.exit()

client.run(token.read())