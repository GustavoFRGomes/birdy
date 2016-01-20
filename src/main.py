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
    time = '11th of January'
    name = '@GustavoFRGomes - Gugas'
    content = 'The content goes here, you should try a new query...'

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

    def list_tweets(self):
        """
            Method that will handle the creation of a list.
        """
        pass

    def printTweet(self, text):
        """
            Method that will print all of the text from the text disctionary.
        """
        self.content = text['content']
        self.name = text['name']
        self.time = text['timestamp']

    def nextPost(self):
        """
            Method that will handle the click to the next post of the list,
            basically the tweets or paragraphs will be moved from left to right
            and this will be the method to go to the next one on the list.
        """
        if self.current == self.list_posts[-1]:
            # this is the end of the line just don't do anything
            pass

        #search for the next tweet
        size = len(self.list_posts)
        for i in range(size):
            if self.list_posts[i] == self.current:
                size = i
                break

        self.current = self.list_post[size+1]

    def prevPost(self):
        """
            Method that will handle the move to the previous post.
        """
        if self.current == self.list_posts[0]:
            # it's still in the first element
            pass

        size = len(self.list_posts)
        for i in range(size):
            if self.list_posts[i] == self.current:
                size = i
                break

        self.current = self.list_post[size-1]

    def analyzeEmotion(self, text):
        """
            Method that will for now simulate the analysis of the emotion
            that is present on the text to be analyzed.
        """
        self.happy = randomize()
        self.sad = randomize()
        self.angry = randomize()
        self.funny = randomize()

    def emotion(self):
        happy = self.happy
        funny = self.funny
        angry = self.angry
        sad = self.sad

        if angry > sad and angry > happy and angry > funny:
            return '../res/anngryy.png'
        elif sad > happy and sad > angry and sad > funny:
            return '../res/sad_crying.png'
        elif funny > happy and funny > angry and funny > sad:
            return '../res/laughing.png'
        return '../res/happy.png'

    def importText(self, text):
        """
            Method that will Import the text to be analyzed.
        """
        print('It was clicked!\n'  + str(text.text))
        pass

if __name__ == '__main__':
    MainApp().run()
