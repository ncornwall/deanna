"""
NWHACKS 2016 AL_C slackbot

To activate locally, just call `python .\slackbot.py`
"""

import time
from slackclient import SlackClient
import requests
from textemotionanalysis import TextEmotionAnalyzer
from bot_history import bot_history
import ast

class Slackbot:

    def __init__(self, token):
        history_length = 20
        summary_frequency = 5
        summary_countdown = summary_frequency
        self.s = requests.Session()
        self.tea = TextEmotionAnalyzer(outputMode="json")
        self.token = token
        sc = SlackClient(token)
        self.history = bot_history(history_length)
        channel = "#dancewithdeanna"
        if sc.rtm_connect():
            while True:
                new_evts = sc.rtm_read()
                for evt in new_evts:
                    if len(evt) !=0:
                        if evt.has_key('text') and not evt.has_key('subtype'):
                            print evt['text']
                            top_emotion = self.analyse(evt['text'], evt['user'], evt['channel'])
                            if top_emotion is None:
                                print "top emotion is None"
                                continue
                            print top_emotion["docEmotions"]

                            if top_emotion["docEmotions"].has_key('anger'):
                                print sc.api_call('chat.postMessage', channel=channel, text='Calm down!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                            elif top_emotion["docEmotions"].has_key('fear'):
                                print sc.api_call('chat.postMessage', channel=channel, text='Dont worry!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                            elif top_emotion["docEmotions"].has_key('joy'):
                                print sc.api_call('chat.postMessage', channel=channel, text='Yay!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                            elif top_emotion["docEmotions"].has_key('sadness'):
                                print sc.api_call('chat.postMessage', channel=channel, text='*hugs*!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
                            elif top_emotion["docEmotions"].has_key('disgust'):
                                print sc.api_call('chat.postMessage', channel=channel, text='Gross!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')

                            if (summary_countdown >= 0):
                                summary_countdown -= 1
                            else:
                                print_summary(self.history)
                    time.sleep(1)
        else:
            print "Connection Failed, invalid token?"

    def analyse(self, textToAnalyze, userId, channelId):
        """
        Return TextEmotionAnalyzer docEmotions as dict for current text. Send res to user of id
        """
        top_response = self.tea.get_top_emotion(textToAnalyze)
        #all_response = self.tea.get_emotions(textToAnalyze)
        try:
            result = {
                "channel": channelId,
                "user": userId,
                "text": textToAnalyze,
                "docEmotions": ast.literal_eval(top_response)
                #"allEmotions": ast.literal_eval(all_response)
            }
            #print result['allEmotions']
            
            #self.history.addResponse(result['allEmotions'])

            return result

        except Exception as e:

            print "Could not get_emotions: " + e.message


if __name__ == "__main__":
    bot = Slackbot("xoxp-21356914545-22690026608-23455833233-8b493b4eae")
    #bot = Slackbot("xoxp-23412134003-23409266740-23415010816-f684006023")
    #bot = Slackbot(token="xoxp-23412134003-23409266740-23444912631-4b1d6ed922")

def print_summary(hist):
    print hist.getAllMeasures()
    print hist.getHighEmotion()



