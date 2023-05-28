import discord

class ClientHandler():
    def __init__(self): # Constructor
        self.client = discord.Client(intents=discord.intents.all())
        self.ownerID = 660631616074547224
        
    def start(self, token:str):
        self.client.run(token)

    def stop(self):
        self.client.close()

    def getOwnerId(self) -> int:
        return self.ownerID
    
    

# method call: ClientHandler.methodName()
