# -*- coding: utf-8 -*-
"""
TextEmotionAnalyzer class to request

Created on Sat Feb 27 16:22:31 2016

@author: Shaylene
"""
import requests

class TextEmotionAnalyzer:

    #s = requests.Session()

    def __init__(self):
        """

        """

        self.s = requests.Session()

        self.apikey = "d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"
        self.params = {}
        self.params['apikey'] = self.apikey
        self.params['outputMode'] = 'json'
        self.post_data = {}
        self.post_data['text'] = "poopies"

        #post_url = "http://gateway-a.watsonplatform.net/calls/html/HTMLGetRawText" + \
        #                '?' + str(params)

        # post_url = "http://access.alchemyapi.com/calls" + "/text/TextGetTextSentiment" + \
        #            '?' + str(params)

        self.post_url = "http://access.alchemyapi.com/calls/text/TextGetEmotion?outputMode=json&apikey=d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"

        # content-is-empty error
        #post_url = "http://access.alchemyapi.com/calls/text/TextGetTargetedSentiment'?outputMode=json&apikey=d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"


    def get_results(self):
        """
        Prints results of call to Watson
        """

        results = self.s.post(url=self.post_url, data=self.post_data)

        print(results.text)
        #return results.text
