Groups
========

This section provides an overview of the group-related methods available in the NextGuild library. The following methods are used to interact with groups:

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