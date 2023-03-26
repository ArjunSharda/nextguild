# -*- coding: utf-8 -*-
import asyncio
import json
from functools import wraps

import websockets

from nextguild.client import Client
from nextguild.message import Message


class Events:
    def __init__(self, client: Client):
        self._message_create_handlers = []
        self._message_update_handlers = []
        self._message_delete_handlers = []
        self._member_join_handlers = []
        self._member_leave_handlers = []
        self._member_banned_handlers = []
        self._member_unbanned_handlers = []
        self._ready_handlers = []
        self.client = client

    def on_message(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_create_handlers.append(wrapper)
        return wrapper

    async def _handle_create_message(self, event_data: dict):
        message = Message(event_data)
        for handler in self._message_create_handlers:
            await handler(message)

    def on_message_update(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_update_handlers.append(wrapper)
        return wrapper

    async def _handle_update_message(self, event_data: dict):
        message = Message(event_data)
        for handler in self._message_update_handlers:
            await handler(message)

    def on_message_delete(self, func):
        @wraps(func)
        def wrapper(message):
            return func(message)

        self._message_delete_handlers.append(wrapper)
        return wrapper

    async def _handle_delete_message(self, event_data: dict):
        message = Message(event_data)
        for handler in self._message_delete_handlers:
            await handler(message)

    def on_member_join(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_join_handlers.append(wrapper)
        return wrapper

    async def _handle_member_join(self, event_data: dict):
        for handler in self._member_join_handlers:
            await handler(event_data)

    def on_member_leave(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_leave_handlers.append(wrapper)
        return wrapper

    async def _handle_member_leave(self, event_data: dict):
        for handler in self._member_leave_handlers:
            await handler(event_data)

    def on_member_banned(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_banned_handlers.append(wrapper)
        return wrapper

    async def _handle_member_banned(self, event_data: dict):
        for handler in self._member_banned_handlers:
            await handler(event_data)

    def on_member_unbanned(self, func):
        @wraps(func)
        def wrapper(member):
            return func(member)

        self._member_unbanned_handlers.append(wrapper)
        return wrapper

    async def _handle_member_unbanned(self, event_data: dict):
        for handler in self._member_unbanned_handlers:
            await handler(event_data)

    def on_ready(self, func):
        @wraps(func)
        async def wrapper():
            return await func()

        self._ready_handlers.append(wrapper)
        return wrapper

    async def _handle_ready(self):
        for handler in self._ready_handlers:
            await handler()

    async def start(self):
        async with websockets.connect(
                'wss://www.guilded.gg/websocket/v1',
                extra_headers={'Authorization': f'Bearer {self.client.token}'}
        ) as websocket:
            await self._handle_ready()
            while True:
                data = await websocket.recv()
                json_data = json.loads(data)

                if 't' in json_data and 'd' in json_data:
                    event_type: str = json_data['t']
                    event_data: dict = json_data['d']
                    event_handlers = {
                        'ChatMessageCreated': self._handle_create_message,
                        'ChatMessageUpdated': self._handle_update_message,
                        'ChatMessageDeleted': self._handle_delete_message,
                        'ServerMemberJoined': self._handle_member_join,
                        'ServerMemberRemoved': self._handle_member_leave,
                        'ServerMemberBanned': self._handle_member_banned,
                        'ServerMemberUnbanned': self._handle_member_unbanned,
                    }
                    handler = event_handlers.get(event_type)
                    if handler:
                        await handler(event_data)

    def run(self):
        try:
            asyncio.run(self.start())
        except KeyboardInterrupt:
            # TODO Handle standard exit
            pass


