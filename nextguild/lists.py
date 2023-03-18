import essentials

def create_listitem(self, channelid, title, note=None):
    data = {'message': title}
    url = f'{self.base_url}/channels/{channelid}/items'
    if note:
        data.update({'note': {'content': note}})
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
        data.update({'message': title})
    if note:
        data.update({'note': {'content': note}})
    response = self.request('PUT', url, json=data)
    return response

def complete_listitem(self, channelid, listitemid):
    url = f'{self.base_url}/channels/{channelid}/items/{listitemid}/complete'
    response = self.request('POST', url)
    return response

def uncomplete_listitem(self, channelid, listitemid):
    url = f'{self.base_url}/channels/{channelid}/items/{listitemid}/complete'
    response = self.request('DELETE', url)
    return response
