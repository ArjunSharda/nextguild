# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Literal

ChannelsTypes = Literal['announcements', 'chat', 'calendar', 'forums', 'media',
                        'docs', 'voice', 'list', 'scheduling', 'stream']


class ServerChannel:
    def __init__(self, payload: dict):
        payload: dict = payload.get('channel', payload)
        self.id: str = payload.get('id')
        self.type: ChannelsTypes = payload.get('type')
        self.name: str = payload.get('name')
        self.topic: str = payload.get('topic')
        self.created_at: datetime = datetime.fromisoformat(
            payload.get('createdAt')
        )
        self.created_by: str = payload.get('createdBy')
        if (updated := payload.get('updatedAt')) is not None:
            self.updated_at: datetime = datetime.fromisoformat(updated)
        else:
            self.updated_at: datetime = self.created_at
        self.server_id: str = payload.get('serverId')
        self.parent_id: str = payload.get('parentId')
        self.category_id: str = payload.get('categoryId')
        self.group_id: str = payload.get('groupId')
        self.is_public: bool = payload.get('isPublic', False)
        self.archived_by: str = payload.get('archivedBy')
        if (archived := payload.get('archivedAt')) is not None:
            self.archived_at: datetime or None = datetime.fromisoformat(
                archived
            )
        else:
            self.archived_at: datetime or None = None
