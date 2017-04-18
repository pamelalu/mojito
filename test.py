from api import app
from api.model.email import Email
from api.model.mailgun import Mailgun

import unittest
import json

class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

        self.test_email = {
            "to": "pamelastone@gmail.com",
            "to_name": "Pam Lu",
            "from": "pamela.stone@gmail.com",
            "from_name": "Pam Sender",
            "subject": "A Message",
            "body": "<h1>Your Bill</h1><p>$10</p>"
        }

    def test_model_email(self):
        email = Email(self.test_email)
        assert email.to_email == self.test_email['to']
        assert email.to_name == self.test_email['to_name']
        assert email.from_email == self.test_email['from']
        assert email.from_name == self.test_email['from_name']
        assert email.subject == self.test_email['subject']
        assert b'Your Bill' in email.body
        assert email.is_valid == True

        email = Email({"to":"test"})
        assert email.is_valid == False

        email = Email({"to": "pamelastone@gmail.com"})
        assert email.is_valid == False

    def test_model_mailgun(self):
        test_url = 'test_url'
        test_key = 'test_key'
        mailgun = Mailgun(test_url, test_key)
        assert mailgun.api_url == test_url
        assert mailgun.api_key == test_key

    def test_api_get_email(self):
        data = self.app.get('/email')
        assert data._status_code == 405

    def test_api_post_email(self):
        r = self.app.post('/email', data = json.dumps(self.test_email), content_type='application/json')
        assert r._status_code == 200

        self.test_email_bad = {
            "to": "pamelastone@gmail.com",
            "to_name": "Pam Lu",
            "from": "pamela.stone@gmail.com",
            "from_name": "Pam Sender"
        }

        r = self.app.post('/email', data=json.dumps(self.test_email_bad), content_type='application/json')
        assert r._status_code == 400


if __name__ == '__main__':
    unittest.main()