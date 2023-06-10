Status
============

This section provides an overview of the status-related methods available in the NextGuild library. The following methods are used to interact with statuses:

update_status
-----------------

.. code-block:: python

    update_status(content, emote_id, expires_at)

Updates the bot's status.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| content           | str,    | The content of the status.                 |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| emote_id          | int,    | The ID of the emote to use.                |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| expires_at        | str,    | The time at which the status will expire.  |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+

delete_status
-----------------

.. code-block:: python

    delete_status()

Deletes the bot's status. No parameters.
