# -*- coding: utf-8 -*-
def get_ids(x: list[dict]) -> list:
    return list(map(lambda y: y.get('id'), x))


class Mentions:
    def __init__(self, payload: dict):
        self.users: list[dict[str, str]] = payload.get('users', [])
        self.channels: list[dict[str, str]] = payload.get('channels', [])
        self.roles: list[dict[str, str]] = payload.get('roles', [])
        self.everyone: bool = payload.get('everyone', False)
        self.here: bool = payload.get('here', False)

    @property
    def users_ids(self) -> list[str]:
        return get_ids(self.users)

    @property
    def channels_ids(self) -> list[str]:
        return get_ids(self.channels)

    @property
    def roles_ids(self) -> list[str]:
        return get_ids(self.roles)
