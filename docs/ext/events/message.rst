Messages
========



This section covers the messages class, and how to properly use it.



on_message
-----------

This is a decorator, which can be used to look for messages.


Example usage:

.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_message
    def your_sample_project(message):
      if message.content == "!ping":
        print(message.authorId)
        
        


message
-------

The message class.
+-----------+------+--------------------------------------------+
| Data      | Type | Description                                |
+===========+======+============================================+
| content   | str  | The content of a message                   |
+-----------+------+--------------------------------------------+
| channelId | str  |The channel ID of where the message was sent|
+-----------+------+--------------------------------------------+
| authorId  | str  | The ID of the author who sent the message  |
+-----------+------+--------------------------------------------+
| guildId   | int  | The guild ID of where the message was sent |
+-----------+------+--------------------------------------------+
| messageId | int  | The ID of the message sent                 |
+-----------+------+--------------------------------------------+


on_member_join
--------------
A decorator for when a member joins a server.
Example usage:
.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_member_join
    def your_sample_project(member):
        client.send_message("YOUR_CHANNEL_ID_HERE", "A new member has joined the server!")
        
        
        
on_member_leave
---------------
A decorator for when a member leaves a server.
Example usage:


.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_member_leave
    def your_sample_project(member):
        client.send_message("YOUR_CHANNEL_ID_HERE", "A member has left the server!")




run
----

Used to keep a websocket connection alive with guilded. Technically used at the end of any code built with NextGuild.

Example usage:



.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    # ...
    
    events.run()
    
    
    
    

