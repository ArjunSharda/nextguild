Calendar Events
===========

This page provides an overview of the calendar event events in the NextGuild library.

This page requires that you've used this code at the top of the file:

.. code-block:: python

    from nextguild import *
    bot = Client('TOKEN')
    events = Events(bot)

on_calendar_event_create
--------

.. code-block:: python

    @events.on_calendar_event_create
    async def example():
        print('A calendar event was created!')

on_calendar_event_update
--------

.. code-block:: python

    @events.on_calendar_event_update
    async def example():
        print('A calendar event was updated!')

on_calendar_event_delete
--------

.. code-block:: python

    @events.on_calendar_event_delete
    async def example():
        print('A calendar event was deleted!')

on_calendar_event_comment_create
--------

.. code-block:: python

    @events.on_calendar_event_comment_create
    async def example():
        print('A calendar event comment was created!')

on_calendar_event_comment_update
--------

.. code-block:: python

    @events.on_calendar_event_comment_update
    async def example():
        print('A calendar event comment was updated!')

on_calendar_event_comment_delete
--------

.. code-block:: python

    @events.on_calendar_event_comment_delete
    async def example():
        print('A calendar event comment was deleted!')

on_calendar_event_rsvp_update
--------

.. code-block:: python

    @events.on_calendar_event_rsvp_update
    async def example():
        print('A calendar event rsvp was updated!')

on_calendar_event_rsvp_many_update
--------

.. code-block:: python

    @events.on_calendar_event_rsvp_many_update
    async def example():
        print('A calendar event rsvp was updated!')

on_calendar_event_rsvp_delete
--------

.. code-block:: python

    @events.on_calendar_event_rsvp_delete
    async def example():
        print('A calendar event rsvp was deleted!')

on_calendar_event_series_create
--------

.. code-block:: python

    @events.on_calendar_event_series_create
    async def example():
        print('A calendar event series was created!')

on_calendar_event_series_delete
--------

.. code-block:: python

    @events.on_calendar_event_series_delete
    async def example():
        print('A calendar event series was deleted!')