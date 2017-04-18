from flask_restful import Resource, reqparse
from api import app, restApi
from api.model.email import Email

class SendEmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('to', type = str, required = True)
        parser.add_argument('to_name', type = str, required = True)
        parser.add_argument('from', type = str, required = True)
        parser.add_argument('from_name', type =str, required = True)
        parser.add_argument('subject', type = str, required = True)
        parser.add_argument('body', type = str, required = True)
        args = parser.parse_args()

        try:
            email = Email(args)
            email.send()
            return (args, 200)
        except Exception as e:
            app.logger.error('SendEmail error: '+ str(e))
            return (str(e), 400)

restApi.add_resource(SendEmail, '/email')

if __name__ == "__main__":
    app.run()