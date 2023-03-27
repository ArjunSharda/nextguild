# -*- coding: utf-8 -*-

class Reaction:
    def __init__(self, eventData: dict):
        print(eventData)
        self.eventData: dict = eventData
        self.serverId: str = eventData['serverId']
        self.channelId: str = eventData['reaction']['channelId']
        self.userId: str = eventData['reaction']['createdBy']
        self.emote_name: str = eventData['reaction']['emote']['name']
        self.emoteid: str = eventData['reaction']['emote']['id']
        self.emote_url: str = eventData['reaction']['emote']['url']


class CalendarReaction:
    def __init__(self, eventData: dict):
        print(eventData)
        self.eventData: dict = eventData
        self.serverId: str = eventData['serverId']
        self.channelId: str = eventData['reaction']['channelId']
        self.userId: str = eventData['reaction']['createdBy']
        self.emote_name: str = eventData['reaction']['emote']['name']
        self.emoteid: str = eventData['reaction']['emote']['id']
        self.emote_url: str = eventData['reaction']['emote']['url']
        self.calendar_event_id: str = eventData['reaction']['calendarEventId']

          
 



class ForumTopicCommentReaction:
    def __init__(self, eventData: dict):
        self.eventData: dict = eventData
        self.serverId: str = eventData['serverId']
        self.channelId: str = eventData['reaction']['channelId']
        self.userId: str = eventData['reaction']['createdBy']
        self.emote_name: str = eventData['reaction']['emote']['name']
        self.emoteid: str = eventData['reaction']['emote']['id']
        self.emote_url: str = eventData['reaction']['emote']['url']
        self.forumTopicId: str = eventData['reaction']['forumTopicId']
        self.forumTopicCommentId: str = eventData['reaction']['forumTopicCommentId']

          
          
          
          
 
