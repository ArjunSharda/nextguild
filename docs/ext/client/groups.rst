Groups
========

This section provides an overview of the group-related methods available in the NextGuild library. The following methods are used to interact with groups:

create_group
------------

.. code-block:: python

    create_group(server_id, name, description, emote_id, is_public)

Creates a group.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to create the group   |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| name              | str     | The name of the group.                     |
+-------------------+---------+--------------------------------------------+
| description       | str     | The description of the group.              |
+-------------------+---------+--------------------------------------------+
| emote_id          | int,    | The ID of the emote to use for the group.  |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| is_public         | bool,   | Whether or not the group is public.        |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+

update_group
------------

.. code-block:: python

    update_group(server_id, group_id, name, description, emote_id, is_public)

Updates a group.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to update the group   |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| group_id          | str     | The ID of the group to update.             |
+-------------------+---------+--------------------------------------------+
| name              | str,    | The name of the group.                     |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| description       | str,    | The description of the group.              |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| emote_id          | int,    | The ID of the emote to use for the group.  |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| is_public         | bool,   | Whether or not the group is public.        |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+

delete_group
------------

.. code-block:: python

    delete_group(server_id, group_id)

Deletes a group.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to delete the group   |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| group_id          | str     | The ID of the group to delete.             |
+-------------------+---------+--------------------------------------------+

get_group
---------

.. code-block:: python

    get_group(server_id, group_id)

Gets a group.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the group      |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| group_id          | str     | The ID of the group to get.                |
+-------------------+---------+--------------------------------------------+

get_groups
----------

.. code-block:: python

    get_groups(server_id)

Gets all groups in a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the groups     |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+

add_group_member
-----------------

.. code-block:: python

    add_group_member(group_id, user_id)

Adds a member to a group.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| group_id          | str     | The ID of the group to add the member to.  |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to add to the group.    |
+-------------------+---------+--------------------------------------------+

remove_group_member
--------------------

.. code-block:: python

    remove_group_member(group_id, user_id)

Removes a member from a group.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| group_id          | str     | The ID of the group to remove the member   |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to remove from the      |
|                   |         | group.                                     |
+-------------------+---------+--------------------------------------------+