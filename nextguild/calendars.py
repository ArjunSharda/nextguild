import essentials

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

def delete_event(self, channelid, eventid):
    url = f'{self.base_url}/channels/{channelid}/events/{eventid}'
    response = self.request('DELETE', url)
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