import imp
import random
import re
from turtle import title
import discord
import os
import time
from termcolor import colored as col3
from colors import Colors

root.iconbitmap('icon.ico')
os.system("cls")
os.system("title CamBot - Starting")

token = open("./token.txt", "r")
OwnerID = 660631616074547224
client = discord.Client()

print(col3("Starting", Colors.DURINGOPERATION))

@client.event
async def on_ready():
    os.system("cls")
    print(col3("Ready", Colors.SUCCESS))
    os.system("title CamBot - Ready")

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
    
    if re.match("lol|lmao|xd", msg):
        await send(":joy:")
        
    if msg.startswith("aa") or msg.startswith("ahh"):
        await send(":scream:")

    if msg == "cam restart" and message.author.id == OwnerID:
        print(col3("[INFO] Restart Request Detected", Colors.INFO))
        os.system('cmd /k "python main.py"')
        os.kill()


client.run(token.read())
