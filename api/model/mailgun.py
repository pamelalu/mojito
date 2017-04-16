import requests
from api import app

class Mailgun:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def send_message(self, Email):
        data = {
            "from": Email.from_email,
            "to": Email.to_email,
            "subject": Email.subject,
            "text": Email.body
        }

        return requests.post(
            self.api_url,
            auth=("api", self.api_key),
            data={
                "from": Email.from_email,
                "to": Email.to_email,
                "subject": Email.subject,
                "text": Email.body
            }
        )