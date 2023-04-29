Lists
===========

This page provides an overview of the list events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_list_item_create
--------

.. code-block:: python

    @events.on_list_item_create
    async def example():
        print('A list item has been created!')

on_list_item_update
--------

.. code-block:: python

    @events.on_list_item_update
    async def example():
        print('A list item has been updated!')

on_list_item_delete
--------

.. code-block:: python

    @events.on_list_item_delete
    async def example():
        print('A list item has been deleted!')

on_list_item_complete
--------

.. code-block:: python

    @events.on_list_item_complete
    async def example():
        print('A list item has been completed!')

on_list_item_uncomplete
--------

.. code-block:: python

    @events.on_list_item_uncomplete
    async def example():
        print('A list item has been uncompleted!')