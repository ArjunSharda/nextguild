import essentials


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
    response = self.request('GET', url, params=data)
    return response

def send_webhook_message(self, serverid, webhookid, content):
    webhookinformation = self.get_webhook(serverid, webhookid)
    token = webhookinformation['webhook']['token']
    url = f'https://media.guilded.gg/webhooks/{webhookid}/{token}'
    data = {'content': content}
    self.request('POST', url, json=data)
