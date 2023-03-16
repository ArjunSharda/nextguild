import requests
import json
import time
class Client:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'User-Agent': 'NextGuild/1.0'
        }
        self.base_url = 'https://www.guilded.gg/api/v1'
        self.cache = {}
    def send_message(self, channel_id, content, *replyids):
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
            data = response.json()
            if 200 <= response.status_code < 300:
                # Write response data to txt file
                #with open('response.txt', 'w') as f:
                    #f.write(json.dump(data, f))
                return data
            else:
                raise ValueError(f'Request failed with status {response.status_code}: {data}')
def main():
    my_client = Client('gapi_FmuNWwIb4I634q63K5y6J8uTT+acJm3fyjrDSBRPbCdM1aaRbk28hVLcP5WEkE/4sg6h7R23nJcD7luRggaqXg==')
    channel_id = 'cfc483c7-b88e-4f9c-92ba-56e30751f49c'
    m_id = ['e3217194-17bc-4447-a38a-d3ca04142d5d', '6db860a5-31a4-49a8-a5c9-3e8a68638f19']
    my_client.send_reply(channel_id, 'this is a reply', m_id)
    my_client.send_message(channel_id, 'and this is a message')
main()