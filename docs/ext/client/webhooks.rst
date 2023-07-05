Webhooks
========

This section provides an overview of the webhook-related methods available in the NextGuild library. The following methods are used to interact with webhooks:

create_webhook
-----------------

.. code-block:: python

    create_webhook(server_id, channel_id, name, avatar_url)

Create a webhook in the specified channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to create the webhook |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| channel_id        | str     | The ID of the channel to create the        |
|                   |         | webhook in.                                |
+-------------------+---------+--------------------------------------------+
| name              | str     | The name of the webhook.                   |
+-------------------+---------+--------------------------------------------+
| avatar_url        | str     | The URL of the avatar to use for the       |
|                   |         | webhook.                                   |
+-------------------+---------+--------------------------------------------+

update_webhook
-----------------

.. code-block:: python

    update_webhook(server_id, webhook_id, name, channel_id, avatar_url)

Update a webhook.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to update the webhook |
|                   |         | in.                                        |
+-------------------+---------+--------------------------------------------+
| webhook_id        | str     | The ID of the webhook to update.           |
+-------------------+---------+--------------------------------------------+
| name              | str     | The new name of the webhook.               |
+-------------------+---------+--------------------------------------------+
| channel_id        | str     | The channel ID to move the webhook to.     |
+-------------------+---------+--------------------------------------------+
| avatar_url        | str     | The URL of the avatar to use for the       |
|                   |         | webhook.                                   |
+-------------------+---------+--------------------------------------------+

delete_webhook
-----------------

.. code-block:: python

    delete_webhook(server_id, webhook_id)

Delete a webhook.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to delete the webhook |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| webhook_id        | str     | The ID of the webhook to delete.           |
+-------------------+---------+--------------------------------------------+

get_webhook
-----------------

.. code-block:: python

    get_webhook(server_id, webhook_id)

Get a webhook.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the webhook    |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| webhook_id        | str     | The ID of the webhook to get.              |
+-------------------+---------+--------------------------------------------+

get_webhooks
-----------------

.. code-block:: python

    get_webhooks(server_id, channel_id)

Get all webhooks in a channel.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to get the webhooks   |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+
| channel_id        | str     | The ID of the channel to get the webhooks  |
|                   |         | from.                                      |
+-------------------+---------+--------------------------------------------+

send_webhook_message
-----------------

.. code-block:: python

    send_webhook_message(server_id, webhook_id, content, embeds, username, avatar_url)

Send a message with a webhook.

+-------------------+---------+--------------------------------------------+
| Parameter         | Type    | Description                                |
+===================+=========+============================================+
| server_id         | str     | The ID of the server to send the webhook   |
|                   |         | message in.                                |
+-------------------+---------+--------------------------------------------+
| webhook_id        | str     | The ID of the webhook to send the message  |
|                   |         | with.                                      |
+-------------------+---------+--------------------------------------------+
| content           | str,    | The content of the message.                |
|                   | OPTIONAL|                                            |
+-------------------+---------+--------------------------------------------+
| embeds            | list,   | A list of embeds to send.                  |
|                   | OPTIONAL|                                            |
+-------------------+---------+--------------------------------------------+
| username          | str,    | The username to send the message with.     |
|                   | OPTIONAL|                                            |
+-------------------+---------+--------------------------------------------+
| avatar_url        | str,    | The URL of the avatar to send the message  |
|                   | OPTIONAL| with.                                      |
+-------------------+---------+--------------------------------------------+
Note that the avatar and username parameters are temporary, and apply only to the message being sent.
