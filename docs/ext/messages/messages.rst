Messages
========
This document provides an overview of the message-related methods available in the NextGuild library. The following methods are used to interact with channels and messages:
class Client:
    ...
    def send_message(self, channel_id, content=None, embed=None):
        """
        Send a message to the specified channel. Optionally, provide content and/or an embed.
        Parameters:
            - channel_id (str): The ID of the channel to send the message to.
            - content (str, optional): The content of the message.
            - embed (object, optional): An embed object to be sent with the message.
        """
    def send_reply(self, channel_id, content, replyids):
        """
        Send a reply to a message in the specified channel.
        Parameters:
            - channel_id (str): The ID of the channel to send the reply to.
            - content (str): The content of the reply.
            - replyids (list): A list of message IDs to reply to.
        """
    def edit_message(self, channel_id, message_id, content):
        """
        Edit an existing message in the specified channel.
        Parameters:
            - channel_id (str): The ID of the channel where the message is.
            - message_id (str): The ID of the message to edit.
            - content (str): The updated content of the message.
        """
    def delete_message(self, channel_id, message_id):
        """
        Delete a message in the specified channel.
        Parameters:
            - channel_id (str): The ID of the channel where the message is.
            - message_id (str): The ID of the message to delete.
        """
    def get_message(self, channel_id, message_id):
        """
        Retrieve a specific message from a channel.
        Parameters:
            - channel_id (str): The ID of the channel where the message is.
            - message_id (str): The ID of the message to retrieve.
        """
    def get_channel_messages(self, channel_id, limit=None, before=None, after=None, includePrivate=None):
        """
        Get messages from a channel with optional parameters for filtering.
        Parameters:
            - channel_id (str): The ID of the channel to fetch messages from.
            - limit (int, optional): The maximum number of messages to retrieve.
            - before (str, optional): Retrieve messages before this message ID.
            - after (str, optional): Retrieve messages after this message ID.
            - includePrivate (bool, optional): Include private messages in the results.
        """
    def purge(self, channel_id, amount):
        """
        Delete a specified number of messages from a channel.
        Parameters:
            - channel_id (str): The ID of the channel to purge messages from.
            - amount (int): The number of messages to delete.
        """
