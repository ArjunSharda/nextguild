Docs
===========

This page provides an overview of the doc events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)


on_doc_create 
--------

.. code-block:: python

    @events.on_doc_create
    async def example(data):
        print(f'A doc with name {data.name} was created!')
    
+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the doc                            |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the doc                         |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the doc                       |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the doc                      |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the doc was created                 |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the doc                 |
+-----------------------------+----------------------------------------------+


on_doc_update
--------

.. code-block:: python

    @events.on_doc_update
    async def example(data):
        print(f'A doc with name {data.name} was updated!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the doc                            |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the doc                         |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the doc                       |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the doc                      |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the doc was created                 |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the doc                 |
+-----------------------------+----------------------------------------------+
| ``data.updated_at``         | The time the doc was updated                 |
+-----------------------------+----------------------------------------------+
| ``data.updated_by``         | The user who updated the doc                 |
+-----------------------------+----------------------------------------------+

on_doc_delete
--------

.. code-block:: python

    @events.on_doc_delete
    async def example(data):
        print(f'A doc with name {data.name} was deleted!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the doc                            |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.title``              | The title of the doc                         |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the doc                       |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the doc                      |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the doc was created                 |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the doc                 |
+-----------------------------+----------------------------------------------+

on_doc_comment_create
--------

.. code-block:: python

    @events.on_doc_comment_create
    async def example(data):
        print(f'A doc comment with content {data.content} was created!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the doc comment                    |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the doc comment               |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the doc comment was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the doc comment         |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.doc_id``             | The ID of the doc                            |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the doc comment              |
+-----------------------------+----------------------------------------------+

on_doc_comment_update
--------

.. code-block:: python

    @events.on_doc_comment_update
    async def example(data):
        print(f'A doc comment with content {data.content} was updated!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the doc comment                    |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the doc comment               |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the doc comment was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the doc comment         |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.doc_id``             | The ID of the doc                            |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the doc comment              |
+-----------------------------+----------------------------------------------+
| ``data.updated_at``         | The time the doc comment was updated         |
+-----------------------------+----------------------------------------------+

on_doc_comment_delete
--------

.. code-block:: python

    @events.on_doc_comment_delete
    async def example(data):
        print(f'A doc comment with content {data.content} was deleted!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| ``data.server_id``          | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| ``data.id``                 | The ID of the doc comment                    |
+-----------------------------+----------------------------------------------+
| ``data.content``            | The content of the doc comment               |
+-----------------------------+----------------------------------------------+
| ``data.created_at``         | The time the doc comment was created         |
+-----------------------------+----------------------------------------------+
| ``data.created_by``         | The user who created the doc comment         |
+-----------------------------+----------------------------------------------+
| ``data.channel_id``         | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| ``data.doc_id``             | The ID of the doc                            |
+-----------------------------+----------------------------------------------+
| ``data.mentions``           | The mentions in the doc comment              |
+-----------------------------+----------------------------------------------+




