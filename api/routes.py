from flask import request
from flask_restful import Resource
from api import app, restApi
from api.model.email import Email

class SendEmail(Resource):
    def post(self):
        args = request.get_json(silent=True)
        try:
            email = Email(args)
            email.send()
            return (args, 200)
        except:
            return 500

restApi.add_resource(SendEmail, '/email')

if __name__ == "__main__":
    app.run()