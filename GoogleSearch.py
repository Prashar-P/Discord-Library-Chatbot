#Name: Chatbot Project - Google Search 
#Function: Allows user to input data to search using google API, the search results are
#          then printed
#API Documentation: https://cloud.google.com/appengine/docs/standard/python/search/



#api search function see documentation
def google_search(search_term, api_key, search_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=search_term, cx=search_id, **kwargs).execute()
    return result


#Main Code
import discord
from googleapiclient.discovery import build

class Chatbot(discord.Client):
    async def on_message(self,message):
        if message.content.startswith("!"):
            args = message.content.split(" ")
            args[0] = args[0].strip("!")
            print(args[0])
            if args[0] == "search":
                #let user input search
                customsearch = args[1:]          
                api_key = "API_KEY"
                search_id = "SEARCH_ID"
                result = google_search(customsearch, api_key, search_id)

#prints the first 5 search result links 
            for x in range(0,5):
                await message.channel.send(result['items'][x]['link'])
        

        

client = Chatbot()
client.run()
