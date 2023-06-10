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
<<<<<<< Updated upstream
    async def example():
        print('A reaction was created on a channel message!')
=======
    async def example(data):
        print(f'A reaction with id {data.id} was created on a channel message!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.message_id``         | The id of the message the reaction was       |
|                             | created on.                                  |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |	
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.message_id``         | The id of the message the reaction was       |
|                             | created on.                                  |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |	
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_channel_message_reaction_delete
--------

.. code-block:: python
    @events.on_channel_message_reaction_delete
    async def example():
        print('A reaction was deleted on a channel message!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.message_id``         | The id of the message the reaction was       |
|                             | created on.                                  |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.deleted_by``         | The user who deleted the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |	
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_channel_message_reaction_many_delete
--------

.. code-block:: python
    @events.on_channel_messager_reaction_many_delete
    async def example():
        print('Many reactions were deleted on a message in a channel!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.topic_id``           | The id of the forum topic the reaction was   |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
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
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | deleted in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who deleted the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | deleted in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.topic_id``           | The id of the forum topic the reaction was   |
|                             | deleted in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | deleted in.                                  |
+-----------------------------+----------------------------------------------+


on_forum_topic_comment_reaction_create
--------

.. code-block:: python
    @events.on_forum_topic_comment_reaction_create
    async def example():
        print('A reaction was created on a forum topic comment!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.topic_id``           | The id of the forum topic the reaction was   |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.comment_id``         | The id of the forum topic comment the        |
|                             | reaction was created in.                     |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_forum_topic_comment_reaction_delete
--------

.. code-block:: python
    @events.on_forum_topic_comment_reaction_delete
    async def example():
        print('A reaction was deleted on a forum topic comment!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.topic_id``           | The id of the forum topic the reaction was   |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.comment_id``         | The id of the forum topic comment the        |
|                             | reaction was created in.                     |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_calendar_event_reaction_create
--------

.. code-block:: python
    @events.on_calendar_reaction_create
    async def example():
        print('A reaction was created on a calendar event!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.event_id``           | The id of the calendar event the reaction    |
|                             | was created in.                              |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_calendar_event_reaction_delete
--------

.. code-block:: python
    @events.on_calendar_reaction_delete
    async def example():
        print('A reaction was deleted on a calendar event!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.event_id``           | The id of the calendar event the reaction    |
|                             | was created in.                              |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_calendar_event_comment_reaction_create
--------

.. code-block:: python
    @events.on_calendar_comment_reaction_create
    async def example(data):
        print(f'A reaction with id {data.id} was created on a calendar event comment!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.event_id``           | The id of the calendar event the reaction    |
|                             | was created in.                              |
+-----------------------------+----------------------------------------------+
| ``data.comment_id``         | The id of the calendar event comment the     |
|                             | reaction was created in.                     |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_calendar_event_comment_reaction_delete
--------

.. code-block:: python
    @events.on_calendar_comment_reaction_delete
    async def example(data):
        print(f'A reaction with id {data.id} was deleted on a calendar event comment!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.event_id``           | The id of the calendar event the reaction    |
|                             | was created in.                              |
+-----------------------------+----------------------------------------------+
| ``data.comment_id``         | The id of the calendar event comment the     |
|                             | reaction was created in.                     |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_announcement_reaction_create
--------

.. code-block:: python
    @events.on_announcement_reaction_create
    async def example():
        print('A reaction was created on an announcement!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.announcement_id``    | The id of the announcement the reaction      |
|                             | was created in.                              |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_announcement_reaction_delete
--------

.. code-block:: python
    @events.on_announcement_reaction_delete
    async def example():
        print('A reaction was deleted on an announcement!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.announcement_id``    | The id of the announcement the reaction      |
|                             | was created in.                              |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_announcement_comment_reaction_create
--------

.. code-block:: python
    @events.on_announcement_comment_reaction_create
    async def example():
        print('A reaction was created on an announcement comment!')
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The id of the server the reaction was        |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The id of the channel the reaction was       |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+
| ``data.announcement_id``    | The id of the announcement the reaction      |
|                             | was created in.                              |
+-----------------------------+----------------------------------------------+
| ``data.comment_id``         | The id of the announcement comment the       |
|                             | reaction was created in.                     |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the reaction.           |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The id of the reaction.                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the reaction.                    |
+-----------------------------+----------------------------------------------+
| ``data.url``                | The url of the reaction.                     |
+-----------------------------+----------------------------------------------+
| ``data.emote_server_id``    | The id of the server the emote was           |
|                             | created in.                                  |
+-----------------------------+----------------------------------------------+

on_announcement_comment_reaction_delete
--------

.. code-block:: python

    @events.on_announcement_comment_reaction_delete
    async def example():