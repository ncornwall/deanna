# NWHACKS 2016 AL_C slackbot
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
                        print obj[0]['text']
                        print obj[0]['user']
                        self.analyse(obj[0]['text'], obj[0]['user'])
                time.sleep(1)
        else:
            print "Connection Failed, invalid token?"

    def analyse(self, textToAnalyze, userId):

        apikey = "d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"
        params = {}

        params['apikey'] = apikey
        params['outputMode'] = 'json'

        post_data = {}
        post_data['text'] = textToAnalyze

        ## Original; prints same as call to get_emotions
        # post_url = "http://access.alchemyapi.com/calls/text/TextGetEmotion?outputMode=json&apikey=d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"
        # results = self.s.post(url=post_url, data=post_data)
        # print("Result" + results.text)

        response = self.tea.get_emotions(textToAnalyze)
        try:
            result = response["docEmotions"]

            # !!! instead of just printing results, spit out / call to user.py or other handler/decisionmaker

            print result

        except:
            print "Could not get_emotions"



if __name__ == "__main__":
    #bot = Slackbot("xoxp-3927713261-3938135231-23401969635-ab0e5635c7")
    #bot = Slackbot("xoxp-23412134003-23409266740-23415010816-f684006023")
    bot = Slackbot(token="xoxp-23412134003-23409266740-23444912631-4b1d6ed922")
