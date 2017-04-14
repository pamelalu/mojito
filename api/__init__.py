from flask import Flask
from flask_restful import Api

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MAIL_PROVIDER'] = 'MAILGUN'

app.config['MAILGUN_DOMAIN'] = 'sandbox94f6ab5904f544dba32852a3e3d4cf1c.mailgun.org'
app.config['MAILGUN_API_KEY'] = 'key-066b9601c57c65b9c272a18110486770'

restApi = Api(app)

import api.routes, api.email
