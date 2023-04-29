Roles
========

This section provides an overview of the role-related methods available in the NextGuild library. The following methods are used to interact with roles:

add_role
-----------------

.. code-block:: python

    add_role(server_id, user_id, role_id)

Adds a role to a user.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the role is     |
|                   |         | added.                                     |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to add the role to.     |
+-------------------+---------+--------------------------------------------+
| role_id           | str     | The ID of the role to add to the user.     |
+-------------------+---------+--------------------------------------------+

remove_role
-----------------

.. code-block:: python

    remove_role(server_id, user_id, role_id)

Removes a role from a user.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the role is     |
|                   |         | removed.                                   |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to remove the role      |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| role_id           | str     | The ID of the role to remove from the      |
|                   |         | user.                                      |
+-------------------+---------+--------------------------------------------+

get_member_roles
-----------------

.. code-block:: python

    get_member_roles(server_id, user_id)

Returns a list of roles that a user has.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the user is     |
|                   |         | located.                                   |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to get the roles of.    |
+-------------------+---------+--------------------------------------------+