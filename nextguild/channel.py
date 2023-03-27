# -*- coding: utf-8 -*-


class Channel:
    def __init__(self, eventData: dict):
        self.eventData: dict = eventData
        self.channelId: str = eventData['channel']['id']
        self.channelName: str = eventData['channel']['name']
        self.channelType: str = eventData['channel']['type']
        self.serverId: str = eventData['serverId']
        self.groupId: str = eventData['channel']['groupId']
        self.createdBy: str = eventData['channel']['createdBy']
          
        
