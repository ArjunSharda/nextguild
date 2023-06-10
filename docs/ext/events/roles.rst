Roles
===========

This page provides an overview of the specific role events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_role_create
--------------

.. code-block:: python

    @events.on_role_create
    async def example(data):
        print(f'A role with id {data.id} was created!')

+-------------------------------+----------------------------------------------+
| Type                          | Description                                  |
+===============================+==============================================+
| `data.server_id`              | The ID of the server                         |
+-------------------------------+----------------------------------------------+
| `data.id`                     | The ID of the role                           |
+-------------------------------+----------------------------------------------+
| `data.created_at`             | The time the role was created                |
+-------------------------------+----------------------------------------------+
| `data.name`                   | The name of the role                         |
+-------------------------------+----------------------------------------------+
| `data.is_displayed_separately`| Whether the role is displayed separately     |
+-------------------------------+----------------------------------------------+
| `data.is_self_assignable`     | Whether the role is self assignable          |
+-------------------------------+----------------------------------------------+
| `data.is_mentionable`         | Whether the role is mentionable              |
+-------------------------------+----------------------------------------------+
| `data.permissions`            | The permissions of the role                  |
+-------------------------------+----------------------------------------------+
| `data.colors`                 | The colors of the role                       |
+-------------------------------+----------------------------------------------+
| `data.icon`                   | The icon URL of the role                     |
+-------------------------------+----------------------------------------------+
| `data.position`               | The position of the role                     |
+-------------------------------+----------------------------------------------+
| `data.is_base`                | Whether the role is the base role            |
+-------------------------------+----------------------------------------------+
| `data.bot_user_id`            | The bot user ID this role has been defined   |
|                               | for. Roles with this populated can only be   |
|                               | deleted by kicking the bot                   |
+-------------------------------+----------------------------------------------+

on_role_update 
--------------

.. code-block:: python

    @events.on_role_update
    async def example(data):
        print(f'The role with id {data.id} was updated!')

+-------------------------------+----------------------------------------------+
| Type                          | Description                                  |
+===============================+==============================================+
| `data.server_id`              | The ID of the server                         |
+-------------------------------+----------------------------------------------+
| `data.id`                     | The ID of the role                           |
+-------------------------------+----------------------------------------------+
| `data.created_at`             | The time the role was created                |
+-------------------------------+----------------------------------------------+
| `data.updated_at`             | The time the role was updated                |
+-------------------------------+----------------------------------------------+
| `data.name`                   | The name of the role                         |
+-------------------------------+----------------------------------------------+
| `data.is_displayed_separately`| Whether the role is displayed separately     |
+-------------------------------+----------------------------------------------+
| `data.is_self_assignable`     | Whether the role is self assignable          |
+-------------------------------+----------------------------------------------+
| `data.is_mentionable`         | Whether the role is mentionable              |
+-------------------------------+----------------------------------------------+
| `data.permissions`            | The permissions of the role                  |
+-------------------------------+----------------------------------------------+
| `data.colors`                 | The colors of the role                       |
+-------------------------------+----------------------------------------------+
| `data.icon`                   | The icon URL of the role                     |
+-------------------------------+----------------------------------------------+
| `data.position`               | The position of the role                     |
+-------------------------------+----------------------------------------------+
| `data.is_base`                | Whether the role is the base role            |
+-------------------------------+----------------------------------------------+
| `data.bot_user_id`            | The bot user ID this role has been defined   |
|                               | for. Roles with this populated can only be   |
|                               | deleted by kicking the bot                   |
+-------------------------------+----------------------------------------------+

on_role_delete
--------------

.. code-block:: python

    @events.on_role_delete
    async def example(data):
        print(f'The role with id {data.id} was deleted!')

+-------------------------------+----------------------------------------------+
| Type                          | Description                                  |
+===============================+==============================================+
| `data.server_id`              | The ID of the server                         |
+-------------------------------+----------------------------------------------+
| `data.id`                     | The ID of the role                           |
+-------------------------------+----------------------------------------------+
| `data.created_at`             | The time the role was created                |
+-------------------------------+----------------------------------------------+
| `data.name`                   | The name of the role                         |
+-------------------------------+----------------------------------------------+
| `data.is_displayed_separately`| Whether the role is displayed separately     |
+-------------------------------+----------------------------------------------+
| `data.is_self_assignable`     | Whether the role is self assignable          |
+-------------------------------+----------------------------------------------+
| `data.is_mentionable`         | Whether the role is mentionable              |
+-------------------------------+----------------------------------------------+
| `data.permissions`            | The permissions of the role                  |
+-------------------------------+----------------------------------------------+
| `data.colors`                 | The colors of the role                       |
+-------------------------------+----------------------------------------------+
| `data.icon`                   | The icon URL of the role                     |
+-------------------------------+----------------------------------------------+
| `data.position`               | The position of the role                     |
+-------------------------------+----------------------------------------------+
| `data.is_base`                | Whether the role is the base role            |
+-------------------------------+----------------------------------------------+
| `data.bot_user_id`            | The bot user ID this role has been defined   |
|                               | for. Roles with this populated can only be   |
|                               | deleted by kicking the bot                   |
+-------------------------------+----------------------------------------------+

on_roles_updated
--------

.. code-block:: python

    @events.on_roles_updated
    async def example(data):
        print(f'{data.role_ids}')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.role_ids`             | A list of the members that was updated along |
|                             | with their role IDs                          |
+-----------------------------+----------------------------------------------+