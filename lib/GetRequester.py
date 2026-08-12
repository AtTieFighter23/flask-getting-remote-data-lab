import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send an HTTP GET request and return the raw response body."""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Parse the raw response body into a Python data structure."""
        return json.loads(self.get_response_body())