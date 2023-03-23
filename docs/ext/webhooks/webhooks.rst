Webhooks
========

This section provides an overview of the webhook-related methods available in the NextGuild library. The following methods are used to interact with webhooks:

create_webhook
--------------

.. code-block:: python

    create_webhook(serverid, channelid, name)

Creates a webhook in the specified channel.

+-------------+---------------+---------------------------------------------+
| Parameter   | Type          | Description                                 |
+=============+===============+=============================================+
| serverid    | str           | The ID of the server to create the webhook  |
+-------------+---------------+---------------------------------------------+
| channelid   | str           | The ID of the channel to create the webhook |
+-------------+---------------+---------------------------------------------+
| name        | str           | The name of the webhook                     |
+-------------+---------------+---------------------------------------------+

update_webhook
--------------

.. code-block:: python

    update_webhook(serverid, webhookid, name, channelid)

Update a specified webhook.

+-------------+----------+------------------------------------------------+
| Parameter   | Type     | Description                                    |
+=============+==========+================================================+
| serverid    | str      | The ID of the server to update the webhook in. |
+-------------+----------+------------------------------------------------+
| webhookid   | str      | The ID of the webhook to update                |
+-------------+----------+------------------------------------------------+
| name        | str      | The name of the webhook                        |
+-------------+----------+------------------------------------------------+
| channelid   | str,     | The ID of the channel to assign the webhook.   |
|             | optional |                                                |
+-------------+----------+------------------------------------------------+

delete_webhook
--------------

.. code-block:: python

    delete_webhook(serverid, webhookid)

Delete a specified webhook.

+-------------+----------+------------------------------------------------+
| Parameter   | Type     | Description                                    |
+=============+==========+================================================+
| serverid    | str      | The ID of the server to delete the webhook in. |
+-------------+----------+------------------------------------------------+
| webhookid   | str      | The ID of the webhook to delete                |
+-------------+----------+------------------------------------------------+

get_webhook
-----------

.. code-block:: python

    get_webhook(serverid, webhookid)

Get a webhook in the specified server.

+-------------+----------+-----------------------------------------------+
| Parameter   | Type     | Description                                   |
+=============+==========+===============================================+
| serverid    | str      | The ID of the server to get the webhook in    |
+-------------+----------+-----------------------------------------------+
| webhookid   | str      | The ID of the webhook to get                  |
+-------------+----------+-----------------------------------------------+

get_webhooks
------------

.. code-block:: python

    get_webhooks(serverid, channelid)
    
Get the webhooks of a specified channel.

+-------------+----------+-----------------------------------------------+
| Parameter   | Type     | Description                                   |
+=============+==========+===============================================+
| serverid    | str      | The ID of the server to get the webhook in    |
+-------------+----------+-----------------------------------------------+
| channelid   | str      | The channel ID for fetching all webhooks from |
+-------------+----------+-----------------------------------------------+


send_webhook_message
--------------------

.. code-block:: python

    send_webhook_message(serverid, webhookid, content, embed)
    
Send a message using a webhook.

+-------------+----------+------------------------------------------------+
| Parameter   | Type     | Description                                    |
+=============+==========+================================================+
| serverid    | str      | The ID of the server to send the message in.   |
+-------------+----------+------------------------------------------------+
| webhookid   | str      | The ID of the webhook to use                   |
+-------------+----------+------------------------------------------------+
| content     | str,     | The content of the message.                    |
|             | optional |                                                |
+-------------+----------+------------------------------------------------+
| embed       | object,  | An embed object to be sent with the message.   |
|             | optional |                                                |
+-------------+----------+------------------------------------------------+

