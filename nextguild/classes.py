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
        self.deleted_by = self._get_deleted_by(event_data)
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
        self.updated_by = self._get_updated_by(event_data)
        self.content = self._get_content(event_data)
        self.embeds = self._get_embeds(event_data)
        self.reply_message_ids = self._get_reply_message_ids(event_data)
        self.is_private = self._get_is_private(event_data)
        self.is_silent = self._get_is_silent(event_data)
        self.mentions = self._get_mentions(event_data)
        self.is_kick = self._get_is_kick(event_data)
        self.is_ban = self._get_is_ban(event_data)
        self.bumped_at = self._get_bumped_at(event_data)
        self.nickname = self._get_nickname(event_data)
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
        self.completed_at = self._get_completed_at(event_data)
        self.completed_by = self._get_completed_by(event_data)
        self.note = self._get_note(event_data)
        self.parent_id = self._get_parent_id(event_data)
        self.is_home = self._get_is_home(event_data)
        self.is_public = self._get_is_public(event_data)
        self.archived_at = self._get_archived_at(event_data)
        self.archived_by = self._get_archived_by(event_data)
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
        self.calendar_event_rsvps = self._get_calendar_event_rsvps(event_data)
        self.count = self._get_count(event_data)
        self.comment_id = self._get_comment_id(event_data)
        self.event_id = self._get_event_id(event_data)
        self.emote_id = self._get_emote_id(event_data)
        self.announcement_id = self._get_announcement_id(event_data)
        self.is_displayed_separately = self._get_is_displayed_separately(event_data)
        self.is_mentionable = self._get_is_mentionable(event_data)
        self.permissions = self._get_permissions(event_data)
        self.colors = self._get_colors(event_data)
        self.icon = self._get_icon(event_data)
        self.position = self._get_position(event_data)
        self.is_base = self._get_is_base(event_data)
        self.bot_user_id = self._get_bot_user_id(event_data)
        self.last_message_id = self._get_last_message_id(event_data)
        self.bot_id = self._get_bot_id(event_data)
        self.heartbeat_interval = self._get_heartbeat_interval(event_data)
        self.op = self._get_op(event_data)
        self.visibility = self._get_visibility(event_data)
        self.users = self._get_users(event_data)
        self.channels = self._get_channels(event_data)
        self.roles = self._get_roles(event_data)

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
                if data == 'Ann6LewA':
                    data = self._get_webhook_id(event_data)
                return data
        return 'None'
    
    def _get_id(self, event_data: dict):
        scenarios = [
            ('serverMemberBan', 'user', 'id'),
            ('id',),
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
            ('calendarEventRsvp', 'calendarEventId'),
            ('listItem', 'id'),
            ('calendarEventComment', 'id'),
            ('calendarEventSeries', 'id'),
            ('group', 'id'),
            ('announcement', 'id'),
            ('announcementComment', 'id'),
            ('role', 'id'),
            ('user', 'id'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_message_id(self, event_data: dict):
        scenarios = [
            ('channel', 'messageId'),
            ('reaction', 'messageId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_user_id(self, event_data: dict):
        scenarios = [
            ('socialLink', 'userId'),
            ('calendarEventRsvp', 'userId'),
            ('d', 'user', 'id'),
        ]
        return self._scenario(event_data, scenarios)

    def _get_server_id(self, event_data: dict):
        scenarios = [
            ('reaction', 'serverId'),
            ('serverId',),
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
            ('calendarEventRsvp', 'channelId'),
            ('listItem', 'channelId'),
            ('calendarEventComment', 'channelId'),
            ('calendarEventSeries', 'channelId'),
            ('announcement', 'channelId'),
            ('announcementComment', 'channelId'),
        ]
        return self._scenario(event_data, scenarios)

    def _get_created_by(self, event_data: dict):
        scenarios = [
            ('createdBy',),
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
            ('calendarEventRsvp', 'createdBy'),
            ('listItem', 'createdBy'),
            ('listItem', 'note', 'createdBy'),
            ('calendarEventComment', 'createdBy'),
            ('group', 'createdBy'),
            ('announcement', 'createdBy'),
            ('announcementComment', 'createdBy'),
            ('d', 'user', 'createdBy')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_deleted_by(self, event_data: dict):
        scenarios = [
            ('deletedBy',),
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
            ('d', 'user', 'type'),
            ('user', 'type'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_name(self, event_data: dict):
        scenarios = [
            ('server', 'name'),
            ('member', 'user', 'name'),
            ('serverMemberBan', 'user', 'name'),
            ('webhook', 'name'),
            ('calendarEvent', 'name'),
            ('reaction', 'emote', 'name'),
            ('group', 'name'),
            ('role', 'name'),
            ('d', 'user', 'name'),
            ('user', 'name'),
            ('nickname'),
            ('channel', 'name'),
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
            ('webhook', 'avatar'),
            ('group', 'avatar'),
            ('d', 'user', 'avatar'),
            ('user', 'avatar')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_banner(self, event_data: dict):
        scenarios = [
            ('server', 'banner'),
            ('member', 'user', 'banner'),
            ('d', 'user', 'banner')
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
            ('calendarEventRsvp', 'createdAt'),
            ('listItem', 'createdAt'),
            ('listItem', 'note', 'createdAt'),
            ('calendarEventComment', 'createdAt'),
            ('group', 'createdAt'),
            ('announcement', 'createdAt'),
            ('announcementComment', 'createdAt'),
            ('role', 'createdAt'),
            ('d', 'user', 'createdAt')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_updated_at(self, event_data: dict):
        scenarios = [
            ('message', 'updatedAt'),
            ('doc', 'updatedAt'),
            ('docComment', 'updatedAt'),
            ('forumTopicComment', 'updatedAt'),
            ('forumTopic', 'updatedAt'),
            ('calendarEventRsvp', 'updatedAt'),
            ('listItem', 'updatedAt'),
            ('listItem', 'note', 'updatedAt'),
            ('calendarEventComment', 'updatedAt'),
            ('group', 'updatedAt'),
            ('announcement', 'updatedAt'),
            ('role', 'updatedAt'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_updated_by(self, event_data: dict):
        scenarios = [
            ('group', 'updatedBy'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_content(self, event_data: dict):
        scenarios = [
            ('message', 'content'),
            ('doc', 'content'),
            ('docComment', 'content'),
            ('forumTopicComment', 'content'),
            ('forumTopic', 'content'),
            ('listItem', 'message'),
            ('listItem', 'note', 'content'),
            ('calendarEventComment', 'content'),
            ('announcement', 'content'),
            ('announcementComment', 'content'),
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
            ('listItem', 'mentions'),
            ('listItem', 'note', 'mentions'),
            ('calendarEventComment', 'mentions'),
            ('announcement', 'mentions'),
            ('announcementComment', 'mentions'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_status(self, event_data: dict):
        scenarios = [
            ('member', 'user', 'status', 'content'),
            ('calendarEventRsvp', 'status'),
            ('d', 'user', 'status', 'content')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_status_emote(self, event_data: dict):
        scenarios = [
            ('member', 'user', 'status', 'emoteId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_completed_at(self, event_data: dict):
        scenarios = [
            ('listItem', 'completedAt'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_completed_by(self, event_data: dict):
        scenarios = [
            ('listItem', 'completedBy'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_note(self, event_data: dict):
        scenarios = [
            ('listItem', 'note'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_parent_id(self, event_data: dict):
        scenarios = [
            ('channel', 'parentId'),
            ('listItem', 'parentListItemId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_home(self, event_data: dict):
        scenarios = [
            ('channel', 'isHome'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_public(self, event_data: dict):
        scenarios = [
            ('channel', 'isPublic'),
            ('group', 'isPublic'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_archived_at(self, event_data: dict):
        scenarios = [
            ('group', 'archivedAt'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_archived_by(self, event_data: dict):
        scenarios = [
            ('group', 'archivedBy'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_description(self, event_data: dict):
        scenarios = [
            ('calendarEvent', 'description'),
            ('group', 'description'),
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
            ('isKick',),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_ban(self, event_data: dict):
        scenarios = [
            ('isBan',),
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
            ('memberRoleIds',),
            ('calendarEvent', 'roleIds'),
            ('user', 'roleIds'),
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
            ('announcement', 'title'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _updated_by(self, event_data: dict):
        scenarios = [
            ('doc', 'updatedBy'),
            ('calendarEventRsvp', 'updatedBy'),
            ('listItem', 'updatedBy'),
            ('listItem', 'note', 'updatedBy'),
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
            ('forumTopicId',),
            ('forumTopicComment', 'forumTopicId'),
            ('reaction', 'forumTopicId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_calendar_event_rsvps(self, event_data: dict):
        scenarios = [
            ('calendarEventRsvps',),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_webhook_id(self, event_data: dict):
        scenarios = [
            ('listItem', 'createdByWebhookId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_count(self, event_data: dict):
        scenarios = [
            ('count',),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_comment_id(self, event_data: dict):
        scenarios = [
            ('reaction', 'forumTopicCommentId'),
            ('reaction', 'calendarEventCommentId'),
            ('reaction', 'docCommentId'),
            ('reaction', 'announcementCommentId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_event_id(self, event_data: dict):
        scenarios = [
            ('calendarEventComment', 'calendarEventId'),
            ('calendarEventId',),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_doc_id(self, event_data: dict):
        scenarios = [
            ('reaction', 'docId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_emote_id(self, event_data: dict):
        scenarios = [
            ('group', 'emoteId'),
            ('d', 'user', 'status', 'emoteId')
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_announcement_id(self, event_data: dict):
        scenarios = [
            ('reaction', 'announcementId'),
            ('announcementComment', 'announcementId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_displayed_separately(self, event_data: dict):
        scenarios = [
            ('role', 'isDisplayedSeparately'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_self_assignable(self, event_data: dict):
        scenarios = [
            ('role', 'isSelfAssignable'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_mentionable(self, event_data: dict):
        scenarios = [
            ('role', 'isMentionable'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_permissions(self, event_data: dict):
        scenarios = [
            ('role', 'permissions'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_colors(self, event_data: dict):
        scenarios = [
            ('role', 'colors'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_icon(self, event_data: dict):
        scenarios = [
            ('role', 'icon'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_icon(self, event_data: dict):
        scenarios = [
            ('role', 'icon'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_position(self, event_data: dict):
        scenarios = [
            ('role', 'position'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_is_base(self, event_data: dict):
        scenarios = [
            ('role', 'isBase'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_bot_user_id(self, event_data: dict):
        scenarios = [
            ('role', 'botUserId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_last_message_id(self, event_data: dict):
        scenarios = [
            ('d', 'lastMessageId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_bot_id(self, event_data: dict):
        scenarios = [
            ('d', 'botId'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_heartbeat_interval(self, event_data: dict):
        scenarios = [
            ('heartbeatInterval'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_op(self, event_data: dict):
        scenarios = [
            ('op'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_visibility(self, event_data: dict):
        scenarios = [
            ('visibility'),
            ('channel', 'visibility'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_users(self, event_data: dict):
        scenarios = [
            ('users'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_channels(self, event_data: dict):
        scenarios = [
            ('channels'),
        ]
        return self._scenario(event_data, scenarios)
    
    def _get_roles(self, event_data: dict):
        scenarios = [
            ('roles'),
        ]
        return self._scenario(event_data, scenarios)