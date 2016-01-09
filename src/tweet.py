import twitter
import json

class Tweets():
	def __init__(self, creds_file):
		"""
			Initialization method to fetch all of the credentials for the
			authentication to the Twitter API.
			Those credentials are:
				- CONSUMER_KEY;
				- CONSUMER_SECRET;
				- OAUTH_TOKEN;
				- OAUTH_TOKEN_SECRET.
		"""
		with open(creds_file, 'r') as f:
			self.creds = json.loads(f)

	def authenticate(self):
		"""
			Create and authenticate connection with the Twitter's API.
		"""
		CONSUMER_KEY = self.creds['CONSUMER_KEY']
		CONSUMER_SECRET = self.creds['CONSUMER_SECRET']
		OAUTH_TOKEN = self.creds['OAUTH_TOKEN']
		OAUTH_TOKEN_SECRET = self.creds['OAUTH_TOKEN_SECRET']

		auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
			CONSUMER_KEY, CONSUMER_SECRET)
		self.twitter = twitter.Twitter(auth)

	def trends(self, woe=1):
		"""
			Method that will fetch all of the trends from a specific Where On
			Earth ID, by default it has been set to 1, which correspond to the
			entire world.
		"""
		return self.twitter.trends.place(woe)

	def search(self, keywords, limit=100):
		"""
			Method that will search for a specific number of tweets containing a
			few words within keywords, it can be a sigle word or a phrase. This
			method will return a limited result set, by default only 100 tweets.
		"""
		return self.twitter.search.tweets(q=keywords, count=limit)

class Analysis():
	def __init__(self):
		pass

	def analyze(self, text, algo=''):
		"""
			Method that will handle all of the sentiment analysis using a
			developer specified algorithm, defaulted to an empty string.
		"""
		pass