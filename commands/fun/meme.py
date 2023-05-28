import requests
import json
from discord import Embed, Color

def getMeme():
    
    embed = Embed()

    try:
        data = json.loads(requests.get("https://meme-api.com/gimme").content)
    except Exception as e:
        embed.color = 0xff0000
        embed.title = "Unable to get a meme !"
        print(e)
        return embed

    embed.url = data["postLink"]
    embed.color = 0x003300
    embed.title = data["title"]
    embed.description = f"by [{data['author']}](https://reddit.com/user/{data['author']}) on Reddit"
    embed.set_footer(text=f"r/{data['subreddit']}", )
    embed.set_image(url=data["url"])

    return embed