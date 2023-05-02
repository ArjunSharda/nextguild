Forums
===========

This page provides an overview of the forum events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_forum_topic_create 
--------

.. code-block:: python

    @events.on_forum_topic_create
    async def example():
        print('A forum topic has been created!')

on_forum_topic_update
--------

.. code-block:: python

    @events.on_forum_topic_update
    async def example():
        print('A forum topic has been updated!')

on_forum_topic_delete
--------

.. code-block:: python

    @events.on_forum_topic_delete
    async def example():
        print('A forum topic has been deleted!')

on_forum_topic_comment_create
--------

.. code-block:: python

    @events.on_forum_topic_comment_create
    async def example():
        print('A comment has been created on a forum topic!')

on_forum_topic_comment_update
--------

.. code-block:: python

    @events.on_forum_topic_comment_update
    async def example():
        print('A comment has been updated on a forum topic!')

on_forum_topic_comment_delete
--------

.. code-block:: python

    @events.on_forum_topic_comment_delete
    async def example():
        print('A comment has been deleted on a forum topic!')

on_forum_topic_pin
--------

.. code-block:: python

    @events.on_forum_topic_pin
    async def example():
        print('A forum topic has been pinned!')

on_forum_topic_unpin
--------

.. code-block:: python

    @events.on_forum_topic_unpin
    async def example():
        print('A forum topic has been unpinned!')

on_forum_topic_lock
--------

.. code-block:: python

    @events.on_forum_topic_lock
    async def example():
        print('A forum topic has been locked!')

on_forum_topic_unlock
--------

.. code-block:: python

    @events.on_forum_topic_unlock
    async def example():
        print('A forum topic has been unlocked!')



