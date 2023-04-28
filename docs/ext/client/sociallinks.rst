Social Links
============

This section provides an overview of the social-link-related methods available in the NextGuild library. The following methods are used to interact with social links:

get_social_link
-----------------

.. code-block:: python

    get_social_link(user_id, link_type)

Gets the social link from a user

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| user_id           | string  | The user ID of the user to get the link    |
+-------------------+---------+--------------------------------------------+
| link_type         | string  | The type of link to get                    |
+-------------------+---------+--------------------------------------------+

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