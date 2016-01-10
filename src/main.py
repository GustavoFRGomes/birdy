"""
	This will be the main script to build the GUI and it will also have the
	screen manager.
"""
from kivy.app import App
from kivy.uix.floatinglayout import FloatingLayout
from kivy.uix.screenmanager import Screen

from kivy.properties import BooleanProperty

class TweetScreen(Screen):
    """
        Screen to handle all of the layout for the Sentiment Analysis part.
    """
    fullscreen = BooleanProperty(False)
    pass

class SearchScreen(Screen):
    """
        Screen to handle the Twitter search. Whenever the user clicks New Query
        on the TweetScreen this will pop up so the user can introduce new
        keywords to search on the Twitter API.
    """
    fullscreen = BooleanProperty(False)
    pass

class ImportScreen(Screen):
    """
        Screen that will handle the submission of text. Basically this will let
        the user to submit more than just tweets for analysis. The user will
        never be able to mix text with tweets.
    """
    fullscreen = BooleanProperty(False)
    pass

class SumScreen(Screen):
    """
        This screen will handle the text summarization of the text that is
        submited.
    """
    fullscreen = BooleanProperty(False)
    pass


class MainApp(FloatingLayout):
    def build(self):
        # Add a ScreenManager in the main app to handle all of the transitions
        # as well as all of the screens.
        self.manager = ScreenManager(transition=SlideTransition(duration=.10))

if __name__ == '__main__':
	MainApp().run()
