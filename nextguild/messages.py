import essentials

class message:

    def content(self, message):
        return message['message']['content']

    def author(self, message):
        return message['message']['author']['username']

    def id(self, message):
        return message['message']['id']



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
    params = {}
    if limit:
        params['limit'] = limit
    if before:
        params['before'] = before
    if after:
        params['after'] = after
    if includePrivate:
        params['includePrivate'] = includePrivate
    response = self.request('GET', url, params=params)
    return response

def purge(self, channel_id, amount):
    messages = self.get_channel_messages(channel_id, amount)
    message_ids = [msg['id'] for msg in messages['messages']]
    for message_id in message_ids:
        self.delete_message(channel_id, message_id)
    return len(message_ids)