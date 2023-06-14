Users
======

This section provides an overview of the user-related methods available in the NextGuild library. The following methods are used to interact with users:

update_nickname
-----------------

.. code-block:: python

    update_nickname(server_id, user_id, nickname)

Updates the nickname of a user on a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | string  | The ID of the server to update the         |
|                   |         | nickname on.                               |
+-------------------+---------+--------------------------------------------+
| user_id           | string  | The ID of the user to update the nickname  |
|                   |         | of.                                        |
+-------------------+---------+--------------------------------------------+
| nickname          | string  | The new nickname of the user.              |
+-------------------+---------+--------------------------------------------+

delete_nickname
-----------------

.. code-block:: python

    delete_nickname(server_id, user_id)

Deletes the nickname of a user on a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | string  | The ID of the server to delete the         |
|                   |         | nickname on.                               |
+-------------------+---------+--------------------------------------------+
| user_id           | string  | The ID of the user to delete the nickname  |
|                   |         | of.                                        |
+-------------------+---------+--------------------------------------------+

kick_member
-----------------

.. code-block:: python

    kick_member(server_id, user_id)

Kicks a user from a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | string  | The ID of the server to kick the user from.|
+-------------------+---------+--------------------------------------------+
| user_id           | string  | The ID of the user to kick.                |
+-------------------+---------+--------------------------------------------+

ban_member
-----------------

.. code-block:: python

    ban_member(server_id, user_id)

Bans a user from a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | string  | The ID of the server to ban the user from. |
+-------------------+---------+--------------------------------------------+
| user_id           | string  | The ID of the user to ban.                 |
+-------------------+---------+--------------------------------------------+

unban_member
-----------------

.. code-block:: python

    unban_member(server_id, user_id)

Unbans a user from a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | string  | The ID of the server to unban the user     |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| user_id           | string  | The ID of the user to unban.               |
+-------------------+---------+--------------------------------------------+

get_member_ban
-----------------

.. code-block:: python

    get_member_ban(server_id, user_id)

Gets the ban information for a user on a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | string  | The ID of the server to get the ban        |
|                   |         | information from.                          |
+-------------------+---------+--------------------------------------------+
| user_id           | string  | The ID of the user to get the ban          |
|                   |         | information for.                           |
+-------------------+---------+--------------------------------------------+

get_user_servers
-----------------

.. code-block:: python

    get_user_servers(user_id)

Gets the servers that a user is a member of.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| user_id           | string  | The ID of the user to get the servers for. |
+-------------------+---------+--------------------------------------------+

member_is_owner
-----------------

.. code-block:: python

    member_is_owner(server_id, user_id)

Checks if a user is the owner of a server. Returns True or False.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | string  | The ID of the server to check the owner of.|
+-------------------+---------+--------------------------------------------+
| user_id           | string  | The ID of the user to check.               |
+-------------------+---------+--------------------------------------------+

get_member_permissions
-----------------

.. code-block:: python

    get_member_permissions(server_id, user_id, permissions)

Gets the permissions of a user on a server.