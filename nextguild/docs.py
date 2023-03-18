import essentials

def create_doc(self, channelid, title, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs'
    data = {'title': title, 'content': content}
    response = self.request('POST', url, json=data)
    return response

def get_docs(self, channelid, before=None, limit=None):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs'
    params = {}
    if before:
        params['before'] = before
    if limit:
        params['limit'] = limit
    response = self.request('GET', url, params=params)
    return response

def get_doc(self, channelid, docid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}'
    response = self.request('GET', url)
    return response

def update_doc(self, channelid, docid, title=None, content=None):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}'
    data = {}
    if title:
        data['title'] = title
    if content:
        data['content'] = content
    response = self.request('PUT', url, json=data)
    return response

def delete_doc(self, channelid, docid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}'
    response = self.request('DELETE', url)
    return response

def create_doc_comment(self, channelid, docid, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}/comments'
    data = {'content': content}
    response = self.request('POST', url, json=data)
    return response

def update_doc_comment(self, channelid, docid, commentid, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}/comments/{commentid}'
    data = {'content': content}
    response = self.request('PATCH', url, json=data)
    return response

def delete_doc_comment(self, channelid, docid, commentid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}/comments/{commentid}'
    response = self.request('DELETE', url)
    return response