# -*- coding: utf-8 -*-
from channel import Channel
from client import Client
from embed import Embed
from events import Events
from message import Message
from reaction import Reaction, CalendarReaction, ForumTopicCommentReaction

bot = Client('gapi_sjBAH9mWdCJltCDfPzSs91xsfHh59JfoU1gKgUIyMYPbeBiknA2s3+up1UKSlGt5oig7dhn5rGv2AjPggOZUqg==')
events = Events(bot)

@events.on_ready
async def on_ready():
    print('Logged in!')

@events.on_message
async def on_message(message):
    print('Received message: ' + message.content)

events.run()