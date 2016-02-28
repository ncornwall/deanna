"""
NWHACKS 2016 AL_C slackbot

To activate locally, just call `python .\slackbot.py`
"""

import time
from slackclient import SlackClient
import requests
from textemotionanalysis import TextEmotionAnalyzer

class Slackbot:

    def __init__(self, token):
        self.s = requests.Session()
        self.tea = TextEmotionAnalyzer(outputMode="json")
        self.token = token
        sc = SlackClient(token)
        if sc.rtm_connect():
            while True:
                obj = sc.rtm_read()
                if len(obj) != 0:
                    if obj[0].has_key('text'):
                        # print "channel: " + obj[0]['channel']
                        # print "text: " + obj[0]['text']
                        # print "user: " + obj[0]['user']
                        self.analyse(obj[0]['text'], obj[0]['user'], obj[0]['channel'])
                time.sleep(1)
        else:
            print "Connection Failed, invalid token?"

    def analyse(self, textToAnalyze, userId, channelId):
        """
        Return TextEmotionAnalyzer docEmotions as dict for current text. Send res to user of id
        """
        response = self.tea.get_emotions(textToAnalyze)
        try:
            result = {
                "channel": channelId,
                "user": userId,
                "text": textToAnalyze,
                "docEmotions": response["docEmotions"]
            }

            print result

        except Exception as e:
            print "Could not get_emotions: " + e.message


if __name__ == "__main__":
    #bot = Slackbot("xoxp-3927713261-3938135231-23401969635-ab0e5635c7")
    #bot = Slackbot("xoxp-23412134003-23409266740-23415010816-f684006023")
    bot = Slackbot(token="xoxp-23412134003-23409266740-23444912631-4b1d6ed922")
