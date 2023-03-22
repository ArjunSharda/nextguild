Groups
======

This section describes the methods for managing group members.

add_group_member
----------------

.. code-block:: python

    bot.add_group_member(groupid, userid)

Adds a member to the specified group.

+-----------+------+--------------------------------------+
| Parameter | Type | Description                          |
+===========+======+======================================+
| groupid   | str  | The ID of the group                  |
+-----------+------+--------------------------------------+
| userid    | str  | The ID of the member to add          |
+-----------+------+--------------------------------------+

remove_group_member
-------------------

.. code-block:: python

    bot.remove_group_member(groupid, userid)

Removes a member from the specified group.

+-----------+------+----------------------------------------+
| Parameter | Type | Description                            |
+===========+======+========================================+
| groupid   | str  | The ID of the group                    |
+-----------+------+----------------------------------------+
| userid    | str  | The ID of the member to remove         |
+-----------+------+----------------------------------------+
