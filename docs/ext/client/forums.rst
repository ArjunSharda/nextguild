Forums
========

This section provides an overview of the forum-related methods available in the NextGuild library. The following methods are used to interact with forums:

create_forum_topic
-----------------

.. code-block:: python

    create_forum_topic(channel_id, title, content)

Creates a forum topic in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to create the topic  |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| title             | str     | The title of the topic.                    |
+-------------------+---------+--------------------------------------------+
| content           | str     | The content of the topic.                  |
+-------------------+---------+--------------------------------------------+

update_forum_topic
-----------------

.. code-block:: python

    update_forum_topic(channel_id, forum_topic_id, title, content)

Updates a forum topic in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to update the topic  |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to update.       |
+-------------------+---------+--------------------------------------------+
| title             | str,    | The title of the topic.                    |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| content           | str,    | The content of the topic.                  |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+

delete_forum_topic
-----------------

.. code-block:: python

    delete_forum_topic(channel_id, forum_topic_id)

Deletes a forum topic in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to delete the topic  |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to delete.       |
+-------------------+---------+--------------------------------------------+

pin_forum_topic
---------------

.. code-block:: python

    pin_forum_topic(channel_id, forum_topic_id)

Pins a forum topic in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to pin the topic     |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to pin.          |
+-------------------+---------+--------------------------------------------+

unpin_forum_topic
-----------------

.. code-block:: python

    unpin_forum_topic(channel_id, forum_topic_id)

Unpins a forum topic in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to unpin the topic   |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to unpin.        |
+-------------------+---------+--------------------------------------------+

lock_forum_topic
----------------

.. code-block:: python

    lock_forum_topic(channel_id, forum_topic_id)

Locks a forum topic in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to lock the topic    |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to lock.         |
+-------------------+---------+--------------------------------------------+

unlock_forum_topic
------------------

.. code-block:: python

    unlock_forum_topic(channel_id, forum_topic_id)

Unlocks a forum topic in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to unlock the topic  |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to unlock.       |
+-------------------+---------+--------------------------------------------+

get_forum_topic
---------------

.. code-block:: python

    get_forum_topic(channel_id, forum_topic_id)

Returns a forum topic in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to get the topic     |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to get.          |
+-------------------+---------+--------------------------------------------+

get_forum_topics
----------------

.. code-block:: python

    get_forum_topics(channel_id, before, limit)

Returns a list of forum topics in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to get the topics    |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| before            | str     | The date-time of when to get the topics    |
|                   |         | before.                                    |
+-------------------+---------+--------------------------------------------+
| limit             | int     | The maximum number of topics to return.    |
+-------------------+---------+--------------------------------------------+

create_forum_comment
--------------------

.. code-block:: python

    create_forum_comment(channel_id, forum_topic_id, content)

Creates a forum comment in the specified channel and topic.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to create the        |
|                   |         | comment in.                                |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to create the    |
|                   |         | comment in.                                |
+-------------------+---------+--------------------------------------------+
| content           | str     | The content of the comment.                |
+-------------------+---------+--------------------------------------------+

update_forum_comment
--------------------

.. code-block:: python

    update_forum_comment(channel_id, forum_topic_id, forum_comment_id, content)

Updates a forum comment in the specified channel and topic.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to update the        |
|                   |         | comment in.                                |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to update the    |
|                   |         | comment in.                                |
+-------------------+---------+--------------------------------------------+
| forum_comment_id  | int     | The ID of the forum comment to update.     |
+-------------------+---------+--------------------------------------------+
| content           | str     | The content of the comment.                |
+-------------------+---------+--------------------------------------------+

delete_forum_comment
--------------------

.. code-block:: python

    delete_forum_comment(channel_id, forum_topic_id, forum_comment_id)

Deletes a forum comment in the specified channel and topic.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to delete the        |
|                   |         | comment in.                                |
+-------------------+---------+--------------------------------------------+
| forum_topic_id    | int     | The ID of the forum topic to delete the    |
|                   |         | comment in.                                |
+-------------------+---------+--------------------------------------------+
| forum_comment_id  | int     | The ID of the forum comment to delete.     |
+-------------------+---------+--------------------------------------------+

