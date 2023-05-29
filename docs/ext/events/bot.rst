Bot
===========

This page provides an overview of the specific bot events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_bot_membership_created
--------

.. code-block:: python

    @events.on_bot_membership_created
    async def example(data):
        print(f'The bot has joined {data.name}!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
|``data.created_by``          | The ID of the user that added the bot        |
+-----------------------------+----------------------------------------------+
|``data.server_id``           | The ID of the server the bot was added to    |
+-----------------------------+----------------------------------------------+
|``data.owner_id``            | The ID of the server owner                   |
+-----------------------------+----------------------------------------------+
|``data.name``                | The name of the server                       |
+-----------------------------+----------------------------------------------+
|``data.type``                | The type of server                           |
+-----------------------------+----------------------------------------------+
|``data.url``                 | The URL of the server                        |
+-----------------------------+----------------------------------------------+
|``data.about``               | The icon of the server                       |
+-----------------------------+----------------------------------------------+
|``data.avatar``              | The icon of the server                       |
+-----------------------------+----------------------------------------------+
|``data.banner``              | The banner of the server                     |
+-----------------------------+----------------------------------------------+
|``data.timezone``            | The timezone of the server                   |
+-----------------------------+----------------------------------------------+
|``data.is_verified``         | Whether the server is verified or not        |
+-----------------------------+----------------------------------------------+
|``data.default_channel_id``  | The ID of the default channel                |
+-----------------------------+----------------------------------------------+
|``data.created_at``          | The time the server was created              |
+-----------------------------+----------------------------------------------+


on_bot_membership_deleted
--------

.. code-block:: python

    @events.on_bot_membership_deleted
    async def example(data):
        print(f'The bot has left {data.name}!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
|``data.deleted_by``          | The ID of the user that removed the bot      |
+-----------------------------+----------------------------------------------+
|``data.server_id``           | The ID of the server the bot was removed from|
+-----------------------------+----------------------------------------------+
|``data.owner_id``            | The ID of the server owner                   |
+-----------------------------+----------------------------------------------+
|``data.name``                | The name of the server                       |
+-----------------------------+----------------------------------------------+
|``data.type``                | The type of server                           |
+-----------------------------+----------------------------------------------+
|``data.url``                 | The URL of the server                        |
+-----------------------------+----------------------------------------------+
|``data.about``               | The icon of the server                       |
+-----------------------------+----------------------------------------------+
|``data.avatar``              | The icon of the server                       |
+-----------------------------+----------------------------------------------+
|``data.banner``              | The banner of the server                     |
+-----------------------------+----------------------------------------------+
|``data.timezone``            | The timezone of the server                   |
+-----------------------------+----------------------------------------------+
|``data.is_verified``         | Whether the server is verified or not        |
+-----------------------------+----------------------------------------------+
|``data.default_channel_id``  | The ID of the default channel                |
+-----------------------------+----------------------------------------------+
|``data.created_at``          | The time the server was created              |
+-----------------------------+----------------------------------------------+
