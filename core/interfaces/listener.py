import requests


class Listener():

    def __init__(self, fetch_url='http://localhost:8000/getall'):
        self._fetch_url = fetch_url

    def send(self, data):
        pass

    def get(self):
        return requests.get(url=self._fetch_url).json()

