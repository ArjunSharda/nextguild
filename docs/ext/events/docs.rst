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
    async def example():
        print('A doc was created!')

on_doc_update
--------

.. code-block:: python

    @events.on_doc_update
    async def example():
        print('A doc was updated!')

on_doc_delete
--------

.. code-block:: python

    @events.on_doc_delete
    async def example():
        print('A doc was deleted!')

on_doc_comment_create
--------

.. code-block:: python

    @events.on_doc_comment_create
    async def example():
        print('A doc comment was created!')

on_doc_comment_update
--------

.. code-block:: python

    @events.on_doc_comment_update
    async def example():
        print('A doc comment was updated!')

on_doc_comment_delete
--------

.. code-block:: python

    @events.on_doc_comment_delete
    async def example():
        print('A doc comment was deleted!')

on_doc_reaction_create
--------

.. code-block:: python

    @events.on_doc_reaction_create
    async def example():
        print('A reaction was created on a doc!')

on_doc_reaction_delete
--------

.. code-block:: python

    @events.on_doc_reaction_delete
    async def example():
        print('A reaction was deleted on a doc!')

on_doc_comment_reaction_create
--------

.. code-block:: python

    @events.on_doc_comment_reaction_create
    async def example():
        print('A reaction was created on a doc comment!')

on_doc_comment_reaction_delete
--------

.. code-block:: python

    @events.on_doc_comment_reaction_delete
    async def example():
        print('A reaction was deleted on a doc comment!')



