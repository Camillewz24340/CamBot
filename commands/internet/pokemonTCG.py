from discord import Embed, Color
from pokemontcgsdk import Card

def get_card(query):

    embed = Embed()

    try:
        try:
            card = Card.where(q=f"!name:{query}", page=1, pagesize=1)[0]
        except:
            card = Card.where(q=f"name:{query}", page=1, pagesize=1)[0]
    except:
        embed.title = "Card not found"
        embed.color = 0xff0000
        return embed
    
    embed.color = 0xffff00
    
    embed.title = card.name

    try:
        embed.title += f" - {card.set.name}"
    except:
        pass

    try:

        attackList = ""

        for attack in card.attacks:
            attackList += f" **{attack.name}**: {attack.text if attack.text else 'No description'}\n"
            
        embed.add_field(name="Attacks" if len(card.attacks) > 1 else "Attack", value=attackList)
    except:
        pass

    try:

        abilityList = ""

        for ability in card.abilities:
            abilityList += f"\n{ability.name}: "
            
        embed.add_field(name="Abilities" if len(card.abilities) > 1 else "Ability", value=abilityList)
    except:
        pass

    try:
        embed.set_image(url=card.images.large)
    except:
        pass

    return embed