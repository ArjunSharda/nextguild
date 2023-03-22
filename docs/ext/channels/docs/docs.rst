Docs
========

This section provides an overview of the document-related methods available in the NextGuild library. The following methods are used to interact with documents:

create_doc
------------

.. code-block:: python

    bot.create_doc(channelid, title, content)

Creates a doc in the specified channel.

+-------------+---------------+---------------------------------------------+
| Parameter   | Type          | Description                                 |
+=============+===============+=============================================+
| channelid   | str           | The ID of the channel to create the doc in. |
+-------------+---------------+---------------------------------------------+
| title       | str           | The title of the doc.                       |
+-------------+---------------+---------------------------------------------+
| content     | str           | The content of the doc.                     |
+-------------+---------------+---------------------------------------------+

update_doc
----------

.. code-block:: python

    bot.update_doc(channelid, docid, title, content)

Updates a doc in the specified channel.

+-------------+---------------+---------------------------------------------+
| Parameter   | Type          | Description                                 |
+=============+===============+=============================================+
| channelid   | str           | The ID of the channel to update the doc in. |
+-------------+---------------+---------------------------------------------+
| docid       | str           | The ID of the doc to update                 |
+-------------+---------------+---------------------------------------------+
| title       | str           | The title of the doc.                       |
+-------------+---------------+---------------------------------------------+
| content     | str           | The content of the doc.                     |
+-------------+---------------+---------------------------------------------+

delete_doc
------------

.. code-block:: python

    bot.delete_doc(channelid, docid)

Deletes a doc in the specified channel.

+-------------+---------------+---------------------------------------------+
| Parameter   | Type          | Description                                 |
+=============+===============+=============================================+
| channelid   | str           | The ID of the channel to update the doc in. |
+-------------+---------------+---------------------------------------------+
| docid       | str           | The ID of the doc to update                 |
+-------------+---------------+---------------------------------------------+

get_doc
--------------

.. code-block:: python

    bot.get_doc(channel_id, message_id)

Retrieves a doc in the specified channel.

+-------------+---------------+---------------------------------------------+
| Parameter   | Type          | Description                                 |
+=============+===============+=============================================+
| channelid   | str           | The ID of the channel to update the doc in. |
+-------------+---------------+---------------------------------------------+
| docid       | str           | The ID of the doc to update                 |
+-------------+---------------+---------------------------------------------+

get_docs
-----------

.. code-block:: python

    bot.get_docs(channel_id)

Retrieves all the docs in the specified channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channel_id  | str     | The ID of the channel to retrieve the    |
|             |         | docs from.                               |
+-------------+---------+------------------------------------------+
