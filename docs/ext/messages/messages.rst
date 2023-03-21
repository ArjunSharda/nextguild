Messages
========

This document provides an overview of the message-related methods available in the NextGuild library. The following methods are used to interact with channels and messages:

send_message
------------

.. code-block:: python

    bot.send_message(channel_id, content=None, embed=None)

Send a message to the specified channel. Optionally, provide content and/or an embed.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel to send the message. |
+-------------+---------------+--------------------------------------------+
| content     | str, optional | The content of the message.                |
+-------------+---------------+--------------------------------------------+
| embed       | object,       | An embed object to be sent with the        |
|             | optional      | message.                                   |
+-------------+---------------+--------------------------------------------+

send_reply
----------

.. code-block:: python

    bot.send_reply(channel_id, content, replyids)

Send a reply to a message in the specified channel.

+-------------+---------+-----------------------------------------+
| Parameter   | Type    | Description                             |
+=============+=========+=========================================+
| channel_id  | str     | The ID of the channel to send the reply.|
+-------------+---------+-----------------------------------------+
| content     | str     | The content of the reply.               |
+-------------+---------+-----------------------------------------+
| replyids    | list    | A list of message IDs to reply to.      |
+-------------+---------+-----------------------------------------+

edit_message
------------

.. code-block:: python

    bot.edit_message(channel_id, message_id, content)

Edit an existing message in the specified channel.

+-------------+---------+-----------------------------------------+
| Parameter   | Type    | Description                             |
+=============+=========+=========================================+
| channel_id  | str     | The ID of the channel where the message |
|             |         | is.                                     |
+-------------+---------+-----------------------------------------+
| message_id  | str     | The ID of the message to edit.          |
+-------------+---------+-----------------------------------------+
| content     | str     | The updated content of the message.     |
+-------------+---------+-----------------------------------------+

delete_message
--------------

.. code-block:: python

    bot.delete_message(channel_id, message_id)

Delete a message in the specified channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channel_id  | str     | The ID of the channel where the message  |
|             |         | is.                                      |
+-------------+---------+------------------------------------------+
| message_id  | str     | The ID of the message to delete.         |
+-------------+---------+------------------------------------------+

get_message
-----------

.. code-block:: python

    bot.get_message(channel_id, message_id)

Retrieve a specific message from a channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channel_id  | str     | The ID of the channel where the message  |
|             |         | is.                                      |
+-------------+---------+------------------------------------------+
| message_id  | str     | The ID of the message to retrieve.       |
+-------------+---------+------------------------------------------+

get_channel_messages
--------------------

.. code-block:: python

    bot.get_channel_messages(channel_id, limit=None, before=None, after=None, includePrivate=None)

Retrieves a list of messages from a channel.

+----------------+----------------+-----------------------------------------------------------------+
| Parameter      | Type           | Description                                                     |
+================+================+=================================================================+
| channel_id     | str            | The ID of the channel to get messages from.                     |
+----------------+----------------+-----------------------------------------------------------------+
| limit          | int, optional  | The maximum number of messages to retrieve.                     |
+----------------+----------------+-----------------------------------------------------------------+
| before         | str, optional  | The message ID to start retrieving messages before.             |
+----------------+----------------+-----------------------------------------------------------------+
| after          | str, optional  | The message ID to start retrieving messages after.              |
+----------------+----------------+-----------------------------------------------------------------+
| includePrivate | bool, optional | Whether to include private messages in the retrieved messages.  |
+----------------+----------------+-----------------------------------------------------------------+

purge
-----

.. code-block:: python

    bot.purge(channel_id, amount)

Purge a specified number of messages from a channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channel_id  | str     | The ID of the channel to purge messages  |
|             |         | from.                                    |
+-------------+---------+------------------------------------------+
| amount      | int     | The number of messages to purge.         |
+-------------+---------+------------------------------------------+

    
