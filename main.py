import discord
import os

token = open("./token.txt", "r")

client = discord.Client()

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.lower() == "hi" or msg.lower() == "hello":
        await message.channel.send("Hi there !")

client.run(token.read())
