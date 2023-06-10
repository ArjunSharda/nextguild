Messages
===========

This page provides an overview of the message events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_message
--------

.. code-block:: python

    @events.on_message
    async def example(data):
        print(data.content)

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server the message was sent in |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the message                        |
+-----------------------------+----------------------------------------------+
| ``data.type``               | The type of message: "system" or "default"   |
|                             | system being Guilded and default being from  |
|                             | an user or a bot                             |
+-----------------------------+----------------------------------------------+
| ``data.group_id``           | The ID of the group the message was sent in  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel the message was sent   |
|                             | in                                           |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the message                   |
+-----------------------------+----------------------------------------------+
| ``data.embeds``             | The embeds of the message                    |
+-----------------------------+----------------------------------------------+
| ``data.reply_message_ids``  | The IDs of the messages that were replied to |
+-----------------------------+----------------------------------------------+
| ``data.is_private``         | Whether the message that was sent is private |
+-----------------------------+----------------------------------------------+
| ``data.is_silent``          | Whether the message that was sent is silent  |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the message                  |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the message was created             |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The ID of the user that created the message  |
+-----------------------------+----------------------------------------------+

on_message_update
----------------

.. code-block:: python

    @events.on_message_update
    async def example(data):
        print(data.content)

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server the message was sent in |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the message                        |
+-----------------------------+----------------------------------------------+
| ``data.type``               | The type of message: "system" or "default"   |  
|                             | system being Guilded and default being from  |
|                             | an user or a bot                             |
+-----------------------------+----------------------------------------------+
| ``data.group_id``           | The ID of the group the message was sent in  |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel the message was sent   |
|                             | in                                           |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the message                   |
+-----------------------------+----------------------------------------------+
| ``data.embeds``             | The embeds of the message                    |
+-----------------------------+----------------------------------------------+
| ``data.reply_message_ids``  | The IDs of the messages that were replied to |
+-----------------------------+----------------------------------------------+
| ``data.is_private``         | Whether the message that was sent is private |
+-----------------------------+----------------------------------------------+
| ``data.is_silent``          | Whether the message that was sent is silent  |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the message                  |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the message was created             |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The ID of the user that created the message  |
+-----------------------------+----------------------------------------------+
| ``data.updated_at``         | The time the message was updated             |
+-----------------------------+----------------------------------------------+


on_message_delete
----------------

.. code-block:: python

    @events.on_message_delete
    async def example(data):
        print("A message in {data.server_id} was deleted")

+-----------------------------+------------------------------------------------+
| Type                        | Description                                    |
+=============================+================================================+
| ``data.server_id``          | The ID of the server                           |
+-----------------------------+------------------------------------------------+
| ``data.id``                 | The ID of the message                          |
+-----------------------------+------------------------------------------------+
| ``data.channel_id``         | The ID of the channel                          |
+-----------------------------+------------------------------------------------+
| ``data.deleted_at``         | The time the message was deleted               |
+-----------------------------+------------------------------------------------+
| ``data.is_private``         | Whether the message that was deleted is private|
+-----------------------------+------------------------------------------------+