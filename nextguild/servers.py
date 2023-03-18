import essentials

def get_server(self, serverid):
    url = f'{self.base_url}/servers/{serverid}'
    response = self.request('GET', url)
    return response

def get_server_members(self, serverid):
    url = f'{self.base_url}/servers/{serverid}/members'
    response = self.request('GET', url)
    return response


def get_server_member(self, serverid, userid):
    url = f'{self.base_url}/servers/{serverid}/members/{userid}'
    response = self.request('GET', url)
    return response

def kick_member(self, serverid, userid):
    url = f'{self.base_url}/servers/{serverid}/members/{userid}'
    response = self.request('DELETE', url)
    return response


def ban_member(self, serverid, userid):
    url = f'{self.base_url}/servers/{serverid}/bans/{userid}'
    response = self.request('PUT', url)
    return response

def unban_member(self, serverid, userid):
    url = f'{self.base_url}/servers/{serverid}/bans/{userid}'
    response = self.request('DELETE', url)
    return response

def get_server_ban(self, serverid, userid):
    url = f'{self.base_url}/servers/{serverid}/bans/{userid}'
    response = self.request('GET', url)
    return response

def get_server_bans(self, serverid):
    url = f'{self.base_url}/servers/{serverid}/bans'
    response = self.request('GET', url)
    return response

def assign_role(self, serverid, userid, roleid):
    url = f'https://www.guilded.gg/api/v1/servers/{serverid}/members/{userid}/roles/{roleid}'
    response = self.request('PUT', url)
    return response

def remove_role(self, serverid, userid, roleid):
    url = f'https://www.guilded.gg/api/v1/servers/{serverid}/members/{userid}/roles/{roleid}'
    response = self.request('DELETE', url)
    return response

def get_roles(self, serverid, userid):
    url = f'https://www.guilded.gg/api/v1/servers/{serverid}/members/{userid}/roles'
    response = self.request('GET', url)
    return response

def assign_group(self, groupid, userid):
    url = f'https://www.guilded.gg/api/v1/groups/{groupid}/members/{userid}'
    response = self.request('PUT', url)
    return response
def remove_group(self, groupid, userid):
    url = f'https://www.guilded.gg/api/v1/groups/{groupid}/members/{userid}'
    response = self.request('DELETE', url)
    return response
def award_user_xp(self, serverid, userid, amount):
    url = f'{self.base_url}/servers/{serverid}/members/{userid}/xp'
    data = {'total': amount}
    response = self.request('PUT', url, json=data)
    return response
def set_user_xp(self, serverid, userid, total):
    url = f'{self.base_url}/servers/{serverid}/members/{userid}/xp'
    data = {'total': total}
    response = self.request('PUT', url, json=data)
    return response
def award_role_xp(self, serverid, roleid, amount):
    url = f'{self.base_url}/servers/{serverid}/roles/{roleid}/xp'
    data = {'amount': amount}
    response = self.request('POST', url, json=data)
    return response