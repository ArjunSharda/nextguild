class Data:
    def __init__(self, event_data: dict):
        self.event_data = event_data
        self.id = self._get_id(event_data)
        self.message_id = self._get_message_id(event_data)
        self.user_id = self._get_user_id(event_data)
        self.server_id = self._get_server_id(event_data)
        self.group_id = self._get_group_id(event_data)
        self.channel_id = self._get_channel_id(event_data)
        self.created_by = self._get_created_by(event_data)
        self.deleted_by
        self.owner_id = self._get_owner_id(event_data)
        self.type = self._get_type(event_data)
        self.name = self._get_name(event_data)
        self.url = self._get_url(event_data)
        self.about = self._get_about(event_data)
        self.avatar = self._get_avatar(event_data)
        self.banner = self._get_banner(event_data)
        self.timezone = self._get_timezone(event_data)
        self.is_verified = self._get_is_verified(event_data)
        self.default_channel_id = self._get_default_channel_id(event_data)
        self.created_at = self._get_created_at(event_data)
        self.updated_at = self._get_updated_at(event_data)
        self.content = self._get_content(event_data)
        self.embeds = self._get_embeds(event_data)
        self.reply_message_ids = self._get_reply_message_ids(event_data)
        self.is_private = self._get_is_private(event_data)
        self.is_silent = self._get_is_silent(event_data)
        self.mentions = self._get_mentions(event_data)
        self.is_kick = self._get_is_kick(event_data)
        self.is_ban = self._get_is_ban(event_data)
        self.is_owner
        self.bumped_at = self._get_bumped_at(event_data)
        self.nickname = self._get_nickname(event_data)
        self.joined_at
        self.role_ids = self._get_role_ids(event_data)
        self.reason = self._get_reason(event_data)
        self.handle = self._get_handle(event_data)
        self.service_id = self._get_service_id(event_data)
        self.token = self._get_token(event_data)
        self.title = self._get_title(event_data)
        self.updated_by = self._updated_by(event_data)
        self.doc_id = self._get_doc_id(event_data)
        self.is_pinned = self._get_is_pinned(event_data)
        self.is_locked = self._get_is_locked(event_data)
        self.status = self._get_status(event_data)
        self.status_emote = self._get_status_emote(event_data)
        self.completed_at
        self.completed_by
        self.note
        self.message_id
        self.parent_id = self._get_parent_id(event_data)
        self.is_home
        self.is_public = self._get_is_public(event_data)
        self.archived_at
        self.archived_by
        self.description = self._get_description(event_data)
        self.location = self._get_location(event_data)
        self.color = self._get_color(event_data)
        self.repeats = self._get_repeats(event_data)
        self.series_id = self._get_series_id(event_data)
        self.rsvp_disabled = self._get_rsvp_disabled(event_data)
        self.is_all_day = self._get_is_all_day(event_data)
        self.rsvp_limit = self._get_rsvp_limit(event_data)
        self.autofill_waitlist = self._get_autofill_waitlist(event_data)
        self.starts_at = self._get_starts_at(event_data)
        self.duration = self._get_duration(event_data)
        self.cancellation = self._get_cancellation(event_data)
        self.topic = self._get_topic(event_data)
        self.root_id = self._get_root_id(event_data)
        self.category_id = self._get_category_id(event_data)
        self.emote_server_id = self._get_original_server_id(event_data)
        self.topic_id = self._get_forum_topic_id(event_data)

    def _scenario(self, event_data, scenarios):
        data = ''
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
                if data == "true":
                    return True
                if data == "false":
                    return False
                return data
        return 'None'
    
    def _get_id(self, event_data: dict):
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
            ('calendarEvent', 'id'),
            ('reaction', 'emote', 'id'),
            ('forumTopicComment', 'id'),
            ('forumTopic', 'id'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_message_id(self, event_data: dict):
        scenarios = [
            ('channel', 'messageId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_user_id(self, event_data: dict):
        scenarios = [
            ('socialLink', 'userId'),
        ]
        return self._scenario(event_data, scenarios)

    def _get_server_id(self, event_data: dict):
        scenarios = [
            ('serverId'),
            ('server', 'id'),
            ('message', 'serverId'),
            ('webhook', 'serverId'),
            ('doc', 'serverId'),
            ('calendarEvent', 'serverId'),
        ]
        return self._scenario(event_data, scenarios)
            
    def _get_group_id(self, event_data: dict):
        scenarios = [
            ('group', 'id'),
            ('message', 'groupId'),
            ('channel', 'groupId')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_channel_id(self, event_data: dict):
        scenarios = [
            ('message', 'channelId'),
            ('webhook', 'channelId'),
            ('doc', 'channelId'),
            ('docComment', 'channelId'),
            ('calendarEvent', 'channelId'),
            ('reaction', 'channelId'),
            ('forumTopicComment', 'channelId'),
            ('forumTopic', 'channelId'),
        ]
        return self._scenario(event_data, scenarios)

    def _get_created_by(self, event_data: dict):
        scenarios = [
            ('createdBy'),
            ('message', 'createdBy'),
            ('serverMemberBan', 'createdBy'),
            ('channel', 'createdBy'),
            ('webhook', 'createdBy'),
            ('doc', 'createdBy'),
            ('docComment', 'createdBy'),
            ('calendarEvent', 'createdBy'),
            ('reaction', 'createdBy'),
            ('forumTopicComment', 'createdBy'),
            ('forumTopic', 'createdBy'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_owner_id(self, event_data: dict):
        scenarios = [
            ('server', 'ownerId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_type(self, event_data: dict):
        scenarios = [
            ('server', 'type'),
            ('message', 'type'),
            ('member', 'user', 'type'),
            ('serverMemberBan', 'user', 'type'),
            ('channel', 'type'),
            ('socialLink', 'type'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_name(self, event_data: dict):
        scenarios = [
            ('server', 'name'),
            ('member', 'user', 'name'),
            ('serverMemberBan', 'user', 'name'),
            ('webhook', 'name'),
            ('calendarEvent', 'name'),
            ('reaction', 'emote', 'name')
        ]
        return self._scenario(event_data, scenarios)
            
    def _get_url(self, event_data: dict):
        scenarios = [
            ('server', 'url'),
            ('calendarEvent', 'url'),
            ('reaction', 'emote', 'url')
        ]
        return self._scenario(event_data, scenarios)
            
    def _get_about(self, event_data: dict):
        scenarios = [
            ('server', 'about'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_avatar(self, event_data: dict):
        scenarios = [
            ('server', 'avatar'),
            ('member', 'user', 'avatar'),
            ('serverMemberBan', 'user', 'avatar'),
            ('webhook', 'avatar')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_banner(self, event_data: dict):
        scenarios = [
            ('server', 'banner'),
            ('member', 'user', 'banner')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_timezone(self, event_data: dict):
        scenarios = [
            ('server', 'timezone'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_verified(self, event_data: dict):
        scenarios = [
            ('server', 'isVerified'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_default_channel_id(self, event_data: dict):
        scenarios = [
            ('server', 'defaultChannelId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_created_at(self, event_data: dict):
        scenarios = [
            ('serverMemberBan', 'createdAt'),
            ('server', 'createdAt'),
            ('message', 'createdAt'),
            ('member', 'user', 'createdAt'),
            ('channel', 'createdAt'),
            ('socialLink', 'createdAt'),
            ('webhook', 'createdAt'),
            ('doc', 'createdAt'),
            ('docComment', 'createdAt'),
            ('calendarEvent', 'createdAt'),
            ('forumTopicComment', 'createdAt'),
            ('forumTopic', 'createdAt'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_updated_at(self, event_data: dict):
        scenarios = [
            ('message', 'updatedAt'),
            ('doc', 'updatedAt'),
            ('docComment', 'updatedAt'),
            ('forumTopicComment', 'updatedAt'),
            ('forumTopic', 'updatedAt'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_content(self, event_data: dict):
        scenarios = [
            ('message', 'content'),
            ('doc', 'content'),
            ('docComment', 'content'),
            ('forumTopicComment', 'content'),
            ('forumTopic', 'content'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_embeds(self, event_data: dict):
        scenarios = [
            ('message', 'embeds'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_reply_message_ids(self, event_data: dict):
        scenarios = [
            ('message', 'replyMessageIds'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_private(self, event_data: dict):
        scenarios = [
            ('message', 'isPrivate'),
            ('calendarEvent', 'isPrivate'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_silent(self, event_data: dict):
        scenarios = [
            ('message', 'isSilent'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_mentions(self, event_data: dict):
        scenarios = [
            ('message', 'mentions'),
            ('doc', 'mentions'),
            ('docComment', 'mentions'),
            ('calendarEvent', 'mentions'),
            ('forumTopicComment', 'mentions'),
            ('forumTopic', 'mentions'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_status(self, event_data: dict):
        scenarios = [
            ('member', 'user', 'status', 'content'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_status_emote(self, event_data: dict):
        scenarios = [
            ('member', 'user', 'status', 'emoteId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_parent_id(self, event_data: dict):
        scenarios = [
            ('channel', 'parentId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_public(self, event_data: dict):
        scenarios = [
            ('channel', 'isPublic'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_description(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'description'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_location(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'location'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_color(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'color'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_repeats(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'repeats'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_series_id(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'seriesId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_rsvp_disabled(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'rsvpDisabled'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_all_day(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'isAllDay'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_rsvp_limit(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'rsvpLimit'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_autofill_waitlist(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'autofillWaitlist'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_starts_at(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'startsAt'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_duration(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'duration'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_cancellation(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'cancellation'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_kick(self, event_data: dict):
        scenarios = [
            ('isKick'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_ban(self, event_data: dict):
        scenarios = [
            ('isBan'),
        ]
        return self._scenario(event_data, scenarios)

    def _get_bumped_at(self, event_data: dict):
        scenarios = [
            ('forumTopic', 'bumpedAt'),
        ]
        return self._scenario(event_data, scenarios)    
    
    def _get_nickname(self, event_data: dict):
        scenarios = [
            ('userInfo', 'nickname'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_role_ids(self, event_data: dict):
        scenarios = [
            ('memberRoleIds'),
            ('calendarEvent', 'roleIds'),
        ]
        return self._scenario(event_data, scenarios)

    def _get_reason(self, event_data: dict):
        scenarios = [
            ('serverMemberBan', 'reason'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_handle(self, event_data: dict):
        scenarios = [
            ('socialLink', 'handle'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_service_id(self, event_data: dict):
        scenarios = [
            ('socialLink', 'serviceId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_token(self, event_data: dict):
        scenarios = [
            ('webhook', 'token'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_title(self, event_data: dict):
        scenarios = [
            ('doc', 'title'),
            ('forumTopic', 'title'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _updated_by(self, event_data: dict):
        scenarios = [
            ('doc', 'updatedBy'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_doc_id(self, event_data: dict):
        scenarios = [
            ('docComment', 'docId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_pinned(self, event_data: dict):
        scenarios = [
            ('forumTopic', 'isPinned'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_locked(self, event_data: dict):
        scenarios = [
            ('forumTopic', 'isLocked'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_topic(self, event_data: dict):
        scenarios = [
            ('channel', 'topic'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_root_id(self, event_data: dict):
        scenarios = [
            ('channel', 'rootId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_category_id(self, event_data: dict):
        scenarios = [
            ('channel', 'categoryId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_original_server_id(self, event_data: dict):
        scenarios = [
            ('reaction', 'emote', 'serverId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_forum_topic_id(self, event_data: dict):
        scenarios = [
            ('forumTopicId'),
        ]
        return self._scenario(event_data, scenarios)