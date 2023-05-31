Social Links
===========

This page provides an overview of the social link events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_member_social_create
--------

.. code-block:: python

    @events.on_member_social_create
    async def example(data):
        print(f"{data.handle} just got added to {data.user_id}'s social links!")

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.type``               | The type of social link created.             |
+-----------------------------+----------------------------------------------+
| ``data.user_id``            | The ID of the user who created the social    |
|                             | link.                                        |
+-----------------------------+----------------------------------------------+
| ``data.handle``             | The handle of the social link created.       |
+-----------------------------+----------------------------------------------+
| ``data.service_id``         | The ID that represents the user's social link|
|                             | within the external service                  |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the social link was created.        |
+-----------------------------+----------------------------------------------+

on_member_social_update
--------

.. code-block:: python

    @events.on_member_social_update
    async def example(data):
        print(f"{data.handle} just got updated for {data.user_id}'s social links!")

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.type``               | The type of social link updated.             |
+-----------------------------+----------------------------------------------+
| ``data.user_id``            | The ID of the user who updated the social    |
|                             | link.                                        |
+-----------------------------+----------------------------------------------+
| ``data.handle``             | The handle of the social link updated.       |
+-----------------------------+----------------------------------------------+
| ``data.service_id``         | The ID that represents the user's social link|
|                             | within the external service                  |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the social link was updated.        |
+-----------------------------+----------------------------------------------+

on_member_social_delete
--------

.. code-block:: python

    @events.on_member_social_delete
    async def example(data):
        print(f"{data.handle} just got deleted from {data.user_id}'s social links!")

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.type``               | The type of social link deleted.             |
+-----------------------------+----------------------------------------------+
| ``data.user_id``            | The ID of the user who deleted the social    |
|                             | link.                                        |
+-----------------------------+----------------------------------------------+
| ``data.handle``             | The handle of the social link deleted.       |
+-----------------------------+----------------------------------------------+
| ``data.service_id``         | The ID that represents the user's social link|
|                             | within the external service                  |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the social link was deleted.        |
+-----------------------------+----------------------------------------------+
