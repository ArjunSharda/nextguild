Channels
===========

This page provides an overview of the channel events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_channel_create
--------

.. code-block:: python

    @events.on_channel_create
    async def example(data):
        print(f'A channel with name {data.name} was created!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server the channel was created |
|                             | in.                                          |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.type``               | The type of the channel                      |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the channel                      |
+-----------------------------+----------------------------------------------+
| ``data.topic``              | The topic of the channel                     |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the channel was created             |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The ID of the user who created the channel   |
+-----------------------------+----------------------------------------------+
| ``data.root_id``            | The ID of the root channel                   |
+-----------------------------+----------------------------------------------+
| ``data.parent_id``          | The ID of the parent channel                 |
+-----------------------------+----------------------------------------------+
| ``data.message_id``         | The ID of the message that created the       |
|                             | channel                                      |
+-----------------------------+----------------------------------------------+
| ``data.category_id``        | The ID of the category the channel is in     |
+-----------------------------+----------------------------------------------+
| ``data.group_id``           | The ID of the group the channel is in        |
+-----------------------------+----------------------------------------------+
| ``data.is_public``          | Whether the channel is public                |
+-----------------------------+----------------------------------------------+

on_channel_delete
--------

.. code-block:: python

    @events.on_channel_delete
    async def example():
        print('A channel was deleted!')
    
on_channel_update
--------

.. code-block:: python

    @events.on_channel_update
    async def example():
        print('A channel was updated!')