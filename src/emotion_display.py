"""
    Sentiment analysis GUI.
    This is the file that will have the text and the results of the sentiment
    analysis.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# from emotional import sentient

class TextLayout(BoxLayout):
    """
        This will be the container for a list of tweets to be presented and
        moved through. Basically the text and info is in the center and in both
        sides would be the buttons that represent the next and previous actions.
    """
    pass

class ResultsLayout(BoxLayout):
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
    def getTweets(self, tweets):
        """
            Method that will receive a list of tweets and assigns them to the
            self.tweets attribute, it must be a list of objects.
        """
        self.tweets = tweets
        self.pos = 0

    def nextTweet(self):
        """
            Method that will go on to the next tweet. It will be the action of
            the next button. The class will have a pos attribute to register in
            which tweet the user is at.
        """
        if len(self.tweets) == (self.pos+1):
            self.pos += 1
        return self.tweets[self.pos]

    def previousTweet(self):
        """
            Method that gets the previous tweet from the tweets attribute list.
        """
        if self.pos != 0:
            self.pos -= 1
        return self.tweets[self.pos]

    def tweetText(self, tweet):
        """
            Method that will dump the JSON tweet and make it more visually
            appealing to the eye of the user.
        """
        text = tweet.author + '\n\n'
        text += tweet.text + '\n\n'
        text += tweet.date + '\n'
        return text

    def analyzeTweet(self):
        """
            Method that will handle all of the sentiment analysis. This method
            will call the lib done for the actual sentiment analysis.
        """
        # use the sentient module
        # print('it reached here')
        pass

    pass

class SentimentApp(App):
    pass

if __name__ == '__main__':
    SentimentApp().run()
