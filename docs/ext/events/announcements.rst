Announcements
===========

This page provides an overview of the announcement events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_announcement_create
--------

.. code-block:: python

    @events.on_announcement_create
    async def example():
        print('An announcement has been created!')

on_announcement_update
--------

.. code-block:: python

    @events.on_announcement_update
    async def example():
        print('An announcement has been updated!')

on_announcement_delete
--------

.. code-block:: python

    @events.on_announcement_delete
    async def example():
        print('An announcement has been deleted!')

on_announcement_comment_create
--------

.. code-block:: python

    @events.on_announcement_comment_create
    async def example():
        print('An announcement comment has been created!')

on_announcement_comment_update
--------

.. code-block:: python

    @events.on_announcement_comment_update
    async def example():
        print('An announcement comment has been updated!')

on_announcement_comment_delete
--------

.. code-block:: python

    @events.on_announcement_comment_delete
    async def example():
        print('An announcement comment has been deleted!')
