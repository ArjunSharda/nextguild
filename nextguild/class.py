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
        self.handle: str|None
        self.service_id: str|None
        self.token: str|None
        self.title: str|None
        self.updated_by: str|None
        self.doc_id: str|None
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
    
    def _get_id(self, event_data: dict) -> str|int:
        scenarios = [
            ('serverMemberBan', 'user', 'id'),
            ('id'),
            ('message', 'id'),
            ('member', 'user', 'id'),
            ('userId'),
            ('userInfo', 'id'),
            ('channel', 'id'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                id = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if id:
                return id
        return ''
    
    def _get_message_id(self, event_data: dict) -> str:
        scenarios = [
            ('channel', 'messageId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                message_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                message_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if message_id:
                return message_id
        return ''

    def _get_server_id(self, event_data: dict) -> str:
        scenarios = [
            ('serverId'),
            ('server', 'id'),
            ('message', 'serverId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                server_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                server_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if server_id:
                return server_id
            
    def _get_group_id(self, event_data: dict) -> str:
        scenarios = [
            ('group', 'id'),
            ('message', 'groupId'),
            ('channel', 'groupId')
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                group_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                group_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if group_id:
                return group_id
        return ''
    
    def _get_channel_id(self, event_data: dict) -> str:
        scenarios = [
            ('message', 'channelId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                channel_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                channel_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if channel_id:
                return channel_id
        return ''

    def _get_created_by(self, event_data: dict) -> str:
        scenarios = [
            ('createdBy'),
            ('message', 'createdBy'),
            ('serverMemberBan', 'createdBy'),
            ('channel', 'createdBy'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                created_by = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                created_by = event_data.get(scenario[0], {}).get(scenario[1], '')
            if created_by == 'Ann6LewA':
                created_by = event_data.get('message', {}).get('createdByWebhookId', '')
            if created_by:
                return created_by
        return ''
    
    def _get_owner_id(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'ownerId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                owner_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                owner_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if owner_id:
                return owner_id
        return ''
    
    def _get_type(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'type'),
            ('message', 'type'),
            ('member', 'user', 'type'),
            ('serverMemberBan', 'user', 'type'),
            ('channel', 'type'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                type = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                type = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                type = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if type:
                return type
        return ''
    
    def _get_name(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'name'),
            ('member', 'user', 'name'),
            ('serverMemberBan', 'user', 'name')
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                name = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                name = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                name = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if name:
                return name
        return ''
            
    def _get_url(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'url'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                url = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                url = event_data.get(scenario[0], {}).get(scenario[1], '')
            if url:
                return url
        return ''
            
    def _get_about(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'about'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                about = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                about = event_data.get(scenario[0], {}).get(scenario[1], '')
            if about:
                return about
        return ''
    
    def _get_avatar(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'avatar'),
            ('member', 'user', 'avatar'),
            ('serverMemberBan', 'user', 'avatar')
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                avatar = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                avatar = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                avatar = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if avatar:
                return avatar
        return ''
    
    def _get_banner(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'banner'),
            ('member', 'user', 'banner')
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                banner = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                banner = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                banner = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if banner:
                return banner
        return ''
    
    def _get_timezone(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'timezone'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                timezone = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                timezone = event_data.get(scenario[0], {}).get(scenario[1], '')
            if timezone:
                return timezone
        return ''
    
    def _get_is_verified(self, event_data: dict) -> bool:
        scenarios = [
            ('server', 'isVerified'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                is_verified = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                is_verified = event_data.get(scenario[0], {}).get(scenario[1], '')
            if is_verified:
                return is_verified
        return ''
    
    def _get_default_channel_id(self, event_data: dict) -> str:
        scenarios = [
            ('server', 'defaultChannelId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                default_channel_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                default_channel_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if default_channel_id:
                return default_channel_id
        return ''
    
    def _get_created_at(self, event_data: dict) -> str:
        scenarios = [
            ('serverMemberBan', 'createdAt'),
            ('server', 'createdAt'),
            ('message', 'createdAt'),
            ('member', 'user', 'createdAt'),
            ('channel', 'createdAt'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                created_at = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                created_at = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                created_at = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if created_at:
                return created_at
        return ''
    
    def _get_updated_at(self, event_data: dict) -> str:
        scenarios = [
            ('message', 'updatedAt'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                updated_at = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                updated_at = event_data.get(scenario[0], {}).get(scenario[1], '')
            if updated_at:
                return updated_at
        return ''
    
    def _get_content(self, event_data: dict) -> str:
        scenarios = [
            ('message', 'content'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                content = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                content = event_data.get(scenario[0], {}).get(scenario[1], '')
            if content:
                return content
        return ''
    
    def _get_embeds(self, event_data: dict) -> list:
        scenarios = [
            ('message', 'embeds'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                embeds = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                embeds = event_data.get(scenario[0], {}).get(scenario[1], '')
            if embeds:
                return embeds
        return ''
    
    def _get_reply_message_ids(self, event_data: dict) -> list:
        scenarios = [
            ('message', 'replyMessageIds'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                reply_message_ids = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                reply_message_ids = event_data.get(scenario[0], {}).get(scenario[1], '')
            if reply_message_ids:
                return reply_message_ids
        return ''
    
    def _get_is_private(self, event_data: dict) -> bool:
        scenarios = [
            ('message', 'isPrivate'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                is_private = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                is_private = event_data.get(scenario[0], {}).get(scenario[1], '')
            if is_private:
                return is_private
        return ''
    
    def _get_is_silent(self, event_data: dict) -> bool:
        scenarios = [
            ('message', 'isSilent'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                is_silent = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                is_silent = event_data.get(scenario[0], {}).get(scenario[1], '')
            if is_silent:
                return is_silent
        return ''
    
    def _get_mentions(self, event_data: dict) -> list:
        scenarios = [
            ('message', 'mentions'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                mentions = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                mentions = event_data.get(scenario[0], {}).get(scenario[1], '')
            if mentions:
                return mentions
        return ''
    
    def _get_status(self, event_data: dict) -> str:
        scenarios = [
            ('member', 'user', 'status', 'content'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                status = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                status = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                status = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if len(scenario) == 4:
                status = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], {}).get(scenario[3], '')
            if status:
                return status
        return ''
    
    def _get_status_emote(self, event_data: dict) -> int:
        scenarios = [
            ('member', 'user', 'status', 'emoteId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                status_emote = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                status_emote = event_data.get(scenario[0], {}).get(scenario[1], '')
            if len(scenario) == 3:
                status_emote = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], '')
            if len(scenario) == 4:
                status_emote = event_data.get(scenario[0], {}).get(scenario[1], {}).get(scenario[2], {}).get(scenario[3], '')
            if status_emote:
                return status_emote
        return ''
    
    def _get_parent_id(self, event_data: dict) -> str:
        scenarios = [
            ('channel', 'parentId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                parent_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                parent_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if parent_id:
                return parent_id
        return ''
    
    def _get_is_public(self, event_data: dict) -> bool:
        scenarios = [
            ('channel', 'isPublic'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                is_public = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                is_public = event_data.get(scenario[0], {}).get(scenario[1], '')
            if is_public:
                return is_public
        return ''
    
    def _get_is_kick(self, event_data: dict) -> bool:
        scenarios = [
            ('isKick'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                is_kick = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                is_kick = event_data.get(scenario[0], {}).get(scenario[1], '')
            if is_kick:
                return is_kick
        return ''
    
    def _get_is_ban(self, event_data: dict) -> bool:
        scenarios = [
            ('isBan'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                is_ban = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                is_ban = event_data.get(scenario[0], {}).get(scenario[1], '')
            if is_ban:
                return is_ban
        return ''
    
    def _get_nickname(self, event_data: dict) -> str:
        scenarios = [
            ('userInfo', 'nickname'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                nickname = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                nickname = event_data.get(scenario[0], {}).get(scenario[1], '')
            if nickname:
                return nickname
        return ''
    
    def _get_role_ids(self, event_data: dict) -> list:
        scenarios = [
            ('memberRoleIds'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                role_ids = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                role_ids = event_data.get(scenario[0], {}).get(scenario[1], '')
            if role_ids:
                return role_ids
        return ''

    def _get_reason(self, event_data: dict) -> str:
        scenarios = [
            ('serverMemberBan', 'reason'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                reason = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                reason = event_data.get(scenario[0], {}).get(scenario[1], '')
            if reason:
                return reason
        return ''
    
    def _get_topic(self, event_data: dict) -> str:
        scenarios = [
            ('channel', 'topic'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                topic = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                topic = event_data.get(scenario[0], {}).get(scenario[1], '')
            if topic:
                return topic
        return ''
    
    def _get_root_id(self, event_data: dict) -> str:
        scenarios = [
            ('channel', 'rootId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                root_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                root_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if root_id:
                return root_id
        return ''
    
    def _get_category_id(self, event_data: dict) -> int:
        scenarios = [
            ('channel', 'categoryId'),
        ]
        for scenario in scenarios:
            if len(scenario) == 1:
                category_id = event_data.get(scenario[0], '')
            if len(scenario) == 2:
                category_id = event_data.get(scenario[0], {}).get(scenario[1], '')
            if category_id:
                return category_id
        return ''