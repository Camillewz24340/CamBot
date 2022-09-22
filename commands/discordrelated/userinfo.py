from dis import dis
import discord
import abc

def main(user):

    info=f"Created at: {user.created_at}\n"

    if not user:
        return "Oops, an error occured"

    ret = discord.Embed(
        title=f"{user.name}",
        description=info,
        footer="User ID: {user.id}"
    )
    

    return ret