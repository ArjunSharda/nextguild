XP
==

This section provides an overview of the XP-related methods available in the NextGuild library. The following methods are used to manage XP:

award_xp
--------

.. code-block:: python

    bot.award_xp(serverid, userid, amount)

Awards XP to a member in the specified server.

+-----------+------+----------------------------------------+
| Parameter | Type | Description                            |
+===========+======+========================================+
| serverid  | str  | The ID of the server                   |
+-----------+------+----------------------------------------+
| userid    | str  | The ID of the member to award XP to    |
+-----------+------+----------------------------------------+
| amount    | int  | The amount of XP to award              |
+-----------+------+----------------------------------------+

get_xp
------

.. code-block:: python

    bot.get_xp(serverid, userid)

Gets the current XP of a member in the specified server.

+-----------+------+--------------------------------------+
| Parameter | Type | Description                          |
+===========+======+======================================+
| serverid  | str  | The ID of the server                 |
+-----------+------+--------------------------------------+
| userid    | str  | The ID of the member to get XP for   |
+-----------+------+--------------------------------------+

set_xp
------

.. code-block:: python

    bot.set_xp(serverid, userid, amount)

Sets the XP of a member in the specified server.

+-----------+------+--------------------------------------+
| Parameter | Type | Description                          |
+===========+======+======================================+
| serverid  | str  | The ID of the server                 |
+-----------+------+--------------------------------------+
| userid    | str  | The ID of the member to set XP for   |
+-----------+------+--------------------------------------+
| amount    | int  | The amount of XP to set              |
+-----------+------+--------------------------------------+

award_xp_to_role
----------------

.. code-block:: python

    bot.award_xp_to_role(serverid, roleid, amount)

Awards XP to all members with a specific role in the specified server.

+-----------+------+------------------------------------------+
| Parameter | Type | Description                              |
+===========+======+==========================================+
| serverid  | str  | The ID of the server                     |
+-----------+------+------------------------------------------+
| roleid    | str  | The ID of the role to award XP to       |
+-----------+------+------------------------------------------+
| amount    | int  | The amount of XP to award               |
+-----------+------+------------------------------------------+
