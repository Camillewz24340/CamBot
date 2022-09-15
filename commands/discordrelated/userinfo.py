import discord

def main(user, client):
    u = client.get_user(int(user))

    if not u:
        return str(u)
    

    return u