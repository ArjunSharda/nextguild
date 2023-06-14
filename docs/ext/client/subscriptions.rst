Subscriptions
============

This section provides an overview of the subscription related methods available in the NextGuild library. The following methods are used to interact with statuses:

get_subscription_tier
-----------------

.. code-block:: python

    get_subscription_tier(server_id, subscription_type)

Gets a subscription tier in a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the tier from. |
+-------------------+---------+--------------------------------------------+
| subscription_type | str     | The type of tier to get, case sensitive.   |
|                   |         | ``Gold``, ``Silver``, or ``Copper``        |
+-------------------+---------+--------------------------------------------+

get_subscription_tiers
-----------------

.. code-block:: python

    get_subscription_tiers(server_id)

Gets all subscription tiers in a server.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the tiers from.|
+-------------------+---------+--------------------------------------------+
