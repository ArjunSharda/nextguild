Events
======

This document provides an overview of the Event-related functions available in the NextGuild library. These functions allow you to create, retrieve, and manage events.

create_event
------------

.. code-block:: python

    bot.create_event(channelid=None, title=None, description=None, location=None, startsAt=None, url=None, color=None, isAllDay=None, rsvpLimit=None, autofillWaitlist=None, duration=None, isPrivate=None, roleIds=None, repeat_type=None, every=None, endsAfterOccurences=None, endDate=None)
    
    
 
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| Parameter              | Type   | Description                                                                                                                  |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| channelid              | str    | The channel ID of the event.                                                                                                 |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| title                  | str    | The name of the event (min length 1; max length 60).                                                                         |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| description            | str    | The description of the event (min length 1; max length 8000) [OPTIONAL].                                                     |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| location               | str    | The location of the event (min length 1; max length 8000) [OPTIONAL].                                                        |  
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| startsAt               | str    | The ISO 8601 timestamp that the event starts at [OPTIONAL].                                                                  |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| url                    | str    | A URL to associate with the event [OPTIONAL].                                                                                |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| color                  | int    | The color of the event when viewing in the calendar (min 0; max 16777215) [INTEGER] [OPTIONAL].                              |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| isAllDay               | bool   | Does the event last all day? example: "true" or "false" [OPTIONAL].                                                          |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| rsvpLimit              | int    | The number of RSVPs to allow before waitlisting RSVPs (min 1).                                                               |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| autofillWaitlist       | bool   | When rsvpLimit is set, users from the waitlist will be added as space becomes available in the event [OPTIONAL].             |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| duration               | int    | The duration of the event in minutes (min 1) [INTEGER] [OPTIONAL].                                                           |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| isPrivate              | bool   | Whether or not the event is private. example: "true" or "false" [OPTIONAL, public by default].                               |         
|                        |        |                                                                                                                              |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| roleIds                | list   | The role IDs to restrict the event to (min items 1; must have unique items true) [ARRAY] [OPTIONAL].                         |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| repeat_type            | str    | How often you want your event to repeat ("once", "everyDay", "everyWeek", "everyMonth", or "custom") [OPTIONAL].             |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| every                  | dict   | Apply further clarification to your events. This must have type set to custom. [OPTIONAL].                                   |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| endsAfterOccurrences   | int    | Used to control the end date of the event repeat (only used when type is custom) (max 24) [NUMBER] [OPTIONAL].               |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+
| endDate                | str    | The ISO 8601 timestamp that the event ends at (only used when type is custom); if used with endsAfterOccurrences,            |
|                        |        | the earliest resultant date of the two will be used [OPTIONAL].                                                              |
+------------------------+--------+------------------------------------------------------------------------------------------------------------------------------+






get_events
----------

.. code-block:: python
   bot.get_events(self, channelid, before=None, after=None, limit=None)
   
Retrieves events from the specified channel.

+-----------+------+--------------------------------------------+
| Parameter | Type | Description                                |
+===========+======+============================================+
| channelid | str  | The channel ID from which to fetch events. |
+-----------+------+--------------------------------------------+
| before    | str  | Retrieve events before this date.          |
+-----------+------+--------------------------------------------+
| after     | str  | Retrieve events after this date.           |
+-----------+------+--------------------------------------------+
| limit     | int  | Limit the number of events retrieved.      |
+-----------+------+--------------------------------------------+

delete_event
------------

.. code-block:: python
    bot.delete_event(self, channelid, eventid)
Deletes an event from the specified channel.

+-----------+------+------------------------------------+
| Parameter | Type | Description                        |
+===========+======+====================================+
| channelid | str  | The channel ID of the event.       |
+-----------+------+------------------------------------+
| eventid   | str  | The event ID to be deleted.        |
+-----------+------+------------------------------------+

get_calendar_event_rsvp
-----------------------

.. code-block:: python
    bot.get_calendar_event_rsvp(self, channelid, eventid)
    
Retrieves the RSVP status for the specified event.

+-----------+------+------------------------------------+
| Parameter | Type | Description                        |
+===========+======+====================================+
| channelid | str  | The channel ID of the event.       |
+-----------+------+------------------------------------+
| eventid   | str  | The event ID to get RSVP status.   |
+-----------+------+------------------------------------+

create_calendar_event_rsvp
--------------------------

.. code-block:: python
    bot.create_calendar_event_rsvp(self, channelid, eventid, rsvp)
Creates an RSVP for the specified event.

+-----------+------+------------------------------------+
| Parameter | Type | Description                        |
+===========+======+====================================+
| channelid | str  | The channel ID of the event.       |
+-----------+------+------------------------------------+
| eventid   | str  | The event ID to RSVP for.          |
+-----------+------+------------------------------------+
| rsvp      | str  | The RSVP status.                   |
+-----------+------+------------------------------------+




delete_calendar_event_rsvp
--------------------------

.. code-block:: python
    bot.delete_calendar_event_rsvp(self, channelid, eventid)
   
Deletes the RSVP for the specified event.

+-----------+------+------------------------------------+
| Parameter | Type | Description                        |
+===========+======+====================================+
| channelid | str  | The channel ID of the event.       |
+-----------+------+------------------------------------+
| eventid   | str  | The event ID to delete RSVP from.  |
+-----------+------+------------------------------------+

get_calendar_event_rsvps
------------------------

.. code-block:: python
    bot.get_calendar_event_rsvps(self, channelid, eventid)
    
Retrieves all RSVPs for the specified event.

+-----------+------+------------------------------------+
| Parameter | Type | Description                        |
+===========+======+====================================+
| channelid | str  | The channel ID of the event.       |
+-----------+------+------------------------------------+
| eventid   | str  | The event ID to get RSVPs for.     |
+-----------+------+------------------------------------+
