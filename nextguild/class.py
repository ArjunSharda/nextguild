class Data:
    def __init__(self, event_data: dict):
        self.event_data: dict = event_data
        self.id: str|int = self._get_id(event_data)
        self.message_id: str = self._get_message_id(event_data)
        self.user_id: str = self._get_user_id(event_data)
        self.server_id: str = self._get_server_id(event_data)
        self.group_id: str = self._get_group_id(event_data)
        self.channel_id: str = self._get_channel_id(event_data)
        self.created_by: str = self._get_created_by(event_data)
        self.deleted_by: str|None
        self.owner_id: str = self._get_owner_id(event_data)
        self.type: str = self._get_type(event_data)
        self.name: str = self._get_name(event_data)
        self.url: str = self._get_url(event_data)
        self.about: str = self._get_about(event_data)
        self.avatar: str = self._get_avatar(event_data)
        self.banner: str = self._get_banner(event_data)
        self.timezone: str = self._get_timezone(event_data)
        self.is_verified: bool = self._get_is_verified(event_data)
        self.default_channel_id: str = self._get_default_channel_id(event_data)
        self.created_at: str = self._get_created_at(event_data)
        self.updated_at: str = self._get_updated_at(event_data)
        self.content: str = self._get_content(event_data)
        self.embeds: list = self._get_embeds(event_data)
        self.reply_message_ids: list = self._get_reply_message_ids(event_data)
        self.is_private: bool = self._get_is_private(event_data)
        self.is_silent: bool = self._get_is_silent(event_data)
        self.mentions: list = self._get_mentions(event_data)
        self.is_kick: bool = self._get_is_kick(event_data)
        self.is_ban: bool = self._get_is_ban(event_data)
        self.emote_id: int|None
        self.is_owner: bool|None
        self.nickname: str = self._get_nickname(event_data)
        self.joined_at: str|None
        self.role_ids: list = self._get_role_ids(event_data)
        self.reason: str = self._get_reason(event_data)
        self.handle: str = self._get_handle(event_data)
        self.service_id: str = self._get_service_id(event_data)
        self.token: str = self._get_token(event_data)
        self.title: str = self._get_title(event_data)
        self.updated_by: str = self._updated_by(event_data)
        self.doc_id: int = self._get_doc_id(event_data)
        self.bumped_at: str|None
        self.is_pinned: bool|None
        self.is_locked: bool|None
        self.status: str = self._get_status(event_data)
        self.status_emote: int = self._get_status_emote(event_data)
        self.completed_at: str|None
        self.completed_by: str|None
        self.note: dict|None
        self.message_id: str|None
        self.parent_id: str = self._get_parent_id(event_data)
        self.is_home: bool|None
        self.is_public: bool = self._get_is_public(event_data)
        self.archived_at: str|None
        self.archived_by: str|None
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
        self.topic: str = self._get_topic(event_data)
        self.root_id: str = self._get_root_id(event_data)
        self.category_id: int = self._get_category_id(event_data)

    def _scenario(self, event_data, scenarios):
        for scenario in scenarios:
            if len(scenario) == 1:
                data = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                data = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                data = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if len(scenario) == 4:
                data = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], {}).get(scenario[3], '')
            if data:
                return data
        return ''
    
    def _get_id(self, event_data: dict) -> str|int:
        scenarios = [
            ('serverMemberBan', 'user', 'id'),
            ('id'),
            ('message', 'id'),
            ('member', 'user', 'id'),
            ('userId'),
            ('userInfo', 'id'),
            ('channel', 'id'),
            ('webhook', 'id'),
            ('docs', 'id'),
            ('docComment', 'id'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_message_id(self, event_data: dict) -> str:
        scenarios = [
            ('channel', 'messageId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_user_id(self, event_data: dict) -> str:
        scenarios = [
            ('socialLink', 'userId'),
        ]
        return self._scenario(event_data, scenarios)

    def _get_server_id(self, event_data: dict) -> str:
        scenarios = [
            ('serverId'),
            ('server', 'id'),
            ('message', 'serverId'),
            ('webhook', 'serverId'),
            ('doc', 'serverId')
        ]
        return self._scenario(event_data, scenarios)
            
    def _get_group_id(self, event_data: dict) -> str:
        scenarios = [
            ('group', 'id'),
            ('message', 'groupId'),
            ('channel', 'groupId')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_channel_id(self, event_data: dict) -> str:
        scenarios = [
            ('message', 'channelId'),
            ('webhook', 'channelId'),
            ('doc', 'channelId'),
            ('docComment', 'channelId')
        ]
        return self._scenario(event_data, scenarios)

    def _get_created_by(self, event_data: dict) -> str:
        scenarios = [
            ('createdBy'),
            ('message', 'createdBy'),
            ('serverMemberBan', 'createdBy'),
            ('channel', 'createdBy'),
            ('webhook', 'createdBy'),
            ('doc', 'createdBy'),
            ('docComment', 'createdBy')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_owner_id(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'ownerId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_type(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'type'),
            ('message', 'type'),
            ('member', 'user', 'type'),
            ('serverMemberBan', 'user', 'type'),
            ('channel', 'type'),
            ('socialLink', 'type'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_name(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'name'),
            ('member', 'user', 'name'),
            ('serverMemberBan', 'user', 'name'),
            ('webhook', 'name'),
        ]
        return self._scenario(event_data, scenarios)
            
    def _get_url(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'url'),
        ]
        return self._scenario(event_data, scenarios)
            
    def _get_about(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'about'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_avatar(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'avatar'),
            ('member', 'user', 'avatar'),
            ('serverMemberBan', 'user', 'avatar'),
            ('webhook', 'avatar')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_banner(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'banner'),
            ('member', 'user', 'banner')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_timezone(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'timezone'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_verified(self, event_data: dict) -> bool:
        scenarios = [
            ('server', 'isVerified'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_default_channel_id(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'defaultChannelId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_created_at(self, event_data: dict) -> str:
        scenarios = [
            ('serverMemberBan', 'createdAt'),
            ('server', 'createdAt'),
            ('message', 'createdAt'),
            ('member', 'user', 'createdAt'),
            ('channel', 'createdAt'),
            ('socialLink', 'createdAt'),
            ('webhook', 'createdAt'),
            ('doc', 'createdAt'),
            ('docComment', 'createdAt')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_updated_at(self, event_data: dict) -> str:
        scenarios = [
            ('message', 'updatedAt'),
            ('doc', 'updatedAt'),
            ('docComment', 'updatedAt')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_content(self, event_data: dict) -> str:
        scenarios = [
            ('message', 'content'),
            ('doc', 'content'),
            ('docComment', 'content')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_embeds(self, event_data: dict) -> list:
        scenarios = [
            ('message', 'embeds'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_reply_message_ids(self, event_data: dict) -> list:
        scenarios = [
            ('message', 'replyMessageIds'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_private(self, event_data: dict) -> bool:
        scenarios = [
            ('message', 'isPrivate'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_silent(self, event_data: dict) -> bool:
        scenarios = [
            ('message', 'isSilent'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_mentions(self, event_data: dict) -> list:
        scenarios = [
            ('message', 'mentions'),
            ('doc', 'mentions'),
            ('docComment', 'mentions')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_status(self, event_data: dict) -> str:
        scenarios = [
            ('member', 'user', 'status', 'content'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_status_emote(self, event_data: dict) -> int:
        scenarios = [
            ('member', 'user', 'status', 'emoteId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_parent_id(self, event_data: dict) -> str:
        scenarios = [
            ('channel', 'parentId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_public(self, event_data: dict) -> bool:
        scenarios = [
            ('channel', 'isPublic'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_kick(self, event_data: dict) -> bool:
        scenarios = [
            ('isKick'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_ban(self, event_data: dict) -> bool:
        scenarios = [
            ('isBan'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_nickname(self, event_data: dict) -> str:
        scenarios = [
            ('userInfo', 'nickname'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_role_ids(self, event_data: dict) -> list:
        scenarios = [
            ('memberRoleIds'),
        ]
        return self._scenario(event_data, scenarios)

    def _get_reason(self, event_data: dict) -> str:
        scenarios = [
            ('serverMemberBan', 'reason'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_handle(self, event_data: dict) -> str:
        scenarios = [
            ('socialLink', 'handle'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_service_id(self, event_data: dict) -> str:
        scenarios = [
            ('socialLink', 'serviceId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_token(self, event_data: dict) -> str:
        scenarios = [
            ('webhook', 'token'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_title(self, event_data: dict) -> str:
        scenarios = [
            ('doc', 'title'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _updated_by(self, event_data: dict) -> str:
        scenarios = [
            ('doc', 'updatedBy'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_doc_id(self, event_data: dict) -> int:
        scenarios = [
            ('docComment', 'docId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_topic(self, event_data: dict) -> str:
        scenarios = [
            ('channel', 'topic'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_root_id(self, event_data: dict) -> str:
        scenarios = [
            ('channel', 'rootId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_category_id(self, event_data: dict) -> int:
        scenarios = [
            ('channel', 'categoryId'),
        ]
        return self._scenario(event_data, scenarios)