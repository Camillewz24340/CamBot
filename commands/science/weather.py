import open_meteo
from open_meteo import OpenMeteo
from discord import Color, Embed
from open_meteo.models import DailyParameters, HourlyParameters
import asyncio
from tabulate import tabulate
from datetime import datetime
import pandas

def getCityInfo(cityName):
    file = pandas.read_csv(
    "./data/constData/datasets/worldcities.csv",
    header=0,
    usecols=["city", "country", "lat", "lng"]
    )

    city = file[file["city"] == cityName].iloc[0]
    coords = [city["lat"], city["lng"]]

    return {"name":city["city"], "coords":coords, "country":city["country"]}
    
    

async def nowWeather(c:str) -> Embed:

    async with OpenMeteo() as open_meteo:
        try:
            try:
                city = getCityInfo(c.title())
                embed = Embed()
                forecast = await open_meteo.forecast(
                    current_weather=True,
                    latitude=city["coords"][0], 
                    longitude=city["coords"][1],
                    daily=[
                        DailyParameters.SUNRISE,
                        DailyParameters.SUNSET,
                        DailyParameters.TEMPERATURE_2M_MIN,
                        DailyParameters.TEMPERATURE_2M_MAX,
                        DailyParameters.APPARENT_TEMPERATURE_MIN,
                        DailyParameters.APPARENT_TEMPERATURE_MAX,
                        DailyParameters.PRECIPITATION_SUM
                    ],
                    hourly=[
                        HourlyParameters.RELATIVE_HUMIDITY_2M
                    ]
                )

                emoji:str = ":sunny:"
                
                if forecast.daily.precipitation_sum[0] >= 0.075:
                    emoji = ":white_sun_cloud:"
                    if forecast.daily.precipitation_sum[0] >= 0.2:
                        emoji = ":cloud:"
                        if forecast.daily.precipitation_sum[0] >= 0.5:
                            emoji = ":white_sun_rain_cloud:"
                            if forecast.daily.precipitation_sum[0] >= 1:
                                emoji = ":cloud_rain:"
                
                embed.title = f"Current weather in {city['name']}"
                embed.description = f"{emoji} {forecast.current_weather.temperature}°C"
                
            except:
                coords = c.split(" ")

                for i in range(len(coords)):
                    if coords[i] == "" or coords[i] == " ":
                        coords.remove(coords[i] - 1)

                embed = Embed()

                forecast = await open_meteo.forecast(
                    current_weather=True,
                    latitude=coords[0], 
                    longitude=coords[1],
                    daily=[
                        DailyParameters.SUNRISE,
                        DailyParameters.SUNSET,
                        DailyParameters.TEMPERATURE_2M_MIN,
                        DailyParameters.TEMPERATURE_2M_MAX,
                        DailyParameters.APPARENT_TEMPERATURE_MIN,
                        DailyParameters.APPARENT_TEMPERATURE_MAX,
                        DailyParameters.PRECIPITATION_SUM
                    ],
                    hourly=[
                        HourlyParameters.RELATIVE_HUMIDITY_2M
                    ]
                )

                emoji:str = ":sunny:"
                
                if forecast.daily.precipitation_sum[0] >= 0.075:
                    emoji = ":white_sun_cloud:"
                    if forecast.daily.precipitation_sum[0] >= 0.2:
                        emoji = ":cloud:"
                        if forecast.daily.precipitation_sum[0] >= 0.5:
                            emoji = ":white_sun_rain_cloud:"
                            if forecast.daily.precipitation_sum[0] >= 1:
                                emoji = ":cloud_rain:"

                embed.title = "Current weather in " + str(coords[0]) + ", " + str(coords[1])
                print(forecast)
                embed.color = 0x000033
                embed.description = f"{emoji} {forecast.current_weather.temperature}°C"

            windDirectionEmoji:str = ""

            windDirection = forecast.current_weather.wind_direction

            if windDirection:
                if windDirection >= 338 or windDirection <= 22:
                    windDirectionEmoji = ":arrow_up:"
                if windDirection >= 23 and windDirection <= 67:
                    windDirectionEmoji = ":arrow_upper_right:"
                if windDirection >= 68 and windDirection <= 112:
                    windDirectionEmoji = ":arrow_right:"
                if windDirection >= 113 and windDirection >= 157:
                    windDirectionEmoji = ":arrow_lower_right:"
                if windDirection >= 158 and windDirection >= 202:
                    windDirectionEmoji = ":arrow_down:"
                if windDirection >= 203 and windDirection >= 247:
                    windDirectionEmoji = ":arrow_lower_left:"
                if windDirection >= 248 and windDirection >= 292:
                    windDirectionEmoji = ":arrow_left:"
                if windDirection >= 293 and windDirection >= 337:
                    windDirectionEmoji = ":arrow_upper_left:"

            try:
                embed.description += f" :small_blue_diamond: {forecast.daily.apparent_temperature_min[0]}°C :small_orange_diamond: {forecast.daily.apparent_temperature_max[0]}°C"
            except:
                pass

            try:
                embed.add_field(name="Wind", value=f"{str(forecast.current_weather.wind_speed) + ' km/h' if forecast.current_weather.wind_speed else ' '} {windDirectionEmoji} _ _")
            except:
                pass

            try:
                embed.add_field(name="Humidity", value=f"{str(forecast.hourly.relative_humidity_2m[datetime.now().hour])}%")
            except Exception as e:
                print(e)

            embed.set_footer(text=f"{city['name']}, {city['country']}, Reports from OpenMeteo, cities data from simplemaps.com")

            return embed
            

        except Exception as e:
            print(e)
            embed = Embed()
            embed.color = 0xff0000
            embed.title = "Oops, an error occured !"
            return embed