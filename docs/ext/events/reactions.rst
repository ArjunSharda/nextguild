Reactions
===========

This page provides an overview of the reaction events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_reaction_create
--------

.. code-block:: python

    @events.on_reaction_create
    async def example():
        print('A reaction was created!')

on_reaction_delete
--------

.. code-block:: python

    @events.on_reaction_delete
    async def example():
        print('A reaction was deleted!')

on_forum_topic_comment_reaction_create
--------

.. code-block:: python

    @events.on_forum_topic_comment_reaction_create
    async def example():
        print('A reaction was created on a forum topic comment!')

on_forum_topic_comment_reaction_delete
--------

.. code-block:: python

    @events.on_forum_topic_comment_reaction_delete
    async def example():
        print('A reaction was deleted on a forum topic comment!')

on_calendar_event_reaction_create
--------

.. code-block:: python

    @events.on_calendar_reaction_create
    async def example():
        print('A reaction was created on a calendar event!')

on_calendar_event_reaction_delete
--------

.. code-block:: python

    @events.on_calendar_reaction_delete
    async def example():
        print('A reaction was deleted on a calendar event!')

