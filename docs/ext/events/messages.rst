Messages
===========

This page provides an overview of the message events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_message
--------

.. code-block:: python

    @events.on_message
    async def example(message):
        print(message.content)

on_message_update
----------------

.. code-block:: python

    @events.on_message_update
    async def example(message):
        print(message.content)

on_message_delete
----------------

.. code-block:: python

    @events.on_message_delete
    async def example():
        print('Message Deleted')