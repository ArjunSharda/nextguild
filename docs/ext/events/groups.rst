Groups
===========

This page provides an overview of the group events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_group_create
---------------

.. code-block:: python

    @events.on_group_create
    async def on_group_create(data):
        print(f'Group {data.name} was created!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the group                          |
+-----------------------------+----------------------------------------------+
| `data.name`                 | The name of the group                        |
+-----------------------------+----------------------------------------------+
| `data.description`          | The description of the group                 |
+-----------------------------+----------------------------------------------+
| `data.avatar``              | The avatar of the group                      |
+-----------------------------+----------------------------------------------+
| `data.emote_id`             | The ID of the emote associated with the group|
+-----------------------------+----------------------------------------------+
| `data.is_public`            | Whether the group is public or not           |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the group was created               |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The ID of the user who created the group     |
+-----------------------------+----------------------------------------------+

on_group_update
---------------

.. code-block:: python

    @events.on_group_update
    async def on_group_update(data):
        print(f'Group {data.name} was updated!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the group                          |
+-----------------------------+----------------------------------------------+
| `data.name`                 | The name of the group                        |
+-----------------------------+----------------------------------------------+
| `data.description`          | The description of the group                 |
+-----------------------------+----------------------------------------------+
| `data.avatar``              | The avatar of the group                      |
+-----------------------------+----------------------------------------------+
| `data.is_home`              | Whether the group is the home group or not   |
+-----------------------------+----------------------------------------------+
| `data.emote_id`             | The ID of the emote associated with the group|
+-----------------------------+----------------------------------------------+
| `data.is_public`            | Whether the group is public or not           |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the group was created               |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The ID of the user who created the group     |
+-----------------------------+----------------------------------------------+
| `data.updated_at`           | The time the group was updated               |
+-----------------------------+----------------------------------------------+
| `data.updated_by`           | The ID of the user who updated the group     |
+-----------------------------+----------------------------------------------+
| `data.archived_at`          | The time the group was archived              |
+-----------------------------+----------------------------------------------+
| `data.archived_by`          | The ID of the user who archived the group    |
+-----------------------------+----------------------------------------------+