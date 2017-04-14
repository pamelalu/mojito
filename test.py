from api import app
from api.email import Email

import unittest
import json

class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

        self.test_email = {
            "to": "pamelastone@gmail.com",
            "to_name": "Pam Lu",
            "from": "pamela.stone@gmail.com",
            "from_name": "Pam Sender",
            "subject": "A Message",
            "body": "1"
        }

    def test_model_email(self):
        email = Email(self.test_email)
        assert email.to_email == self.test_email['to']
        assert email.to_name == self.test_email['to_name']
        assert email.from_email == self.test_email['from']
        assert email.from_name == self.test_email['from_name']
        assert email.subject == self.test_email['subject']
        assert email.body == self.test_email['body']
        assert email.is_valid == True

    def test_api_get_email(self):
        data = self.app.get('/email')
        assert data._status_code == 405

    def test_api_post_email(self):
        return_data = self.app.post('/email', data = json.dumps(self.test_email), content_type='application/json')

        #assert return_data.data['to'] == 'pamelastone@gmail.com'
        #assert return_data.data == '{"test":"pamtest"}'
        assert b'pamelastone' in return_data.data

if __name__ == '__main__':
    unittest.main()