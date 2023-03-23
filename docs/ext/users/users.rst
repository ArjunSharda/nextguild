Users
----------------
This section provides an overview of the user-related methods available in the NextGuild library. The following methods are used to interact with users:

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
+--------------------+-----------------------+
|Social link         |Type                   |
+====================+=======================+
|Twitch              |twitch                 |
+--------------------+-----------------------+
|Battle.net          |bnet                   |
+--------------------+-----------------------+
|Playstation Network |psn                    |
+--------------------+-----------------------+
|Xbox                |xbox                   |
+--------------------+-----------------------+
|Steam               |steam                  |
+--------------------+-----------------------+
|Origin              |origin                 |
+--------------------+-----------------------+
|Youtube             |youtube                |
+--------------------+-----------------------+
|Twitter             |twitter                |
+--------------------+-----------------------+
|Facebook            |facebook               |
+--------------------+-----------------------+
|Nintento Switch     |switch                 |
+--------------------+-----------------------+
|Patreon             |patreon                |
+--------------------+-----------------------+
|Roblox              |roblox                 |
+--------------------+-----------------------+
|Epic Games          |epic                   |
+--------------------+-----------------------+



.. code-block:: python

   get_bot_user_id()
   
Gets the user id of the bot. No parameters
 
