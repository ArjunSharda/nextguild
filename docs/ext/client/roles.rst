Roles
========

This section provides an overview of the role-related methods available in the NextGuild library. The following methods are used to interact with roles:

create_role
-----------------

.. code-block:: python

    create_role(server_id, name, is_displayed_separately, is_self_assignable, is_mentionable, permissions, color)

Creates a role on a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to create the role    |
|                   |         | on.                                        |
+-------------------+---------+--------------------------------------------+
| name              | str     | The name of the role.                      |
+-------------------+---------+--------------------------------------------+
| is_displayed_     | bool,   | Whether or not the role is displayed       |
| separately        | optional| separately from other users.               |
+-------------------+---------+--------------------------------------------+
| is_self_assignable| bool,   | Whether or not the role is self-assignable.|
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| is_mentionable    | bool,   | Whether or not the role is mentionable.    |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| permissions       | list,   | The permissions of the role.               |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| color             | list,   | The color of the role.                     |
|                   | optional| (two values for a gradient color)          |
+-------------------+---------+--------------------------------------------+

update_role
-----------------

.. code-block:: python

    update_role(server_id, role_id, name, is_displayed_separately, is_self_assignable, is_mentionable, permissions, color)

Updates a role on a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the role is     |
|                   |         | located.                                   |
+-------------------+---------+--------------------------------------------+
| role_id           | int     | The ID of the role to update.              |
+-------------------+---------+--------------------------------------------+
| name              | str,    | The name of the role.                      |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| is_displayed_     | bool,   | Whether or not the role is displayed       |
| separately        | optional| separately from other users.               |
+-------------------+---------+--------------------------------------------+
| is_self_assignable| bool,   | Whether or not the role is self-assignable.|
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| is_mentionable    | bool,   | Whether or not the role is mentionable.    |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| permissions       | list,   | The permissions of the role.               |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| color             | list,   | The color of the role.                     |
|                   | optional| (two values for a gradient color)          |
+-------------------+---------+--------------------------------------------+

delete_role
-----------------

.. code-block:: python

    delete_role(server_id, role_id)

Deletes a role from a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the role is     |
|                   |         | located.                                   |
+-------------------+---------+--------------------------------------------+
| role_id           | int     | The ID of the role to delete.              |
+-------------------+---------+--------------------------------------------+


get_role
-----------------

.. code-block:: python

    get_role(server_id, role_id)

Returns a role object.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the role is     |
|                   |         | located.                                   |
+-------------------+---------+--------------------------------------------+
| role_id           | int     | The ID of the role to get.                 |
+-------------------+---------+--------------------------------------------+

get_roles
-----------------

.. code-block:: python

    get_roles(server_id)

Returns a list of role objects for a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the roles of.  |
+-------------------+---------+--------------------------------------------+

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
| role_id           | int     | The ID of the role to add to the user.     |
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
| role_id           | int     | The ID of the role to remove from the      |
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

member_has_role
-----------------

.. code-block:: python

    member_has_role(server_id, user_id, role_id, type)

Returns True if a user has a role, False otherwise. This accepts both lists and integers for the role_id parameter.
If you pass a list of role IDs, the type is defaulted to ``any``.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server where the user is     |
|                   |         | located.                                   |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to check the roles of.  |
+-------------------+---------+--------------------------------------------+
| role_id           | int,    | The ID of the role(s) to check for.        |
|                   | list    |                                            |
+-------------------+---------+--------------------------------------------+
| type              | str,    | The type of check to perform. Valid        |
|                   | optional| options are ``any`` and ``all``.           |
+-------------------+---------+--------------------------------------------+