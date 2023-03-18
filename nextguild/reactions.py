import essentials

def create_reaction(self, channelid, contentid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/content/{contentid}/emotes/{emoteid}'
    response = self.request('PUT', url)
    return response

def delete_reaction(self, channelid, contentid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/content/{contentid}/emotes/{emoteid}'
    response = self.request('DELETE', url)
    return response

def create_topic_reaction(self, channelid, topicid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{topicid}/emotes/{emoteid}'
    response = self.request('PUT', url)
    return response

def delete_topic_reaction(self, channelid, topicid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{topicid}/emotes/{emoteid}'
    response = self.request('DELETE', url)
    return response

def create_topic_comment_reaction(self, channelid, topicid, topiccommentid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{topicid}/comments/{topiccommentid}/emotes/{emoteid}'
    response = self.request('PUT', url)
    return response

def delete_topic_comment_reaction(self, channelid, topicid, topiccommentid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{topicid}/comments/{topiccommentid}/emotes/{emoteid}'
    response = self.request('DELETE', url)
    return response

def create_event_reaction(self, channelid, eventid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/events/{eventid}/emotes/{emoteid}'
    response = self.request('PUT', url)
    return response

def delete_event_reaction(self, channelid, eventid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/events/{eventid}/emotes/{emoteid}'
    response = self.request('DELETE', url)
    return response

def create_event_comment_reaction(self, channelid, eventid, commentid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/events/{eventid}/comments/{commentid}/emotes/{emoteid}'
    response = self.request('PUT', url)
    return response

def delete_event_comment_reaction(self, channelid, eventid, commentid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/events/{eventid}/comments/{commentid}/emotes/{emoteid}'
    response = self.request('DELETE', url)
    return response

def create_doc_reaction(self, channelid, docid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}/emotes/{emoteid}'
    response = self.request('PUT', url)
    return response

def delete_doc_reaction(self, channelid, docid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}/emotes/{emoteid}'
    response = self.request('DELETE', url)
    return response

def create_doc_comment_reaction(self, channelid, docid, commentid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}/comments/{commentid}/emotes/{emoteid}'
    response = self.request('PUT', url)
    return response

def delete_doc_comment_reaction(self, channelid, docid, commentid, emoteid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/docs/{docid}/comments/{commentid}/emotes/{emoteid}'
    response = self.request('DELETE', url)
    return response