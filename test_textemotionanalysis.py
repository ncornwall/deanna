"""
Manual testing of textemotionanalysis

Run `python ./test_textemotionanalysis.py` and results should print out
"""
from textemotionanalysis import TextEmotionAnalyzer


def test_tea():
    tea = TextEmotionAnalyzer()
    print "get_sentiment:"
    print tea.get_sentiment(text="poopies!")
    print "get_emotions:"
    print tea.get_emotions(text="poopies!")

    print "get_top_emotion:"
    print tea.get_top_emotion()

