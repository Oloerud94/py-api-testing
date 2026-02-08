from src.api.base_client import BaseApiClient

class UsersApi(BaseApiClient):
    endpoint = 'users'
    def create_user(self,payload):
        return self.post(self.endpoint, json=payload)

    def delete_user(self,userid):
        return self.delete(f'{self.endpoint}/{userid}')
