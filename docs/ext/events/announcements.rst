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
    async def example(data):
        print(f'An announcement with the title {data.title} has been created!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the announcement                   |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the announcement was created        |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The ID of the user who created the           |
|                             | announcement                                 |
+-----------------------------+----------------------------------------------+
| `data.title`                | The title of the announcement                |
+-----------------------------+----------------------------------------------+
| `data.content`              | The content of the announcement              |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions in the announcement             |
+-----------------------------+----------------------------------------------+

on_announcement_update
--------

.. code-block:: python

    @events.on_announcement_update
    async def example(data):
        print(f'An announcement with the title {data.title} has been updated!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the announcement                   |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the announcement was created        |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The ID of the user who created the           |
|                             | announcement                                 |
+-----------------------------+----------------------------------------------+
| `data.title`                | The title of the announcement                |
+-----------------------------+----------------------------------------------+
| `data.content`              | The content of the announcement              |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions in the announcement             |
+-----------------------------+----------------------------------------------+

on_announcement_delete
--------

.. code-block:: python

    @events.on_announcement_delete
    async def example(data):
        print(f'An announcement with the title {data.title} has been deleted!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the announcement                   |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the announcement was created        |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The ID of the user who created the           |
|                             | announcement                                 |
+-----------------------------+----------------------------------------------+
| `data.title`                | The title of the announcement                |
+-----------------------------+----------------------------------------------+
| `data.content`              | The content of the announcement              |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions in the announcement             |
+-----------------------------+----------------------------------------------+

on_announcement_comment_create
--------

.. code-block:: python

    @events.on_announcement_comment_create
    async def example(data):
        print(f'An announcement comment with the content {data.content} has been created!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the announcement comment           |
+-----------------------------+----------------------------------------------+
| `data.content`              | The content of the announcement comment      |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the announcement comment was        |
|                             | created                                      |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The ID of the user who created the           |
|                             | announcement comment                         |
+-----------------------------+----------------------------------------------+
| `data.announcement_id`      | The ID of the announcement                   |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions in the announcement comment     |
+-----------------------------+----------------------------------------------+

on_announcement_comment_update
--------

.. code-block:: python

    @events.on_announcement_comment_update
    async def example(data):
        print(f'An announcement comment with the content {data.content} has been updated!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the announcement comment           |
+-----------------------------+----------------------------------------------+
| `data.content`              | The content of the announcement comment      |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the announcement comment was        |
|                             | created                                      |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The ID of the user who created the           |
|                             | announcement comment                         |
+-----------------------------+----------------------------------------------+
| `data.updated_at`           | The time the announcement comment was        |
|                             | updated                                      |
+-----------------------------+----------------------------------------------+
| `data.announcement_id`      | The ID of the announcement                   |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions in the announcement comment     |
+-----------------------------+----------------------------------------------+

on_announcement_comment_delete
--------

.. code-block:: python

    @events.on_announcement_comment_delete
    async def example(data):
        print(f'An announcement comment with the content {data.content} has been deleted!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the announcement comment           |
+-----------------------------+----------------------------------------------+
| `data.content`              | The content of the announcement comment      |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the announcement comment was        |
|                             | created                                      |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The ID of the user who created the           |
|                             | announcement comment                         |
+-----------------------------+----------------------------------------------+
| `data.announcement_id`      | The ID of the announcement                   |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions in the announcement comment     |
+-----------------------------+----------------------------------------------+
