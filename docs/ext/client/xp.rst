XP
========

This section provides an overview of the xp-related methods available in the NextGuild library. The following methods are used to interact with xp:

award_xp
-----------------

.. code-block:: python

    award_xp(server_id, user_id, amount)

Awards XP to a member of a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to award XP in.       |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to award XP to.         |
+-------------------+---------+--------------------------------------------+
| amount            | int     | The amount of XP to award.                 |
+-------------------+---------+--------------------------------------------+

get_xp
-----------------

.. code-block:: python

    get_xp(server_id, user_id)

Gets the amount of XP a member of a server has.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the user is     |
|                   |         | located.                                   |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to get the XP from.     |
+-------------------+---------+--------------------------------------------+

set_xp
-----------------

.. code-block:: python

    set_xp(server_id, user_id, amount)

Sets the amount of XP a member of a server has.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the user is     |
|                   |         | located.                                   |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to set the XP for.      |
+-------------------+---------+--------------------------------------------+
| amount            | int     | The amount of XP to set.                   |
+-------------------+---------+--------------------------------------------+

set_bulk_xp
-----------------

.. code-block:: python

    set_bulk_xp(server_id, user_ids, amount)

Sets the amount of XP for multiple members.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the user is     |
|                   |         | located.                                   |
+-------------------+---------+--------------------------------------------+
| user_ids          | list    | The IDs of the users to set the XP for.    |
+-------------------+---------+--------------------------------------------+
| amount            | int     | The amount of XP to set.                   |
+-------------------+---------+--------------------------------------------+

award_xp_to_role
-----------------

.. code-block:: python

    award_xp_to_role(server_id, role_id, amount)

Awards XP to all members of a role in a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to award XP in.       |
+-------------------+---------+--------------------------------------------+
| role_id           | int     | The ID of the role to award XP to.         |
+-------------------+---------+--------------------------------------------+
| amount            | int     | The amount of XP to award.                 |
+-------------------+---------+--------------------------------------------+
