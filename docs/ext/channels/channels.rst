Channels
========

This document provides an overview of the channel-related methods available in the NextGuild library. The following methods are used to interact with channels:


create_channel
--------------

.. code-block:: python

     bot.create_channel(self, name, type, serverid, groupid=None, categoryid=None, ispublic=None):

Create a new channel in the specified server or group.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| name        | str     | The name of the channel.                 |
+-------------+---------+------------------------------------------+
| type        | str     | The type of the channel (e.g. "text").   |
+-------------+---------+------------------------------------------+
| serverid    | str     | The ID of the server to create the       |
|             |         | channel in.                              |
+-------------+---------+------------------------------------------+
| groupid     | str,    | The ID of the group to create the        |
|             | optional| channel in.                              |
+-------------+---------+------------------------------------------+
| categoryid  | str,    | The ID of the category to create         |
|             | optional| the channel in.                          |
+-------------+---------+------------------------------------------+
| ispublic    | bool,   | Whether the channel is public or         |
|             | optional| private.                                 |
+-------------+---------+------------------------------------------+

get_channel
-----------

.. code-block:: python

    bot.get_channel(self, channelid):

Retrieve information about a specific channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channelid   | str     | The ID of the channel to retrieve.       |
+-------------+---------+------------------------------------------+

delete_channel
--------------

.. code-block:: python

    bot.delete_channel(self, channelid):

Delete a specific channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channelid   | str     | The ID of the channel to delete.         |
+-------------+---------+------------------------------------------+

update_channel
--------------

.. code-block:: python

    bot.update_channel(self, channelid, name=None, topic=None, ispublic=None):

Update a specific channel's information.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channelid   | str     | The ID of the channel to update.         |
+-------------+---------+------------------------------------------+
| name        | str     |    The new name for the channel.         |
|             |         |                                          |
+-------------+---------+------------------------------------------+
| topic       | str,    | The new topic for the channel.           |
|             | optional|                                          |
+-------------+---------+------------------------------------------+
| ispublic    | bool,   |  Whether the channel is public           |
|             | optional|  or not.                                 |
+-------------+---------+------------------------------------------+
