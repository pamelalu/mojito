import requests, json

class Mandrill:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def send_message(self, Email):
        try:
            r = requests.post(
                self.api_url,
                data=json.dumps({
                    "key": self.api_key,
                    "message": {
                        "from_email": Email.from_email,
                        "from_name": Email.from_name,
                        'to': [{'email': Email.to_email,
                                'name': Email.to_name,
                                'type': 'to'}],
                        "subject": Email.subject,
                        "text": Email.body
                    }
                })
            )
            content = json.loads(r._content)

            if r.status_code != 200:
                return "Mandrill API status error: " + r.status_code
            if content[0]['status'] == 'rejected':
                return "Mandrill API status error: " + content[0]['status']
        except:
            return "Mandrill Send Mail Error"


