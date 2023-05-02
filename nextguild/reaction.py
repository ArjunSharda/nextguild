# -*- coding: utf-8 -*-
class Reaction:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.message_id: str = event_data.get('reaction', {}).get('messageId')
        self.server_id: str = event_data.get('serverId')
        self.channel_id: str = event_data.get('reaction', {}).get('channelId')
        self.user_id: str = event_data.get('reaction', {}).get('createdBy')
        self.emote_name: str = event_data.get('reaction', {}).get(
            'emote', {}
        ).get('name')
        self.emote_id: str = event_data.get('reaction', {}).get(
            'emote', {}
        ).get('id')
        self.emote_url: str = event_data.get('reaction', {}).get(
            'emote', {}
        ).get('url')


class CalendarReaction(Reaction):
    def __init__(self, event_data: dict):
        super().__init__(event_data)
        self.calendar_event_id: int = event_data.get('reaction', {}).get(
            'calendarEventId'
        )


class ForumTopicCommentReaction(Reaction):
    def __init__(self, event_data: dict):
        super().__init__(event_data)
        self.forum_topic_id: int = event_data.get(
            'reaction', {}
        ).get('forumTopicId')
        self.forum_topic_comment_id: int = event_data.get(
            'reaction', {}
        ).get('forumTopicCommentId')
