Users
================

This section provides an overview of the user-related methods available in the NextGuild library. The following methods are used to interact with users:

Get Social Link
------------

.. code-block:: python

    get_social_link(userid, type)

+-----------+------+-------------------------------------+
| Parameter | Type | Description                         |
+===========+======+=====================================+
| userid    | str  | The ID of the user                  |
+-----------+------+-------------------------------------+
| type      | str  | The type of the social link         |
+-----------+------+-------------------------------------+

These are the available types:

+---------------------+------------------------+
| Social Link         | Type                   |
+=====================+========================+
| Twitch              | ``twitch``             |
+---------------------+------------------------+
| Battle.net          | ``bnet``               |
+---------------------+------------------------+
| Playstation Network | ``psn``                |
+---------------------+------------------------+
| Xbox                | ``xbox``               |
+---------------------+------------------------+
| Steam               | ``steam``              |
+---------------------+------------------------+
| Origin              | ``origin``             |
+---------------------+------------------------+
| Youtube             | ``youtube``            |
+---------------------+------------------------+
| Twitter             | ``twitter``            |
+---------------------+------------------------+
| Facebook            | ``facebook``           |
+---------------------+------------------------+
| Nintento Switch     | ``switch``             |
+---------------------+------------------------+
| Patreon             | ``patreon``            |
+---------------------+------------------------+
| Roblox              | ``roblox``             |
+---------------------+------------------------+
| Epic Games          | ``epic``               |
+---------------------+------------------------+

Get Bot User ID
------------

.. code-block:: python

   get_bot_user_id()
   
Gets the user id of the bot. No parameters

Get User's Servers
------------

.. code-block:: python

   get_user_servers(userid)
   
Gets all the servers that the specified user is in. Currently the bot can only get the servers that itself is in.

+-----------+------+-------------------------------------+
| Parameter | Type | Description                         |
+===========+======+=====================================+
| userid    | str  | The ID of the user                  |
+-----------+------+-------------------------------------+


Get Bot's Servers
------------

.. code-block:: python

   get_bot_servers()
   

Gets all the servers that the bot is in. No parameters.
 
