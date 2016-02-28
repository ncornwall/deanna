# NWHACKS 2016 AL_C slackbot
import time
from slackclient import SlackClient
import requests

s = requests.Session()

def analyse(textToAnalyze):

	apikey = "d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"
	params = {}

	params['apikey'] = apikey
	params['outputMode'] = 'json'

	post_data = {}
	post_data['text'] = textToAnalyze

	#post_url = "http://gateway-a.watsonplatform.net/calls/html/HTMLGetRawText" + \
	#                '?' + str(params)

	# post_url = "http://access.alchemyapi.com/calls" + "/text/TextGetTextSentiment" + \
	#            '?' + str(params)
	            
	post_url = "http://access.alchemyapi.com/calls/text/TextGetEmotion?outputMode=json&apikey=d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"

	results = s.post(url=post_url, data=post_data)

	print("Result" + results.text)

token = "xoxp-3927713261-3938135231-23401969635-ab0e5635c7"# found at https://api.slack.com/web#authentication
sc = SlackClient(token)
##if sc.rtm_connect():
##    while True:
##        obj = sc.rtm_read()
##        if len(obj) != 0:
##		    if obj[0].has_key('text'):
##		    	print obj[0]['text']
##		    	analyse(obj[0]['text'])
##        time.sleep(1)
##else:
##    print "Connection Failed, invalid token?"

token2 = "xoxp-3927713261-4234411675-23415124327-eb87f5a223"# found at https://api.slack.com/web#authentication
sc2 = SlackClient(token2)
if sc2.rtm_connect() and sc.rtm_connect():
    while True:
        obj1 = sc.rtm_read()
        obj2 = sc2.rtm_read()
        if len(obj1) != 0:
		    if obj1[0].has_key('text'):
		    	print obj1[0]['text']
		    	analyse(obj1[0]['text'])
	if len(obj2) != 0:
                if obj2[0].has_key('text'):
		    	print obj2[0]['text']
		    	analyse(obj2[0]['text'])
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"

# from urllib.parse import urlencode
