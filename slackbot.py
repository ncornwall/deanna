# NWHACKS 2016 AL_C slackbot
import time
from slackclient import SlackClient

token = "xoxp-3927713261-3938135231-23401969635-ab0e5635c7"# found at https://api.slack.com/web#authentication
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"