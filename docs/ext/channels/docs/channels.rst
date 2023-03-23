Channels
============

This section provides an overview of the channel-related methods available in the NextGuild library. The following methods are used to interact with channels:

create_channel
--------------

.. code-block:: python

    create_channel(name, type, serverid, groupid=None, categoryid=None, ispublic=None)

Creates a new channel.

+-------------+---------------+-----------------------------------------------+
| Parameter   | Type          | Description                                   |
+=============+===============+===============================================+
| name        | str           | The name of the channel.                      |
+-------------+---------------+-----------------------------------------------+
| type        | str           | The type of the channel.                      |
+-------------+---------------+-----------------------------------------------+
| serverid    | str           | The ID of the server to create the channel in.|
+-------------+---------------+-----------------------------------------------+
| groupid     | str, optional | The ID of the group to create the channel in. |
+-------------+---------------+-----------------------------------------------+
| categoryid  | str, optional |The ID of the category to create the channel in|
+-------------+---------------+-----------------------------------------------+
| ispublic    | bool, optional| Whether the channel is public or not.         |
+-------------+---------------+-----------------------------------------------+

get_channel
-----------

.. code-block:: python

    get_channel(channelid)

Retrieves information about a channel.

+-------------+--------+----------------------------------------+
| Parameter   | Type   | Description                            |
+=============+========+========================================+
| channelid   | str    | The ID of the channel to retrieve.     |
+-------------+--------+----------------------------------------+

delete_channel
--------------

.. code-block:: python

    delete_channel(channelid)

Deletes a channel.

+-------------+--------+----------------------------------------+
| Parameter   | Type   | Description                            |
+=============+========+========================================+
| channelid   | str    | The ID of the channel to delete.       |
+-------------+--------+----------------------------------------+

update_channel
--------------

.. code-block:: python

    update_channel(channelid, name=None, topic=None, ispublic=None)

Updates a channel.

+-------------+--------+----------------------------------------+
| Parameter   | Type   | Description                            |
+=============+========+========================================+
| channelid   | str    | The ID of the channel to update.       |
+-------------+--------+----------------------------------------+
| name        | str, optional | The new name of the channel.    |
+-------------+--------+----------------------------------------+
| topic       | str, optional | The new topic of the channel.   |
+-------------+--------+----------------------------------------+
| ispublic    | bool, optional| Whether the channel is public   |
|             |               |  or not.
+-------------+--------+----------------------------------------+
