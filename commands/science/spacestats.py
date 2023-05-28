import requests
import json
from discord import Color, Embed, File

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

def getStats():
    embed = Embed()
    
    try:
        ISSLocation = json.loads(requests.get("http://api.open-notify.org/iss-now.json").content)
        SpaceHumans = json.loads(requests.get("http://api.open-notify.org/astros.json").content)
        print(ISSLocation)

    except:
        embed.title = "Failed to access space stats"
        embed.color = 0xff0000
        return embed

    m = Basemap(projection='robin', lon_0=0, resolution='l')

    lats = [float(ISSLocation['iss_position']['latitude'])]
    lons = [float(ISSLocation['iss_position']['longitude'])]

    m.drawcountries(color='#ffffff', linewidth=0.5)
    m.fillcontinents(color='#c0c0c0', lake_color='#ffffff')

    x, y = m(lons, lats)
    plt.plot(x, y, "bo", color='#0000ff', markersize=5)

    plt.savefig("./data/TempData/ISSMap.png")

    embed.color = 0x000033
    embed.title = "Space"
    embed.description = f"The ISS is at {ISSLocation['iss_position']['latitude']} {ISSLocation['iss_position']['longitude']} and there is {SpaceHumans['number']} humans in space !"


    HumansNames = ""
    HumansLocations = ""

    for human in SpaceHumans["people"]:
        HumansNames += f"{human['name']}\n"
        HumansLocations += f"{human['craft']}\n"

    embed.add_field(name="Person Name", value=HumansNames)
    embed.add_field(name="In", value=HumansLocations)

    return embed