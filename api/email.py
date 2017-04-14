from api.schema import emailSchema
from jsonschema import validate

from api import app
from mailgun import Mailgun


class Email(object):
    def __init__(self, args):
        try:
            self.to_email = args['to']
            self.to_name = args['to_name']
            self.from_email = args['from']
            self.from_name = args['from_name']
            self.subject = args['subject']
            self.body = args['body']
            self.is_valid = True

            validate(args, emailSchema)

        except:
            self.is_valid = False

    def send(self):
        if app.config['MAIL_PROVIDER'] == 'MAILGUN':
            Mailgun().send_message(self)


