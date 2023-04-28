Docs
========

This section provides an overview of the doc-related methods available in the NextGuild library. The following methods are used to interact with docs:

create_doc
-----------------

.. code-block:: python

    create_doc(channel_id, title, content)

Creates a doc in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to create the doc in |
+-------------------+---------+--------------------------------------------+
| title             | str     | The title of the doc                       |
+-------------------+---------+--------------------------------------------+
| content           | str     | The content of the doc                     |
+-------------------+---------+--------------------------------------------+

get_docs
-----------------

.. code-block:: python

    get_docs(channel_id, before, limit)

Gets a list of docs in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to get docs from      |
+-------------------+---------+---------------------------------------------+
| before            | str     | The date-time of when to get the docs before|
+-------------------+---------+---------------------------------------------+
| limit             | int     | The maximum number of docs to get           |
+-------------------+---------+---------------------------------------------+

get_doc
-----------------

.. code-block:: python

    get_doc(channel_id, doc_id)

Gets a doc in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to get the doc from   |
+-------------------+---------+---------------------------------------------+
| doc_id            | int     | The ID of the doc to get                    |
+-------------------+---------+---------------------------------------------+

update_doc
-----------------

.. code-block:: python

    update_doc(channel_id, doc_id, title, content)

Updates a doc in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to update the doc in  |
+-------------------+---------+---------------------------------------------+
| doc_id            | int     | The ID of the doc to update                 |
+-------------------+---------+---------------------------------------------+
| title             | str     | The title of the doc                        |
+-------------------+---------+---------------------------------------------+
| content           | str     | The content of the doc                      |
+-------------------+---------+---------------------------------------------+

delete_doc
-----------------

.. code-block:: python

    delete_doc(channel_id, doc_id)

Deletes a doc in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to delete the doc in  |
+-------------------+---------+---------------------------------------------+
| doc_id            | int     | The ID of the doc to delete                 |
+-------------------+---------+---------------------------------------------+

create_doc_comment
-----------------

.. code-block:: python

    create_doc_comment(channel_id, doc_id, content)

Creates a comment on a doc in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to create the comment |
+-------------------+---------+---------------------------------------------+
| doc_id            | int     | The ID of the doc to create the comment on  |
+-------------------+---------+---------------------------------------------+
| content           | str     | The content of the comment                  |
+-------------------+---------+---------------------------------------------+

update_doc_comment
-----------------

.. code-block:: python

    update_doc_comment(channel_id, doc_id, comment_id, content)

Updates a comment on a doc in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to update the comment |
+-------------------+---------+---------------------------------------------+
| doc_id            | int     | The ID of the doc to update the comment on  |
+-------------------+---------+---------------------------------------------+
| comment_id        | int     | The ID of the comment to update             |
+-------------------+---------+---------------------------------------------+
| content           | str     | The content of the comment                  |
+-------------------+---------+---------------------------------------------+

delete_doc_comment
-----------------

.. code-block:: python

    delete_doc_comment(channel_id, doc_id, comment_id)

Deletes a comment on a doc in the specified channel.

+-------------------+---------+---------------------------------------------+
| Parameter         | Type    | Description                                 |
+===================+=========+=============================================+
| channel_id        | str     | The ID of the channel to delete the comment |
+-------------------+---------+---------------------------------------------+
| doc_id            | int     | The ID of the doc to delete the comment on  |
+-------------------+---------+---------------------------------------------+
| comment_id        | int     | The ID of the comment to delete             |
+-------------------+---------+---------------------------------------------+
