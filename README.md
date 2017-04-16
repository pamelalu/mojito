# Project Mojito

A HTTP emailing service that delivers email via Mailgun or Mandrill


## Getting Started

You can download the code at https://github.com/pstone/mojito


### Prerequisites

You will need Python 2.6 or newer

```
python -v
```

### Installing

Set up virtual env

```
cd mojito
sudo pip install virtualenv
virtualenv venv
. venv/bin/activate
```

then install packages
```
pip install Flask
pip install flask-restful
pip install requests
pip install html2text
```

Finally run
```
export FLASK_APP=./api/routes.py
flask run
```

### API Endpoints
POST /email

Sample request:
```
curl -H "Content-Type: application/json" -X POST -d '{"to":"pamelastone@gmail.com","to_name":"Pam Lu","from":"pamela.stone@gmail.com", "from_name": "Pam Sender", "subject": "A Message", "body": "<h1>Your Bill</h1><p>$10</p>"}' http://127.0.0.1:5000/email
```

### Testing

```
python test.py
```

### To do
- Create env specific configs
- Store API keys outside repo
- Better error handling and messages
