Server
========

This section provides an overview of the server-related methods available in the NextGuild library. The following methods are used to interact with the servers:

get_server
----------

.. code-block:: python

    get_server(server_id)

Gets a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get.               |
+-------------------+---------+--------------------------------------------+

get_server_members
------------------

.. code-block:: python

    get_server_members(server_id)

Gets the members of a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the members    |
|                   |         | of.                                        |
+-------------------+---------+--------------------------------------------+

get_server_member
-----------------

.. code-block:: python

    get_server_member(server_id, user_id)

Gets a member of a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the member of. |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to get.                 |
+-------------------+---------+--------------------------------------------+