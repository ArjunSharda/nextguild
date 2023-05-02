# -*- coding: utf-8 -*-
from .embed import Embed


class Message:
    def __init__(self, payload: dict):
        """This could be run from single message GET call with response:
        {"message: {...}}
        Or from serialize:
        ["00": {...}, "01": {...}, "02": {...}]
        """
        message: dict = payload.get('message', payload)
        self.id: str = message.get('id')
        self.type: str = message.get('type')
        self.server_id: str = message.get('serverId')
        self.channel_id: str = message.get('channelId')
        # "content" is optional in favor of "embeds"
        self.content: str = message.get('content', '')
        # "embeds" is optional in favor of "content"
        self.embeds: list[Embed] = list(map(
            lambda em: Embed(**em),
            message.get('embeds', [])
        ))
        # If message is not a response it's empty
        self.reply_message_ids: list[str] = message.get('replyMessageIds', [])
        self.is_private: bool = message.get('isPrivate', False)
        self.is_silent: bool = message.get('isSilent', False)
        # If message has no mentions it's empty
        # TODO Model "mentions" attribute
        self.mentions = [mention['id'] for mention in message.get('mentions', {}).get('users', [])]
        self.created_at: str = message.get('createdAt')
        self.author_id: str = message.get('createdBy')
        self.webhook_id: str = message.get('createdByWebhookId')
        self.updated_at: str = message.get('updatedAt')

    async def reply(self):  # TODO "reply" method
        pass


class Webhook:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.id: str = event_data.get('webhook', {}).get('id')
        self.name: str = event_data.get('webhook', {}).get('name')
        self.channel_id: str = event_data.get('webhook', {}).get('channelId')
        self.server_id: str = event_data.get('serverId')
        self.created_at: str = event_data.get('webhook', {}).get('createdAt')
        self.author_id: str = event_data.get('webhook', {}).get('createdBy')
