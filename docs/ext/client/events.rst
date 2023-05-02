Events
========

This section provides an overview of the event-related methods available in the NextGuild library. The following methods are used to interact with events:

create_event
-----------------

.. code-block:: python

    create_event(channel_id, name, description, location, startsAt, url, color, isAllDay, rspvDisabled, rspvLimit, autofillWaitlist, duration, isPrivate, roleIds, repeatInfo)

Create an event in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to create the event  |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| name              | str     | The name of the event.                     |
+-------------------+---------+--------------------------------------------+
| description       | str,    | The description of the event.              |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| location          | str,    | The location of the event.                 |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| startsAt          | str,    | The start time of the event. In date-time. |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| url               | str,    | The URL of the event.                      |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| color             | int,    | The decimal color of the event.            |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| isAllDay          | bool,   | Whether the event is all day.              |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| rspvDisabled      | bool,   | When disabled, users will not be able      |
|                   | optional| to RSVP to the event.                      |
+-------------------+---------+--------------------------------------------+
| rspvLimit         | int,    | The maximum number of users that can RSVP  |
|                   | optional| to the event.                              |
+-------------------+---------+--------------------------------------------+
| autofillWaitlist  | bool,   | When enabled, users on the waitlist will   |
|                   | optional| automatically be added to the event when   |
|                   |         | a spot opens up.                           |
+-------------------+---------+--------------------------------------------+
| duration          | int,    | The duration of the event in minutes.      |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| isPrivate         | bool,   |                                            |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| roleIds           | list,   | A list of role IDs that has access to the  |
|                   | optional| event.                                     |
+-------------------+---------+--------------------------------------------+
| repeatInfo        | dict,   | A dictionary containing the repeat info    |
|                   | optional| for the event.                             |
+-------------------+---------+--------------------------------------------+

.. code-block:: python

    repeatInfo = {
        "type": "custom",
        "endsAfterOccurrences": 1,
        "endDate": "2000-01-01T00:00:00.000Z",
        "on": ["monday", "thursday"]
        "every": {
            "count": 1,
            "interval": "day"
        }
    }

+---------------------+---------+--------------------------------------------+
| Parameter           | Type    | Description                                |
+=====================+=========+============================================+
| type                | str     | The type of repeat.                        |
|                     |         | "once", "everyDay", "everyWeek",           |
|                     |         | "everyMonth", or "custom"                  |
+---------------------+---------+--------------------------------------------+
| endsAfterOccurrences| int,    | The number of times the event will repeat. |
|                     | optional|                                            |
+---------------------+---------+--------------------------------------------+
| endDate             | str,    | The date the event will stop repeating.    |
|                     | optional|                                            |
+---------------------+---------+--------------------------------------------+
| on                  | list,   | A list of days the event will repeat on.   |
|                     | optional|                                            |
+---------------------+---------+--------------------------------------------+	

To use ``every``, the ``type`` has to be set to ``"custom"``.

+---------------------+---------+--------------------------------------------+
| Parameter           | Type    | Description                                |
+=====================+=========+============================================+
| count               | int,    | The number of times the event will repeat. |
+---------------------+---------+--------------------------------------------+
| interval            | str     | The interval the event will repeat on.     |
|                     |         | "day", "week", "month", or "year"          |
+---------------------+---------+--------------------------------------------+

update_event
-----------------

.. code-block:: python

    update_event(channel_id, event_id, name, description, location, startsAt, url, color, isAllDay, rspvDisabled, rspvLimit, autofillWaitlist, duration, isPrivate, roleIds, cancellation)

Update an event in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to update the event  |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event to update.             |
+-------------------+---------+--------------------------------------------+
| name              | str,    | The name of the event.                     |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| description       | str,    | The description of the event.              |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| location          | str,    | The location of the event.                 |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| startsAt          | str,    | The start time of the event. In date-time. |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| url               | str,    | The URL of the event.                      |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| color             | int,    | The decimal color of the event.            |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| isAllDay          | bool,   | Whether the event is all day.              |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| rspvDisabled      | bool,   | When disabled, users will not be able      |
|                   | optional| to RSVP to the event.                      |
+-------------------+---------+--------------------------------------------+
| rspvLimit         | int,    | The maximum number of users that can RSVP  |
|                   | optional| to the event.                              |
+-------------------+---------+--------------------------------------------+
| autofillWaitlist  | bool,   | When enabled, users on the waitlist will   |
|                   | optional| automatically be added to the event when   |
|                   |         | a spot opens up.                           |
+-------------------+---------+--------------------------------------------+
| duration          | int,    | The duration of the event in minutes.      |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| isPrivate         | bool,   |                                            |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| roleIds           | list,   | A list of role IDs that has access to the  |
|                   | optional| event.                                     |
+-------------------+---------+--------------------------------------------+
| cancellation      | dict,   | A dictionary containing the cancellation   |
|                   | optional| info for the event.                        |
+-------------------+---------+--------------------------------------------+


Here is how to use the ``cancellation`` parameter.

.. code-block:: python

    cancellation = {
        "description": "The event has been cancelled."
    }

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| description       | str,    | The description of the cancellation.       |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+

delete_event
-----------------

.. code-block:: python

    delete_event(channel_id, event_id)

Delete an event in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to delete the event  |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event to delete.             |
+-------------------+---------+--------------------------------------------+


get_events
-----------------

.. code-block:: python

    get_events(channel_id, before, after, limit)

Get a list of events in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to get events from.  |
+-------------------+---------+--------------------------------------------+
| before            | str,    | The date-time to get events before.        |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| after             | str,    | The date-time to get events after.         |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+
| limit             | int,    | The maximum number of events to get.       |
|                   | optional|                                            |
+-------------------+---------+--------------------------------------------+

create_calendar_event_rsvp
-----------------

.. code-block:: python

    create_calendar_event_rsvp(channel_id, event_id, user_id, status)

Create an RSVP for an event in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to create the RSVP   |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event to create the RSVP for.|
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to create the RSVP for. |
+-------------------+---------+--------------------------------------------+
| status            | str,    | The status of the RSVP.                    |
|                   |         | "going", "maybe", "declined", or "invited  |
+-------------------+---------+--------------------------------------------+

delete_calendar_event_rsvp
-----------------

.. code-block:: python

    delete_calendar_event_rsvp(channel_id, event_id, user_id)

Delete an RSVP for an event in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to delete the RSVP   |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event to delete the RSVP for.|
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to delete the RSVP for. |
+-------------------+---------+--------------------------------------------+

get_calendar_event_rsvp
-----------------

.. code-block:: python

    get_calendar_event_rsvp(channel_id, event_id, user_id)

Get an RSVP for an event in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to get the RSVP from.|
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event to get the RSVP for.   |
+-------------------+---------+--------------------------------------------+
| user_id           | str     | The ID of the user to get the RSVP for.    |
+-------------------+---------+--------------------------------------------+

get_calendar_event_rsvps
-----------------

.. code-block:: python

    get_calendar_event_rsvps(channel_id, event_id)

Get a list of RSVPs for an event in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| channel_id        | str     | The ID of the channel to get the RSVPs     |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| event_id          | int     | The ID of the event to get the RSVPs for.  |
+-------------------+---------+--------------------------------------------+
