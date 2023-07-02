# ©️ The NextGuild Project 2023-present
# If support is needed, you can join the support server (guilded.gg/nextguild) or raise an issue.
# NOTICE: This example requires a external library, that is not endorsed or supported by The NextGuild Project.
# CODE LEVEL // BEGINNER - Easy to follow
# You can install the appropriate dependencies with the following commands in the terminal:
# pip install nextguild
# pip install random
# pip install websockets
# pip install requests

from nextguild import *
import random
token = "YOUR_TOKEN_HERE" # Replace with your bot's token
bot = Client(token) # Define the 'bot' variable, and pass on the token to the client
events = Events(bot) # Define events and pass the 'bot' variable containing the client information to register and pass valid information to the Guilded API

@events.on_message # Use the 'on_message' event to make a conditional usage
async def random_number(message): # Define the name of the function within the event and look specifically only from the messages section of the Guilded API
    if message.content == "!random_number": # Look if the message equals '!random_number'. If it does, do the code below this specific 'if' statement.
        bot.send_message(message.channel_id, f"Here is your random number: {random.choice(range(1,101))") # The range is put until 101 because python generally does what we would do a 1-100 range to a 0-99 range. So, we have to add a 1 to the 100 so it becomes 0-100 when randomly generated via the random library.
events.run()
