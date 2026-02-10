import requests
from src.config import config

class BaseApiClient:
    def __init__(self, base_url = None, api_key = None):
        self.base_url = config.BASE_URL
        self.api_key = api_key or config.API_KEY
        self.session = requests.Session()
        self._set_headers()

    def _set_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        if self.api_key:
            headers['X-Api-Key'] = self.api_key

        self.session.headers.update(headers)

    def set_api_key(self, api_key):
        self.api_key = api_key
        self._set_headers()

    def request(self, method, endpoint, **kwargs):
        url = f'{self.base_url}/{endpoint}'
        response = self.session.request(method, url, **kwargs)
        # response.raise_for_status()
        return response

    def get(self, endpoint, **kwargs):
        return self.request('GET', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request('POST', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request('DELETE', endpoint, **kwargs)