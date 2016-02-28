"""
Manual testing of slackbot

Run `python ./test_slackbot.py` and results should print out
"""
from slackbot import Slackbot


def test_slackbot():
    print "slackbot:"
    # bot = Slackbot("xoxp-3927713261-3938135231-23401969635-ab0e5635c7")
    bot = Slackbot("xoxp-23412134003-23409266740-23444912631-4b1d6ed922")

if __name__ == "__main__":
    test_slackbot()
