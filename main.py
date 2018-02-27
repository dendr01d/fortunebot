import tweepy
import time
import random
from math import ceil

from markov import *
from cred_sensitive import *

# authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# instantiate the graph
chain = Graph()
chain.feedCorpus('EICorpus.txt')

while(1):
	msg = chain.generate()
	print('New message: {}'.format(msg))

	try:
		print('[{}]'.format(time.strftime('%X')))	
		print('Sending tweet...')
		api.update_status(msg)
		print('Success!')

		naptime = random.randint(900, 1800)
		print('Sleeping for ~{} minutes'.format(ceil(naptime/60)))
		time.sleep(naptime)

	except tweepy.TweepError as err:
		print('Failed to send tweet, because:')
		print(err.reason)
		print('Trying again in 30 seconds...')
		time.sleep(30)

		
