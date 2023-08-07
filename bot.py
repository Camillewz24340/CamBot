from utils import botstatus, consoledebug as Debug

Debug.DuringOperation("Importing libraries")

import atexit
from platform import platform
import random
import re
import discord
from discord.ext import tasks
import os 
import time
import platform
from datetime import datetime
import sys
import math
import stopwatch

botstatus.clear_console_output()

if platform.system() == "Windows":
    os.system("cmd /c title CamBot - Starting")
Debug.DuringOperation("Starting...")

token = open("./token.txt", "r")
OwnerID = 660631616074547224

Debug.DuringOperation("Initialazing client")

client = discord.Client(intents=discord.Intents.all())
uptime = stopwatch.Stopwatch()
uptime.start()

Debug.Info("Uptime started")

startupTime = datetime.now()

day = startupTime.weekday()

if day == 0:
    day = "Monday"
if day == 1:
    day = "Tuesday"
if day == 2:
    day = "Wednesday"
if day == 3:
    day = "Thursday"
if day == 4:
    day = "Friday"
if day == 5:
    day = "Saturday"
if day == 6:
    day = "Sunday"

upSince = f"{str(day)} {str(startupTime.day)}/{str(startupTime.month)} at {str(startupTime.hour)}:{str(startupTime.minute)} !"

isStatusCustom = False

async def set_status(s=None):
    status = discord.Status.online
    
    if not isStatusCustom:
        if(datetime.now().hour < 8 or datetime.now().hour > 18):
            status = discord.Status.idle
    else:
        try:
            status = s
        except:
            status = discord.Status.online
        await client.change_presence(status=status)
    
    return status

@tasks.loop(seconds=2)
async def checkEvents():
    if open("./states/trayRestart.txt").read() == "1" or open("./states/trayStop.txt").read() == 1:
        open("./states/isReady.txt", "w").write("0")
        open("./states/isOnline.txt", "w").write("0")
        sys.exit(0)

@tasks.loop(seconds=10)
async def change_activity():
    if not isStatusCustom:
        activityList = [
        f"Im up since {upSince} !",
        "I'm cool !",
        f"I'm in {str(len(client.guilds))} servers !",
        f"Today is {datetime.now().day}/{datetime.now().month}/{datetime.now().year}",
        f"{datetime.now().hour}:{datetime.now().minute}",
        "Hi ! :D",
        "cam help"
        ]

        await client.change_presence(status=await set_status(),activity = discord.Activity(name=activityList[random.randint(0, len(activityList) - 1)],type=1))
    else:
        return

Debug.DuringOperation("Connecting to Discord...")

@client.event
async def on_ready():
    with open("./states/isReady.txt", "w") as f:
        f.write("1")
    with open("./states/isOnline.txt", "w") as f:
        f.write("1")
    botstatus.clear_console_output()
    Debug.Success(f"Ready, Connected as {client.user} in {str(len(client.guilds))} servers")
    if platform.system() == "Windows":
        os.system("cmd /c title CamBot - Ready")
    
    change_activity.start()
    checkEvents.start()

