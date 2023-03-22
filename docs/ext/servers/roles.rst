Roles
=====


This section provides an overview of the role-related methods available in the NextGuild library. The following methods are used to interact with roles:


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
