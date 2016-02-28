# NWHACKS 2016 AL_C slackbot
import time
from slackclient import SlackClient
import requests

class Slackbot:
    
    

	def __init__(self, token):
		self.s = requests.Session()

		self.token = token
		sc = SlackClient(token)
		if sc.rtm_connect():
		    while True:
		        new_evts = sc.rtm_read()
		        for evt in new_evts:
		            if len(evt) !=0:
		                if evt.has_key('text') and not evt.has_key('subtype'):
		                #if evt.has_key('text'):
		                    print evt['text']
		                    self.analyse(evt['text'])
		                    print sc.api_call('chat.postMessage', channel="#al_c", text='Hello World!', username='DeannaTroi', icon_emoji=':woman::skin-tone-2:', as_user='false')
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
