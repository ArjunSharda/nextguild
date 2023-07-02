Data
========

The Data class is an extremely useful class that allows you to parse the data from the responses of the API requests, since they are returned in a JSON format.
Please note that this does **NOT** include events, since they are already parsed by default.

Example of usage:

.. code-block:: python

    new_channel_id = Data(bot.create_channel("name", "chat", "server_id")).id

new_channel_id will now be set to the channel id of the newly created channel.


If you need any help using this, feel free to join the support server! https://guilded.gg/nextguild

Happy coding!