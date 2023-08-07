from discord import User, Embed

async def get_user_info(user:User):
    
    try:
        if not user:
            return Embed(color=0xff0000, title="User not found")

        embed = Embed()

        embed.title = user.name
        embed.description = "\nThis account is a Bot" if user.bot else ""

        embed.set_image(url=str(user.banner) if user.banner else None)
        embed.set_thumbnail(url=str(user.avatar) if user.avatar else None)

        embed.add_field(name=f"Discord user since", value=f"{user.created_at.day if user.created_at.day > 10 else '0' + str(user.created_at.day)}/{user.created_at.month if user.created_at.month > 10 else '0' + str(user.created_at.month)}/{user.created_at.year}") if user.created_at else None

        embed.set_footer(text=f"User ID: {user.id}")
        embed.color = user.accent_color if user.accent_color else 0x000033
    except Exception as e:
        print(e)
        embed.color = 0xff0000
        embed.title = "User not found"

    return embed