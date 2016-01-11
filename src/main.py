"""
	This will be the main script to build the GUI and it will also have the
	screen manager.
"""
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.image import Image
from kivy.properties import StringProperty

import random

class ScrollMessages(BoxLayout):
    pass

class TweetScreen(Screen):
    """
        Screen to handle all of the layout for the Sentiment Analysis part.
    """
    pass

class SearchScreen(Screen):
    """
        Screen to handle the Twitter search. Whenever the user clicks New Query
        on the TweetScreen this will pop up so the user can introduce new
        keywords to search on the Twitter API.
    """
    pass

class ImportScreen(Screen):
    """
        Screen that will handle the submission of text. Basically this will let
        the user to submit more than just tweets for analysis. The user will
        never be able to mix text with tweets.
    """
    pass

class SumScreen(Screen):
    """
        This screen will handle the text summarization of the text that is
        submited.
    """
    def summarize(self):
            """
                Method that handles the summarization of text.
                Basically it wil search for newlines and fetch only the first
                sentence of each paragraph.
            """
            # print('Summarizing clicked.')
            #self.text is the text from the InputText
            self.text = self.ids.sum_text.text
            self.summed = []

            # separating the text by the newlines.
            paragraphs = self.text.split('\n')
            for element in paragraphs:
                self.summed.append(element.split('.')[0])

            # print(self.summed)
            # Printing it out in the right side.
            self.ids.summed_text.text = '\n'.join(self.summed)


class MainApp(App):

    images = {}
    sad = 0.0
    funny = 0.0
    angry = 0.0
    happy = 0.0
    search_results = StringProperty('')

    def build(self):
        # Add a ScreenManager in the main app to handle all of the transitions
        # as well as all of the screens.
        # self.manager = ScreenManager(transition=SlideTransition(duration=.10))
        Builder.load_file('main.kv')
        self.images = {}
        self.getImages()
        print('Loaded emotions')

    def printf(self):
        print('What the hell')

    def getImages(self, path='../res/'):
        """
            Method to load the images for the different emotions passed on.
        """
        self.images = {'angry': path+'angry.png',
                'sad': path+'sad_crying.png',
                'happy': path+'happy.png',
                'funny': path+'laughing.png'}

    def randomize(start=0, stop=100):
        """
            Helper method for the simulation of the sentiment analysis.
        """
        return float(random.randrange(start, stop)/100)

    def analyzeEmotion(self, text):
        """
            Method that will for now simulate the analysis of the emotion
            that is present on the text to be analyzed.
        """
        happy = randomize()
        sad = randomize()
        angry = randomize()
        funny = randomize()

        self.happy = happy
        self.sad = sad
        self.angry = angry
        self.funny = funny

    def emotion(self):
        happy = self.happy
        funny = self.funny
        angry = self.angry
        sad = self.sad

        if happy > sad and happy > angry and happy > funny:
            return '../res/happy.png'
        elif sad > happy and sad > angry and sad > funny:
            return '../res/sad_crying.png'
        elif funny > happy and funny > angry and funny > sad:
            return '../res/laughing.png'
        return '../res/angry.png'

    def importText(self, text):
        """
            Method that will Import the text to be analyzed.
        """
        print('It was clicked!'  + str(text.text))
        pass

if __name__ == '__main__':
    MainApp().run()
