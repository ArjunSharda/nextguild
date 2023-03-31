# -*- coding: utf-8 -*-
from os import getenv

from nextguild import Client, Events, Message

if __name__ == '__main__':
    BOT_TOKEN = getenv('BOT_TOKEN')
    if BOT_TOKEN is None:
        raise RuntimeError('Please set "BOT_TOKEN" variable')
    client = Client(BOT_TOKEN)
    events = Events(client)


    @events.on_ready
    async def on_ready():
        print('Ready!')


    @events.on_message
    async def ping_command(message: Message):
        if message.content.startswith('!ping'):
            client.send_message(message.channel_id, 'Pong!')


    events.run()
