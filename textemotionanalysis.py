# -*- coding: utf-8 -*-
"""
TextEmotionAnalyzer class to request

Created on Sat Feb 27 16:22:31 2016

@author: Shaylene
"""

import requests
import json
import operator


class TextEmotionAnalyzer:

    def __init__(self, outputMode="json", apikey="d39ed152b9ca4e2b4eb9828c0379a44f33ef0f65"):
        """
        Create instance of TextEmotionAnalyzer to use

        Optional params: outputMode, apikey
        """
        self.s = requests.Session()
        self.params = {}
        self.params['apikey'] = apikey
        self.params['outputMode'] = outputMode

    def get_sentiment(self, text=""):
        """
        Returns overall sentiment of provided text
        """
        post_data = {}

        if not text:
            return json.dumps({"error": "No text provided"})

        post_data['text'] = text

        post_url = "http://access.alchemyapi.com/calls" + "/text/TextGetTextSentiment" + \
                   '?' + "outputMode=json&apikey=" + self.params['apikey']

        results = self.s.post(url=post_url, data=post_data)
        return results.text

    def get_emotions(self, text=""):
        """
        Returns values for the 5 emotions of provided text
        """
        post_data = {}

        if not text:
            return json.dumps({"error": "No text provided"})

        post_data['text'] = text

        post_url = "http://access.alchemyapi.com/calls" + "/text/TextGetEmotion" + \
                   '?' + "outputMode=json&apikey=" + self.params['apikey']

        results = self.s.post(url=post_url, data=post_data)
        return results.text

    def get_top_emotion(self):
        """
        Returns top emotion and its value,

        e.g. {"joy": "0.515193"}
        """
        res = json.loads(self.get_emotions(text="poopies!"))['docEmotions']

        abc = max(res.iteritems(), key=operator.itemgetter(1))

        return json.dumps({abc[0]: abc[1]})
