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
    print "slackbot:"
    bot = Slackbot("xoxp-21356914545-22690026608-23455833233-8b493b4eae")

    # if 'code' in request.args:
    #     print request.args.get('code', '')
    #     response = requests.get(
    #     SLACK_OAUTH_URL,
    #     params={
    #         'client_id': SLACK_CLIENT_ID,
    #         'client_secret': SLACK_CLIENT_SECRET,
    #         'code': flask.request.args['code'],
    #         'redirect_uri': "http://intense-hamlet-80471.herokuapp.com",
    #     })
    #     print response.json()
    #     if response.ok:
    #         content = response.json()
    #         if content.has_key('bot'):
    #             bot = content['bot']
    #             if bot.has_key('bot_access_token'):
    #                 slackbot = Slackbot(bot['bot_access_token'])
    #                 return render_template('success.html')
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()