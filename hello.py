from flask import Flask
from flask import render_template
from flask import request
from flask_oauth import OAuth
from flask import session
from slackbot import Slackbot

import json
import os
import sys
from urlparse import urlparse
import uuid

import flask
import requests

SLACK_CLIENT_ID = "3927713261.23411567264"
SLACK_CLIENT_SECRET = "7eff0ae701eb73a07cab2b5c9d091795"
SLACK_AUTHORIZE_URL = 'https://slack.com/oauth/authorize'
SLACK_OAUTH_URL = 'https://slack.com/api/oauth.access'

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    if 'code' in request.args:
        print request.args.get('code', '')
        response = requests.get(
        SLACK_OAUTH_URL,
        params={
            'client_id': SLACK_CLIENT_ID,
            'client_secret': SLACK_CLIENT_SECRET,
            'code': flask.request.args['code'],
            'redirect_uri': "http://127.0.0.1:5000",
        })
        print response.json()
        if response.ok:
            content = response.json()
            if content.has_key('bot'):
                bot = content['bot']
                if bot.has_key('bot_access_token'):
                    # slackbot = Slackbot(bot['bot_access_token'])
                    def handle_sub_view(data):
                        slackbot = Slackbot(data)
                    data = bot['bot_access_token']
                    thread.start_new_thread(handle_sub_view, data)
                    return render_template('success.html')
                    # slackbot = Slackbot(bot['bot_access_token'])
                    # return render_template('hello.html')
    return render_template('hello.html')

# @app.route('/auth')
# def main_view():
#     if 'error' in flask.request.args:
#         return 'Access was denied', 403, {'Content-type': 'text/plain'}
#     if 'code' in flask.request.args:
#         response = requests.get(
#             SLACK_OAUTH_URL,
#             params={
#                 'client_id': SLACK_CLIENT_ID,
#                 'client_secret': SLACK_CLIENT_SECRET,
#                 'code': flask.request.args['code'],
#                 'redirect_uri': flask.url_for('.main_view', _external=True),
#             })
#         return (json.dumps(response.json()), 200,
#                 {'Content-type': 'application/json'})
#     redirect_url = '{}?{}'.format(
#         SLACK_AUTHORIZE_URL,
#         urlencode({
#             'client_id': SLACK_CLIENT_ID,
#             'redirect_uri': flask.url_for('.main_view', _external=True),
#             'scope': 'identify,read,post,client',
#             'state': str(uuid.uuid4()),
#             # 'team': None,
#         }))
#     return flask.redirect(redirect_url)

if __name__ == '__main__':
    app.run()