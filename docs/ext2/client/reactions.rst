Reactions
========

This section provides an overview of the reaction-related methods available in the NextGuild library. The following methods are used to interact with reactions:

create_message_reaction
-----------------

.. code-block:: python

    create_message_reaction(channel_id, message_id, emote_id)

Create a reaction on a message.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the message is in.   |
+-------------------+---------+--------------------------------------------+
| message_id        | str     | The ID of the message to react to.         |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to react with.         |
+-------------------+---------+--------------------------------------------+

delete_message_reaction
-----------------

.. code-block:: python

    delete_message_reaction(channel_id, message_id, emote_id)

Delete a reaction on a message.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the message is in.   |
+-------------------+---------+--------------------------------------------+
| message_id        | str     | The ID of the message to remove the        |
|                   |         | reaction from.                             |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to remove.             |
+-------------------+---------+--------------------------------------------+

create_topic_reaction
-----------------

.. code-block:: python

    create_topic_reaction(channel_id, topic_id, emote_id)

Create a reaction on a topic.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the topic is in.     |
+-------------------+---------+--------------------------------------------+
| topic_id          | int     | The ID of the topic to react to.           |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to react with.         |
+-------------------+---------+--------------------------------------------+

delete_topic_reaction
-----------------

.. code-block:: python

    delete_topic_reaction(channel_id, topic_id, emote_id)

Delete a reaction on a topic.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the topic is in.     |
+-------------------+---------+--------------------------------------------+
| topic_id          | int     | The ID of the topic to remove the          |
|                   |         | reaction from.                             |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to remove.             |
+-------------------+---------+--------------------------------------------+

create_topic_comment_reaction
-----------------

.. code-block:: python

    create_topic_comment_reaction(channel_id, topic_id, topic_comment_id, emote_id)

Create a reaction on a topic comment.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the topic comment is |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| topic_id          | int     | The ID of the topic the comment is in.     |
+-------------------+---------+--------------------------------------------+
| topic_comment_id  | int     | The ID of the topic comment to react to.   |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to react with.         |
+-------------------+---------+--------------------------------------------+

delete_topic_comment_reaction
-----------------

.. code-block:: python

    delete_topic_comment_reaction(channel_id, topic_id, topic_comment_id, emote_id)

Delete a reaction on a topic comment.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the topic comment is |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| topic_id          | int     | The ID of the topic the comment is in.     |
+-------------------+---------+--------------------------------------------+
| topic_comment_id  | int     | The ID of the topic comment to remove the  |
|                   |         | reaction from.                             |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to remove.             |
+-------------------+---------+--------------------------------------------+

create_event_reaction
-----------------

.. code-block:: python

    create_event_reaction(channel_id, event_id, emote_id)

Create a reaction on an event.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the event is in.     |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event to react to.           |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to react with.         |
+-------------------+---------+--------------------------------------------+

delete_event_reaction
-----------------

.. code-block:: python

    delete_event_reaction(channel_id, event_id, emote_id)

Delete a reaction on an event.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the event is in.     |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event to remove the reaction |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to remove.             |
+-------------------+---------+--------------------------------------------+

create_event_comment_reaction
-----------------

.. code-block:: python

    create_event_comment_reaction(channel_id, event_id, comment_id, emote_id)

Create a reaction on an event comment.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the event comment is |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event the comment is in.     |
+-------------------+---------+--------------------------------------------+
| comment_id        | int     | The ID of the event comment to react to.   |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to react with.         |
+-------------------+---------+--------------------------------------------+

delete_event_comment_reaction
-----------------

.. code-block:: python

    delete_event_comment_reaction(channel_id, event_id, comment_id, emote_id)

Delete a reaction on an event comment.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel the event comment is |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event the comment is in.     |
+-------------------+---------+--------------------------------------------+
| comment_id        | int     | The ID of the event comment to remove the  |
|                   |         | reaction from.                             |
+-------------------+---------+--------------------------------------------+
| emote_id          | int     | The ID of the emote to remove.             |
+-------------------+---------+--------------------------------------------+

