Embeds
======

This page provides an overview of the Embed class and its methods available in the NextGuild library. The Embed class is used to create rich embeds for messages.


Embed
----------

.. code-block:: python

    yourembed = Embed(title, description, color, author, author_url, author_icon, footer, footer_icon, thumbnail, image, fields)
                     
The constructor for the Embed class. Initializes an embed object with the provided parameters.

+---------------+------------------+-------------------------------------------------+
| Parameter     | Type             | Description                                     |
+===============+==================+=================================================+
| title         | str, optional    | The title of the embed.                         |
+---------------+------------------+-------------------------------------------------+
| description   | str, optional    | The description of the embed.                   |
+---------------+------------------+-------------------------------------------------+
| color         | str, optional    | The color of the embed, as a hexadecimal string.|
+---------------+------------------+-------------------------------------------------+
| author        | str, optional    | The name of the author for the embed.           |
+---------------+------------------+-------------------------------------------------+
| author_url    | str, optional    | The URL for the author in the embed.            |
+---------------+------------------+-------------------------------------------------+
| author_icon   | str, optional    | The URL for the author icon in the embed.       |
+---------------+------------------+-------------------------------------------------+
| footer        | str, optional    | The footer text for the embed.                  |
+---------------+------------------+-------------------------------------------------+
| footer_icon   | str, optional    | The URL for the footer icon in the embed.       |
+---------------+------------------+-------------------------------------------------+
| thumbnail     | str, optional    | The URL for the thumbnail image in the embed.   |
+---------------+------------------+-------------------------------------------------+
| image         | str, optional    | The URL for the main image in the embed.        |
+---------------+------------------+-------------------------------------------------+
| fields        | list, optional   | A list of fields to be added to the embed.      |
+---------------+------------------+-------------------------------------------------+

add_field
---------

.. code-block:: python

    Embed.add_field(title, value):

Adds a field to the embed.

+-----------+------+----------------------------------------+
| Parameter | Type | Description                            |
+===========+======+========================================+
| title     | str  | The title of the field.                |
+-----------+------+----------------------------------------+
| value     | str  | The value of the field.                |
+-----------+------+----------------------------------------+