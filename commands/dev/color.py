from discord import Embed,Color
import re

def getColor(colorInput: str):

    try:
        
        embed = Embed()

        parsedInput = colorInput

        parsedInput = parsedInput.replace("#", "")
        parsedInput = parsedInput.replace("  ", " ")
        parsedInput = parsedInput.replace(",", " ")

        colorList = list(parsedInput.split(" "))
        
        for i in colorList:
            if i == "":
                colorList.remove("")
            if int(i) > 255:
                embed.add_field(name="Details:", value="Number(s) is/are higher than 255")
                raise ValueError

        embed.title = f"RGB: {colorList[0]}, {colorList[1]}, {colorList[2]}"
        embed.color = Color.from_rgb(r=int(colorList[0]), g=int(colorList[1]), b=int(colorList[2]))

        return embed
    
    except Exception as e:
    
        embed.color = 0xE74C3C
        embed.title = "Invalid color code"
        embed.description = "Please retry with a valid RGB code !"

        return embed