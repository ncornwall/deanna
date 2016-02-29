from flask import Flask
from flask import render_template
from flask import request
from flask import session
from slackbot import Slackbot
from celery import Celery

import json
import os
import sys
from urlparse import urlparse
import uuid
import redis

import flask
import requests

SLACK_CLIENT_ID = "3927713261.23411567264"
SLACK_CLIENT_SECRET = "7eff0ae701eb73a07cab2b5c9d091795"
SLACK_AUTHORIZE_URL = 'https://slack.com/oauth/authorize'
SLACK_OAUTH_URL = 'https://slack.com/api/oauth.access'

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

@celery.task
def start_bot(token, channel):
    Slackbot(token, channel)
    return 0

@app.route('/')
def hello_world():
    print flask.url_for('.hello_world', _external=True)
    if 'code' in request.args:
        print request.args.get('code', '')
        response = requests.get(
        SLACK_OAUTH_URL,
        params={
            'client_id': SLACK_CLIENT_ID,
            'client_secret': SLACK_CLIENT_SECRET,
            'code': flask.request.args['code'],
            'redirect_uri': flask.url_for('.hello_world', _external=True),
        })
        print response.json()
        if response.ok:
            try:
                content = response.json()
                bot_token = content['bot']['bot_access_token']
                bot_channel = content['incoming_webhook']['channel']
                print "slackbot:"
                task = start_bot.delay(bot_token, bot_channel)
                return render_template('success.html')
            except KeyError:
                print 'Decoding JSON has failed'
                return render_template('hello.html')
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(threaded=True)