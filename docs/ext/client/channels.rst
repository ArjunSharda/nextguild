Channels
========

This section provides an overview of the channel-related methods available in the NextGuild library. The following methods are used to interact with channels:

create_channel
--------------
.. code-block:: python

    create_channel(name, channel_type, server_id, server_id, group_id, category_id, is_public, parent_id, message_id)

Create a channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| name              | str     | The name of the channel.                    |
+-------------------+---------+---------------------------------------------+
| channel_type      | str     | The type of the channel.                    |
+-------------------+---------+---------------------------------------------+
| server_id         | str     | The ID of the server to create the channel. |
+-------------------+---------+---------------------------------------------+
| group_id          | str,    | The ID of the group to create the channel.  |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+
| category_id       | str,    | The ID of the category to create the        |
|                   | optional| channel.                                    |
+-------------------+---------+---------------------------------------------+
| is_public         | bool    | If the channel is public.                   |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+
| parent_id         | str,    | The ID of the parent channel.               |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+
| message_id        | str,    | The ID of the message to create the channel.|
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+


update_channel
--------------

.. code-block:: python

    update_channel(channel_id, name, topic, is_public)

Update a channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to update.            |
+-------------------+---------+---------------------------------------------+
| name              | str     | The name of the channel.                    |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+
| topic             | str     | The topic of the channel.                   |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+
| is_public         | bool    | If the channel is public.                   |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+

delete_channel
--------------

.. code-block:: python

    delete_channel(channel_id)

Delete a channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to delete.            |
+-------------------+---------+---------------------------------------------+

get_channel
------------

.. code-block:: python

    get_channel(channel_id)

Get a channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to get.               |
+-------------------+---------+---------------------------------------------+

get_default_channel
-------------------

.. code-block:: python

    get_default_channel(server_id)

Get the default channel of a server.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| server_id         | str     | The ID of the server to get the default     |
|                   |         | channel of.                                 |
+-------------------+---------+---------------------------------------------+
