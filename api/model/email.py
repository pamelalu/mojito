from api import app
from html2text import html2text
from validate_email import validate_email

class Email(object):
    def __init__(self, args):
        try:
            if validate_email(args['to']) and validate_email(args['from']):
                self.to_email = args['to']
                self.to_name = args['to_name']
                self.from_email = args['from']
                self.from_name = args['from_name']
                self.subject = args['subject']
                self.body = html2text(args['body'])
                self.is_valid = True
            else:
                self.is_valid = False
        except:
            self.is_valid = False



    def send(self, emailProvider):
        message = emailProvider.send_message(self)

        if message:
            app.logger.error(message)
