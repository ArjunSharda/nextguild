Lists
===========

This page provides an overview of the list events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_list_item_create
--------

.. code-block:: python

    @events.on_list_item_create
<<<<<<< Updated upstream
    async def example():
        print('A list item has been created!')
=======
    async def example(data):
        notedata = Data(data.note)
        print(f'A list item with content {data.content} has been created! The note attached to it has the content {notedata.content}!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the list item                 |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the list item                |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the list item was created           |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The ID of the user who created the list item,|
|                             | this will also contain createdByWebhookId    |
|                             | if the list item was created by a webhook    |
+-----------------------------+----------------------------------------------+
| ``data.parent_id``          | The ID of the parent list item if this list  |
|                             | item is nested                               |
+-----------------------------+----------------------------------------------+
| ``data.note``               | The note attached to the list item           |
+-----------------------------+----------------------------------------------+

Below is the data for the note attached to the list item.
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``notedata.created_at``     | The time the note was created                |
+-----------------------------+----------------------------------------------+
| ``notedata.created_by``       | The ID of the user who created the note,     |
|                             | this will also contain createdByWebhookId    |
|                             | if the note was created by a webhook         |
+-----------------------------+----------------------------------------------+
| ``notedata.content``        | The content of the note                      |
+-----------------------------+----------------------------------------------+
| ``notedata.mentions``       | The mentions in the note                     |
+-----------------------------+----------------------------------------------+

>>>>>>> Stashed changes

on_list_item_update
--------

.. code-block:: python

    @events.on_list_item_update
<<<<<<< Updated upstream
    async def example():
        print('A list item has been updated!')
=======
    async def example(data):
        notedata = Data(data.note)
        print(f'A list item with content {data.content} has been updated! The note attached to it has the content {notedata.content}!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the list item                 |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the list item                |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the list item was created           |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The ID of the user who created the list item,|
|                             | this will also contain createdByWebhookId    |
|                             | if the list item was created by a webhook    |
+-----------------------------+----------------------------------------------+
| ``data.updated_at``         | The time the list item was updated           |
+-----------------------------+----------------------------------------------+
| ``data.updated_by``         | The ID of the user who updated the list item |
+-----------------------------+----------------------------------------------+
| ``data.parent_id``          | The ID of the parent list item if this list  |
|                             | item is nested                               |
+-----------------------------+----------------------------------------------+
| ``data.completed_at``       | The time the list item was completed         |
+-----------------------------+----------------------------------------------+
| ``data.completed_by``       | The ID of the user who completed the list    |
|                             | item                                         |
+-----------------------------+----------------------------------------------+
| ``data.note``               | The note attached to the list item           |
+-----------------------------+----------------------------------------------+

Below is the data for the note attached to the list item.
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``notedata.created_at``     | The time the note was created                |
+-----------------------------+----------------------------------------------+
| ``notedata.created_by``     | The ID of the user who created the note,     |
|                             | this will also contain createdByWebhookId    |
|                             | if the note was created by a webhook         |
+-----------------------------+----------------------------------------------+
| ``notedata.updated_at``     | The time the note was updated                |
+-----------------------------+----------------------------------------------+
| ``notedata.updated_by``     | The ID of the user who updated the note      |
+-----------------------------+----------------------------------------------+
| ``notedata.content``        | The content of the note                      |
+-----------------------------+----------------------------------------------+
| ``notedata.mentions``       | The mentions in the note                     |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_list_item_delete
--------

.. code-block:: python

    @events.on_list_item_delete
<<<<<<< Updated upstream
    async def example():
        print('A list item has been deleted!')
=======
    async def example(data):
        notedata = Data(data.note)
        print(f'A list item with content {data.content} has been deleted! The note attached to it has the content {notedata.content}!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the list item                 |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the list item                |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the list item was created           |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The ID of the user who created the list item,|
|                             | this will also contain createdByWebhookId    |
|                             | if the list item was created by a webhook    |
+-----------------------------+----------------------------------------------+
| ``data.parent_id``          | The ID of the parent list item if this list  |
|                             | item is nested                               |
+-----------------------------+----------------------------------------------+
| ``data.note``               | The note attached to the list item           |
+-----------------------------+----------------------------------------------+

Below is the data for the note attached to the list item.
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``notedata.created_at``     | The time the note was created                |
+-----------------------------+----------------------------------------------+
| ``notedata.created_by``     | The ID of the user who created the note,     |
|                             | this will also contain createdByWebhookId    |
|                             | if the note was created by a webhook         |
+-----------------------------+----------------------------------------------+
| ``notedata.content``        | The content of the note                      |
+-----------------------------+----------------------------------------------+
| ``notedata.mentions``       | The mentions in the note                     |
+-----------------------------+----------------------------------------------+

>>>>>>> Stashed changes

on_list_item_complete
--------

.. code-block:: python

    @events.on_list_item_complete
<<<<<<< Updated upstream
    async def example():
        print('A list item has been completed!')
=======
    async def example(data):
        notedata = Data(data.note)
        print(f'A list item with content {data.content} has been completed! The note attached to it has the content {notedata.content}!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the list item                 |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the list item                |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the list item was created           |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The ID of the user who created the list item,|
|                             | this will also contain createdByWebhookId    |
|                             | if the list item was created by a webhook    |
+-----------------------------+----------------------------------------------+
| ``data.parent_id``          | The ID of the parent list item if this list  |
|                             | item is nested                               |
+-----------------------------+----------------------------------------------+
| ``data.note``               | The note attached to the list item           |
+-----------------------------+----------------------------------------------+

Below is the data for the note attached to the list item.
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``notedata.created_at``     | The time the note was created                |
+-----------------------------+----------------------------------------------+
| ``notedata.created_by``     | The ID of the user who created the note,     |
|                             | this will also contain createdByWebhookId    |
|                             | if the note was created by a webhook         |
+-----------------------------+----------------------------------------------+
| ``notedata.content``        | The content of the note                      |
+-----------------------------+----------------------------------------------+
| ``notedata.mentions``       | The mentions in the note                     |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes

on_list_item_uncomplete
--------

.. code-block:: python

    @events.on_list_item_uncomplete
<<<<<<< Updated upstream
    async def example():
        print('A list item has been uncompleted!')
=======
    async def example(data):
        notedata = Data(data.note)
        print(f'A list item with content {data.content} has been uncompleted! The note attached to it has the content {notedata.content}!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the list item                 |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the list item                |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the list item was created           |
+-----------------------------+----------------------------------------------+
| ``data.created_by``           | The ID of the user who created the list item,|
|                             | this will also contain createdByWebhookId    |
|                             | if the list item was created by a webhook    |
+-----------------------------+----------------------------------------------+
| ``data.parent_id``          | The ID of the parent list item if this list  |
|                             | item is nested                               |
+-----------------------------+----------------------------------------------+
| ``data.note``               | The note attached to the list item           |
+-----------------------------+----------------------------------------------+

Below is the data for the note attached to the list item.
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``notedata.created_at``     | The time the note was created                |
+-----------------------------+----------------------------------------------+
| ``notedata.created_by``     | The ID of the user who created the note,     |
|                             | this will also contain createdByWebhookId    |
|                             | if the note was created by a webhook         |
+-----------------------------+----------------------------------------------+
| ``notedata.content``        | The content of the note                      |
+-----------------------------+----------------------------------------------+
| ``notedata.mentions``       | The mentions in the note                     |
+-----------------------------+----------------------------------------------+
>>>>>>> Stashed changes
