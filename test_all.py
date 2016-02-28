"""
Manual testing of everything that has tests written

Run `python ./test_all.py` and results should print out
"""
from test_textemotionanalysis import test_tea
from test_slackbot import test_slackbot

print ""
print "========== Testing textemotionalanalysis... =========="
test_tea()

print ""
print "========== Testing slackbot... =========="
test_slackbot()
