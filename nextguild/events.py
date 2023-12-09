# -*- coding: utf-8 -*-
import asyncio
import json
from functools import wraps
import time
import websockets
import traceback

from .classes import Data


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
        self._forum_topic_pinned_handlers = []
        self._forum_topic_unpinned_handlers = []
        self._forum_topic_reaction_create_handlers = []
        self._forum_topic_reaction_delete_handlers = []
        self._forum_topic_lock_handlers = []
        self._forum_topic_unlock_handlers = []
        self._forum_topic_comment_create_handlers = []
        self._forum_topic_comment_update_handlers = []
        self._forum_topic_comment_delete_handlers = []
        self._calendar_event_rsvp_update_handlers = []
        self._calendar_event_rsvp_many_update_handlers = []
        self._calendar_event_rsvp_delete_handlers = []
        self._list_item_create_handlers = []
        self._list_item_update_handlers = []
        self._list_item_delete_handlers = []
        self._list_item_complete_handlers = []
        self._list_item_uncomplete_handlers = []
        self._channel_message_reaction_create_handlers = []
        self._channel_message_reaction_delete_handlers = []
        self._channel_message_reaction_many_delete_handlers = []
        self._channel_archive_handlers = []
        self._channel_restore_handlers = []
        self._calendar_event_comment_create_handlers = []
        self._calendar_event_comment_update_handlers = []
        self._calendar_event_comment_delete_handlers = []
        self._calendar_event_comment_reaction_create_handlers = []
        self._calendar_event_comment_reaction_delete_handlers = []
        self._doc_reaction_create_handlers = []
        self._doc_reaction_delete_handlers = []
        self._doc_comment_reaction_create_handlers = []
        self._doc_comment_reaction_delete_handlers = []
        self._calendar_event_series_create_handlers = []
        self._calendar_event_series_delete_handlers = []
        self._announcement_create_handlers = []
        self._announcement_update_handlers = []
        self._announcement_delete_handlers = []
        self._announcement_reaction_create_handlers = []
        self._announcement_reaction_delete_handlers = []
        self._announcement_comment_create_handlers = []
        self._announcement_comment_update_handlers = []
        self._announcement_comment_delete_handlers = []
        self._announcement_comment_reaction_create_handlers = []
        self._announcement_comment_reaction_delete_handlers = []
        self._group_create_handlers = []
        self._group_update_handlers = []
        self._group_delete_handlers = []
        self._user_status_create_handlers = []
        self._user_status_delete_handlers = []
        self._role_create_handlers = []
        self._role_update_handlers = []
        self._role_delete_handlers = []
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

    def on_member_updated(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_update_handlers.append(wrapper)
        return wrapper

    def on_roles_updated(self, func):
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

    def on_doc_delete(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_deleted_handlers.append(wrapper)
        return wrapper

    def on_doc_update(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_updated_handlers.append(wrapper)
        return wrapper

    def on_doc_create(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_created_handlers.append(wrapper)
        return wrapper

    def on_doc_comment_create(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_comment_created_handlers.append(wrapper)
        return wrapper

    def on_doc_comment_update(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._doc_comment_updated_handlers.append(wrapper)
        return wrapper

    def on_doc_comment_delete(self, func):
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
        async def wrapper(ready):
            return await func(ready)

        self._ready_handlers.append(wrapper)
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

    def on_channel_archive(self, func):
        @wraps(func)
        def wrapper(channel):
            return func(channel)
            
        self._channel_archive_handlers.append(wrapper)
        return wrapper



    def on_channel_restore(self, func):
        @wraps(func)
        def wrapper(channel):
            return func(channel)
            
        self._channel_restore_handlers.append(wrapper)
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

    def on_forum_topic_pin(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_pinned_handlers.append(wrapper)
        return wrapper

    def on_forum_topic_unpin(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_unpinned_handlers.append(wrapper)
        return wrapper

    def on_forum_topic_reaction_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_reaction_create_handlers.append(wrapper)
        return wrapper

    def on_forum_topic_reaction_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_reaction_delete_handlers.append(wrapper)
        return wrapper

    def on_forum_topic_lock(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_lock_handlers.append(wrapper)
        return wrapper

    def on_forum_topic_unlock(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_unlock_handlers.append(wrapper)
        return wrapper

    def on_forum_topic_comment_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_comment_create_handlers.append(wrapper)
        return wrapper

    def on_forum_topic_comment_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_comment_update_handlers.append(wrapper)
        return wrapper

    def on_forum_topic_comment_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._forum_topic_comment_delete_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_rsvp_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_rsvp_update_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_rsvp_many_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_rsvp_many_update_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_rsvp_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_rsvp_delete_handlers.append(wrapper)
        return wrapper

    def on_list_item_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._list_item_create_handlers.append(wrapper)
        return wrapper

    def on_list_item_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._list_item_update_handlers.append(wrapper)
        return wrapper

    def on_list_item_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._list_item_delete_handlers.append(wrapper)
        return wrapper

    def on_list_item_complete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._list_item_complete_handlers.append(wrapper)
        return wrapper

    def on_list_item_uncomplete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._list_item_uncomplete_handlers.append(wrapper)
        return wrapper

    def on_channel_message_reaction_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._channel_message_reaction_create_handlers.append(wrapper)
        return wrapper

    def on_channel_message_reaction_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._channel_message_reaction_delete_handlers.append(wrapper)
        return wrapper

    def on_channel_message_reaction_many_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._channel_message_reaction_many_delete_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_comment_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_comment_create_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_comment_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_comment_update_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_comment_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_comment_delete_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_comment_reaction_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_comment_reaction_create_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_comment_reaction_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_comment_reaction_delete_handlers.append(wrapper)
        return wrapper

    def on_doc_reaction_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._doc_reaction_create_handlers.append(wrapper)
        return wrapper

    def on_doc_reaction_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._doc_reaction_delete_handlers.append(wrapper)
        return wrapper

    def on_doc_comment_reaction_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._doc_comment_reaction_create_handlers.append(wrapper)
        return wrapper

    def on_doc_comment_reaction_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._doc_comment_reaction_delete_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_series_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_series_create_handlers.append(wrapper)
        return wrapper

    def on_calendar_event_series_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._calendar_event_series_delete_handlers.append(wrapper)
        return wrapper

    def on_announcement_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_create_handlers.append(wrapper)
        return wrapper

    def on_announcement_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_update_handlers.append(wrapper)
        return wrapper

    def on_announcement_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_delete_handlers.append(wrapper)
        return wrapper

    def on_announcement_reaction_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_reaction_create_handlers.append(wrapper)
        return wrapper

    def on_announcement_reaction_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_reaction_delete_handlers.append(wrapper)
        return wrapper

    def on_announcement_comment_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_comment_create_handlers.append(wrapper)
        return wrapper

    def on_announcement_comment_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_comment_update_handlers.append(wrapper)
        return wrapper

    def on_announcement_comment_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_comment_delete_handlers.append(wrapper)
        return wrapper

    def on_announcement_comment_reaction_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_comment_reaction_create_handlers.append(wrapper)
        return wrapper

    def on_announcement_comment_reaction_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._announcement_comment_reaction_delete_handlers.append(wrapper)
        return wrapper

    def on_group_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._group_create_handlers.append(wrapper)
        return wrapper

    def on_group_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._group_update_handlers.append(wrapper)
        return wrapper

    def on_group_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._group_delete_handlers.append(wrapper)
        return wrapper

    def on_user_status_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._user_status_create_handlers.append(wrapper)
        return wrapper

    def on_user_status_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._user_status_delete_handlers.append(wrapper)
        return wrapper

    def on_role_create(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._role_create_handlers.append(wrapper)
        return wrapper

    def on_role_update(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._role_update_handlers.append(wrapper)
        return wrapper

    def on_role_delete(self, func):
        @wraps(func)
        def wrapper(event):
            return func(event)

        self._role_delete_handlers.append(wrapper)
        return wrapper

    async def _handle_bot_server_membership_created(self, event_data):
        event = Data(event_data)
        for handler in self._bot_server_join_handlers:
            await handler(event)

    async def _handle_bot_server_membership_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._bot_server_leave_handlers:
            await handler(event)

    async def _handle_server_member_updated(self, event_data):
        event = Data(event_data)
        for handler in self._member_update_handlers:
            await handler(event)

    async def _handle_server_roles_updated(self, event_data):
        event = Data(event_data)
        for handler in self._roles_update_handlers:
            await handler(event)

    async def _handle_server_member_social_links_created(self, event_data):
        event = Data(event_data)
        for handler in self._member_social_create_handlers:
            await handler(event)

    async def _handle_server_member_social_links_updated(self, event_data):
        event = Data(event_data)
        for handler in self._member_social_update_handlers:
            await handler(event)

    async def _handle_server_member_social_links_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._member_social_delete_handlers:
            await handler(event)

    async def _handle_doc_created(self, event_data):
        event = Data(event_data)
        for handler in self._doc_create_handlers:
            await handler(event)

    async def _handle_doc_updated(self, event_data):
        event = Data(event_data)
        for handler in self._doc_update_handlers:
            await handler(event)

    async def _handle_doc_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._doc_delete_handlers:
            await handler(event)

    async def _handle_doc_comment_updated(self, event_data):
        event = Data(event_data)
        for handler in self._doc_comment_update_handlers:
            await handler(event)

    async def _handle_doc_comment_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._doc_comment_delete_handlers:
            await handler(event)

    async def _handle_doc_comment_created(self, event_data):
        event = Data(event_data)
        for handler in self._doc_comment_create_handlers:
            await handler(event)

    async def _handle_calendar_event_created(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_create_handlers:
            await handler(event)

    async def _handle_calendar_event_updated(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_update_handlers:
            await handler(event)

    async def _handle_calendar_event_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_delete_handlers:
            await handler(event)

    async def _handle_forum_topic_created(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_create_handlers:
            await handler(event)

    async def _handle_forum_topic_updated(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_update_handlers:
            await handler(event)

    async def _handle_forum_topic_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_delete_handlers:
            await handler(event)

    async def _handle_server_member_banned(self, event_data):
        event = Data(event_data)
        for handler in self._member_banned_handlers:
            await handler(event)

    async def _handle_create_message(self, event_data):
        event = Data(event_data)
        for handler in self._message_create_handlers:
            await handler(event)

    async def _handle_update_message(self, event_data):
        event = Data(event_data)
        for handler in self._message_update_handlers:
            await handler(event)

    async def _handle_delete_message(self, event_data):
        event = Data(event_data)
        for handler in self._message_delete_handlers:
            await handler(event)

    async def _handle_member_join(self, event_data):
        event = Data(event_data)
        for handler in self._member_join_handlers:
            await handler(event)

    async def _handle_member_leave(self, event_data):
        event = Data(event_data)
        for handler in self._member_leave_handlers:
            await handler(event)

    async def _handle_member_banned(self, event_data):
        event = Data(event_data)
        for handler in self._member_banned_handlers:
            await handler(event)

    async def _handle_member_unbanned(self, event_data):
        event = Data(event_data)
        for handler in self._member_unbanned_handlers:
            await handler(event)

    async def _handle_ready(self, event_data):
        event = Data(event_data)
        for handler in self._ready_handlers:
            await handler(event)

    async def _handle_create_reaction(self, event_data):
        event = Data(event_data)
        for handler in self._reaction_create_handlers:
            await handler(event)

    async def _handle_delete_reaction(self, event_data):
        event = Data(event_data)
        for handler in self._reaction_delete_handlers:
            await handler(event)

    async def _handle_forum_topic_comment_reaction_create(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_comment_reaction_create_handlers:
            await handler(event)

    async def _handle_forum_topic_comment_reaction_delete(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_comment_reaction_delete_handlers:
            await handler(event)

    async def _handle_calendar_event_reaction_create(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_reaction_create_handlers:
            await handler(event)

    async def _handle_calendar_event_reaction_delete(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_reaction_delete_handlers:
            await handler(event)

    async def _handle_create_channel(self, event_data):
        event = Data(event_data)
        for handler in self._channel_create_handlers:
            await handler(event)

    async def _handle_delete_channel(self, event_data):
        event = Data(event_data)
        for handler in self._channel_delete_handlers:
            await handler(event)

    async def _handle_update_channel(self, event_data):
        event = Data(event_data)
        for handler in self._channel_update_handlers:
            await handler(event)

    async def _handle_channel_archive(self, event_data):
        event = Data(event_data)
        for handler in self._channel_archive_handlers:
            await handler(event)


    async def _handle_channel_restore(self, event_data):
        event = Data(event_data)
        for handler in self._channel_restore_handlers:
            await handler(event)

    async def _handle_create_webhook(self, event_data):
        event = Data(event_data)
        for handler in self._webhook_create_handlers:
            await handler(event)

    async def _handle_update_webhook(self, event_data):
        event = Data(event_data)
        for handler in self._webhook_update_handlers:
            await handler(event)

    async def _handle_forum_topic_pinned(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_pinned_handlers:
            await handler(event)

    async def _handle_forum_topic_unpinned(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_unpinned_handlers:
            await handler(event)

    async def _handle_forum_topic_reaction_created(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_reaction_create_handlers:
            await handler(event)

    async def _handle_forum_topic_reaction_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_reaction_delete_handlers:
            await handler(event)

    async def _handle_forum_topic_locked(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_lock_handlers:
            await handler(event)

    async def _handle_forum_topic_unlocked(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_unlock_handlers:
            await handler(event)

    async def _handle_forum_topic_comment_created(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_comment_create_handlers:
            await handler(event)

    async def _handle_forum_topic_comment_updated(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_comment_update_handlers:
            await handler(event)

    async def _handle_forum_topic_comment_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._forum_topic_comment_delete_handlers:
            await handler(event)

    async def _handle_calendar_event_rsvp_updated(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_rsvp_update_handlers:
            await handler(event)

    async def _handle_calendar_event_rsvp_many_updated(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_rsvp_many_update_handlers:
            await handler(event)

    async def _handle_calendar_event_rsvp_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_rsvp_delete_handlers:
            await handler(event)

    async def _handle_list_item_created(self, event_data):
        event = Data(event_data)
        for handler in self._list_item_create_handlers:
            await handler(event)

    async def _handle_list_item_updated(self, event_data):
        event = Data(event_data)
        for handler in self._list_item_update_handlers:
            await handler(event)

    async def _handle_list_item_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._list_item_delete_handlers:
            await handler(event)

    async def _handle_list_item_completed(self, event_data):
        event = Data(event_data)
        for handler in self._list_item_complete_handlers:
            await handler(event)

    async def _handle_list_item_uncompleted(self, event_data):
        event = Data(event_data)
        for handler in self._list_item_uncomplete_handlers:
            await handler(event)

    async def _handle_channel_message_reaction_created(self, event_data):
        event = Data(event_data)
        for handler in self._channel_message_reaction_create_handlers:
            await handler(event)

    async def _handle_channel_message_reaction_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._channel_message_reaction_delete_handlers:
            await handler(event)

    async def _handle_channel_message_reaction_many_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._channel_message_reaction_many_delete_handlers:
            await handler(event)

    async def _handle_calendar_event_comment_created(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_comment_create_handlers:
            await handler(event)

    async def _handle_calendar_event_comment_updated(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_comment_update_handlers:
            await handler(event)

    async def _handle_calendar_event_comment_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_comment_delete_handlers:
            await handler(event)

    async def _handle_calendar_event_comment_reaction_created(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_comment_reaction_create_handlers:
            await handler(event)

    async def _handle_calendar_event_comment_reaction_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_comment_reaction_delete_handlers:
            await handler(event)

    async def _handle_doc_reaction_created(self, event_data):
        event = Data(event_data)
        for handler in self._doc_reaction_create_handlers:
            await handler(event)

    async def _handle_doc_reaction_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._doc_reaction_delete_handlers:
            await handler(event)

    async def _handle_doc_comment_reaction_created(self, event_data):
        event = Data(event_data)
        for handler in self._doc_comment_reaction_create_handlers:
            await handler(event)

    async def _handle_doc_comment_reaction_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._doc_comment_reaction_delete_handlers:
            await handler(event)

    async def _handle_calendar_event_series_updated(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_series_update_handlers:
            await handler(event)

    async def _handle_calendar_event_series_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._calendar_event_series_delete_handlers:
            await handler(event)

    async def _handle_announcement_created(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_create_handlers:
            await handler(event)

    async def _handle_announcement_updated(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_update_handlers:
            await handler(event)

    async def _handle_announcement_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_delete_handlers:
            await handler(event)

    async def _handle_announcement_reaction_created(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_reaction_create_handlers:
            await handler(event)

    async def _handle_announcement_reaction_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_reaction_delete_handlers:
            await handler(event)

    async def _handle_announcement_comment_created(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_comment_create_handlers:
            await handler(event)

    async def _handle_announcement_comment_updated(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_comment_update_handlers:
            await handler(event)

    async def _handle_announcement_comment_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_comment_delete_handlers:
            await handler(event)

    async def _handle_announcement_comment_reaction_created(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_comment_reaction_create_handlers:
            await handler(event)

    async def _handle_announcement_comment_reaction_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._announcement_comment_reaction_delete_handlers:
            await handler(event)

    async def _handle_group_created(self, event_data):
        event = Data(event_data)
        for handler in self._group_create_handlers:
            await handler(event)

    async def _handle_group_updated(self, event_data):
        event = Data(event_data)
        for handler in self._group_update_handlers:
            await handler(event)

    async def _handle_group_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._group_delete_handlers:
            await handler(event)

    async def _handle_user_status_created(self, event_data):
        event = Data(event_data)
        for handler in self._user_status_create_handlers:
            await handler(event)

    async def _handle_user_status_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._user_status_delete_handlers:
            await handler(event)

    async def _handle_role_created(self, event_data):
        event = Data(event_data)
        for handler in self._role_create_handlers:
            await handler(event)

    async def _handle_role_updated(self, event_data):
        event = Data(event_data)
        for handler in self._role_update_handlers:
            await handler(event)

    async def _handle_role_deleted(self, event_data):
        event = Data(event_data)
        for handler in self._role_delete_handlers:
            await handler(event)

    async def start(self):
        async with websockets.connect(
                'wss://www.guilded.gg/websocket/v1',
                extra_headers={
                    'Authorization': f'Bearer {self.client.token}'
                }
        ) as websocket:
            response = await websocket.recv()
            data = json.loads(response)
            await self._handle_ready(data)
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
                    'ForumTopicDeleted': self._handle_forum_topic_deleted,
                    'ForumTopicPinned': self._handle_forum_topic_pinned,
                    'ForumTopicUnpinned': self._handle_forum_topic_unpinned,
                    'ForumTopicReactionCreated': self._handle_forum_topic_reaction_created,
                    'ForumTopicReactionDeleted': self._handle_forum_topic_reaction_deleted,
                    'ForumTopicLocked': self._handle_forum_topic_locked,
                    'ForumTopicUnlocked': self._handle_forum_topic_unlocked,
                    'ForumTopicCommentCreated': self._handle_forum_topic_comment_created,
                    'ForumTopicCommentUpdated': self._handle_forum_topic_comment_updated,
                    'ForumTopicCommentDeleted': self._handle_forum_topic_comment_deleted,
                    'CalendarEventRsvpUpdated': self._handle_calendar_event_rsvp_updated,
                    'CalendarEventRsvpManyUpdated': self._handle_calendar_event_rsvp_many_updated,
                    'CalendarEventRsvpDeleted': self._handle_calendar_event_rsvp_deleted,
                    'ListItemCreated': self._handle_list_item_created,
                    'ListItemUpdated': self._handle_list_item_updated,
                    'ListItemDeleted': self._handle_list_item_deleted,
                    'ListItemCompleted': self._handle_list_item_completed,
                    'ListItemUncompleted': self._handle_list_item_uncompleted,
                    'ChannelMessageReactionCreated': self._handle_channel_message_reaction_created,
                    'ChannelMessageReactionDeleted': self._handle_channel_message_reaction_deleted,
                    'ChannelMessageReactionManyDeleted': self._handle_channel_message_reaction_many_deleted,
                    'CalendarEventCommentCreated': self._handle_calendar_event_comment_created,
                    'CalendarEventCommentUpdated': self._handle_calendar_event_comment_updated,
                    'CalendarEventCommentDeleted': self._handle_calendar_event_comment_deleted,
                    'CalendarEventCommentReactionCreated': self._handle_calendar_event_comment_reaction_created,
                    'CalendarEventCommentReactionDeleted': self._handle_calendar_event_comment_reaction_deleted,
                    'DocReactionCreated': self._handle_doc_reaction_created,
                    'DocReactionDeleted': self._handle_doc_reaction_deleted,
                    'DocCommentReactionCreated': self._handle_doc_comment_reaction_created,
                    'DocCommentReactionDeleted': self._handle_doc_comment_reaction_deleted,
                    'CalendarEventSeriesUpdated': self._handle_calendar_event_series_updated,
                    'CalendarEventSeriesDeleted': self._handle_calendar_event_series_deleted,
                    'AnnouncementCreated': self._handle_announcement_created,
                    'AnnouncementUpdated': self._handle_announcement_updated,
                    'AnnouncementDeleted': self._handle_announcement_deleted,
                    'AnnouncementReactionCreated': self._handle_announcement_reaction_created,
                    'AnnouncementReactionDeleted': self._handle_announcement_reaction_deleted,
                    'AnnouncementCommentCreated': self._handle_announcement_comment_created,
                    'AnnouncementCommentUpdated': self._handle_announcement_comment_updated,
                    'AnnouncementCommentDeleted': self._handle_announcement_comment_deleted,
                    'AnnouncementCommentReactionCreated': self._handle_announcement_comment_reaction_created,
                    'AnnouncementCommentReactionDeleted': self._handle_announcement_comment_reaction_deleted,
                    'GroupCreated': self._handle_group_created,
                    'GroupUpdated': self._handle_group_updated,
                    'GroupDeleted': self._handle_group_deleted,
                    'UserStatusCreated': self._handle_user_status_created,
                    'UserStatusDeleted': self._handle_user_status_deleted,
                    'RoleCreated': self._handle_role_created,
                    'RoleUpdated': self._handle_role_updated,
                    'RoleDeleted': self._handle_role_deleted,

                }
                handler = event_handlers.get(event_type)
                if handler:
                    await handler(event_data)

    async def on_disconnect(self):
        while True:
            try:
                await self.start()
                break
            except Exception as e:
                print(f"An exception occurred: {e}")
                traceback.print_exc()
                time.sleep(10)

    async def run(self):
        try:
            await self.on_disconnect()
        except KeyboardInterrupt:
            # TODO Handle standard exit
            pass

