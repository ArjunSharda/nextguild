# -*- coding: utf-8 -*-
import asyncio
import json
from functools import wraps

import websockets

from nextguild.channel import Channel
from nextguild.message import Message, Webhook
from nextguild.reaction import Reaction, CalendarReaction, ForumTopicCommentReaction


class Events:
    def __init__(self, client):
        self._message_create_handlers = []
        self._message_update_handlers = []
        self._message_delete_handlers = []
        self._member_join_handlers = []
        self._member_leave_handlers = []
        self._bot_join_handlers = []
        self._bot_leave_handlers = []
        self._member_banned_handlers = []
        self._member_unbanned_handlers = []
        self._ready_handlers = []
        self._reaction_create_handlers = []
        self._reaction_delete_handlers = []
        self._forum_topic_comment_reaction_create_handlers = []
        self._forum_topic_comment_reaction_delete_handlers = []
        self._calendar_event_reaction_create_handlers = []
        self._calendar_event_reaction_delete_handlers = []
        self._channel_create_handlers = []
        self._channel_delete_handlers = []
        self._channel_update_handlers = []
        self._webhook_create_handlers = []
        self._webhook_delete_handlers = []
        self._webhook_update_handlers = []
        self.client = client

    def on_message(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_create_handlers.append(wrapper)
        return wrapper

    async def _handle_create_message(self, event_data):
        message = Message(event_data)
        for handler in self._message_create_handlers:
            await handler(message)

    def on_message_update(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_update_handlers.append(wrapper)
        return wrapper

    async def _handle_update_message(self, event_data):
        message = Message(event_data)
        for handler in self._message_update_handlers:
            await handler(message)

    def on_message_delete(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_delete_handlers.append(wrapper)
        return wrapper

    async def _handle_delete_message(self, event_data):
        message = Message(event_data)
        for handler in self._message_delete_handlers:
            await handler(message)

    def on_member_join(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_join_handlers.append(wrapper)
        return wrapper

    async def _handle_member_join(self, event_data):
        for handler in self._member_join_handlers:
            await handler(event_data)

    def on_member_leave(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_leave_handlers.append(wrapper)
        return wrapper

    async def _handle_member_leave(self, event_data):
        for handler in self._member_leave_handlers:
            await handler(event_data)

    def on_member_banned(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_banned_handlers.append(wrapper)
        return wrapper

    async def _handle_member_banned(self, event_data):
        for handler in self._member_banned_handlers:
            await handler(event_data)

    def on_member_unbanned(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_unbanned_handlers.append(wrapper)
        return wrapper

    async def _handle_member_unbanned(self, event_data):
        for handler in self._member_unbanned_handlers:
            await handler(event_data)

    def on_ready(self, func):
        @wraps(func)
        async def wrapper():
            return await func()

        self._ready_handlers.append(wrapper)
        return wrapper

    async def _handle_ready(self):
        for handler in self._ready_handlers:
            await handler()

    def on_reaction_create(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._reaction_create_handlers.append(wrapper)
        return wrapper

    async def _handle_create_reaction(self, event_data):
        reaction = Reaction(event_data)
        for handler in self._reaction_create_handlers:
            await handler(reaction)

    def on_reaction_delete(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._reaction_delete_handlers.append(wrapper)
        return wrapper

    async def _handle_delete_reaction(self, event_data):
        reaction = Reaction(event_data)
        for handler in self._reaction_delete_handlers:
            await handler(reaction)

    def on_forum_topic_comment_reaction_create(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._forum_topic_comment_reaction_create_handlers.append(wrapper)
        return wrapper

    async def _handle_forum_topic_comment_reaction_create(self, event_data):
        reaction = ForumTopicCommentReaction(event_data)
        for handler in self._forum_topic_comment_reaction_create_handlers:
            await handler(reaction)

    def on_forum_topic_comment_reaction_delete(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._forum_topic_comment_reaction_delete_handlers.append(wrapper)
        return wrapper

    async def _handle_forum_topic_comment_reaction_delete(self, event_data):
        reaction = ForumTopicCommentReaction(event_data)
        for handler in self._forum_topic_comment_reaction_delete_handlers:
            await handler(reaction)

    def on_calendar_event_reaction_create(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._calendar_event_reaction_create_handlers.append(wrapper)
        return wrapper

    async def _handle_calendar_event_reaction_create(self, event_data):
        reaction = CalendarReaction(event_data)
        for handler in self._calendar_event_reaction_create_handlers:
            await handler(reaction)

    def on_calendar_event_reaction_delete(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._calendar_event_reaction_delete_handlers.append(wrapper)
        return wrapper

    async def _handle_calendar_event_reaction_delete(self, event_data):
        reaction = CalendarReaction(event_data)
        for handler in self._calendar_event_reaction_delete_handlers:
            await handler(reaction)

    def on_channel_create(self, func):
        @wraps(func)
        def wrapper(channel):
            return func(channel)

        self._channel_create_handlers.append(wrapper)
        return wrapper

    async def _handle_create_channel(self, event_data):
        channel = Channel(event_data)
        for handler in self._channel_create_handlers:
            await handler(channel)

    def on_channel_delete(self, func):
        @wraps(func)
        def wrapper(channel):
            return func(channel)

        self._channel_delete_handlers.append(wrapper)
        return wrapper

    async def _handle_delete_channel(self, event_data):
        channel = Channel(event_data)
        for handler in self._channel_delete_handlers:
            await handler(channel)

    def on_channel_update(self, func):
        @wraps(func)
        def wrapper(channel):
            return func(channel)

        self._channel_update_handlers.append(wrapper)
        return wrapper

    async def _handle_update_channel(self, event_data):
        channel = Channel(event_data)
        for handler in self._channel_update_handlers:
            await handler(channel)

    def on_webhook_create(self, func):
        @wraps(func)
        def wrapper(webhook):
            return func(webhook)

        self._webhook_create_handlers.append(wrapper)
        return wrapper

    async def _handle_create_webhook(self, event_data):
        webhook = Webhook(event_data)
        for handler in self._webhook_create_handlers:
            await handler(webhook)

    def on_webhook_update(self, func):
        @wraps(func)
        def wrapper(webhook):
            return func(webhook)

        self._webhook_update_handlers.append(wrapper)
        return wrapper

    async def _handle_update_webhook(self, event_data):
        webhook = Webhook(event_data)
        for handler in self._webhook_update_handlers:
            await handler(webhook)

    async def start(self):
        async with websockets.connect(
                'wss://www.guilded.gg/websocket/v1',
                extra_headers={
                    'Authorization': f'Bearer {self.client.token}'
                }
        ) as websocket:
            await self._handle_ready()
            while True:
                data = await websocket.recv()
                json_data = json.loads(data)

                if 't' in json_data and 'd' in json_data:
                    event_type, event_data = json_data['t'], json_data['d']
                else:
                    continue

                event_handlers = {
                    'ChatMessageCreated': self._handle_create_message,
                    'ChatMessageUpdated': self._handle_update_message,
                    'ChatMessageDeleted': self._handle_delete_message,
                    'ServerMemberJoined': self._handle_member_join,
                    'ServerMemberRemoved': self._handle_member_leave,
                    'ServerMemberBanned': self._handle_member_banned,
                    'ServerMemberUnbanned': self._handle_member_unbanned,
                    'ChannelMessageReactionCreated':
                        self._handle_create_reaction,
                    'ChannelMessageReactionDeleted':
                        self._handle_delete_reaction,
                    'ForumTopicCommentReactionCreated':
                        self._handle_forum_topic_comment_reaction_create,
                    'ForumTopicCommentReactionDeleted':
                        self._handle_forum_topic_comment_reaction_delete,
                    'CalendarEventReactionCreated':
                        self._handle_calendar_event_reaction_create,
                    'CalendarEventReactionDeleted':
                        self._handle_calendar_event_reaction_delete,
                    'ServerChannelCreated': self._handle_create_channel,
                    'ServerChannelDeleted': self._handle_delete_channel,
                    'ServerChannelUpdated': self._handle_update_channel,
                    'ServerWebhookCreated': self._handle_create_webhook,
                    'ServerWebhookUpdated': self._handle_update_webhook

                }
                handler = event_handlers.get(event_type)
                if handler:
                    await handler(event_data)

    def run(self):
        try:
            asyncio.run(self.start())
        except KeyboardInterrupt:
            # TODO Handle standard exit
            pass
