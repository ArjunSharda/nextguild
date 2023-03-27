Events
========

This section covers the events that the NextGuild library has to offer, and how to implement them.



on_message
-----------

This is a decorator, which can be used to look for messages.


Example usage:

.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_message
    async def on_message_example(message):
      if message.content == "!ping":
        print(message.authorId)
        
        
on_message_update
-----------
A decorator used for when a message is updated

Example usage:

.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_message_update
    async def on_message_update_example(message):
      if message.content == "!ping":
        print(message.authorId)

on_message_delete
-----------
A decorator used for when a message is deleted

Example usage:

.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_message_delete
    async def on_message_delete_example(message):
      print(f'{message.authorId} just deleted a message!')

on_member_banned
-----------
A decorator used for when a member is banned

Example usage:

.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_member_ban
    async def on_member_banned_example(member):
      print('Someone just got banned!')

on_member_unbanned
-----------
A decorator used for when a member is unbanned

Example usage:

.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_member_unbanned
    async def on_member_unbanned_example(member):
      print('Someone just got unbanned!')
      

on_member_join
--------------
A decorator for when a member joins a server.
Example usage:

.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_member_join
    async def on_member_join_example(member):
        client.send_message("YOUR_CHANNEL_ID_HERE", "A member has joined the server!")
        
        
        
on_member_leave
---------------
A decorator for when a member leaves a server.
Example usage:


.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_member_leave
    async def on_member_leave_example(member):
        client.send_message("YOUR_CHANNEL_ID_HERE", "A member has left the server!")
        
 
on_webhook_create
---------------
A decorator for when a webhook is created.
Example usage:


.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_webhook_create
    async def on_webhook_create(webhook):
        client.send_message("YOUR_CHANNEL_ID_HERE", "A webhook has been created!")
        
on_webhook_update
---------------
A decorator for when a webhook is updated.
Example usage:


.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_webhook_update
    async def on_webhook_update(webhook):
        client.send_message("YOUR_CHANNEL_ID_HERE", "A webhook has been updated!")


on_reaction_create
----------------
A decorator for when a reaction is created.
Example usage:


.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_reaction_create
    async def on_webhook_create(reaction):
        client.send_message("YOUR_CHANNEL_ID_HERE", "A reaction has been created!")

on_reaction_delete
----------------
A decorator for when a reaction is deleted.
Example usage:


.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_reaction_delete
    async def on_webhook_delete(reaction):
        client.send_message("YOUR_CHANNEL_ID_HERE", "A reaction has been deleted!")


on_ready
--------
Used to, normally, execute a action when the bot is ready to be used.

Example usage:


.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    @events.on_ready
    async def on_ready_example():
      print("Bot is ready!")
    


run
----

Used to keep a websocket connection alive with guilded. Technically used at the end of any code built with NextGuild.

Example usage:



.. code-block:: python

    client = Client("YOUR_TOKEN_HERE")
    events = Events(client)
    
    
    # ...
    
    events.run()
    
    
    
 
    
    

