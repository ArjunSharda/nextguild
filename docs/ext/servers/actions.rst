Actions
=======

This section describes various actions that can be performed using the provided methods.

update_nickname
---------------

.. code-block:: python

    bot.update_nickname(serverid, userid, nickname)

Updates the nickname of a member in the specified server.

+-----------+------+---------------------------------------------------+
| Parameter | Type | Description                                       |
+===========+======+===================================================+
| serverid  | str  | The ID of the server where the member is located |
+-----------+------+---------------------------------------------------+
| userid    | str  | The ID of the member whose nickname to update    |
+-----------+------+---------------------------------------------------+
| nickname  | str  | The new nickname for the member                   |
+-----------+------+---------------------------------------------------+

delete_nickname
---------------

.. code-block:: python

    bot.delete_nickname(serverid, userid)

Deletes the nickname of a member in the specified server.

+-----------+------+---------------------------------------------------+
| Parameter | Type | Description                                       |
+===========+======+===================================================+
| serverid  | str  | The ID of the server where the member is located |
+-----------+------+---------------------------------------------------+
| userid    | str  | The ID of the member whose nickname to delete    |
+-----------+------+---------------------------------------------------+

kick_member
-----------

.. code-block:: python

    bot.kick_member(serverid, userid)

Kicks a member from the specified server.

+-----------+------+----------------------------------------------+
| Parameter | Type | Description                                  |
+===========+======+==============================================+
| serverid  | str  | The ID of the server to kick the member from |
+-----------+------+----------------------------------------------+
| userid    | str  | The ID of the member to kick                 |
+-----------+------+----------------------------------------------+

ban_member
----------

.. code-block:: python

    bot.ban_member(serverid, userid)

Bans a member from the specified server.

+-----------+------+---------------------------------------------+
| Parameter | Type | Description                                 |
+===========+======+=============================================+
| serverid  | str  | The ID of the server to ban the member from |
+-----------+------+---------------------------------------------+
| userid    | str  | The ID of the member to ban                 |
+-----------+------+---------------------------------------------+

add_role
--------

.. code-block:: python

    bot.add_role(serverid, userid, roleid)

Adds a role to a member in the specified server.

+-----------+------+----------------------------------------------+
| Parameter | Type | Description                                  |
+===========+======+==============================================+
| serverid  | str  | The ID of the server where the member is located |
+-----------+------+----------------------------------------------+
| userid    | str  | The ID of the member to add the role to      |
+-----------+------+----------------------------------------------+
| roleid    | str  | The ID of the role to add                    |
+-----------+------+----------------------------------------------+

remove_role
-----------

.. code-block:: python

    bot.remove_role(serverid, userid, roleid)

Removes a role from a member in the specified server.

+-----------+------+----------------------------------------------+
| Parameter | Type | Description                                  |
+===========+======+==============================================+
| serverid  | str  | The ID of the server where the member is located |
+-----------+------+----------------------------------------------+
| userid    | str  | The ID of the member to remove the role from |
+-----------+------+----------------------------------------------+
| roleid    | str  | The ID of the role to remove                 |
+-----------+------+----------------------------------------------+


get_member_roles
----------------

.. code-block:: python

    bot.get_member_roles(serverid, userid)

Gets the roles of a member in the specified server.

+-----------+------+---------------------------------------------------+
| Parameter | Type | Description                                       |
+===========+======+===================================================+
| serverid  | str  | The ID of the server where the member is located |
+-----------+------+---------------------------------------------------+
| userid    | str  | The ID of the member whose roles to fetch        |
+-----------+------+---------------------------------------------------+

unban_member
------------

.. code-block:: python

    bot.unban_member(serverid, userid)

Unbans a member from the specified server.

+-----------+------+-----------------------------------------------+
| Parameter | Type | Description                                   |
+===========+======+===============================================+
| serverid  | str  | The ID of the server to unban the member from |
+-----------+------+-----------------------------------------------+
| userid    | str  | The ID of the member to unban                 |
+-----------+------+-----------------------------------------------+

get_member_ban
--------------

.. code-block:: python

    bot.get_member_ban(serverid, userid)

Gets the ban information for a member in the specified server.

+-----------+------+---------------------------------------------------+
| Parameter | Type | Description                                       |
+===========+======+===================================================+
| serverid  | str  | The ID of the server where the member is banned  |
+-----------+------+---------------------------------------------------+
| userid    | str  | The ID of the banned member                       |
+-----------+------+---------------------------------------------------+

get_member_bans
---------------

.. code-block:: python

    bot.get_member_bans(serverid)

Gets the ban information for all banned members in the specified server.

+-----------+------+------------------------------------------+
| Parameter | Type | Description                              |
+===========+======+==========================================+
| serverid  | str  | The ID of the server to fetch bans from  |
+-----------+------+------------------------------------------+
