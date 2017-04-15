import requests
from api import app

class Mailgun:
    def __init__(self):
        self.api_url = app.config['MAILGUN_SEND_ENDPOINT']
        self.api_key = app.config['MAILGUN_API_KEY']

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