import json
import time
import requests

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