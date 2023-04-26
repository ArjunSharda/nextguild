Quickstart
========

Looking for a quick example of what a bot may look like? Here's a simple example of a bot that responds to a command with a message of ping:

Example Bot
--------------------

.. code-block:: python

    from nextguild import *
    token = "YOUR_TOKEN_HERE"

    bot = Client(token)
    events = Events(bot)

    @events.on_message
    async def pingcommand(message):
        if message.content == "!ping":
            bot.send_message(message.channelId, "Pong!")
    events.run()

This bot will respond to any message that says "!ping" with "Pong!".

Great! You've now made your first bot!

Now, you've marked a checkpoint towards the path of using the NextGuild library proficiently. You can check the website for references, etc, while using our library.
