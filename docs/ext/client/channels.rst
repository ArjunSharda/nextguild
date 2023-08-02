Channels
========

This section provides an overview of the channel-related methods available in the NextGuild library. The following methods are used to interact with channels:

create_channel
--------------
.. code-block:: python

    create_channel(name, channel_type, topic, server_id, server_id, group_id, category_id, is_public, parent_id, message_id) 

Create a channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| name              | str     | The name of the channel.                    |
+-------------------+---------+---------------------------------------------+
| channel_type      | str     | The type of the channel.                    |
+-------------------+---------+---------------------------------------------+
| topic             | str,    | The topic of the channel.                   |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+
| server_id         | str,    | The ID of the server to create the channel. |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+
| group_id          | str,    | The ID of the group to create the channel.  |
|                   | optional|                                             |
+-------------------+---------+---------------------------------------------+
| category_id       | str,    | The ID of the category to create the        |
|                   | optional| channel.                                    |
+-------------------+---------+---------------------------------------------+
| visibility        | str,    | The channel's visibility. None by default   |
|                   | optional| None, private or public                     |
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
| visibility        | str     | If the channel is public. Private by default|
|                   | optional| None, private or public                     |
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

archive_channel
---------------
.. code-block:: python

    archive_channel(channel_id)

Archive a channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to archive.           |
+-------------------+---------+---------------------------------------------+

restore_channel
---------------
.. code-block:: python

    restore_channel(channel_id)

Restore a channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to restore.           |
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
