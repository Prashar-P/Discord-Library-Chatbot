#Name: Chatbot Project - Library Rental System 
#Function: Allows user to 'rent' a book, depending on whether the book has been rented or not
#          an appropriate message is sent



import discord
class Chatbot(discord.Client):
    async def on_message(self,message):
        if message.content.startswith("!borrowbook"):
            file = open("Book.txt","r")
            readline = file.readline()
            users = readline.split(',')
            if str(message.author.id) in users[0]:
                await message.channel.send("You have already borrowed a book")
            elif str(message.author.id) not in users:
                await message.channel.send("You have not rented any books")
                file = open("Book.txt","a")
                file.write(str(message.author.id) + "\n")
                file.close()
            
                #implent user options to search for books (google API)



client = Chatbot()
client.run('token')


