
from api import app
from mailgun import Mailgun
from jsonschema import validate
from api.schema import emailSchema

class Email(object):
    def __init__(self, args):

        self.to_email = args['to']
        self.to_name = args['to_name']
        self.from_email = args['from']
        self.from_name = args['from_name']
        self.subject = args['subject']
        self.body = args['body']

        try:
            self.is_valid = self.validate_email(args, emailSchema)

        except:
            self.is_valid = False

    def send(self):
        if app.config['TESTING'] != True:
            if app.config['MAIL_PROVIDER'] == 'MAILGUN':
                Mailgun().send_message(self)
            #elif app.config['MAIL_PROVIDER'] == 'MANDRILL':
            #    Mandrill().send_message(self)


    def validate_email(self, args, emailSchema):
        try:
            validate(args, emailSchema)
            return True
        except:
            return False