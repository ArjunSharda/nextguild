Essentials
===========

This page provides an overview of the essentials events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)


on_ready
--------

It is generally recommended to save the data in a global variable, so you can access it from anywhere in your code.
.. code-block:: python

    @events.on_ready
    async def on_ready(data):
        global bot
        bot = data
        print(f'Successfully logged in as {bot.name}! ({bot.id})')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``bot.id``                  | The ID of the bot.                           |
+-----------------------------+----------------------------------------------+
| ``bot.name``                | The name of the bot.                         |	
+-----------------------------+----------------------------------------------+
| ``bot.avatar``              | The avatar of the bot.                       |
+-----------------------------+----------------------------------------------+
| ``bot.banner``              | The banner of the bot.                       |
+-----------------------------+----------------------------------------------+
| ``bot.created_at``          | The date and time the bot was created.       |
+-----------------------------+----------------------------------------------+
| ``bot.status``              | The status of the bot.                       |
+-----------------------------+----------------------------------------------+
| ``bot.emote_id``            | The ID of the bot's status emote.            |
+-----------------------------+----------------------------------------------+
| ``bot.created_by``          | The ID of the user who created the bot.      |
+-----------------------------+----------------------------------------------+