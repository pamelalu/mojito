from flask import Flask
from flask_restful import Api

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MAIL_PROVIDER'] = 'NONE'

app.config['MAILGUN_SEND_ENDPOINT'] = 'https://api.mailgun.net/v3/sandbox94f6ab5904f544dba32852a3e3d4cf1c.mailgun.org/messages'
app.config['MAILGUN_API_KEY'] = 'key-066b9601c57c65b9c272a18110486770'

app.config['MANDRILL_SEND_ENDPOINT'] = 'https://mandrillapp.com/api/1.0/'
app.config['MANDRILL_API_KEY'] = 'ZG-Uoq8cxKE7CT-noEMtfw'

restApi = Api(app)

import api.routes, model