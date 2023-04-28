# -*- coding: utf-8 -*-
import asyncio
import json
from functools import wraps

import websockets

from channel import Channel
from message import Message, Webhook
from reaction import Reaction, CalendarReaction, ForumTopicCommentReaction


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
        #start        
        self._bot_server_join_handlers = []
        self._bot_server_leave_handlers = []
        self._member_update_handlers = []
        self._roles_update_handlers = []
        self._member_social_create_handlers = []
        self._member_social_update_handlers = []
        self._member_social_delete_handlers = []
        self._doc_delete_handlers = []
        self._doc_update_handlers = []
        self._doc_create_handlers = []
        self._doc_comment_create_handlers = []
        self._doc_comment_update_handlers = []
        self._doc_comment_delete_handlers = []
        self._calendar_event_create_handlers = []
        self._calendar_event_update_handlers = []
        self._calendar_event_delete_handlers = []
        self._forum_topic_create_handlers = []
        self._forum_topic_update_handlers = []
        self._forum_topic_delete_handlers = []
        self.client = client
    
    def on_bot_membership_created(self, func):
        @wraps(func)
        def wrapper(server):
            return func(server)

        self._bot_server_join_handlers.append(wrapper)
        return wrapper

    def on_bot_membership_deleted(self, func):
        @wraps(func)
        def wrapper(server):
            return func(server)

        self._bot_server_leave_handlers.append(wrapper)
        return wrapper
    
    def on_member_update(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_update_handlers.append(wrapper)
        return wrapper
    
    def on_roles_update(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._roles_update_handlers.append(wrapper)
        return wrapper
    
    def on_member_social_create(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_social_create_handlers.append(wrapper)
        return wrapper
    
    def on_member_social_update(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_social_update_handlers.append(wrapper)
        return wrapper
    
    def on_member_social_delete(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_social_delete_handlers.append(wrapper)
        return wrapper
    
    def on_doc_deleted(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_deleted_handlers.append(wrapper)
        return wrapper
    
    def on_doc_updated(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_updated_handlers.append(wrapper)
        return wrapper
    
    def on_doc_created(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_created_handlers.append(wrapper)
        return wrapper
    
    def on_doc_comment_created(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_comment_created_handlers.append(wrapper)
        return wrapper
    
    def on_doc_comment_updated(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_comment_updated_handlers.append(wrapper)
        return wrapper
    
    def on_doc_comment_deleted(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_comment_deleted_handlers.append(wrapper)
        return wrapper
    
    def on_calendar_event_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_create_handlers.append(wrapper)
        return wrapper
    
    def on_calendar_event_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_update_handlers.append(wrapper)
        return wrapper
    
    def on_calendar_event_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_delete_handlers.append(wrapper)
        return wrapper
    
    def on_forum_topic_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_create_handlers.append(wrapper)
        return wrapper
    
    def on_forum_topic_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_update_handlers.append(wrapper)
        return wrapper
    
    def on_forum_topic_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_delete_handlers.append(wrapper)
        return wrapper
    

    def on_message(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_create_handlers.append(wrapper)
        return wrapper



    def on_message_update(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_update_handlers.append(wrapper)
        return wrapper



    def on_message_delete(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_delete_handlers.append(wrapper)
        return wrapper



    def on_member_join(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_join_handlers.append(wrapper)
        return wrapper



    def on_member_leave(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_leave_handlers.append(wrapper)
        return wrapper



    def on_member_banned(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_banned_handlers.append(wrapper)
        return wrapper


    def on_member_unbanned(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_unbanned_handlers.append(wrapper)
        return wrapper



    def on_ready(self, func):
        @wraps(func)
        async def wrapper():
            return await func()

        self._ready_handlers.append(wrapper)
        return wrapper



    def on_reaction_create(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._reaction_create_handlers.append(wrapper)
        return wrapper



    def on_reaction_delete(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._reaction_delete_handlers.append(wrapper)
        return wrapper



    def on_forum_topic_comment_reaction_create(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._forum_topic_comment_reaction_create_handlers.append(wrapper)
        return wrapper



    def on_forum_topic_comment_reaction_delete(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._forum_topic_comment_reaction_delete_handlers.append(wrapper)
        return wrapper


    def on_calendar_event_reaction_create(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._calendar_event_reaction_create_handlers.append(wrapper)
        return wrapper



    def on_calendar_event_reaction_delete(self, func):
        @wraps(func)
        def wrapper(reaction):
            return func(reaction)

        self._calendar_event_reaction_delete_handlers.append(wrapper)
        return wrapper



    def on_channel_create(self, func):
        @wraps(func)
        def wrapper(channel):
            return func(channel)

        self._channel_create_handlers.append(wrapper)
        return wrapper


    def on_channel_delete(self, func):
        @wraps(func)
        def wrapper(channel):
            return func(channel)

        self._channel_delete_handlers.append(wrapper)
        return wrapper


    def on_channel_update(self, func):
        @wraps(func)
        def wrapper(channel):
            return func(channel)

        self._channel_update_handlers.append(wrapper)
        return wrapper


    def on_webhook_create(self, func):
        @wraps(func)
        def wrapper(webhook):
            return func(webhook)

        self._webhook_create_handlers.append(wrapper)
        return wrapper

    def on_webhook_update(self, func):
        @wraps(func)
        def wrapper(webhook):
            return func(webhook)

        self._webhook_update_handlers.append(wrapper)
        return wrapper
    
    async def _handle_bot_server_membership_created(self, event_data):
        for handler in self._bot_server_join_handlers:
            await handler(event_data)
    
    async def _handle_bot_server_membership_deleted(self, event_data):
        # TODO: server class
        for handler in self._bot_server_leave_handlers:
            await handler(event_data)
        
    async def _handle_server_member_updated(self, event_data):
        # TODO: member class
        for handler in self._member_update_handlers:
            await handler(event_data)

    async def _handle_server_roles_updated(self, event_data):
        for handler in self._roles_update_handlers:
            await handler(event_data)

    async def _handle_server_member_social_links_created(self, event_data):
        for handler in self._member_social_create_handlers:
            await handler(event_data)
    
    async def _handle_server_member_social_links_updated(self, event_data):
        for handler in self._member_social_update_handlers:
            await handler(event_data)
    
    async def _handle_server_member_social_links_deleted(self, event_data):
        for handler in self._member_social_delete_handlers:
            await handler(event_data)

    async def _handle_doc_created(self, event_data):
        for handler in self._doc_create_handlers:
            await handler(event_data)
    
    async def _handle_doc_updated(self, event_data):
        for handler in self._doc_update_handlers:
            await handler(event_data)
    
    async def _handle_doc_deleted(self, event_data):
        for handler in self._doc_delete_handlers:
            await handler(event_data)

    async def _handle_doc_comment_updated(self, event_data):
        for handler in self._doc_comment_update_handlers:
            await handler(event_data)
    
    async def _handle_doc_comment_deleted(self, event_data):
        for handler in self._doc_comment_delete_handlers:
            await handler(event_data)
    
    async def _handle_doc_comment_created(self, event_data):
        for handler in self._doc_comment_create_handlers:
            await handler(event_data)
    
    async def _handle_calendar_event_created(self, event_data):
        for handler in self._calendar_event_create_handlers:
            await handler(event_data)
    
    async def _handle_calendar_event_updated(self, event_data):
        for handler in self._calendar_event_update_handlers:
            await handler(event_data)
    
    async def _handle_calendar_event_deleted(self, event_data):
        for handler in self._calendar_event_delete_handlers:
            await handler(event_data)
    
    async def _handle_forum_topic_created(self, event_data):
        for handler in self._forum_topic_create_handlers:
            await handler(event_data)
    
    async def _handle_forum_topic_updated(self, event_data):
        for handler in self._forum_topic_update_handlers:
            await handler(event_data)
    
    async def _handle_forum_topic_deleted(self, event_data):
        for handler in self._forum_topic_delete_handlers:
            await handler(event_data)

    async def _handle_server_member_banned(self, event_data):
        # TODO: member class
        for handler in self._member_banned_handlers:
            await handler(event_data)

    async def _handle_create_message(self, event_data):
        message = Message(event_data)
        for handler in self._message_create_handlers:
            await handler(message)

    async def _handle_update_message(self, event_data):
        message = Message(event_data)
        for handler in self._message_update_handlers:
            await handler(message)

    async def _handle_delete_message(self, event_data):
        message = Message(event_data)
        for handler in self._message_delete_handlers:
            await handler(message)

    async def _handle_member_join(self, event_data):
        for handler in self._member_join_handlers:
            await handler(event_data)

    async def _handle_member_leave(self, event_data):
        for handler in self._member_leave_handlers:
            await handler(event_data)

    async def _handle_member_banned(self, event_data):
        for handler in self._member_banned_handlers:
            await handler(event_data)

    async def _handle_member_unbanned(self, event_data):
        for handler in self._member_unbanned_handlers:
            await handler(event_data)

    async def _handle_ready(self):
        for handler in self._ready_handlers:
            await handler()

    async def _handle_create_reaction(self, event_data):
        reaction = Reaction(event_data)
        for handler in self._reaction_create_handlers:
            await handler(reaction)

    async def _handle_delete_reaction(self, event_data):
        reaction = Reaction(event_data)
        for handler in self._reaction_delete_handlers:
            await handler(reaction)

    async def _handle_forum_topic_comment_reaction_create(self, event_data):
        reaction = ForumTopicCommentReaction(event_data)
        for handler in self._forum_topic_comment_reaction_create_handlers:
            await handler(reaction)

    async def _handle_forum_topic_comment_reaction_delete(self, event_data):
        reaction = ForumTopicCommentReaction(event_data)
        for handler in self._forum_topic_comment_reaction_delete_handlers:
            await handler(reaction)

    async def _handle_calendar_event_reaction_create(self, event_data):
        reaction = CalendarReaction(event_data)
        for handler in self._calendar_event_reaction_create_handlers:
            await handler(reaction)

    async def _handle_calendar_event_reaction_delete(self, event_data):
        reaction = CalendarReaction(event_data)
        for handler in self._calendar_event_reaction_delete_handlers:
            await handler(reaction)

    async def _handle_create_channel(self, event_data):
        channel = Channel(event_data)
        for handler in self._channel_create_handlers:
            await handler(channel)

    async def _handle_delete_channel(self, event_data):
        channel = Channel(event_data)
        for handler in self._channel_delete_handlers:
            await handler(channel)
    
    async def _handle_update_channel(self, event_data):
        channel = Channel(event_data)
        for handler in self._channel_update_handlers:
            await handler(channel)
    
    async def _handle_create_webhook(self, event_data):
        webhook = Webhook(event_data)
        for handler in self._webhook_create_handlers:
            await handler(webhook)

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
                    'ChannelMessageReactionCreated': self._handle_create_reaction,
                    'ChannelMessageReactionDeleted': self._handle_delete_reaction,
                    'ForumTopicCommentReactionCreated': self._handle_forum_topic_comment_reaction_create,
                    'ForumTopicCommentReactionDeleted': self._handle_forum_topic_comment_reaction_delete,
                    'CalendarEventReactionCreated': self._handle_calendar_event_reaction_create,
                    'CalendarEventReactionDeleted': self._handle_calendar_event_reaction_delete,
                    'ServerChannelCreated': self._handle_create_channel,
                    'ServerChannelDeleted': self._handle_delete_channel,
                    'ServerChannelUpdated': self._handle_update_channel,
                    'ServerWebhookCreated': self._handle_create_webhook,
                    'ServerWebhookUpdated': self._handle_update_webhook,
                    'BotServerMembershipCreated': self._handle_bot_server_membership_created,
                    'BotServerMembershipDeleted': self._handle_bot_server_membership_deleted,
                    'ServerMemberUpdated': self._handle_server_member_updated,
                    'ServerRolesUpdated': self._handle_server_roles_updated,
                    'ServerMemberSocialLinksCreated': self._handle_server_member_social_links_created,
                    'ServerMemberSocialLinksUpdated': self._handle_server_member_social_links_updated,
                    'ServerMemberSocialLinksDeleted': self._handle_server_member_social_links_deleted,
                    'DocCreated': self._handle_doc_created,
                    'DocUpdated': self._handle_doc_updated,
                    'DocDeleted': self._handle_doc_deleted,
                    'DocCommentCreated': self._handle_doc_comment_created,
                    'DocCommentUpdated': self._handle_doc_comment_updated,
                    'DocCommentDeleted': self._handle_doc_comment_deleted,
                    'CalendarEventCreated': self._handle_calendar_event_created,
                    'CalendarEventUpdated': self._handle_calendar_event_updated,
                    'CalendarEventDeleted': self._handle_calendar_event_deleted,
                    'ForumTopicCreated': self._handle_forum_topic_created,
                    'ForumTopicUpdated': self._handle_forum_topic_updated,
                    'ForumTopicDeleted': self._handle_forum_topic_deleted


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
