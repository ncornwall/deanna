# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:22:31 2016

@author: Shaylene
"""
import requests

s = requests.Session()

from urllib.parse import urlencode

apikey = "d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"
params = {}

params['apikey'] = apikey
params['outputMode'] = 'json'

post_data = {}
post_data['text'] = ""

#post_url = "http://gateway-a.watsonplatform.net/calls/html/HTMLGetRawText" + \
#                '?' + str(params)

# post_url = "http://access.alchemyapi.com/calls" + "/text/TextGetTextSentiment" + \
#            '?' + str(params)
            
post_url = "http://access.alchemyapi.com/calls/text/TextGetEmotion?outputMode=json&apikey=d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"

results = s.post(url=post_url, data=post_data)

print(results.text)