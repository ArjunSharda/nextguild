Reactions
=========

This section provides an overview of the reaction-related methods available in the NextGuild library. The following methods are used to interact with reactions:

create_reaction
---------------

.. code-block:: python

    bot.create_reaction(channelid, contentid, emoteid)

React to a specified message with a specified emoteid.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the message is |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| contentid   | str           | The content ID of the message.             |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to react with                 |
+-------------+---------------+--------------------------------------------+

delete_reaction
---------------

.. code-block:: python

    bot.delete_reaction(channelid, contentid, emoteid)

Delete a reaction from a message.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the message is |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| contentid   | str           | The content ID of the message.             |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to delete the reaction        |
+-------------+---------------+--------------------------------------------+

create_topic_reaction
---------------------

.. code-block:: python

    bot.create_topic_reaction(channelid, topicid, emoteid)

Creates a reaction on the topic.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the message is |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| topicid     | str           | The topic ID to react onto.                |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to react with                 |
+-------------+---------------+--------------------------------------------+

delete_topic_reaction
---------------------

.. code-block:: python

    bot.delete_topic_reaction(channelid, topicid, emoteid)

Deletes a reaction from the topic.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the message is |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| topicid     | str           | The topic ID to delete the reaction from.  |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to delete the reaction        |
+-------------+---------------+--------------------------------------------+

create_topic_comment_reaction
-----------------------------

.. code-block:: python

    bot.create_topic_comment_reaction(channelid, topicid, topiccommentid, emoteid)

Creates a reaction on a topic's comment.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the comment is |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| topicid     | str           |The topic ID where the comment is located in|
+-------------+---------------+--------------------------------------------+
|topiccomentid|  str          |  The topic's comment ID to react to.       |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to react with                 |
+-------------+---------------+--------------------------------------------+

delete_topic_comment_reaction
-----------------------------

.. code-block:: python

    bot.delete_topic_comment_reaction(channelid, topicid, topiccommentid, emoteid)

Deletes a reaction on a topic's comment.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the comment is |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| topicid     | str           |The topic ID where the comment is located in|
+-------------+---------------+--------------------------------------------+
|topiccomentid|  str          |The comment ID to delete the reaction from  |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to delete the reaction        |
+-------------+---------------+--------------------------------------------+

create_event_reaction
---------------------

.. code-block:: python

    bot.create_event_reaction(channelid, eventid, emoteid)

Create a reaction on a event.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the event is   |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| eventid     | str           |The event ID, to react to                   |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to create the reaction        |
+-------------+---------------+--------------------------------------------+

delete_event_reaction
---------------------

.. code-block:: python

    bot.delete_event_reaction(channelid, eventid, emoteid)

Delete a reaction on a event.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the event is   |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| eventid     | str           |The event ID, to delete the reaction from   |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to delete the reaction        |
+-------------+---------------+--------------------------------------------+

create_event_comment_reaction
-----------------------------

.. code-block:: python

    bot.create_event_comment_reaction(channelid, eventid, commentid, emoteid)

Create a reaction on a event's comment.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the comment is |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| eventid     | str           |The event ID where the comment is located in|
+-------------+---------------+--------------------------------------------+
|commentid    |  str          |The comment ID to create the reaction on    |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to create the reaction        |
+-------------+---------------+--------------------------------------------+

delete_event_comment_reaction
-----------------------------

.. code-block:: python

    bot.delete_event_comment_reaction(channelid, eventid, commentid, emoteid)

Delete a reaction on a event's comment.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the comment is |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| eventid     | str           |The event ID where the comment is located in|
+-------------+---------------+--------------------------------------------+
|commentid.   |  str          |The comment ID to delete the reaction from  |
+-------------+---------------+--------------------------------------------+
| emoteid     | str           | The emote ID to delete the reaction        |
+-------------+---------------+--------------------------------------------+

