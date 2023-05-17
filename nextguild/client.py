# -*- coding: utf-8 -*-
import json
import time
from datetime import datetime

import requests

from .embed import Embed
from .message import Message


class Client:
    def __init__(self, token: str) -> None:
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'User-Agent': 'NextGuild/1.0',
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        self.base_url = 'https://www.guilded.gg/api/v1'
        self.cache = {}
        self._message_handlers = []

    def send_message(
            self,
            channel_id: str,
            content: str = None,
            *,
            embed: Embed = None,
            is_private: bool = False,
            is_silent: bool = False,
            reply_message_ids: list[str] = None
    ):
        """Docs: https://www.guilded.gg/docs/api/chat/ChannelMessageCreate
        """
        # No need for checking if boolean values exist.
        payload = {
            # It could be "not private" as default.
            'isPrivate': str(is_private).lower(),
            # It could be "not silent" as default.
            'isSilent': str(is_silent).lower()
        }

        if reply_message_ids is not None:
            payload['replyMessageIds'] = reply_message_ids

        if content is not None:
            payload['content'] = content

        if embed is not None:
            payload['embeds'] = [embed.to_dict]

        response = self.request(
            method='POST',
            url=f'{self.base_url}/channels/{channel_id}/messages',
            json=payload
        )
        return Message(response)

    def edit_message(
            self,
            channel_id: str,
            message_id: str,
            content: str = None,
            *,
            embed: Embed = None
    ):
        """Docs: https://www.guilded.gg/docs/api/chat/ChannelMessageUpdate
        """
        payload = {}

        if content is not None:
            payload['content'] = content

        if embed is not None:
            payload['embeds'] = [embed.to_dict]

        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/messages/{message_id}',
            json=payload
        )
        return Message(response)

    def delete_message(
            self,
            channel_id: str,
            message_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
        )
        return response

    def get_message(
            self,
            channel_id: str,
            message_id: str
    ):
        """Docs: https://www.guilded.gg/docs/api/chat/ChannelMessageRead
        """
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
        )
        return Message(response)

    def get_channel_messages(
            self,
            channel_id,
            limit=None,
            before=None,
            after=None,
            include_private=None
    ):
        """Docs: https://www.guilded.gg/docs/api/chat/ChannelMessageReadMany
        """
        params = {}

        if limit:
            params['limit'] = limit

        if before:
            params['before'] = before

        if after:
            params['after'] = after

        if include_private:
            params['includePrivate'] = include_private

        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/messages',
            params=params
        )
        return list(map(
            lambda msg: Message(msg),
            response.get('messages', [])
        ))

    def purge(
            self,
            channel_id: str,
            amount: int
    ):
        messages = self.get_channel_messages(channel_id, amount)
        message_ids = [msg.id for msg in messages]
        for id in message_ids:
            self.delete_message(channel_id, id)
        return len(message_ids)

    def request(self, method: str, url: str, **kwargs) -> dict:
        response = requests.request(
            method,
            url,
            headers=self.headers,
            **kwargs
        )
        if (code := response.status_code) == 429:
            retry_after = int(response.headers.get('retry-after', '1'))
            print(
                f'Received {code} status. Retrying after'
                f' {retry_after} seconds.'
            )
            time.sleep(retry_after)
            return self.request(method, url, **kwargs)
        # try:
        #     data = response.json()
        #     breakpoint()
        # except json.JSONDecodeError:
        #     data = response.text
        #     breakpoint()
        try:
            data: dict = json.loads(response.content)
        except:
            return
        if 200 <= code < 300:
            return data
        raise ValueError(f'Request failed with status {code}: {data}')

    def create_channel(
            self,
            name: str,
            channel_type,
            server_id: str,
            group_id: str = None,
            category_id: int = None,
            is_public: bool = False
    ):
        data = {'name': name, 'type': channel_type}
        if category_id:
            data.update({'categoryId': category_id})
        if group_id:
            data.update({'group_id': group_id})
        if server_id:
            data.update({'server_id': server_id})
        data.update({"isPublic": str(is_public).lower()})
        response = self.request(
            'POST',
            f'{self.base_url}/channels',
            json=data
        )
        return response

    def get_channel(
            self,
            channel_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}'
        )
        return response

    def delete_channel(
            self,
            channel_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}'
        )
        return response

    def update_channel(
            self,
            channel_id: str,
            name: str = None,
            topic: str = None,
            is_public: bool = False
    ):
        data = {}

        if name:
            data.update({'name': name})

        if topic:
            data.update({'topic': topic})

        if is_public:
            data.update({'isPublic': str(is_public).lower()})

        response = self.request(
            'PATCH',
            f'{self.base_url}/channels/{channel_id}',
            json=data
        )
        return response

    def get_server(
            self,
            server_id: str
    ):
        response = self.request('GET', f'{self.base_url}/servers/{server_id}')
        return response

    def get_server_members(
            self,
            server_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/servers/{server_id}/members'
        )
        return response

    def get_server_member(
            self,
            server_id: str,
            user_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/servers/{server_id}/members/{user_id}'
        )
        return response

    def update_nickname(
            self,
            server_id: str,
            user_id: str,
            nickname: str
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/servers/{server_id}/members/{user_id}/nickname',
            json={'nickname': nickname}
        )
        return response

    def delete_nickname(
            self,
            server_id: str,
            user_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/servers/{server_id}/members/{user_id}/nickname'
        )
        return response

    def kick_member(
            self,
            server_id: str,
            user_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/servers/{server_id}/members/{user_id}'
        )
        return response

    def ban_member(
            self,
            server_id: str,
            user_id: str
    ):
        response = self.request(
            'POST',
            f'{self.base_url}/servers/{server_id}/bans/{user_id}'
        )
        return response

    def add_role(
            self,
            server_id: str,
            user_id: str,
            role_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/servers/{server_id}/members/{user_id}/roles/'
            f'{role_id}'
        )
        return response

    def remove_role(
            self,
            server_id: str,
            user_id: str,
            role_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/servers/{server_id}/members/{user_id}/roles/'
            f'{role_id}'
        )
        return response

    def get_member_roles(
            self,
            server_id: str,
            user_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/servers/{server_id}/members/{user_id}/roles'
        )
        return response['roleIds']

    def unban_member(
            self,
            server_id: str,
            user_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/servers/{server_id}/bans/{user_id}'
        )
        return response

    def get_member_ban(
            self,
            server_id: str,
            user_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/servers/{server_id}/bans/{user_id}'
        )
        return response

    def add_group_member(
            self,
            group_id: str,
            user_id: str
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/groups/{group_id}/members/{user_id}'
        )
        return response

    def remove_group_member(
            self,
            group_id: str,
            user_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/groups/{group_id}/members/{user_id}'
        )
        return response

    def get_member_bans(
            self,
            server_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/servers/{server_id}/bans'
        )
        return response

    def get_social_link(
            self,
            user_id: str,
            link_type: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/users/{user_id}/social-links/{link_type}'
        )
        return response

    def award_xp(
            self,
            server_id: str,
            user_id: str,
            amount: int
    ):
        response = self.request(
            'POST',
            f'{self.base_url}/servers/{server_id}/members/{user_id}/xp',
            json={'amount': amount}
        )
        return response

    def get_xp(
            self,
            server_id: str,
            user_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/servers/{server_id}/members/{user_id}/xp'
        )
        return response

    def set_xp(
            self,
            server_id: str,
            user_id: str,
            amount: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/servers/{server_id}/members/{user_id}/xp',
            json={'amount': amount}
        )
        return response

    def award_xp_to_role(
            self,
            server_id: str,
            role_id: int,
            amount: int
    ):
        response = self.request(
            'POST',
            f'{self.base_url}/servers/{server_id}/roles/{role_id}/xp',
            json={'amount': amount}
        )
        return response

    def create_list_item(
            self,
            channel_id: str,
            title: str,
            note: str = None
    ):
        data = {'message': title}
        if note:
            data.update({'note': {'content': note}})
        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/items',
            json=data
        )
        return response

    def get_list_item(
            self,
            channel_id: str,
            list_item_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/items/{list_item_id}'
        )
        return response

    def get_list_items(
            self,
            channel_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/items'
        )
        return response

    def delete_list_item(
            self,
            channel_id: str,
            list_item_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/items/{list_item_id}'
        )
        return response

    def update_list_item(
            self,
            channel_id: str,
            list_item_id: str,
            message: str,
            note: str = None
    ):
        data = {'message': message}

        if note:
            data.update({'note': {'content': note}})

        response = self.request(
            'PATCH',
            f'{self.base_url}/channels/{channel_id}/items/{list_item_id}',
            json=data
        )
        return response

    def complete_list_item(
            self,
            channel_id: str,
            list_item_id: str
    ):
        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/items/{list_item_id}'
            f'/complete'
        )
        return response

    def uncomplete_list_item(
            self,
            channel_id: str,
            list_item_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/items/{list_item_id}'
            f'/complete'
        )
        return response

    def create_event(
            self,
            channel_id: str,
            title: str,
            **kwargs
    ):
        data = {'name': title}
        for key, value in kwargs.items():
            data.update({key: value})
        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/events',
            json=data
        )
        return response

    def update_event(
            self,
            channel_id: str,
            event_id: int,
            **kwargs
    ):
        data = {}
        for key, value in kwargs.items():
            data.update({key: value})
        response = self.request(
            'PATCH',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}',
            json=data
        )
        return response

    def member_is_owner(self, server_id: str, user_id: str):
        """Checks if a user is the owner of a server."""
        ownerid = self.get_server(server_id).get('server', {}).get('ownerId')
        return ownerid == user_id

    def get_events(
            self,
            channel_id: str,
            before: datetime = None,
            after: datetime = None,
            limit: int = None
    ):
        params = {}

        if before:
            params['before'] = before.isoformat()

        if after:
            params['after'] = after.isoformat()

        if limit:
            params['limit'] = limit

        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/events',
            params=params
        )
        return response

    def delete_event(
            self,
            channel_id: str,
            event_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}'
        )
        return response

    def get_calendar_event_rsvp(
            self,
            channel_id: str,
            event_id: int,
            user_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}/rsvps/{user_id}'
        )
        return response

    def create_calendar_event_rsvp(
            self,
            channel_id: str,
            event_id: int,
            user_id: str,
            status: str
    ):
        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}/rsvps/{user_id}',
            json={'status': status}
        )
        return response

    def delete_calendar_event_rsvp(
            self,
            channel_id: str,
            event_id: int,
            user_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}/rsvps/{user_id}'
        )
        return response

    def get_calendar_event_rsvps(
            self,
            channel_id: str,
            event_id: int
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}/rsvps'
        )
        return response

    def create_announcement(self, channel_id: str, title: str, content: str):
        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/announcements',
            json={'title': title, 'content': content}
        )
        return response

    def get_announcement(self, channel_id: str, announcement_id: str):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}'
        )
        return response

    def get_announcements(self, channel_id: str, before: str = None, limit: str = None):
        params = {}
        if before:
            params['before'] = before
        if limit:
            params['limit'] = limit
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/announcements'
        )
        return response

    def update_announcement(self, channel_id: str, announcement_id: str, title: str = None, content: str = None):
        params = {}
        if title:
            params['title'] = title
        if content:
            params['content'] = content
        response = self.request(
            'PATCH',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}',
            json=params
        )
        return response

    def delete_announcement(self, channel_id: str, announcement_id: str):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}'
        )
        return response

    def create_announcement_comment(self, channel_id: str, announcement_id: str, content: str):
        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/comments',
            json={'content': content}
        )
        return response

    def get_announcement_comment(self, channel_id: str, announcement_id: str, comment_id: int):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/comments/{comment_id}'
        )
        return response

    def get_announcement_comments(self, channel_id: str, announcement_id: str):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/comments'
        )
        return response

    def update_announcement_comment(self, channel_id: str, announcement_id: str, comment_id: int, content: str):
        response = self.request(
            'PATCH',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/comments/{comment_id}',
            json={'content': content}
        )
        return response

    def delete_announcement_comment(self, channel_id: str, announcement_id: str, comment_id: int):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/comments/{comment_id}'
        )
        return response

    def create_webhook(
            self,
            server_id: str,
            channel_id: str,
            name: str
    ):
        response = self.request(
            'POST',
            f'{self.base_url}/servers/{server_id}/webhooks',
            json={'name': name, 'channel_id': channel_id}
        )
        return response

    def update_webhook(
            self,
            server_id: str,
            webhook_id: str,
            name: str,
            channel_id: str = None
    ):
        data = {'name': name}

        if channel_id:
            data.update({'channel_id': channel_id})

        response = self.request(
            'PUT',
            f'{self.base_url}/servers/{server_id}/webhooks/{webhook_id}',
            json=data
        )
        return response

    def delete_webhook(
            self,
            server_id: str,
            webhook_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/servers/{server_id}/webhooks/{webhook_id}'
        )
        return response

    def get_webhook(
            self,
            server_id: str,
            webhook_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/servers/{server_id}/webhooks/{webhook_id}'
        )
        return response

    def get_webhooks(
            self,
            server_id: str,
            channel_id: str
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/servers/{server_id}/webhooks',
            params={'channel_id': channel_id}
        )
        return response

    def send_webhook_message(
            self,
            server_id: str,
            webhook_id: str,
            content: str,
    ):
        token = self.get_webhook(server_id, webhook_id)['webhook']['token']

        response = self.request(
            'POST',
            f'https://media.guilded.gg/webhooks/{webhook_id}/{token}',
            json={'content': content}
        )
        return response

    def create_forum_topic(
            self,
            channel_id: str,
            title: str,
            content: str,
    ):

        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/topics',
            json={'title': title, 'content': content}
        )
        return response

    def get_forum_topics(
            self,
            channel_id: str,
            before: datetime = None,
            limit: int = None
    ):
        params = {}

        if before:
            params['before'] = before.isoformat()

        if limit:
            params['limit'] = limit

        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/topics',
            params=params
        )
        return response

    def get_forum_topic(
            self,
            channel_id: str,
            forum_topic_id: int
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}'
        )
        return response

    def update_forum_topic(
            self,
            channel_id: str,
            forum_topic_id: int,
            title: str = None,
            content: str = None,
    ):
        data = {}

        if content:
            data['content'] = content

        if title:
            data['title'] = title

        response = self.request(
            'PATCH',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}',
            json=data
        )
        return response

    def delete_forum_topic(
            self,
            channel_id: str,
            forum_topic_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}'
        )
        return response

    def pin_forum_topic(
            self,
            channel_id: str,
            forum_topic_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/pin'
        )
        return response

    def unpin_forum_topic(
            self,
            channel_id: str,
            forum_topic_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/pin'
        )
        return response

    def lock_forum_topic(
            self,
            channel_id: str,
            forum_topic_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/lock'
        )
        return response

    def unlock_forum_topic(
            self,
            channel_id: str,
            forum_topic_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/lock'
        )
        return response

    def create_forum_comment(
            self,
            channel_id: str,
            forum_topic_id: int,
            content: str,
    ):

        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/comments',
            json={'content': content}
        )
        return response

    def get_forum_comments(
            self,
            channel_id: str,
            forum_topic_id: int
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/comments'
        )
        return response

    def get_forum_comment(
            self,
            channel_id: str,
            forum_topic_id: int,
            forum_comment_id: int
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/comments/{forum_comment_id}'
        )
        return response

    def update_forum_comment(
            self,
            channel_id: str,
            forum_topic_id: int,
            forum_comment_id: int,
            content: str,
    ):

        response = self.request(
            'PATCH',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/comments/{forum_comment_id}',
            json={'content': content}
        )
        return response

    def delete_forum_comment(
            self,
            channel_id: str,
            forum_topic_id: int,
            forum_comment_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/topics/{forum_topic_id}/comments/'
            f'{forum_comment_id}'
        )
        return response

    def create_message_reaction(
            self,
            channel_id: str,
            message_id: str,
            emote_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/messages/{message_id}/emotes/{emote_id}'
        )
        return response

    def delete_message_reaction(
            self,
            channel_id: str,
            message_id: str,
            emote_id: int,
            user_id: str
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/messages/{message_id}/emotes/{emote_id}',
            params={'userId': user_id}
        )
        return response

    def create_topic_reaction(
            self,
            channel_id: str,
            topic_id: int,
            emote_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/topics/{topic_id}/emotes/{emote_id}'
        )
        return response

    def delete_topic_reaction(
            self,
            channel_id: str,
            topic_id: int,
            emote_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/topics/{topic_id}/emotes/{emote_id}'
        )
        return response

    def create_topic_comment_reaction(
            self,
            channel_id: str,
            topic_id: int,
            topic_comment_id: int,
            emote_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/topics/{topic_id}'
            f'{self.base_url}/comments/{topic_comment_id}/emotes/{emote_id}'
        )
        return response

    def delete_topic_comment_reaction(
            self,
            channel_id: str,
            topic_id: int,
            topic_comment_id: int,
            emote_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/topics/{topic_id}/comments/{topic_comment_id}/emotes/{emote_id}'
        )
        return response

    def create_event_reaction(
            self,
            channel_id: str,
            event_id: int,
            emote_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}/emotes/'
            f'{emote_id}'
        )
        return response

    def delete_event_reaction(
            self,
            channel_id: str,
            event_id: int,
            emote_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}/emotes/{emote_id}'
        )
        return response

    def create_event_comment_reaction(
            self,
            channel_id: str,
            event_id: int,
            comment_id: int,
            emote_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}/comments/{comment_id}/emotes/{emote_id}'
        )
        return response

    def delete_event_comment_reaction(
            self,
            channel_id: str,
            event_id: int,
            comment_id: int,
            emote_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/events/{event_id}'
            f'/comments/{comment_id}/emotes/{emote_id}'
        )
        return response

    def create_announcement_reaction(
            self,
            channel_id: str,
            announcement_id: str,
            emote_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/emotes/{emote_id}'
        )
        return response

    def delete_announcement_reaction(
            self,
            channel_id: str,
            announcement_id: str,
            emote_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/emotes/{emote_id}'
        )
        return response

    def create_announcement_comment_reaction(
            self,
            channel_id: str,
            announcement_id: str,
            comment_id: int,
            emote_id: int
    ):
        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/comments/{comment_id}/emotes/{emote_id}'
        )
        return response

    def delete_announcement_comment_reaction(
            self,
            channel_id: str,
            announcement_id: str,
            comment_id: int,
            emote_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/announcements/{announcement_id}/comments/{comment_id}/emotes/{emote_id}'
        )
        return response

    def create_doc(
            self,
            channel_id: str,
            title: str,
            content: str
    ):

        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/docs',
            json={'title': title, 'content': content}
        )
        return response

    def get_docs(
            self,
            channel_id: str,
            before: datetime = None,
            limit: int = None
    ):
        params = {}

        if before:
            params['before'] = before.isoformat()

        if limit:
            params['limit'] = limit

        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/docs',
            params=params
        )
        return response

    def get_doc(
            self,
            channel_id: str,
            doc_id: int
    ):
        response = self.request(
            'GET',
            f'{self.base_url}/channels/{channel_id}/docs/{doc_id}'
        )
        return response

    def update_doc(
            self,
            channel_id: str,
            doc_id: int,
            title: str,
            content: str,
    ):

        response = self.request(
            'PUT',
            f'{self.base_url}/channels/{channel_id}/docs/{doc_id}',
            json={'title': title, 'content': content}
        )
        return response

    def delete_doc(
            self,
            channel_id: str,
            doc_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/docs/{doc_id}'
        )
        return response

    def create_doc_comment(
            self,
            channel_id: str,
            doc_id: int,
            content: str,
    ):

        response = self.request(
            'POST',
            f'{self.base_url}/channels/{channel_id}/docs/{doc_id}/comments',
            json={'content': content}
        )
        return response

    def update_doc_comment(
            self,
            channel_id: str,
            doc_id: int,
            comment_id: int,
            content: str,
    ):

        response = self.request(
            'PATCH',
            f'{self.base_url}/channels/{channel_id}/docs/{doc_id}/comments/'
            f'{comment_id}',
            json={'content': content}
        )
        return response

    def delete_doc_comment(
            self,
            channel_id: str,
            doc_id: int,
            comment_id: int
    ):
        response = self.request(
            'DELETE',
            f'{self.base_url}/channels/{channel_id}/docs/{doc_id}/comments/'
            f'{comment_id}'
        )
        return response

    def get_bot_user_id(self):
        response = self.request('GET', f'{self.base_url}/users/@me')
        return response['user']['id']

    def get_user_servers(self, user_id: str):
        response = self.request('GET', f'{self.base_url}users/{user_id}/servers')
        return response

    def get_bot_servers(self):
        response = self.request('GET', f'{self.base_url}/users/@me/servers')
        return response

    def get_default_channel(self, server_id: str):
        r = self.request('GET', f'{self.base_url}/servers/{server_id}')
        try:
            print(r)
            response = r['server']['defaultChannelId']
        except:
            response = 'No default channel found'
        return response


    def create_group(self, server_id: str, name: str, description: str, emote_id: int, is_public: bool):
        response = self.request('POST', f'{self.base_url}/servers/{server_id}/groups', json={'name': name, 'description': description, 'emoteId': emote_id, 'isPublic': is_public})
        return response

    def get_groups(self, server_id: str):
        response = self.request('GET', f'{self.base_url}/servers/{server_id}/groups')
        return response


    def get_group(self, server_id: str, group_id: str):
        response = self.request('GET', f'{self.base_url}/servers/{server_id}/groups/{group_id}')
        return response

    def update_group(self, server_id: str, group_id: str, name: str, description: str, emote_id: int, is_public: bool):

        response = self.request('PATCH', f'{self.base_url}/servers/{server_id}/groups/{group_id}', json={'name': name, 'description': description, 'emoteId': emote_id, 'isPublic': is_public})
        return response


    def delete_group(self, server_id: str, group_id: str):
        response = self.request('DELETE', f'{self.base_url}/servers/{server_id}/groups/{group_id}')
        return response



    def update_status(self, content: str, emote_id: int):
        response = self.request('PUT', f'{self.base_url}/users/@me/status', json={'content': content, 'emoteId': emote_id})
        return response


    def delete_status(self):
        response = self.request('DELETE', f'{self.base_url}/users/@me/status')
        return response


    def member_has_role(self, server_id: str, user_id: str, role_id: int or list, type: str = 'any'):
        r = self.get_member_roles(server_id, user_id)
        if isinstance(role_id, list):
            if type == 'any':
                for i in role_id:
                    if i in r:
                        return True
                return False
            if type == 'all':
                for i in role_id:
                    if i not in r:
                        return False
                return True
        if role_id in r:
            return True
        else:
            return False

    def member_is_owner(self, server_id: str, user_id: str):
        r = self.get_server(server_id)
        if r['server']['ownerId'] == user_id:
            return True
        else:
            return False




