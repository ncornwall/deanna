# -*- coding: utf-8 -*-
"""
TextEmotionAnalyzer class to request

Created on Sat Feb 27 16:22:31 2016

@author: Shaylene
"""

import requests
import json
import operator
import ast


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
        #return results.text                    # returns string
        return ast.literal_eval(results.text)   # returns dict


    def check_results(self, results):
        """
        Checks if response returned an error status
        """

        results = results
        status = results['status']
        if status is "OK":
            print "yay!"
        

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
        #return results.text                    # returns string
        return ast.literal_eval(results.text)   # returns dict

    def get_top_emotion(self, text=""):
        """
        Returns top emotion and its value,

        e.g. {"joy": "0.515193"}
        """
        # res = json.loads(self.get_emotions(text="poopies!"))['docEmotions']http://nwhacks2016.devpost.com
        res = self.get_emotions(text)['docEmotions']
        abc = max(res.iteritems(), key=operator.itemgetter(1))
        return json.dumps({abc[0]: abc[1]})
        #return ast.literal_eval(abc)
