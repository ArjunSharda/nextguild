Lists
========

This section provides an overview of the list-related methods available in the NextGuild library. The following methods are used to interact with lists:

create_list_item
-----------------

.. code-block:: python

    create_list_item(channel_id, title, note)

Create a list-item in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to create the list-  |
|                   |         | item in.                                   |
+-------------------+---------+--------------------------------------------+
| title             | str     | The title of the list-item.                |
+-------------------+---------+--------------------------------------------+
| note              | str,    | The note of the list-item.                 |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+

update_list_item
-----------------

.. code-block:: python

    update_list_item(channel_id, list_item_id, message, note)

Update a list-item in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to update the list-  |
|                   |         | item in.                                   |
+-------------------+---------+--------------------------------------------+
| list_item_id      | str     | The ID of the list-item to update.         |
+-------------------+---------+--------------------------------------------+
| message           | str,    | The message of the list-item.              |
+-------------------+---------+--------------------------------------------+
| note              | str,    | The note of the list-item.                 |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+

delete_list_item
-----------------

.. code-block:: python

    delete_list_item(channel_id, list_item_id)

Delete a list-item in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to delete the list-  |
|                   |         | item in.                                   |
+-------------------+---------+--------------------------------------------+
| list_item_id      | str     | The ID of the list-item to delete.         |
+-------------------+---------+--------------------------------------------+

get_list_item
-------------

.. code-block:: python

    get_list_item(channel_id, list_item_id)

Get a list-item in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to get the list-item |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| list_item_id      | str     | The ID of the list-item to get.            |
+-------------------+---------+--------------------------------------------+

get_list_items
--------------

.. code-block:: python

    get_list_items(channel_id)

Get all list-items in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to get the list-     |
|                   |         | items from.                                |
+-------------------+---------+--------------------------------------------+

complete_list_item
------------------

.. code-block:: python

    complete_list_item(channel_id, list_item_id)

Complete a list-item in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to complete the list-|
|                   |         | item in.                                   |
+-------------------+---------+--------------------------------------------+
| list_item_id      | str     | The ID of the list-item to complete.       |
+-------------------+---------+--------------------------------------------+

uncomplete_list_item
--------------------

.. code-block:: python

    uncomplete_list_item(channel_id, list_item_id)

Uncomplete a list-item in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to uncomplete the    |
|                   |         | list-item in.                              |
+-------------------+---------+--------------------------------------------+
| list_item_id      | str     | The ID of the list-item to uncomplete.     |
+-------------------+---------+--------------------------------------------+