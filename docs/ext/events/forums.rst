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
<<<<<<< Updated upstream
    async def example():
        print('A forum topic has been created!')
=======
    async def example(data):
        print(f'A forum topic with the name {data.title} been created!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the forum topic                 |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the forum topic was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the forum topic         |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the forum topic               |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the forum topic              |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_forum_topic_update
--------

.. code-block:: python

    @events.on_forum_topic_update
<<<<<<< Updated upstream
    async def example():
        print('A forum topic has been updated!')
=======
    async def example(data):
        print(f'A forum topic with the name {data.title} been updated!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the forum topic                 |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the forum topic was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the forum topic         |
+-----------------------------+----------------------------------------------+
| ``data.updated_at``         | The time the forum topic was updated         |
+-----------------------------+----------------------------------------------+
| ``data.bumped_at``          | The time the forum topic was bumped          |
+-----------------------------+----------------------------------------------+
| ``data.is_pinned``          | Whether the forum topic is pinned            |
+-----------------------------+----------------------------------------------+
| ``data.is_locked``          | Whether the forum topic is locked            |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the forum topic               |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the forum topic              |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_forum_topic_delete
--------

.. code-block:: python

    @events.on_forum_topic_delete
<<<<<<< Updated upstream
    async def example():
        print('A forum topic has been deleted!')
=======
    async def example(data):
        print(f'A forum topic with the name {data.title} been deleted!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the forum topic                 |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the forum topic was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the forum topic         |
+-----------------------------+----------------------------------------------+
| ``data.updated_at``         | The time the forum topic was updated         |
+-----------------------------+----------------------------------------------+
| ``data.bumped_at``          | The time the forum topic was bumped          |
+-----------------------------+----------------------------------------------+
| ``data.is_pinned``          | Whether the forum topic is pinned            |
+-----------------------------+----------------------------------------------+
| ``data.is_locked``          | Whether the forum topic is locked            |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the forum topic               |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the forum topic              |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_forum_topic_comment_create
--------

.. code-block:: python

    @events.on_forum_topic_comment_create
<<<<<<< Updated upstream
    async def example():
        print('A comment has been created on a forum topic!')
=======
    async def example(data):
        print(f'A comment with the content {data.content} has been created on a forum topic!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the comment                   |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the comment was created             |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the comment             |
+-----------------------------+----------------------------------------------+
| ``data.topic_id``           | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the comment                  |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_forum_topic_comment_update
--------

.. code-block:: python

    @events.on_forum_topic_comment_update
<<<<<<< Updated upstream
    async def example():
        print('A comment has been updated on a forum topic!')
=======
    async def example(data):
        print(f'A comment with the content {data.content} has been updated on a forum topic!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the comment                   |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the comment was created             |
+-----------------------------+----------------------------------------------+
| ``data.updated_at``         | The time the comment was updated             |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the comment             |
+-----------------------------+----------------------------------------------+
| ``data.topic_id``           | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the comment                  |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_forum_topic_comment_delete
--------

.. code-block:: python

    @events.on_forum_topic_comment_delete
<<<<<<< Updated upstream
    async def example():
        print('A comment has been deleted on a forum topic!')
=======
    async def example(data):
        print(f'A comment with the content {data.content} has been deleted on a forum topic!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the comment                   |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the comment was created             |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the comment             |
+-----------------------------+----------------------------------------------+
| ``data.topic_id``           | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the comment                  |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_forum_topic_pin
--------

.. code-block:: python

    @events.on_forum_topic_pin
<<<<<<< Updated upstream
    async def example():
        print('A forum topic has been pinned!')
=======
    async def example(data):
        print(f'A forum topic with the name {data.title} been pinned!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the forum topic                 |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the forum topic was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the forum topic         |
+-----------------------------+----------------------------------------------+
| ``data.bumped_at``          | The time the forum topic was bumped          |
+-----------------------------+----------------------------------------------+
| ``data.is_pinned``          | Whether the forum topic is pinned            |
+-----------------------------+----------------------------------------------+
| ``data.is_locked``          | Whether the forum topic is locked            |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the forum topic               |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the forum topic              |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_forum_topic_unpin
--------

.. code-block:: python

    @events.on_forum_topic_unpin
<<<<<<< Updated upstream
    async def example():
        print('A forum topic has been unpinned!')
=======
    async def example(data):
        print(f'A forum topic with the name {data.title} been unpinned!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the forum topic                 |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the forum topic was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the forum topic         |
+-----------------------------+----------------------------------------------+
| ``data.bumped_at``          | The time the forum topic was bumped          |
+-----------------------------+----------------------------------------------+
| ``data.is_pinned``          | Whether the forum topic is pinned            |
+-----------------------------+----------------------------------------------+
| ``data.is_locked``          | Whether the forum topic is locked            |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the forum topic               |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the forum topic              |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_forum_topic_lock
--------

.. code-block:: python

    @events.on_forum_topic_lock
<<<<<<< Updated upstream
    async def example():
        print('A forum topic has been locked!')
=======
    async def example(data):
        print(f'A forum topic with the name {data.title} been locked!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the forum topic                 |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the forum topic was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the forum topic         |
+-----------------------------+----------------------------------------------+
| ``data.bumped_at``          | The time the forum topic was bumped          |
+-----------------------------+----------------------------------------------+
| ``data.is_pinned``          | Whether the forum topic is pinned            |
+-----------------------------+----------------------------------------------+
| ``data.is_locked``          | Whether the forum topic is locked            |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the forum topic               |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the forum topic              |
+-----------------------------+----------------------------------------------+

>>>>>>> Stashed changes

on_forum_topic_unlock
--------

.. code-block:: python

    @events.on_forum_topic_unlock
<<<<<<< Updated upstream
    async def example():
        print('A forum topic has been unlocked!')
=======
    async def example(data):
        print(f'A forum topic with the name {data.title} been unlocked!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the forum topic                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the forum topic                 |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the forum topic was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the forum topic         |
+-----------------------------+----------------------------------------------+
| ``data.bumped_at``          | The time the forum topic was bumped          |
+-----------------------------+----------------------------------------------+
| ``data.is_pinned``          | Whether the forum topic is pinned            |
+-----------------------------+----------------------------------------------+
| ``data.is_locked``          | Whether the forum topic is locked            |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the forum topic               |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the forum topic              |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes



