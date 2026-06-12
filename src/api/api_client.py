import requests

BASE_URL = "http://localhost:8000"

class TableSAAPI:
    def __init__(self):
        self.base_url = BASE_URL

    def get_restaurants(self):
        return requests.get(
            f"{self.base_url}/restaurants"
        ).json()

    def get_reservations(self):
        return requests.get(
            f"{self.base_url}/reservations"
        ).json()

    def create_reservation(self, data):
        return requests.post(
            f"{self.base_url}/reservations",
            json=data
        ).json()

    def register_user(self, data):
        return requests.post(
            f"{self.base_url}/register",
            json=data
        ).json()

    def login_user(self, email, password):
        return requests.post(
            f"{self.base_url}/login",
            json={
                "email": email,
                "password": password
            }
        ).json()
