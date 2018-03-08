import tweepy
import time
import random
from math import ceil
import pickle

from markov2 import *
from cred_sensitive import *

# authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

corpora = [
'singleFortune.txt',
'EICorpus.txt',
'handmadeCorpus.txt',
'wikiCorpus.txt']


print('If you want to load a file, what\'s it\'s name?')
fileName = input('?>')

web = {}
chain = Graph()

if fileName != '':
	try:
		web = pickle.load(open(fileName, 'rb'))
		print('File loaded')
		chain.load(web)

	except IOError as e:
		print('Could not open \'{}\':'.format(fileName))
		print('I/O error ({}): {}'.format(e.errno, e.strerror))

# if nothing's been loaded into the web
elif web == {}:
	print('Create a new model from scratch?')
	cmd = input('?>')

	if cmd[0] == 'y':
		print('Loading corpora...')
		for f in corpora:
			chain.feedCorpus(f)
	else:
		print('Well then what DO you want?')
		exit()

print('Okay time to start tweeting')


while(1):
	msg = chain.generate()

	try:
		print('[{}] {}'.format(time.strftime('%X'), msg))	
		print('Sending tweet...')
		api.update_status(msg)
		print('Success!')

		naptime = random.randint(900, 1200)
		print('Sleeping for ~{} minutes'.format(ceil(naptime/60)))
		time.sleep(naptime)

	except tweepy.TweepError as err:
		print('Failed to send tweet, because:')
		print(err.reason)
		print('Trying again in 30 seconds...')
		time.sleep(30)

		
