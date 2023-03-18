import essentials

def get_user(self, userid):
    url = f'https://www.guilded.gg/api/v1/users/{userid}'
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

def get_user_social(self, serverid, userid, socialtype):
    url = f'{self.base_url}/servers/{serverid}/members/{userid}/social-links/{socialtype}'
    response = self.request('GET', url)
    return response
