import requests
import json
import time


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

  def send_message(self, channel_id, content):
    url = f'{self.base_url}/channels/{channel_id}/messages'
    data = {'content': content}
    response = self.request('POST', url, json=data)
    return response

  def send_reply(self, channel_id, content, replyids):
    url = f'{self.base_url}/channels/{channel_id}/messages'
    data = {'content': content, 'replyMessageIds': replyids}
    response = self.request('POST', url, json=data)
    return response

  def edit_message(self, channel_id, message_id, content):
    url = f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
    data = {'content': content}
    response = self.request('PUT', url, json=data)
    return response

  def delete_message(self, channel_id, message_id):
    url = f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
    response = self.request('DELETE', url)
    return response

  def get_message(self, channel_id, message_id):
    url = f'{self.base_url}/channels/{channel_id}/messages/{message_id}'
    response = self.request('GET', url)
    return response

  def get_channel_messages(self,
                           channel_id,
                           limit=None,
                           before=None,
                           after=None,
                           includePrivate=None):
    url = f'{self.base_url}/channels/{channel_id}/messages'
    params = {}
    if limit:
      params['limit'] = limit
    if before:
      params['before'] = before
    if after:
      params['after'] = after
    if includePrivate:
      params['includePrivate'] = includePrivate
    response = self.request('GET', url, params=params)
    return response

  def purge(self, channel_id, amount):
    messages = self.get_channel_messages(channel_id, amount)
    message_ids = [msg['id'] for msg in messages['messages']]
    for message_id in message_ids:
      self.delete_message(channel_id, message_id)
    return len(message_ids)

  def request(self, method, url, **kwargs):
    response = requests.request(method, url, headers=self.headers, **kwargs)
    if response.status_code == 429:
      retry_after = int(response.headers.get('retry-after', '1'))
      print(f'Received 429 status. Retrying after {retry_after} seconds.')
      time.sleep(retry_after)
      return self.request(method, url, **kwargs)
    else:
      try:
        data = response.json()
      except json.JSONDecodeError:
        data = response.text
      if 200 <= response.status_code < 300:
        return data
      else:
        raise ValueError(
          f'Request failed with status {response.status_code}: {data}')

  def create_channel(self,
                     name,
                     type,
                     serverid,
                     groupid=None,
                     categoryid=None,
                     ispublic=None):
    data = {'name': name, 'type': type}
    url = f'{self.base_url}/channels'
    if categoryid:
      data.update({'categoryId': categoryid})
    if groupid:
      data.update({'groupId': groupid})
    if serverid:
      data.update({'serverId': serverid})
    if ispublic:
      data.update({"isPublic": ispublic})
    response = self.request('POST', url, json=data)
    return response

  def get_channel(self, channelid):
    url = f'{self.base_url}/channels/{channelid}'
    response = self.request('GET', url)
    return response

  def delete_channel(self, channelid):
    url = f'{self.base_url}/channels/{channelid}'
    response = self.request('DELETE', url)
    return response

  def update_channel(self, channelid, name=None, topic=None, ispublic=None):
    data = {}
    url = f'{self.base_url}/channels/{channelid}'
    if name:
      data.update({'name': name})
    if topic:
      data.update({'topic': topic})
    if ispublic:
      data.update({'ispublic': ispublic})
    response = self.request('PATCH', url, json=data)
    return response

  def get_server(self, serverid):
    url = f'{self.base_url}/servers/{serverid}'
    response = self.request('GET', url)
    return response

  def get_server_members(self, serverid):
    url = f'{self.base_url}/servers/{serverid}/members'
    response = self.request('GET', url)
    return response

  def update_nickname(self, serverid, userid, nickname):
    url = f'{self.base_url}/servers/{serverid}/members/{userid}/nickname'
    data = {'nickname': nickname}
    response = self.request('PUT', url, json=data)
    return response

  def delete_nickname(self, serverid, userid):
    url = f'{self.base_url}/servers/{serverid}/members/{userid}/nickname'
    response = self.request('DELETE', url)
    return response

  def get_server_member(self, serverid, userid):
    url = f'{self.base_url}/servers/{serverid}/members/{userid}'
    response = self.request('GET', url)
    return response

  def create_listitem(self, channelid, title, note=None):
    data = {'message': title}
    url = f'{self.base_url}/channels/{channelid}/items'
    if note:
      data.update({'note': {'content': note}})
    response = self.request('POST', url, json=data)
    return response

  def get_listitem(self, channelid, listitemid):
    url = f'{self.base_url}/channels/{channelid}/items/{listitemid}'
    response = self.request('GET', url)
    return response

  def get_listitems(self, channelid):
    url = f'{self.base_url}/channels/{channelid}/items'
    response = self.request('GET', url)
    return response

  def delete_listitem(self, channelid, listitemid):
    url = f'{self.base_url}/channels/{channelid}/items/{listitemid}'
    response = self.request('DELETE', url)
    return response

  def update_listitem(self, channelid, listitemid, title, note=None):
    data = {}
    url = f'{self.base_url}/channels/{channelid}/items/{listitemid}'
    if title:
      data.update({'message': title})
    if note:
      data.update({'note': {'content': note}})
    response = self.request('PUT', url, json=data)
    return response

  def complete_listitem(self, channelid, listitemid):
    url = f'{self.base_url}/channels/{channelid}/items/{listitemid}/complete'
    response = self.request('POST', url)
    return response

  def uncomplete_listitem(self, channelid, listitemid):
    url = f'{self.base_url}/channels/{channelid}/items/{listitemid}/complete'
    response = self.request('DELETE', url)
    return response

  def create_event(self, channelid, title, **args):
    """
        Creates an event in the chosen channel.
        Args:
            name: The name of the event (min length 1; max length 60)
            description: The description of the event (min length 1; max length 8000) [OPTIONAL]
            location: The location of the event (min length 1; max length 8000) [OPTIONAL]
            startsAt: The ISO 8601 timestamp that the event starts at [OPTIONAL]
            url: A URL to associate with the event [OPTIONAL]
            color: The color of the event when viewing in the calendar (min 0; max 16777215) [INTEGER] [OPTIONAL]
            isAllDay: Does the event last all day? If passed with duration, duration will only be applied if it is an interval of minutes represented in days (e.g., duration: 2880) example: "true" or "false" [OPTIONAL]
            rsvpLimit: The number of RSVPs to allow before waitlisting RSVPs (min 1)
            autofillWaitlist: When rsvpLimit is set, users from the waitlist will be added as space becomes available in the event. example: "true" or "false" [OPTIONAL]
            duration: The duration of the event in minutes (min 1) [INTEGER] [OPTIONAL]
            isPrivate: Whether or not the event is private. example: "true" or "false" [OPTIONAL, public by default]
            roleIds: The role IDs to restrict the event to (min items 1; must have unique items true). [ARRAY] [OPTIONAL]
                repeatinfo below [OPTIONAL]:
                    type: How often you want your event to repeat (important note: this will repeat for the next 180 days unless custom is defined) (default once)
                        string ("once", "everyDay", "everyWeek", "everyMonth", or "custom") 
                    every: Apply further clarification to your events. This must have type set to custom. [OPTIONAL]
                        count: How often between your interval the event should repeat. For example, 1 would be every interval, 2 would be every second occurrence of the interval. [NUMBER]
                        interval: Coupled with count, this indicates the time range you are repeating your event over
                            string ("day", "month", "year", or "week")
                    endsAfterOccurrences: Used to control the end date of the event repeat (only used when type is custom; if used with endDate, the earliest resultant date of the two will be used) (max 24) [NUMBER] [OPTIONAL]
                    endDate: The ISO 8601 timestamp that the event ends at. Used to control the end date of the event repeat (only used when type is custom; if used with endsAfterOccurrences, the earliest resultant date of the two will be used) [OPTIONAL]
                    on: Used to control the day of the week that the event should repeat on (only used when type is custom and when every.interval is week) (min items 1) [OPTIONAL]
                        string[] ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", or "saturday")
        Returns:
            A description of what the function returns, if applicable.
        """
    data = {'name': title}
    eurl = f'{self.base_url}/channels/{channelid}/events'
    for key, value in args.items():
      data.update({key: value})
    response = self.request('POST', eurl, json=data)
    return response

  def get_events(self, channelid, before=None, after=None, limit=None):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/events'
    params = {}
    if before:
      params['before'] = before
    if after:
      params['after'] = after
    if limit:
      params['limit'] = limit
    response = self.request('GET', url, params=params)
    return response

  def create_webhook(self, serverid, channelid, name):
    url = f'{self.base_url}/servers/{serverid}/webhooks'
    data = {'name': name, 'channelId': channelid}
    response = self.request('POST', url, json=data)
    return response

  def update_webhook(self, serverid, webhookid, name, channelid=None):
    url = f'https://www.guilded.gg/api/v1/servers/{serverid}/webhooks/{webhookid}'
    data = {'name': name}
    if channelid:
      data.update({'channelId': channelid})
    response = self.request('PUT', url, json=data)
    return response

  def delete_webhook(self, serverid, webhookid):
    url = f'https://www.guilded.gg/api/v1/servers/{serverid}/webhooks/{webhookid}'
    response = self.request('DELETE', url)
    return response

  def get_webhook(self, serverid, webhookid):
    url = f'https://www.guilded.gg/api/v1/servers/{serverid}/webhooks/{webhookid}'
    response = self.request('GET', url)
    return response

  def get_webhooks(self, serverid, channelid):
    url = f'https://www.guilded.gg/api/v1/servers/{serverid}/webhooks'
    data = {'channelId': channelid}
    response = self.request('GET', url, params=data)
    return response

  def send_webhook_message(self, serverid, webhookid, content):
    webhookinformation = self.get_webhook(serverid, webhookid)
    token = webhookinformation['webhook']['token']
    url = f'https://media.guilded.gg/webhooks/{webhookid}/{token}'
    data = {'content': content}
    self.request('POST', url, json=data)

  def create_forum_post(self, channelid, title, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics'
    data = {'title': title, 'content': content}
    response = self.request('POST', url, json=data)
    return response

  def get_forum_topics(self, channelid, before=None, limit=None):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics'
    params = {}
    if before:
      params['before'] = before
    if limit:
      params['limit'] = limit
    response = self.request('GET', url, params=params)
    return response

  def get_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}'
    response = self.request('GET', url)
    return response

  def update_forum_topic(self, channelid, forumtopicid, title=None, content=None):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}'
    data = {}
    if title:
      data['title'] = title
    if content:
      data['content'] = content
    response = self.request('PATCH', url, json=data)
    return response

  def delete_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}'
    response = self.request('DELETE', url)
    return response

  def pin_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/pin'
    response = self.request('PUT', url)
    return response

  def unpin_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/pin'
    response = self.request('DELETE', url)
    return response

  def lock_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/lock'
    response = self.request('PUT', url)
    return response

  def unlock_forum_topic(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/lock'
    response = self.request('DELETE', url)
    return response

  def create_forum_comment(self, channelid, forumtopicid, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments'
    data = {'content': content}
    response = self.request('POST', url, json=data)
    return response

  def get_forum_comments(self, channelid, forumtopicid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments'
    response = self.request('GET', url)
    return response

  def get_forum_comment(self, channelid, forumtopicid, forumcommentid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments/{forumcommentid}'
    response = self.request('GET', url)
    return response

  def update_forum_comment(self, channelid, forumtopicid, forumcommentid, content):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments/{forumcommentid}'
    data = {'content': content}
    response = self.request('PATCH', url, json=data)
    return response

  def delete_forum_comment(self, channelid, forumtopicid, forumcommentid):
    url = f'https://www.guilded.gg/api/v1/channels/{channelid}/topics/{forumtopicid}/comments/{forumcommentid}'
    response = self.request('DELETE', url)
    return response


    
class message:

  def content(self, message):
    return message['message']['content']

  def author(self, message):
    return message['message']['author']['username']

  def id(self, message):
    return message['message']['id']


def get_id(obj):
  if isinstance(obj, dict):
    for key, value in obj.items():
      if key == 'id':
        return value
      else:
        result = get_id(value)
        if result is not None:
          return result
  elif isinstance(obj, list):
    for item in obj:
      result = get_id(item)
      if result is not None:
        return result
