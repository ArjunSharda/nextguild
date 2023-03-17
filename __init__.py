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

    def get_channel_messages(self, channel_id):
        if channel_id in self.cache:
            return self.cache[channel_id]
        else:
            url = f'{self.base_url}/channels/{channel_id}/messages'
            messages = []
            response = self.request('GET', url)
            while response:
                messages.extend(response)
                last_message_id = response
                response = self.request('GET', url, params={'before': last_message_id})
            self.cache[channel_id] = messages
            return messages

    def purge(self, channel_id, amount):
        messages = self.get_channel_messages(channel_id)[:amount]
        message_ids = [message['id'] for message in messages]
        for message_id in message_ids:
            self.delete_message(channel_id, message_id)
        return len(message_ids)

    def request(self, method, url, **kwargs):
        response = requests.request(method, url, headers=self.headers, **kwargs)
        if response.status_code == 429:
            retry_after = int(response.headers.get('retry-after', '1'))
            print(f'Received 429 status. Retrying after {retry_after} seconds.')
            time.sleep(retry_after)
            return self.request(method, url, **kwargs)
        else:
            try:
                data = response.json()
            except json.JSONDecodeError:
                data = response.text
            if 200 <= response.status_code < 300:
                # Write response data to txt file
                # with open('response.txt', 'w') as f:
                # f.write(json.dump(data, f))
                return data
            else:
                raise ValueError(f'Request failed with status {response.status_code}: {data}')

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

    def get_server_members(self, serverid):
        url = f'{self.base_url}/servers/{serverid}/members'
        response = self.request('GET', url)
        return response

    def update_nickname(self, serverid, userid, nickname):
        url = f'{self.base_url}/servers/{serverid}/members/{userid}/nickname'
        data = {'nickname': nickname}
        response = self.request('PUT', url, json=data)
        return response


    def delete_nickname(self, serverid, userid):
        url = f'{self.base_url}/servers/{serverid}/members/{userid}/nickname'
        response = self.request('DELETE', url)
        return response

    def get_server_member(self, serverid, userid):
        url = f'{self.base_url}/servers/{serverid}/members/{userid}'
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

    def create_webhook(self, serverid, channelid, name):
        url = f'{self.base_url}/servers/{serverid}/webhooks'
        data = {'name': name, 'channelId': channelid}
        response = self.request('POST', url, json=data)
        return response

    def update_webhook(self, serverid, webhookid, name, channelid=None):
        url = f'https://www.guilded.gg/api/v1/servers/{serverid}/webhooks/{webhookid}'
        data = {'name': name}
        if channelid:
            data.update({'channelId': channelid})
        response = self.request('PUT', url, json=data)
        return response

    def delete_webhook(self, serverid, webhookid):
        url = f'https://www.guilded.gg/api/v1/servers/{serverid}/webhooks/{webhookid}'
        response = self.request('DELETE', url)
        return response

    def get_webhook(self, serverid, webhookid):
        url = f'https://www.guilded.gg/api/v1/servers/{serverid}/webhooks/{webhookid}'
        response = self.request('GET', url)
        return response

    def get_webhooks(self, serverid, channelid):
        url = f'https://www.guilded.gg/api/v1/servers/{serverid}/webhooks'
        data = {'channelId': channelid}
        response = self.request('GET', url, json=data)
        return response

    def send_webhook_message(self, serverid, webhookid, content):
        webhookinformation = self.get_webhook(serverid, webhookid)
        token = webhookinformation['webhook']['token']
        url = f'https://media.guilded.gg/webhooks/{webhookid}/{token}'
        data = {'content': content}
        self.request('POST', url, json=data)



class message:
    def content(self, message):
        return message['message']['content']

    def author(self, message):
        return message['message']['author']['username']

    def id(self, message):
        return message['message']['id']


