"""
    Sentiment analysis GUI.
    This is the file that will have the text and the results of the sentiment
    analysis.
"""
from kivy.uix.boxlayout import BoxLayout

class TextLayout(BoxLayout):
    """
        This will be the container for a list of tweets to be presented and
        moved through. Basically the text and info is in the center and in both
        sides would be the buttons that represent the next and previous actions.
    """
    pass

class ResultsLLayout(BoxLayout):
    """
        This class will represent the other adjacent part of the screen that
        will give out to the user the values that the text in question got as
        well as the emotion detected and a smilley face for visual purposes.
    """
    pass

class SentimentalLayout(BoxLayout):
    """
        This is the layout or screen that will contain the above ones, the Text
        and the Results. They should go side by side for better occupation of
        the horizontal/landscape screen.
    """
    pass
