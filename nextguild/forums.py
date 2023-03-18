import essentials

def create_forum_post(self, channelid, title, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics'
    data = {'title': title, 'content': content}
    response = self.request('POST', url, json=data)
    return response

def get_forum_topics(self, channelid, before=None, limit=None):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics'
    params = {}
    if before:
        params['before'] = before
    if limit:
        params['limit'] = limit
    response = self.request('GET', url, params=params)
    return response

def get_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}'
    response = self.request('GET', url)
    return response

def update_forum_topic(self, channelid, forumtopicid, title=None, content=None):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}'
    data = {}
    if title:
        data['title'] = title
    if content:
        data['content'] = content
    response = self.request('PATCH', url, json=data)
    return response

def delete_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}'
    response = self.request('DELETE', url)
    return response

def pin_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/pin'
    response = self.request('PUT', url)
    return response

def unpin_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/pin'
    response = self.request('DELETE', url)
    return response

def lock_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/lock'
    response = self.request('PUT', url)
    return response

def unlock_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/lock'
    response = self.request('DELETE', url)
    return response

def create_forum_comment(self, channelid, forumtopicid, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments'
    data = {'content': content}
    response = self.request('POST', url, json=data)
    return response

def get_forum_comments(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments'
    response = self.request('GET', url)
    return response

def get_forum_comment(self, channelid, forumtopicid, forumcommentid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments/{forumcommentid}'
    response = self.request('GET', url)
    return response

def update_forum_comment(self, channelid, forumtopicid, forumcommentid, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments/{forumcommentid}'
    data = {'content': content}
    response = self.request('PATCH', url, json=data)
    return response

def delete_forum_comment(self, channelid, forumtopicid, forumcommentid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments/{forumcommentid}'
    response = self.request('DELETE', url)
    return response