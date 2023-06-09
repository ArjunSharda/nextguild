Reactions
===========

This page provides an overview of the reaction events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_channel_message_reaction_create
--------

.. code-block:: python

    @events.on_channel_message_reaction_create
    async def example():
        print('A reaction was created on a channel message!')

on_channel_message_reaction_delete
--------

.. code-block:: python

    @events.on_channel_message_reaction_delete
    async def example():
        print('A reaction was deleted on a channel message!')

on_channel_message_reaction_many_delete
--------

.. code-block:: python

    @events.on_channel_messager_reaction_many_delete
    async def example():
        print('Many reactions were deleted on a message in a channel!')

on_forum_topic_reaction_create 
--------

.. code-block:: python

    @events.on_forum_topic_reaction_create
    async def example(data):
        print(f'A reaction with id {data.id} was created on a forum topic!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.channel_id`           | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| `data.name`                 | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| `data.url`                  | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| `data.server_id`            | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| `data.topic_id`             | The id of the forum topic the reaction was   |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| `data.emote_server_id`      | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_forum_topic_reaction_delete
--------

.. code-block:: python

    @events.on_forum_topic_reaction_delete
    async def example(data):
        print(f'A reaction with id {data.id} was deleted on a forum topic!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.channel_id`           | The id of the channel the reaction was       |
|                             | deleted in.                                  |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The user who deleted the reaction.           |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| `data.name`                 | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| `data.url`                  | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| `data.server_id`            | The id of the server the reaction was        |
|                             | deleted in.                                  |
+-----------------------------+----------------------------------------------+
| `data.topic_id`             | The id of the forum topic the reaction was   |
|                             | deleted in.                                  |
+-----------------------------+----------------------------------------------+
| `data.emote_server_id`      | The id of the server the emote was           |
|                             | deleted in.                                  |
+-----------------------------+----------------------------------------------+


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

on_announcement_reaction_create
--------

.. code-block:: python

    @events.on_announcement_reaction_create
    async def example():
        print('A reaction was created on an announcement!')

on_announcement_reaction_delete
--------

.. code-block:: python

    @events.on_announcement_reaction_delete
    async def example():
        print('A reaction was deleted on an announcement!')

on_announcement_comment_reaction_create
--------

.. code-block:: python

    @events.on_announcement_comment_reaction_create
    async def example():
        print('A reaction was created on an announcement comment!')

on_announcement_comment_reaction_delete
--------

.. code-block:: python

    @events.on_announcement_comment_reaction_delete
    async def example():
        print('A reaction was deleted on an announcement comment!')