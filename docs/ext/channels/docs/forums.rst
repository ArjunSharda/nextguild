Forums
======

This section provides an overview of the forum-related methods available in the NextGuild library. The following methods are used to interact with forums:

create_forum_post
-----------------

.. code-block:: python

    bot.create_forum_post(channelid, title, content=None, embed=None)

Create a forum post with a specified title and optional content or embed.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the post is    |
|             |               |   in.                                      |
+-------------+---------------+--------------------------------------------+
| title       | str           | The title of the forum post.               |
+-------------+---------------+--------------------------------------------+
| content     | str, optional | Content of the forum post.                 |
+-------------+---------------+--------------------------------------------+
| embed       |Embed, optional|  Optional embed for the forum post.        |
+-------------+---------------+--------------------------------------------+

get_forum_topics
----------------

.. code-block:: python

    bot.get_forum_topics(channelid, before=None, limit=None)

Get a list of forum topics in a specified channel.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel to get topics from.  |
+-------------+---------------+--------------------------------------------+
| before      | str           | Get topics before a certain ID.            |
+-------------+---------------+--------------------------------------------+
| limit       | int           | Limit the number of topics returned.       |
+-------------+---------------+--------------------------------------------+

get_forum_topic
---------------

.. code-block:: python

    bot.get_forum_topic(channelid, forumtopicid)

Get a specific forum topic using the topic ID.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the topic is.  |
+-------------+---------------+--------------------------------------------+
| forumtopicid| str           | The ID of the forum topic to get.          |
+-------------+---------------+--------------------------------------------+

update_forum_topic
------------------

.. code-block:: python

    bot.update_forum_topic(channelid, forumtopicid, title=None, content=None, embed=None)

Update a forum topic with a new title, content, or embed.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the topic is.  |
+-------------+---------------+--------------------------------------------+
| forumtopicid| str           | The ID of the forum topic to update.       |
+-------------+---------------+--------------------------------------------+
| title       | str           | New title for the forum topic.             |
+-------------+---------------+--------------------------------------------+
| content     | str, optional | New content for the forum topic.           |
+-------------+---------------+--------------------------------------------+
| embed       |Embed, optional| New embed for the forum topic.             |
+-------------+---------------+--------------------------------------------+

delete_forum_topic
------------------

.. code-block:: python

    bot.delete_forum_topic(channelid, forumtopicid)

Delete a forum topic using the topic ID.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the topic is.  |
+-------------+---------------+--------------------------------------------+
| forumtopicid| str           | The ID of the forum topic to delete.       |


+-------------+---------------+--------------------------------------------+

pin_forum_topic
---------------

.. code-block:: python

    bot.pin_forum_topic(channelid, forumtopicid)

Pin a forum topic using the topic ID.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the topic is.  |
+-------------+---------------+--------------------------------------------+
| forumtopicid| str           | The ID of the forum topic to pin.          |
+-------------+---------------+--------------------------------------------+

unpin_forum_topic
-----------------

.. code-block:: python

    bot.unpin_forum_topic(channelid, forumtopicid)

Unpin a forum topic using the topic ID.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the topic is.  |
+-------------+---------------+--------------------------------------------+
| forumtopicid| str           | The ID of the forum topic to unpin.        |
+-------------+---------------+--------------------------------------------+

lock_forum_topic
----------------

.. code-block:: python

    bot.lock_forum_topic(channelid, forumtopicid)

Lock a forum topic using the topic ID.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the topic is.  |
+-------------+---------------+--------------------------------------------+
| forumtopicid| str           | The ID of the forum topic to lock.         |
+-------------+---------------+--------------------------------------------+

unlock_forum_topic
------------------

.. code-block:: python

    bot.unlock_forum_topic(channelid, forumtopicid)

Unlock a forum topic using the topic ID.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel where the topic is.  |
+-------------+---------------+--------------------------------------------+
| forumtopicid| str           | The ID of the forum topic to unlock.       |
+-------------+---------------+--------------------------------------------+

