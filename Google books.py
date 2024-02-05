##Main Code
import discord
import requests

from googleapiclient.discovery import build

api_key = "API_KEY"
client_id = "CLIENT_KEY"
                
#import discord
from googleapiclient.discovery import build

class Chatbot(discord.Client):
    async def on_message(self,message):
        if message.content.startswith("!books"):
            args = message.content.split(" ")
            args[0] = args[0].strip("!")
            if args[0] == "books":
            #let user input search
                customsearch = args[1:]
                search = request.get(client_id)
                print(search.status.code)
        
client = Chatbot()
client.run('token')