@client.event
async def on_message(message:discord.Message):

    msg = message.content.lower()
    send = message.channel.send

    if message.author.id == client.user.id: return

    if re.match("^cam ", msg):
        if message.channel.guild and message.channel.guild.id != 690177824937476144:
            if not message.channel.guild.me.guild_permissions.manage_messages and message.author.id != OwnerID:
                await send("Not activating; missing permissions. Request terminated.")
                return

    if re.match("^cam help", msg):
        
        page = msg.replace("cam help ", "")
        
        helpEmbed = discord.Embed()
        helpEmbed.color = 0x000033

        from pathlib import Path

        try:

            try:
                command = page
                with open(f"data/constData/Help/Commands/{command.lower()}.txt", "r", encoding="utf-8") as helpFile:
                    helpEmbed.title = f"Help: {command}"
                    data = helpFile.read()
                    helpEmbed.description = data
                    await send(embed=helpEmbed)
                    return
                    
            except Exception as e:
                pass

            
            helpEmbed.title = "Help"
                
            totalPages = 0

            for p in Path("./data/constData/").rglob("Page*.txt"):
                totalPages += 1

            with open(f"data/constData/Help/Page{page}.txt", "r") as helpFile:
                data = helpFile.read()
                
                helpEmbed.set_footer(text=f"Page {page}/{totalPages}")
                helpEmbed.description = data

        except Exception as e:
            with open("data/constData/Help/Page1.txt") as helpFile:
                data = helpFile.read()

                helpEmbed.set_footer(text=f"Page 1/{totalPages}")
                helpEmbed.description = data 

        await send(embed=helpEmbed)
        

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

    if msg == "cam cum":
        await send("What do you want you dingus ?!!")
    
    if msg == "afk" or msg == "back" or msg == "im back" or msg == "i'm back":
        await message.add_reaction("👍")

    if re.match("cam say ", msg):
        txt = msg.replace("cam say ", "")
        if message.author.id == OwnerID:
            try:
                await message.delete()
            except:
                pass
            await send(txt)

    if re.match("^cam space", msg):

        sentMsg = await send("Loading space data things... :3")
        
        from commands.science import spacestats

        await sentMsg.edit(content=None, embed=spacestats.getStats())

    if re.match("^cam wiki", msg):
        query = message.content.replace("cam wiki", "")
        if query == "" or query == "_ _":
            await send("Search something, not the void ! :joy:")
            return
        from commands.internet import wikisearch
        await send(wikisearch.main(query, message.author.name))

    if re.match("^cam tcg", msg) or re.match("^cam pokemon", msg):
        card = message.content.replace("cam tcg ", "").replace("cam pokemon ", "")

        from commands.internet import pokemonTCG

        await send(embed=pokemonTCG.get_card(card))

    if re.match("^cam meme", msg):

        sentMsg = await send("Let's look for a funny meme on Reddit :)")
        
        from commands.fun import meme

        await sentMsg.edit(content=None, embed=meme.getMeme())

    if msg == "cam wake up":
        await send("You can't wake me up, coz i already woke up :D")
    
    if msg == "cam die":
        await send("😡😡😡")

    if re.match("cam removelast", msg):
        try: 
            await message.delete()
            await message.channel.purge(limit=1)
        except: 
            await send("Lemme remove messages 😡😡😡")

    if re.match("cam secretping", msg):
        await message.delete()
        await send("@everyone")
        await message.channel.purge(limit=1)

    if re.match("^cam setstatus ", msg):
        global isStatusCustom
        if message.author.id == OwnerID:
            st = msg.replace("cam setstatus ", "")
            if st != "none":
                if st == "online" or st == "1":
                    isStatusCustom = True
                    await set_status(discord.Status.online)
                if st == "invisible" or st == "0" or st == "inv" or st == "offline":
                    isStatusCustom = True
                    await set_status(discord.Status.invisible)
                if st == "idle":
                    isStatusCustom = True
                    await set_status(discord.Status.idle)
                if st == "dnd":
                    isStatusCustom = True
                    await set_status(discord.Status.dnd)
            else:
                isStatusCustom = False
                

    if msg == "cam lines":
        
        l = 0
        c = 0
        from pathlib import Path
        pathlist = Path("./").rglob('*.py')
        for path in pathlist:
            with open(str(path), "r", encoding="utf-8") as lines:
                for count, line in enumerate(lines):   
                    c += len(line)
                        
            l += count + 1
        
        await send(f"In all my files, i have {str(l)} lines of code and {str(c)} characters !")

    if re.match("^cam qrcode",msg):
        from commands.internet import qrcodemake
        QRText = message.content.replace("cam qrcode","")
        if QRText == "":
            await send("You didn't precise data ! I'm gonna use my invitation link !", file=qrcodemake.makeqr("https://discord.com/api/oauth2/authorize?client_id=991796518904414218&permissions=8&scope=bot"))
            return    

        await send(file=qrcodemake.makeqr(QRText))
    
    if re.match("^cam user", msg):

        from commands.discordrelated import userinfo

        try:
            try:
                search = re.search("\d+", message.content).group()
            except:
                return await send("Please provide a valid user mention or ID !")
            user = client.get_user(int(search))
        except:
            return await send("Didn't find the user ! Please check and try again !")
            
        await send(embed=await userinfo.get_user_info(user))

    if re.match("^cam pycode ",msg):
        try:
            code = message.content.replace("cam pycode ","")
            print(code)
            from commands.dev import pycode
            await send(pycode.pycode(str(code)))
            
        except Exception as e:
            await send("An error occured:" + "`" + str(e) + "`")
            return "An error occured:" + str(e)
        
    if re.match("^cam color", msg):

        col = msg.replace("cam color ", "")

        from commands.dev import color

        await send(embed=color.getColor(col))

    if re.match("^cam joke", msg):
        
        filters = msg.replace("cam joke", "")

        from commands.fun import joke

        await send(await joke.GetJoke(filters, message.author.name))

    if re.match("^cam product ", msg):
        
        FoodID = msg.replace("cam product ", "")

        from commands.internet import foodinfo
        
        await send(embed=foodinfo.GetFoodInfo(FoodID, message.author.name))

    if re.match("^cam serverinfo", msg):
        
        from commands.discordrelated import serverinfo

        if not message.guild:
            await send("Oh, looks like you are not in a server !")

        await send(embed=serverinfo.ServerInfo(message.guild))

    if re.match("^cam math ", msg):
        
        expression = message.content.replace("cam math ", "")

        from commands.dev import mathsingleexpr

        try:
            await send(mathsingleexpr.mathsingleexpr(expression, message.author.name))
        except discord.errors.HTTPException:
            await send("Empty or too long output :3")

    if re.match("^cam weather now", msg):
        from commands.science.weather import nowWeather

        newMessage = message.content.replace("cam weather now ", "").replace("\s{2-100}", " ").replace(",", " ")

        await send(embed=await nowWeather(newMessage))

    if re.match("^cam education school", msg) or re.match("^cam edu school", msg):
            from commands.internet.school import schoolInfo

            newMessage = message.content.replace("cam edu school ", "").replace("cam education school ", "")

            await send(embed=await schoolInfo(newMessage))

    if re.match("^cam account create", msg):
        
        from data.data_storage_handlers import money

        accountCreation = money.create_account(message.author)

        if accountCreation == 0:
            await send("Your bank account has been created !")
        if accountCreation == 1:
            await send("Your bank account already exists !")
        if accountCreation == -1:
            await send("There was an error while creating your account !")

    if re.match("^cam balance", msg) or re.match("^cam money", msg):

        from data.data_storage_handlers import money

        balance = money.get_money_counts(message.author)

        try:
            await send(f"You have <:camcoin:1107809307304677428>{balance[0]} in your wallet and <:camcoin:1107809307304677428>{balance[1]} in your bank !")
        except:
            await send("You don't have a bank account, use `cam account create` !")

    if re.match("^cam deposit ", msg):

        try:
            amount = int(msg.replace("cam deposit ", ""))
        except:
            return await send("Please put a valid amount !")

        from data.data_storage_handlers import money

        result = money.transfer_money(message.author, "bank", amount)

        try:
            if result == 0:
                await send(f"wallet -> <:camcoin:1107809307304677428>{amount} -> bank\n<:camcoin:1107809307304677428>{amount} have been deposited to your bank !")
            if result == 1:
                await send("You don't have a bank account, use `cam account create` !")
            if result == -1:
                await send("An error occured !")
            if result == 2:
                await send("You don't have enough money !")
            if result == 3:
                await send("Please put a valid number")
        except:
            await send("Invalid usage !")


    if re.match("^cam withdraw ", msg):

        try:
            amount = int(msg.replace("cam withdraw ", ""))
        except:
            return await send("Please put a valid amount !")

        from data.data_storage_handlers import money

        result = money.transfer_money(message.author, "wallet", amount)
        
        try:
            if result == 0:
                await send(f"bank -> <:camcoin:1107809307304677428>{amount} -> wallet\n<:camcoin:1107809307304677428>{amount} have been withdrawn from your bank !")
            if result == 1:
                await send("You don't have a bank account, use `cam account create` !")
            if result == -1:
                await send("An error occured !")
            if result == 2:
                await send("You don't have enough money !")
            if result == 3:
                await send("Please put a valid number")
        except:
            await send("Invalid usage !")

    
    
    if re.match("^cam give ", msg):
        await send(":+1:")



    if msg == "cam stop":
        Debug.DuringOperation("Stopping Request Detected, checking if owner...")
        if not message.author.id == OwnerID:
            await send("Nobody can't stop me >:D, except my owner :sweat_smile:")
            Debug.Error("Author ID doesn\'t match, not stopping")
            return
        Debug.Success("Author ID matches !")
        sentMsg = await send("Ok, i'm stopping !")
        time.sleep(2)
        try:
            await message.delete()
        except:
            pass
        await sentMsg.delete()
        Debug.DuringOperation("Stopping...")
        if platform.system() == "Windows":
            os.system("cmd /c title CamBot - Stopping")
        time.sleep(1)
        open("./states/isOnline.txt", "w").write("0")
        sys.exit(0)

    if msg == "cam restart" or msg == "cam rs":
        Debug.DuringOperation("Restart Request Detected, checking if owner...")
        if not message.author.id == OwnerID:
            await send("Nobody can't restart me >:D, except my owner :sweat_smile:")
            Debug.Error("Author ID doesn\'t match, not restarting")
            return
        Debug.Success("Author ID matches !")
        sentMsg = await send("Ok, i'm restarting !")
        time.sleep(2)
        try:
            await message.delete()
        except:
            pass
        await sentMsg.delete()
        Debug.DuringOperation("Restarting...")
        if platform.system() == "Windows":
            os.system("cmd /c title CamBot - Restarting...")
        time.sleep(1)
        open("./states/isOnline.txt", "w").write("0")
        open("./states/isRestarting.txt", "w").write("1")
        sys.exit(0)

def exitHandler():
    open("./states/isOnline.txt", "w").write("0")

atexit.register(exitHandler)

client.run(token.read())