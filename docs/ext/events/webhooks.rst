Webhooks
===========

This page provides an overview of the webhook events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_webhook_create
--------

.. code-block:: python

    @events.on_webhook_create
    async def example(data):
        print(f'A webhook with name {data.name} was created!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the webhook                        |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the webhook                      |
+-----------------------------+----------------------------------------------+
| ``data.avatar``             | The avatar of the webhook                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel the webhook            |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the webhook was created             |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the webhook             |
+-----------------------------+----------------------------------------------+
| ``data.token``              | The token of the webhook                     |
+-----------------------------+----------------------------------------------+


on_webhook_update
--------

.. code-block:: python

    @events.on_webhook_update
    async def example(data):
        print(f'A webhook with name {data.name} was updated!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the webhook                        |
+-----------------------------+----------------------------------------------+
| ``data.name``               | The name of the webhook                      |
+-----------------------------+----------------------------------------------+
| ``data.avatar``             | The avatar of the webhook                    |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel the webhook            |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the webhook was created             |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the webhook             |
+-----------------------------+----------------------------------------------+
| ``data.token``              | The token of the webhook                     |
+-----------------------------+----------------------------------------------+
