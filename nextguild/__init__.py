import requests
import json
import time

#all the files
import calendars
import channels
import docs
import essentials
import forums
import lists
import messages
import reactions
import servers
import users
import webhooks


class Client:

    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'User-Agent': 'NextGuild/1.0',
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        self.base_url = 'https://www.guilded.gg/api/v1'
        self.cache = {}