create_listitem
---------------

.. code-block:: python

    bot.create_listitem(channelid, title, note=None)

Creates a new list item in the specified channel.

+-----------+---------+-------------------------------------------+
| Parameter | Type    | Description                               |
+===========+=========+===========================================+
| channelid | str     | The ID of the channel to create the item  |
+-----------+---------+-------------------------------------------+
| title     | str     | The title of the list item                |
+-----------+---------+-------------------------------------------+
| note      | str,    | A note for the list item                  |
|           | Optional|                                           |
+-----------+---------+-------------------------------------------+

get_listitem
------------

.. code-block:: python

    bot.get_listitem(channelid, listitemid)

Retrieves a list item from the specified channel.

+------------+------+--------------------------------------------+
| Parameter  | Type | Description                                |
+============+======+============================================+
| channelid  | str  | The ID of the channel containing the item  |
+------------+------+--------------------------------------------+
| listitemid | str  | The ID of the list item to retrieve        |
+------------+------+--------------------------------------------+

get_listitems
-------------

.. code-block:: python

    bot.get_listitems(channelid)

Retrieves all list items from the specified channel.

+-----------+------+--------------------------------------------------+
| Parameter | Type | Description                                      |
+===========+======+==================================================+
| channelid | str  | The ID of the channel containing the list items |
+-----------+------+--------------------------------------------------+


delete_listitem
---------------

.. code-block:: python

    bot.delete_listitem(channelid, listitemid)

Deletes a list item from the specified channel.

+------------+------+--------------------------------------------+
| Parameter  | Type | Description                                |
+============+======+============================================+
| channelid  | str  | The ID of the channel containing the item  |
+------------+------+--------------------------------------------+
| listitemid | str  | The ID of the list item to delete          |
+------------+------+--------------------------------------------+

update_listitem
---------------

.. code-block:: python

    bot.update_listitem(channelid, listitemid, title, note=None)

Updates a list item in the specified channel.


+-----------+---------+-------------------------------------------+
| Parameter | Type    | Description                               |
+===========+=========+===========================================+
| channelid | str     | The ID of the channel to create the item  |
+-----------+---------+-------------------------------------------+
| listitemid| str     | The title of the list item                |
+-----------+---------+-------------------------------------------+
| title     | str,    | The new title of the list item            |
+-----------+---------+-------------------------------------------+
|  note     | str,    |  A new note for the list item             |
|           | optional|                                           |
+-----------+---------+-------------------------------------------+

complete_listitem
-----------------

.. code-block:: python

    bot.complete_listitem(channelid, listitemid)

Marks a list item as complete in the specified channel.

+------------+------+--------------------------------------------+
| Parameter  | Type | Description                                |
+============+======+============================================+
| channelid  | str  | The ID of the channel containing the item  |
+------------+------+--------------------------------------------+
| listitemid | str  | The ID of the list item to be completed    |
+------------+------+--------------------------------------------+



uncomplete_listitem
-----------------

.. code-block:: python

    bot.uncomplete_listitem(channelid, listitemid)


+------------+------+--------------------------------------------+
| Parameter  | Type | Description                                |
+============+======+============================================+
| channelid  | str  | The ID of the channel containing the item  |
+------------+------+--------------------------------------------+
| listitemid | str  | The ID of the list item to be uncompleted  |
+------------+------+--------------------------------------------+




