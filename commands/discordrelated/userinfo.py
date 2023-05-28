from discord import User, Embed

async def get_user_info(user:User):
    
    try:
        if not user:
            return Embed(color=0xff0000, title="User not found")

        embed = Embed()

        embed.title = user.name
        embed.description = "\nThis account is a Bot" if user.bot else ""
        embed.set_footer(text=f"User ID: {user.id}")
        embed.color = 0x000033

    except:
        
        embed.color = 0xff0000
        embed.title = "User not found"

    return embed