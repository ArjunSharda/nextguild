Webhooks
===========

This page provides an overview of the webhook events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_webhook_create
--------

.. code-block:: python

    @events.on_webhook_create
    async def example():
        print('A webhook was created!')

on_webhook_update
--------

.. code-block:: python

    @events.on_webhook_update
    async def example():
        print('A webhook was updated!')

on_webhook_delete
--------

.. code-block:: python

    @events.on_webhook_delete
    async def example():
        print('A webhook was deleted!')