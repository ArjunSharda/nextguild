# -*- coding: utf-8 -*-
class Reaction:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.server_id: str = event_data.get('serverId')
        self.channel_id: str = event_data.get('reaction', {}).get('channelId')
        self.user_id: str = event_data.get('reaction', {}).get('createdBy')
        self.emote_name: str = event_data.get('reaction', {}).get('emote', {}).get('name')
        self.emote_id: str = event_data.get('reaction', {}).get('emote', {}).get('id')
        self.emote_url: str = event_data.get('reaction', {}).get('emote', {}).get('url')


class CalendarReaction:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.server_id: str = event_data.get('serverId')
        self.channel_id: str = event_data.get('reaction', {}).get('channelId')
        self.user_id: str = event_data.get('reaction', {}).get('createdBy')
        self.emote_name: str = event_data.get('reaction', {}).get('emote', {}).get('name')
        self.emote_id: str = event_data.get('reaction', {}).get('emote', {}).get('id')
        self.emote_url: str = event_data.get('reaction', {}).get('emote', {}).get('url')
        self.calendar_event_id: str = event_data.get('reaction', {}).get('calendarEventId')

          
class ForumTopicCommentReaction:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.server_id: str = event_data.get('serverId')
        self.channel_id: str = event_data.get('reaction', {}).get('channelId')
        self.user_id: str = event_data.get('reaction', {}).get('createdBy')
        self.emote_name: str = event_data.get('reaction', {}).get('emote', {}).get('name')
        self.emote_id: str = event_data.get('reaction', {}).get('emote', {}).get('id')
        self.emote_url: str = event_data.get('reaction', {}).get('emote', {}).get('url')
        self.forum_topic_id: str = event_data.get('reaction', {}).get('forumTopicId')
        self.forum_topic_comment_id: str = event_data.get('reaction', {}).get('forumTopicCommentId')

 
