import essentials


def create_channel(self, name, type, serverid,groupid=None, categoryid=None, ispublic=None):
    data = {'name': name, 'type': type}
    url = f'{self.base_url}/channels'
    if categoryid:
        data.update({'categoryId': categoryid})
    if groupid:
        data.update({'groupId': groupid})
    if serverid:
        data.update({'serverId': serverid})
    if ispublic:
        data.update({"isPublic": ispublic})
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
        data.update({'name': name})
    if topic:
        data.update({'topic': topic})
    if ispublic:
        data.update({'ispublic': ispublic})
    response = self.request('PATCH', url, json=data)
    return response