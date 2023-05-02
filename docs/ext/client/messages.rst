Messages
========

This section provides an overview of the message-related methods available in the NextGuild library. The following methods are used to interact with messages:

send_message
-------------

.. code-block:: python

    send_message(channel_id, content, embed, isPrivate)

Send a message to the specified channel. Optionally, provide content and/or an embed.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to send the message. |
+-------------------+---------+--------------------------------------------+
| content           | str,    | The content of the message.                |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| embed             | object, | An embed object to be sent with the        |
|                   | optional| message.                                   |
+-------------------+---------+--------------------------------------------+
| isPrivate         | bool    | If the message should be private or not.   |
+-------------------+---------+--------------------------------------------+
| isSilent          | bool    | If the message should be silent or not.    |
+-------------------+---------+--------------------------------------------+
| reply_message_ids | list    | If the message should be private or not.   |
+-------------------+---------+--------------------------------------------+


edit_message
-------------

.. code-block:: python

    edit_message(channel_id, message_id, content, embed)

Edit a message to the specified channel. Optionally, provide content and/or an embed.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to edit the message. |
+-------------------+---------+--------------------------------------------+
| message_id        | str     | The ID of the message in the channel.      |
+-------------------+---------+--------------------------------------------+
| content           | str,    | The content of the message.                |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| embed             | object, | An embed object to be sent with the        |
|                   | optional| message.                                   |
+-------------------+---------+--------------------------------------------+


delete_message
---------------

.. code-block:: python

    delete_message(channel_id, message_id)

Delete a message in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to delete the message.|
+-------------------+---------+---------------------------------------------+
| message_id        | str     | The ID of the message in the channel.       |
+-------------------+---------+---------------------------------------------+

get_message
------------
.. code-block:: python

    get_message(channel_id, message_id)

Get a message in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to get the message.   |
+-------------------+---------+---------------------------------------------+
| message_id        | str     | The ID of the message in the channel.       |
+-------------------+---------+---------------------------------------------+

get_channel_messages
--------------------
.. code-block:: python

    get_channel_messages(channel_id, limit, before, after, includePrivate)

Gets the messages from the specified channel

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to get the messages.  |
+-------------------+---------+---------------------------------------------+
| limit             | int     | The maximum number of messages to get.      |
+-------------------+---------+---------------------------------------------+
| before            | str     | The ID of the message to get messages       |
|                   |         | before.                                     |
+-------------------+---------+---------------------------------------------+
| after             | str     | The ID of the message to get messages       |
|                   |         | after.                                      |
+-------------------+---------+---------------------------------------------+
| includePrivate    | bool    | If private messages should be included.     |
+-------------------+---------+---------------------------------------------+

purge
------
.. code-block:: python

    purge(channel_id, amount)

Purges the specified amount of messages from the channel

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to purge messages.    |
+-------------------+---------+---------------------------------------------+
| amount            | int     | The number of messages to purge.            |
+-------------------+---------+---------------------------------------------+