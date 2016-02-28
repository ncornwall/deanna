# NWHACKS 2016 AL_C slackbot
import time
from slackclient import SlackClient
import requests

class Slackbot:

    # run on initial bot launch to get list of users,create user objects
    # currently doesn't urn
    def enumerateUsers(self):
        # channels = self.sc.server.channels
        # print channels
        username = self.sc.server.username
        print username
        # raw = self.sc.server
        # print 'Server is: ' + str(raw)
        # raw = self.sc.server.channels
        # print 'Channels: ' + str(raw)

    def __init__(self, token):
        self.s = requests.Session()

        self.token = token
        sc = SlackClient(token)
        self.sc = sc
        historyLength = 20
        self.history = bot_history(historyLength)
        
        if sc.rtm_connect():
            # self.users = self.enumerateUsers()
            while True:
                obj = sc.rtm_read()
                if len(obj) != 0:
                    if obj[0].has_key('text'):
                        print obj[0]['text']
                        self.analyse(obj[0]['text'])
                time.sleep(1)
        else:
            print "Connection Failed, invalid token?"

    # from urllib.parse import urlencode
    def analyse(self, textToAnalyze):

        apikey = "d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"
        params = {}

        params['apikey'] = apikey
        params['outputMode'] = 'json'

        post_data = {}
        post_data['text'] = textToAnalyze

        post_url = "http://access.alchemyapi.com/calls/text/TextGetEmotion?outputMode=json&apikey=d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"

        results = self.s.post(url=post_url, data=post_data)

        print("Result" + results.text)

