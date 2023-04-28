# -*- coding: utf-8 -*-
from datetime import datetime


class UserSummary:
    def __init__(self, payload: dict):
        self.id: str = payload.get('id')
        # According to API docs if `type` is not preset it's 'user' by default
        self.type: str = payload.get('type', 'user')
        self.name: str = payload.get('name')
        self.avatar: str = payload.get('avatar', '')

    @property
    def is_bot(self) -> bool:
        return self.type == 'bot'


class User(UserSummary):
    def __init__(self, payload: dict):
        super().__init__(payload)
        self.banner: str = payload.get('banner', '')
        self.created_at: datetime = datetime.fromisoformat(
            payload.get('createdAt')
        )


class ServerMemberSummary:
    def __init__(self, payload: dict):
        self.user: UserSummary = UserSummary(payload.get('user'))
        self.role_ids: list[str] = payload.get('roleIds', [])


class ServerMember(ServerMemberSummary):
    def __init__(self, payload: dict):
        super().__init__(payload)
        # Overwritten intentionally as `User` inherits from `UserSummary`
        self.user: User = User(payload.get('user'))
        self.nickname: str = payload.get('nickname', '')
        self.joined_at: datetime = datetime.fromisoformat(
            payload.get('joinedAt')
        )
        self.is_owner: bool = payload.get('isOwner', False)

    @property
    def dispaly_name(self) -> str:
        return self.nickname or self.user.name
