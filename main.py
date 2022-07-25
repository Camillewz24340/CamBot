from random import random
import discord
import os
import random
import time
token = open("./token.txt", "r")

client = discord.Client()

@client.event
async def on_ready():
    print("Ready")

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
    
    if msg.startswith("lol"):
        await send(":joy:")
        
    if msg.startswith("aa") or msg.startswith("ahh"):
        await send(":scream:")

client.run(token.read())
