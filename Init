import requests
import json
import time
import os
import sys
import asyncio
import random
import datetime
import aiohttp

class client:
    def __init__(self, token):
        self.token = token
        self.session = requests.Session()
        self.headers = {
            'Authorization': f'Bot {self.token}',
            'User-Agent': 'NextGuild/1.0'
        }
        self.base_url = 'https://guilded.gg/api/v1'
        self.cache = {}

    async def send_message(self, channel_id, content):
        url = f'{self.base_url}/channels/{channel_id}/messages'
        data = {'content': content}
        response = await self.request('POST', url, data=data)
        return response

    async def delete_message(self, channel_id, message_id):
        url = f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
        response = await self.request('DELETE', url)
        return response

    async def edit_message(self, channel_id, message_id, content):
        url = f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
        data = {'content': content}
        response = await self.request('PATCH', url, data=data)
        return response

    async def purge(self, channel_id):
        messages = await self.get_channel_messages(channel_id)
        message_ids = [message['id'] for message in messages]
        for message_id in message_ids:
            await self.delete_message(channel_id, message_id)
        return len(message_ids)

    async def get_channel_messages(self, channel_id):
        if channel_id in self.cache:
            return self.cache[channel_id]
        else:
            url = f'{self.base_url}/channels/{channel_id}/messages'
            messages = []
            response = await self.request('GET', url)
            while response:
                messages.extend(response)
                last_message_id = response[-1]['id']
                response = await self.request('GET', url, params={'before': last_message_id})
            self.cache[channel_id] = messages
            return messages

    async def request(self, method, url, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=self.headers, **kwargs) as response:
                if response.status == 429:
                    retry_after = int(response.headers.get('retry-after', '1'))
                    print(f'Received 429 status. Retrying after {retry_after} seconds.')
                    await asyncio.sleep(retry_after)
                    return await self.request(method, url, **kwargs)
                else:
                    data = await response.json()
                    if 200 <= response.status < 300:
                        return data
                    else:
                        raise ValueError(f'Request failed with status {response.status}: {data}')
