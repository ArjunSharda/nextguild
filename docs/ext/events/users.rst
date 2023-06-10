Users
===========

This page provides an overview of the user events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_member_join
--------

.. code-block:: python

    @events.on_member_join
    async def example(data):
        print(f'{data.name} joined the server!')

+-----------------------------+------------------------------------------------+
| Type                        | Description                                    |
+=============================+================================================+
| ``data.server_id``          | The ID of the server the user joined.          |
+-----------------------------+------------------------------------------------+
| ``data.id``                 | The ID of the user that joined.                |
+-----------------------------+------------------------------------------------+
| ``data.type``               | The type of user                               |
+-----------------------------+------------------------------------------------+
| ``data.name``               | The name of the user                           |
+-----------------------------+------------------------------------------------+
| ``data.avatar``             | The avatar of the user                         |
+-----------------------------+------------------------------------------------+
| ``data.banner``             | The banner of the user                         |
+-----------------------------+------------------------------------------------+
| ``data.created_at``         | The date the user account was created          |
+-----------------------------+------------------------------------------------+
| ``data.status``             | The status of the user                         |
+-----------------------------+------------------------------------------------+
| ``data.status_emote``       | The emote that the user has as its status      |
+-----------------------------+------------------------------------------------+

on_member_leave
--------

.. code-block:: python

    @events.on_member_leave
    async def example(data):
        print(f'{data.id} left the server!')

+-----------------------------+------------------------------------------------+
| Type                        | Description                                    |
+=============================+================================================+
| ``data.server_id``          | The ID of the server the user left.            |
+-----------------------------+------------------------------------------------+
| ``data.id``                 | The ID of the user that left.                  |
+-----------------------------+------------------------------------------------+
| ``data.is_kick``            | Whether the user was kicked or not.            |
+-----------------------------+------------------------------------------------+
| ``data.is_ban``             | Whether the user was banned or not.            |
+-----------------------------+------------------------------------------------+

on_member_banned
--------

.. code-block:: python

    @events.on_member_banned
    async def example(data):
        print(f'{data.name} was banned from the server!')

+-----------------------------+------------------------------------------------+
| Type                        | Description                                    |
+=============================+================================================+
| ``data.server_id``          | The ID of the server the user was banned from. |
+-----------------------------+------------------------------------------------+
| ``data.id``                 | The ID of the user that was banned.            |
+-----------------------------+------------------------------------------------+
| ``data.type``               | The type of user                               |
+-----------------------------+------------------------------------------------+
| ``data.name``               | The name of the user                           |
+-----------------------------+------------------------------------------------+
| ``data.avatar``             | The avatar of the user                         |
+-----------------------------+------------------------------------------------+
| ``data.reason``             | The reason the user was banned                 |
+-----------------------------+------------------------------------------------+
| ``data.created_by``         | The ID of the user that banned the user        |
+-----------------------------+------------------------------------------------+
| ``data.created_at``         | The time the user was banned                   |
+-----------------------------+------------------------------------------------+

on_member_unbanned
--------

.. code-block:: python

    @events.on_member_unbanned
    async def example(data):
        print(f'{data.name} was unbanned from the server!')

+-----------------------------+------------------------------------------------+
| Type                        | Description                                    |
+=============================+================================================+
| ``data.server_id``          | The ID of the server the user was unbanned from|
+-----------------------------+------------------------------------------------+
| ``data.id``                 | The ID of the user that was unbanned.          |
+-----------------------------+------------------------------------------------+
| ``data.type``               | The type of user                               |
+-----------------------------+------------------------------------------------+
| ``data.name``               | The name of the user                           |
+-----------------------------+------------------------------------------------+
| ``data.avatar``             | The avatar of the user                         |
+-----------------------------+------------------------------------------------+
| ``data.reason``             | The reason the user was previously banned      |
+-----------------------------+------------------------------------------------+
| ``data.created_by``         | The ID of the user that banned the user        |
+-----------------------------+------------------------------------------------+
| ``data.created_at``         | The time the user was banned                   |
+-----------------------------+------------------------------------------------+

on_member_updated
--------

.. code-block:: python

    @events.on_member_updated
    async def example(data):
        print(f'{data.name} updated their profile!')

+-----------------------------+------------------------------------------------+
| Type                        | Description                                    |
+=============================+================================================+
| ``data.server_id``          | The ID of the server the user updated their    |
|                             | profile in.                                    |
+-----------------------------+------------------------------------------------+
| ``data.id``                 | The ID of the user whos profile was updated    |
+-----------------------------+------------------------------------------------+
| ``data.nickname``           | The new nickname of the user                   |
+-----------------------------+------------------------------------------------+
=======
    @events.on_member_update
    async def example():
        print('A member was updated!')
