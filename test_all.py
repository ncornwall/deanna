"""
Manual testing of everything that has tests written

Run `python ./test_all.py` and results should print out
"""
from test_textemotionanalysis import test_tea
from test_user import test_user
from test_slackbot import test_slackbot

print ""
print "========== Testing textemotionalanalysis... =========="
test_tea()

print ""
print "========== Testing user =========="
test_user()

print ""
print "========== Testing slackbot... =========="
test_slackbot()
