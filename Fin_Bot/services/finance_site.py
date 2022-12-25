from urllib import response
import requests


class FinanceSiteService:
    limit = 5
    base_url = "http://127.0.0.1:8000/api/"

    def create_user(self, tier: dict):
        response = requests.post(f"{self.base_url}users/", data=tier)
        response.raise_for_status()
        return response.json()

    def get_users(self, page=1):
        query_params = dict(limit=self.limit, offset=(page - 1) * self.limit)
        response = requests.get(f"{self.base_url}users/", params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user(self, user_id):
        response = requests.get(f"{self.base_url}users/{user_id}/")
        response.raise_for_status()
        return response.json()
    
    def update_user(self, user_id, tier: dict):
        response = requests.patch(f"{self.base_url}users/{user_id}/", data=tier)
        # print("/" * 50)
        # print(response.content)
        # print("/" * 50)
        response.raise_for_status()
        return response.json()

    def get_events(self, page=1):
        query_params = dict(limit=self.limit, offset=(page - 1) * self.limit)
        response = requests.get(f"{self.base_url}event/", params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event(self, event_id):
            response = requests.get(f"{self.base_url}event/{event_id}/")
            response.raise_for_status()
            return response.json()

    def add_event(self, tier: dict):
        response = requests.post(f"{self.base_url}event/", data=tier)
        # print("/" * 50)
        # print(response.content)
        # print("/" * 50)
        response.raise_for_status()
        return response.json()


fin_service = FinanceSiteService()

