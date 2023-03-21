Quickstart
========

Looking for a quick example of what a bot may look like? Here's a simple example of a bot that responds to a command with a message:

Example Bot
--------------------

.. code-block:: python

    from nextguild import Client, Events, Message, Embed
    token = "YOUR_TOKEN_HERE"

    bot = Client(token)
    events = Events(bot)

    @events.on_message
    def pingcommand(message):
        if message.content == "!ping":
            bot.send_message(message.channelId, "Pong!")
    bot.run()

This bot will respond to any message that says "!ping" with "Pong!".

Great! You've now made your first bot!
Now continue down your path of becoming a great bot developer...