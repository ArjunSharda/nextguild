# -*- coding: utf-8 -*-


class Channel:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.channel_id: str = event_data.get('channel', {}).get('id')
        self.channel_name: str = event_data.get('channel', {}).get('name')
        self.channel_type: str = event_data.get('channel', {}).get('type')
        self.server_id: str = event_data.get('serverId')
        self.group_id: str = event_data.get('channel', {}).get('groupId')
        self.created_by: str = event_data.get('channel', {}).get('createdBy')
