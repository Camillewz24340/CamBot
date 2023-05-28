from discord import Guild, Embed, Asset

def ServerInfo(server:Guild):
    
    embed = Embed()
    
    embed.title = server.name

    embed.add_field(name="Owner", value=server.owner)
    embed.add_field(name="Member count", value=server.member_count)
    embed.add_field(name="Created at", value=str(f"`{server.created_at.day}/{server.created_at.month}/{server.created_at.year}`"))
    embed.add_field(name="Main language code", value=f"`{server.preferred_locale}`")
    
    embed.set_footer(text="Server ID: " + str(server.id))

    return embed
