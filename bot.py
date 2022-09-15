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

botstatus.clear_console_output()

if platform.system() == "Windows":
    os.system("cmd /k title CamBot - Starting")
Debug.DuringOperation("Starting...")

token = open("./token.txt", "r")
OwnerID = 660631616074547224
client = discord.Client()

@tasks.loop(seconds=10)
async def change_activity():
    activityList = [
    f"I'm in {str(len(client.guilds))} servers !",
    f"Today is {datetime.now().day}/{datetime.now().month}/{datetime.now().year}",
    f"{datetime.now().hour}:{datetime.now().minute}",
    f"Hi ! :D"
    ]
    await client.change_presence(activity= discord.Activity(name=activityList[random.randint(0, len(activityList) - 1)],type=1))
    

@client.event
async def on_ready():
    botstatus.clear_console_output()
    Debug.Success(f"Ready, Connected as {client.user} in {str(len(client.guilds))} servers")
    if platform.system() == "Windows":
        os.system("cmd /k title CamBot - Ready")

    change_activity.start()

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    msg = message.content.lower()
    send = message.channel.send

    if msg == "hi" or msg == "hello" or msg == "cam hello" or msg == "cam hi" or msg == "hey" or msg == "cam hey":
        messages = ["Hi !","Hi there !","Hey ! how it's going ?","Yo ! Whats up ?","Hey !","Hello !","Oh, hi !"]
        randMessage = random.randint(0,len(messages) - 1)
        await send(messages[randMessage])

    if msg.startswith("hm"):
        await send(":thinking:")

    if re.match(f"{str(client.user.id)}", message.content):
        print("e")
        reactMsg = message.id
        await message.add_reaction("🏓")

    if re.match("bruh", msg):
        await send("https://tenor.com/view/bruh-gif-24665421")
    
    if re.match("lol|lmao|xd", msg):
        await send(":joy:")
        
    if msg.startswith("aaaa") or msg.startswith("ahh"):
        await send(":scream:")

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

    if re.match("^cam qrcode",msg):
        from commands.internet import qrcodemake
        QRText = message.content.replace("cam qrcode","")
        if QRText == "":
            await send("You didn't precise data ! I'm gonna use my invitation link !", file=qrcodemake.makeqr("https://discord.com/api/oauth2/authorize?client_id=991796518904414218&permissions=8&scope=bot"))
            return    

        await send(file=qrcodemake.makeqr(QRText))
    
    if re.match("^cam user", msg):
        search = message.content.replace("cam user","")

        from commands.discordrelated import userinfo
        await send(userinfo.main(search, client))

    if re.match("^cam pycode ",msg):
        try:
            code = message.content.replace("cam pycode ","")
            print(code)
            from commands.dev import pycode
            await send(pycode.pycode(str(code)))
            
        except Exception as e:
            await send("An error occured:" + "`" + str(e) + "`")
            return "An error occured:" + str(e)

    if msg == "cr":
        Debug.DuringOperation("Restart Request Detected, checking if owner...")
        if not message.author.id == OwnerID:
            Debug.Error("Author ID doesn\'t match, not restarting")
            return
        await message.delete()
        Debug.Success("Author ID matches !")
        Debug.DuringOperation("Restarting...")
        botstatus.restart_bot()


client.run(token.read())