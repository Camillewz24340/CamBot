from discord import Embed, Colour
import openfoodfacts
import json

foodID = "5411188112709"

def GetFoodInfo(foodID, user=None):

    embed = Embed()

    search = openfoodfacts.products.search(query=foodID)

    try:
        if search["products"][0]["_id"]:
            foodID = search["products"][0]["_id"]
    except:
        pass

    data = openfoodfacts.products.get_product(foodID)

    try:
        embed.title = "Product"
        embed.set_footer(text="Product barcode: " + data["product"]["_id"] + ". Source: OpenFoodFacts")
        embed.url = "https://world.openfoodfacts.org/product/" + data["product"]["_id"]

        embed.add_field(name="Brand", value=data["product"]["brands"])
        try:
            embed.add_field(name="Description", value=data["product"]["generic_name"])
        except Exception:
            embed.add_field(name="Description", value="None")

        try:
            if data["product"]["ingredients_text_en"]:
                embed.add_field(name="Ingredients", value=data["product"]["ingredients_text_en"])
            elif data["product"]["ingredients_text"]:
                embed.add_field(name="Ingredients", value="`" + data["product"]["ingredients_text"] + "`")
            else:
                embed.add_field(name="Ingredients", value="`Unknown`")
        except:
            embed.add_field(name="Ingredients", value="`Unknown`")
        
        try:
            if data["product"]["nutriscore_grade"]:
                embed.add_field(name="Nutri-Score", value=data["product"]["nutriscore_grade"].upper())
            else:
                embed.add_field(name="Nutri-Score", value="Unknown")
        except:
            embed.add_field(name="Nutri-Score", value="Unknown")
        
        try:
            if data["product"]["nova_group"]:
                embed.add_field(name="NOVA", value=data["product"]["nova_group"])
            else:
                embed.add_field(name="NOVA", value="Unknown")
        except:
            embed.add_field(name="NOVA", value="Unknown")

        try:
            if data["product"]["ecoscore_tags"]:
                embed.add_field(name="Eco-score", value=data["product"]["ecoscore_tags"][0].upper())
            else:
                embed.add_field(name="Eco-score", value="Unknown")
        except Exception as e:
            embed.add_field(name="Eco-score", value="Unknown")

        if data["product"]["image_front_small_url"]:
            try:
                embed.set_image(url=data["product"]["image_front_url"])
            except:
                pass
        embed.color = Colour.green()
            

    except Exception as e:
        embed.title = "Product not found"
        embed.set_footer(text=None)
        embed.color = Colour.red()
    
    return embed
