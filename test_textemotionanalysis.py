"""
Manual testing of textemotionanalysis

Run `python ./test_textemotionanalysis.py` and results should print out
"""

from textemotionanalysis import TextEmotionAnalyzer

tea = TextEmotionAnalyzer()
print tea.get_results()
