# NWHACKS 2016 AL_C slackbot
import time
from slackclient import SlackClient
import requests

class Slackbot:

	def __init__(self, token):
		self.s = requests.Session()
		self.token = token
		sc = SlackClient(self.token)

		if sc.rtm_connect():
		    while True:
		        obj = sc.rtm_read()
		        print obj
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
