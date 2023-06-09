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
    async def example(data):
        print(f'A calendar event with name {data.name} was created!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the calendar event                 |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.name`                 | The name of the calendar event               |
+-----------------------------+----------------------------------------------+
| `data.description`          | The description of the calendar event        |
+-----------------------------+----------------------------------------------+
| `data.location`             | The location of the calendar event           |
+-----------------------------+----------------------------------------------+
| `data.url`                  | The URL of the calendar event                |
+-----------------------------+----------------------------------------------+
| `data.color`                | The color of the calendar event              |
+-----------------------------+----------------------------------------------+
| `data.repeats`              | If the calendar event repeats itself         |
+-----------------------------+----------------------------------------------+
| `data.series_id`            | The ID of the calendar event series          |
+-----------------------------+----------------------------------------------+
| `data.role_ids`             | The IDs of the roles the event is restricted |
|                             | to                                           |
+-----------------------------+----------------------------------------------+
| `data.rsvp_disabled`        | If the RSVP is disabled                      |
+-----------------------------+----------------------------------------------+
| `data.is_all_day`           | If the event is all day                      |
+-----------------------------+----------------------------------------------+
| `data.rsvp_limit`           | The RSVP limit of the event                  |
+-----------------------------+----------------------------------------------+
| `data.autofill_waitlist`    | If the waitlist will autofill                |
+-----------------------------+----------------------------------------------+
| `data.starts_at`            | The start time of the event                  |
+-----------------------------+----------------------------------------------+
| `data.duration`             | The duration of the event                    |
+-----------------------------+----------------------------------------------+
| `data.is_private`           | If the event is private                      |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions of the event                    |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the event was created               |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The user who created the event               |
+-----------------------------+----------------------------------------------+
| `data.cancellation`         | Cancellation info                            |
+-----------------------------+----------------------------------------------+

on_calendar_event_update
--------

.. code-block:: python

    @events.on_calendar_event_update
    async def example(data):
        print(f'A calendar event with name {data.name} was updated!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the calendar event                 |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.name`                 | The name of the calendar event               |
+-----------------------------+----------------------------------------------+
| `data.description`          | The description of the calendar event        |
+-----------------------------+----------------------------------------------+
| `data.location`             | The location of the calendar event           |
+-----------------------------+----------------------------------------------+
| `data.url`                  | The URL of the calendar event                |
+-----------------------------+----------------------------------------------+
| `data.color`                | The color of the calendar event              |
+-----------------------------+----------------------------------------------+
| `data.repeats`              | If the calendar event repeats itself         |
+-----------------------------+----------------------------------------------+
| `data.series_id`            | The ID of the calendar event series          |
+-----------------------------+----------------------------------------------+
| `data.role_ids`             | The IDs of the roles the event is restricted |
|                             | to                                           |
+-----------------------------+----------------------------------------------+
| `data.rsvp_disabled`        | If the RSVP is disabled                      |
+-----------------------------+----------------------------------------------+
| `data.is_all_day`           | If the event is all day                      |
+-----------------------------+----------------------------------------------+
| `data.rsvp_limit`           | The RSVP limit of the event                  |
+-----------------------------+----------------------------------------------+
| `data.autofill_waitlist`    | If the waitlist will autofill                |
+-----------------------------+----------------------------------------------+
| `data.starts_at`            | The start time of the event                  |
+-----------------------------+----------------------------------------------+
| `data.duration`             | The duration of the event                    |
+-----------------------------+----------------------------------------------+
| `data.is_private`           | If the event is private                      |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions of the event                    |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the event was created               |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The user who created the event               |
+-----------------------------+----------------------------------------------+
| `data.cancellation`         | Cancellation info                            |
+-----------------------------+----------------------------------------------+



on_calendar_event_delete
--------

.. code-block:: python

    @events.on_calendar_event_delete
    async def example(data):
        print(f'A calendar event with name {data.name} was deleted!')

+-----------------------------+----------------------------------------------+
| Type                        | Description                                  |
+=============================+==============================================+
| `data.server_id`            | The ID of the server                         |
+-----------------------------+----------------------------------------------+
| `data.id`                   | The ID of the calendar event                 |
+-----------------------------+----------------------------------------------+
| `data.channel_id`           | The ID of the channel                        |
+-----------------------------+----------------------------------------------+
| `data.name`                 | The name of the calendar event               |
+-----------------------------+----------------------------------------------+
| `data.description`          | The description of the calendar event        |
+-----------------------------+----------------------------------------------+
| `data.location`             | The location of the calendar event           |
+-----------------------------+----------------------------------------------+
| `data.url`                  | The URL of the calendar event                |
+-----------------------------+----------------------------------------------+
| `data.color`                | The color of the calendar event              |
+-----------------------------+----------------------------------------------+
| `data.repeats`              | If the calendar event repeats itself         |
+-----------------------------+----------------------------------------------+
| `data.series_id`            | The ID of the calendar event series          |
+-----------------------------+----------------------------------------------+
| `data.role_ids`             | The IDs of the roles the event is restricted |
|                             | to                                           |
+-----------------------------+----------------------------------------------+
| `data.rsvp_disabled`        | If the RSVP is disabled                      |
+-----------------------------+----------------------------------------------+
| `data.is_all_day`           | If the event is all day                      |
+-----------------------------+----------------------------------------------+
| `data.rsvp_limit`           | The RSVP limit of the event                  |
+-----------------------------+----------------------------------------------+
| `data.autofill_waitlist`    | If the waitlist will autofill                |
+-----------------------------+----------------------------------------------+
| `data.starts_at`            | The start time of the event                  |
+-----------------------------+----------------------------------------------+
| `data.duration`             | The duration of the event                    |
+-----------------------------+----------------------------------------------+
| `data.is_private`           | If the event is private                      |
+-----------------------------+----------------------------------------------+
| `data.mentions`             | The mentions of the event                    |
+-----------------------------+----------------------------------------------+
| `data.created_at`           | The time the event was created               |
+-----------------------------+----------------------------------------------+
| `data.created_by`           | The user who created the event               |
+-----------------------------+----------------------------------------------+
| `data.cancellation`         | Cancellation info                            |
+-----------------------------+----------------------------------------------+

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