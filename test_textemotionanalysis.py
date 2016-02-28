"""
Manual testing of textemotionanalysis

Run `python ./test_textemotionanalysis.py` and results should print out
"""

from textemotionanalysis import TextEmotionAnalyzer
from slackbot import Slackbot

tea = TextEmotionAnalyzer()
print "get_sentiment:"
print tea.get_sentiment(text="poopies!")
print "get_emotions:"
print tea.get_emotions(text="poopies!")

print "get_top_emotion:"
print tea.get_top_emotion()

print "slackbot:"
bot = Slackbot("xoxp-3927713261-3938135231-23401969635-ab0e5635c7")
