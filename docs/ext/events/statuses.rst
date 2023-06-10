Groups
===========

This page provides an overview of the group events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_user_status_create
---------------

.. code-block:: python

    @events.on_user_status_create
    async def on_user_status_create(data):
        print(f'A user with the id {data.user_id} has changed their status!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.expires_at``           | The time when the status expires.            |
+-----------------------------+----------------------------------------------+
| ``data.user_id``              | The id of the user who changed their status. |
+-----------------------------+----------------------------------------------+
| ``data.content``              | The content of the status.                   |
+-----------------------------+----------------------------------------------+
| ``data.emote_id``             | The id of the emote used in the status.      |
+-----------------------------+----------------------------------------------+

on_user_status_delete
---------------

.. code-block:: python

    @events.on_user_status_delete
    async def on_user_status_delete(data):
        print(f'A user with the id {data.user_id} has deleted their status!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.user_id``              | The id of the user who deleted their status. |
+-----------------------------+----------------------------------------------+
| ``data.content``              | The content of the status.                   |
+-----------------------------+----------------------------------------------+
| ``data.emote_id``             | The id of the emote used in the status.      |
+-----------------------------+----------------------------------------------+