"""
Manual testing of slackbot

Run `python ./test_slackbot.py` and results should print out
"""
from slackbot import Slackbot


def test_slackbot():
    print "slackbot:"
    # bot = Slackbot("xoxp-3927713261-3938135231-23401969635-ab0e5635c7")
    bot = Slackbot("xoxb-23448150406-BlXuLBCuCZQtPzRGCsDWGPhu")

if __name__ == "__main__":
    test_slackbot()
