import requests

class Mailgun:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def send_message(self, Email):
        try:
            r = requests.post(
                self.api_url,
                auth=("api", self.api_key),
                data={
                    "from": Email.from_name + " <" + Email.from_email + ">",
                    "to": Email.to_name + " <" + Email.to_email + ">",
                    "subject": Email.subject,
                    "text": Email.body
                    }
                )
            if (r.status_code != 200):
                return "MAILGUN API status error: " + r.status_code
        except:
            return "MAILGUN SEND EMAIL ERROR"