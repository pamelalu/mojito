import requests
from api import app

class Mailgun:
    def __init__(self):
        self.api_url = "https://api.mailgun.net/v3/"+ app.config['MAILGUN_DOMAIN'] +"/messages"
        self.api_key = app.config['MAILGUN_API_KEY']
        self.domain_name = app.config['MAILGUN_DOMAIN']

    def send_message(self, Email):
        data = {"from": Email.from_email,
                  "to": Email.to_email,
                  "subject": Email.subject,
                  "text": Email.body}
        url = self.api_url
        api = self.api_key

        print data

        #return requests.post(
        #    self.api_url,
        #   auth=("api", self.api_key),
        #    data={"from": Email.from_email,
        #          "to": Email.to_email,
        #          "subject": Email.title,
    #          "text": Email.body})