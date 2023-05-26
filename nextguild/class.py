class Data:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.id: str|int = self._get_id(event_data)
        self.user_id: str = self._get_user_id(event_data)
        self.server_id: str = self._get_server_id(event_data)
        self.channel_id: str = self._get_channel_id(event_data)

        #not done yet!
        self.created_by: str|None
        self.deleted_by: str|None
        self.owner_id: str|None
        self.type: str|None
        self.name: str|None
        self.url: str|None
        self.about: str|None
        self.avatar: str|None
        self.banner: str|None
        self.timezone: str|None
        self.is_verified: bool|None
        self.default_channel_id: str|None
        self.created_at: str|None
        self.updated_at: str|None
        self.content: str|None
        self.embeds: list|None
        self.reply_message_ids: list|None
        self.is_private: bool|None
        self.is_silent: bool|None
        self.mentions: list|None
        self.emote_id: int|None
        self.is_owner: bool|None
        self.nickname: str|None
        self.joined_at: str|None
        self.role_ids: list|None
        self.reason: str|None
        self.handle: str|None
        self.service_id: str|None
        self.token: str|None
        self.title: str|None
        self.updated_by: str|None
        self.doc_id: str|None
        self.bumped_at: str|None
        self.is_pinned: bool|None
        self.is_locked: bool|None
        self.status: str|None
        self.parent_list_item_id: str|None
        self.completed_at: str|None
        self.completed_by: str|None
        self.note: dict|None
        self.message_id: str|None
        self.parent_id: str|None
        self.is_home: bool|None
        self.is_public: bool|None
        self.archived_at: str|None
        self.archived_by: str|None

        #annoying
        self.description: str|None
        self.location: str|None
        self.color: int|None
        self.repeats: bool|None
        self.series_id: str|None
        self.rsvp_disabled: bool|None
        self.is_all_day: bool|None
        self.rsvp_limit: int|None
        self.autofill_waitlist: bool|None
        self.starts_at: str|None
        self.duration: int|None
        self.cancellation_description: str|None
        self.cancellation_created_by: str|None

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