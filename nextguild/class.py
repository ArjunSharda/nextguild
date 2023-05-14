class Data:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.id: str|int = self._get_id(event_data)
        self.user_id: str = self._get_user_id(event_data)
        self.server_id: str = self._get_server_id(event_data)
        self.channel_id: str = self._get_channel_id(event_data)

    def _get_user_id(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'createdBy'),
            ('server', 'deletedBy'),
            ('message', 'createdBy'),
            ('member', 'user', 'id'),
            ('userId'),
            ('serverMemberBan', 'user', 'id'),
            ('userInfo', 'id'),
            ('memberRoleIds', 'userId'),
            ('channel', 'createdBy'),
            ('socialLink', 'userId'),
            ('webhook', 'createdBy'),
            ('doc', 'createdBy'),
            ('docComment', 'createdBy'),
            ('calendarEvent', 'createdBy'),
            ('forumTopic', 'createdBy'),
            ('reaction', 'createdBy'),
            ('forumTopicComment', 'createdBy'),
            ('calendarEventRsvp', 'userId'),
            ('listItem', 'createdBy'),
            ('calendarEventComment', 'createdBy'),
            ('group', 'createdBy'),
            ('announcement', 'createdBy'),
            ('announcementComment', 'createdBy')

        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                user_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                user_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            elif len(scenario) == 3:
                user_id = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if user_id:
                return user_id
        return ''
    
    def _get_id(self, event_data: dict) -> str|int:
        scenarios = [
            ('message', 'id'),
            ('channel', 'id'),
            ('webhook', 'id'),
            ('doc', 'id'),
            ('docComment', 'id'),
            ('calendarEvent', 'id'),
            ('forumTopic', 'id'),
            ('forumTopicComment', 'id'),
            ('listItem', 'id'),
            ('calendarEventComment', 'id'),
            ('calendarEventSeries', 'id'),
            ('group', 'id'),
            ('announcement', 'id')
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                id = event_data.get(scenario[0], {}).get(scenario[1], '')
            elif len(scenario) == 3:
                id = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if id:
                return id
        return ''

    def _get_server_id(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'id'),
            ('serverId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                server_id = event_data.get(scenario[0], '')
            elif len(scenario) == 2:
                server_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if server_id:
                return server_id
        return ''
    
    def _get_channel_id(self, event_data: dict) -> str:
        scenarios = [
            ('message', 'channelId'),
            ('channel', 'id'),
            ('webhook', 'channelId'),
            ('doc', 'channelId'),
            ('docComment', 'channelId'),
            ('calendarEvent', 'channelId'),
            ('forumTopic', 'channelId'),
            ('forumTopicComment', 'channelId'),
            ('reaction', 'channelId'),
            ('calendarEventRsvp', 'channelId'),
            ('listItem', 'channelId'),
            ('channelId'),
            ('calendarEventComment', 'channelId'),
            ('calendarEventSeries', 'channelId'),
            ('announcement', 'channelId'),
            ('announcementComment', 'channelId')
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                channel_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                channel_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            elif len(scenario) == 3:
                channel_id = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if channel_id:
                return channel_id
        return ''