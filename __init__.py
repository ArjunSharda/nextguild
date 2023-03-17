import requests
import json
import time
from typing import Optional
class Client:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'User-Agent': 'NextGuild/1.0'
        }
        self.base_url = 'https://www.guilded.gg/api/v1'
        self.cache = {}
    def send_message(self, channel_id, content):
        url = f'{self.base_url}/channels/{channel_id}/messages'
        data = {'content': content}
        response = self.request('POST', url, json=data)
        return response
    def send_reply(self, channel_id, content, replyids):
        url = f'{self.base_url}/channels/{channel_id}/messages'
        data = {'content': content, 'replyMessageIds': replyids}
        response = self.request('POST', url, json=data)
        return response
    def edit_message(self, channel_id, message_id, content):
        url = f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
        data = {'content': content}
        response = self.request('PUT', url, json=data)
        return response
    def delete_message(self, channel_id, message_id):
     url = f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
     response = self.request('DELETE', url)
     return response
    def get_message(self, channel_id, message_id):
        url = f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
        response = self.request('GET', url)
        return response
    def get_channel_messages(self, channel_id, limit=None, before=None, after=None, includePrivate=None):
        url = f'{self.base_url}/channels/{channel_id}/messages'
        data = {}
        if limit:
            data.update({'limit': limit})
        if before:
            data.update({'before': before})
        if after:
            data.update({'after': after})
        if includePrivate:
            data.update({'includePrivate': includePrivate})
        response = self.request('GET', url, data=data)
        return response
    def purge(self, channel_id, amount):
     messages = self.get_channel_messages(channel_id, amount)
     message_ids = [msg['id'] for msg in messages['messages']]
     for message_id in message_ids:
        self.delete_message(channel_id, message_id)
     return len(message_ids)
    def request(self, method, url, **kwargs):
        response = requests.request(method, url, headers=self.headers, **kwargs)
        if response.status_code == 429:
            time.sleep(response.json()['retryAfter'])
            response = self.request(method, url, **kwargs)
        return response.json()



    def create_channel(self, name, type, serverid, groupid=None, categoryid=None, ispublic=None):
        data = {'name': name, 'type': type}
        url = f'{self.base_url}/channels'
        if categoryid:
            categoryid = {'categoryId': categoryid}
            data.update(categoryid)
        if groupid:
            groupid = {'groupId': groupid}
            data.update(groupid)
        if serverid:
            serverid = {'serverId': serverid}
            data.update(serverid)
        if ispublic:
            ispublic = {"isPublic": ispublic}
            data.update(ispublic)
        response = self.request('POST', url, json=data)
        return response
    def get_channel(self, channelid):
        url = f'{self.base_url}/channels/{channelid}'
        response = self.request('GET', url)
        return response
    def delete_channel(self, channelid):
        url = f'{self.base_url}/channels/{channelid}'
        response = self.request('DELETE', url)
        return response
    def update_channel(self, channelid, name=None, topic=None, ispublic=None):
        data = {}
        url = f'{self.base_url}/channels/{channelid}'
        if name:
            name = {'name': name}
            data.update(name)
        if topic:
            topic = {'topic': topic}
            data.update(topic)
        if ispublic:
            ispublic = {'ispublic': ispublic}
            data.update(ispublic)
        response = self.request('PATCH', url, json=data)
        return response
    def get_server(self, serverid):
        url = f'{self.base_url}/servers/{serverid}'
        response = self.request('GET', url)
        return response
    def create_listitem(self, channelid, title, note=None):
        data = {'message': title}
        url = f'{self.base_url}/channels/{channelid}/items'
        if note:
            note = {'note': {'content': note}}
            data.update(note)
        response = self.request('POST', url, json=data)
        return response
    def get_listitem(self, channelid, listitemid):
        url = f'{self.base_url}/channels/{channelid}/items/{listitemid}'
        response = self.request('GET', url)
        return response
    def get_listitems(self, channelid):
        url = f'{self.base_url}/channels/{channelid}/items'
        response = self.request('GET', url)
        return response
    def delete_listitem(self, channelid, listitemid):
        url = f'{self.base_url}/channels/{channelid}/items/{listitemid}'
        response = self.request('DELETE', url)
        return response
    def update_listitem(self, channelid, listitemid, title, note=None):
        data = {}
        url = f'{self.base_url}/channels/{channelid}/items/{listitemid}'
        if title:
            title = {'message': title}
            data.update(title)
        if note:
            note = {'note': {'content': note}}
            data.update(note)
        response = self.request('PUT', url, json=data)
        return response
    def complete_listitem(self, channelid, listitemid):
        url = f'{self.base_url}/channels/{channelid}/items/{listitemid}/complete'
        response = self.request('POST', url)
        return response
