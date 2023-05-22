Users
===========

This page provides an overview of the user events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_member_join
--------

.. code-block:: python

    @events.on_member_join
    async def example():
        print('A user joined the server!')

on_member_leave
--------

.. code-block:: python

    @events.on_member_leave
    async def example():
        print('A user left the server!')

on_member_banned
--------

.. code-block:: python

    @events.on_member_banned
    async def example():
        print('A user was banned from the server!')

on_member_unbanned
--------

.. code-block:: python

    @events.on_member_unbanned
    async def example():
        print('A user was unbanned from the server!')
        
on_member_update
--------

.. code-block:: python

    @events.on_member_update
    async def example():
        print('A member was updated!')
