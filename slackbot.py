"""
NWHACKS 2016 AL_C slackbot

To activate locally, just call `python .\slackbot.py`
"""

import time
from slackclient import SlackClient
import requests
from textemotionanalysis import TextEmotionAnalyzer
import ast

class Slackbot:

    def __init__(self, token):
        self.s = requests.Session()
        self.tea = TextEmotionAnalyzer(outputMode="json")
        self.token = token
        sc = SlackClient(token)
        if sc.rtm_connect():
            while True:
                new_evts = sc.rtm_read()
                for evt in new_evts:
                    if len(evt) !=0:
                        if evt.has_key('text') and not evt.has_key('subtype'):
                            print evt['text']
                            top_emotion = self.analyse(evt['text'], evt['user'], evt['channel'])
                            print top_emotion["docEmotions"]
                            if top_emotion["docEmotions"].has_key('anger'):
                                print sc.api_call('chat.postMessage', channel="#al_c", text='Calm down!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                            elif top_emotion["docEmotions"].has_key('fear'):
                                print sc.api_call('chat.postMessage', channel="#al_c", text='Dont worry!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                            elif top_emotion["docEmotions"].has_key('joy'):
                                print sc.api_call('chat.postMessage', channel="#al_c", text='Yay!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                            elif top_emotion["docEmotions"].has_key('sadness'):
                                print sc.api_call('chat.postMessage', channel="#al_c", text='*hugs*!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                            elif top_emotion["docEmotions"].has_key('disgust'):
                                print sc.api_call('chat.postMessage', channel="#al_c", text='Gross!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                    time.sleep(1)
        else:
            print "Connection Failed, invalid token?"

    def analyse(self, textToAnalyze, userId, channelId):
        """
        Return TextEmotionAnalyzer docEmotions as dict for current text. Send res to user of id
        """
        response = self.tea.get_top_emotion(textToAnalyze)
        try:
            result = {
                "channel": channelId,
                "user": userId,
                "text": textToAnalyze,
                "docEmotions": ast.literal_eval(response)
            }

            return result

        except Exception as e:
            print "Could not get_emotions: " + e.message


if __name__ == "__main__":
    bot = Slackbot("xoxp-3927713261-3938135231-23401969635-ab0e5635c7")
    #bot = Slackbot("xoxp-23412134003-23409266740-23415010816-f684006023")
    #bot = Slackbot(token="xoxp-23412134003-23409266740-23444912631-4b1d6ed922")
