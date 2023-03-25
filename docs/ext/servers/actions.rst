Actions
=======

This section describes various actions that can be performed using the provided methods.

get_server
---------------

.. code-block:: python

    get_server(serverid)

Gets information from the specified server.

+-----------+------+---------------------------------------------------+
| Parameter | Type | Description                                       |
+===========+======+===================================================+
| serverid  | str  | The ID of the server to get                       |
+-----------+------+---------------------------------------------------+

get_server_members
---------------

.. code-block:: python

    get_server_members(serverid)

Gets the members in a specified server.

+-----------+------+---------------------------------------------------+
| Parameter | Type | Description                                       |
+===========+======+===================================================+
| serverid  | str  | The ID of the server to get the members from      |
+-----------+------+---------------------------------------------------+

get_server_member
---------------

.. code-block:: python

    get_server_member(serverid, memberid)

Gets the specified member in the specified server.

+-----------+------+---------------------------------------------------+
| Parameter | Type | Description                                       |
+===========+======+===================================================+
| serverid  | str  | The ID of the server to get the member from       |
+-----------+------+---------------------------------------------------+
| memberid  | str  | The ID of member to get                           |
+-----------+------+---------------------------------------------------+


update_nickname
---------------

.. code-block:: python

    update_nickname(serverid, userid, nickname)

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

    delete_nickname(serverid, userid)

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

    kick_member(serverid, userid)

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

    ban_member(serverid, userid)

Bans a member from the specified server.

+-----------+------+---------------------------------------------+
| Parameter | Type | Description                                 |
+===========+======+=============================================+
| serverid  | str  | The ID of the server to ban the member from |
+-----------+------+---------------------------------------------+
| userid    | str  | The ID of the member to ban                 |
+-----------+------+---------------------------------------------+



unban_member
------------

.. code-block:: python

    unban_member(serverid, userid)

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

    get_member_ban(serverid, userid)

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

    get_member_bans(serverid)

Gets the ban information for all banned members in the specified server.

+-----------+------+------------------------------------------+
| Parameter | Type | Description                              |
+===========+======+==========================================+
| serverid  | str  | The ID of the server to fetch bans from  |
+-----------+------+------------------------------------------+
