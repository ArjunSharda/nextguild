Roles
===========

This page provides an overview of the specific role events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_roles_updated
--------

.. code-block:: python

    @events.on_roles_updated
    async def example(data):
        print(f'{data.role_ids}')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.role_ids``           | A list of the members that was updated along |
|                             | with their role IDs                          |
+-----------------------------+----------------------------------------------+