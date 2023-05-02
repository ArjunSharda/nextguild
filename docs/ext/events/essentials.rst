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

.. code-block:: python

    @events.on_ready
    async def on_ready():
        print('Bot is ready!')