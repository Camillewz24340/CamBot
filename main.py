from random import random
import discord
import os
import random

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

    if msg == "hi" or msg == "hello" or msg == "cam hello" or msg == "cam hi":
        messages = ["Hi !","Hi there !","Hey ! how it's going ?","Yo ! Whats up ?","Hey !","Hello !","Oh, hi !"]
        randMessage = random.randint(0,len(messages) - 1)
        await message.channel.send(messages[randMessage])

client.run(token.read())
