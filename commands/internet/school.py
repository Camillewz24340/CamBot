from discord import Embed
import pandas

async def getSchoolInfo(schoolName):
        
        file = pandas.read_csv(
        "./data/constData/datasets/schools.csv",
        header=0,
        low_memory=False
        )

        school = file[file["name"] == schoolName.title()].iloc[0]

        return {
            "name":school["name"],
            "status":school["status"] if school["status"] else "",
            "address":[
                str(school["address_1"]) if school["address_1"] else None,
                str(school["zip_code"]) if school["zip_code"] else None,
                str(school["city_name"]) if school["city_name"] else None,
            ],
            "type":school["type"] 
            }

async def schoolInfo(schoolName):

    try:
        embed = Embed()
        school = await getSchoolInfo(schoolName)
        
        embed.title = school["name"]
        embed.color = 0x2b2d31
        embed.description = ""

        try:
            embed.description += f"{school['status'] if school['status'] else ''} {school['type'] if school['type'] else ''}".capitalize()
        except Exception as e:
            print(e)
            pass

        try:
            embed.add_field(name="Address", value=f"{str(school['address'][0])}, {str(school['address'][1])}, {str(school['address'][2])}")
        except:
            pass

        return embed

    except:
        embed = Embed()
        embed.title = "School not found !"
        embed.color = 0xff0000
        return embed