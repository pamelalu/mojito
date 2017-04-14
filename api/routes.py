from flask import request
from flask_restful import Resource

from api import app, restApi
from api.email import Email

#@app.route("/email", methods=['POST'])

#def email():
    # request.method
#print request.__dict__
#return "Hello World!"

class SendEmail(Resource):
    def post(self):
        args = request.get_json(silent=True)
        #try:

        email = Email(args)
        email.send()

        return args
        #except:
        #    return {}

restApi.add_resource(SendEmail, '/email')

if __name__ == "__main__":
    app.run()