import tweepy

from cred_sensitive import *

# authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
	print('Tweeting test tweet...')
	thing = api.update_status('This is a test tweet!')

except tweepy.TweepError as e:
	print('Couldn\'t post the tweet because:')
	print(e.reason)

idNum = input('What was the id number of that tweet?\n')

if idNum == '0':
	print('Fine, deal with it yourself')
else:
	try:
		print('Destroying tweet ', idNum)
		api.destroy_status(idNum)

	except tweepy.TweepError as e:
		print('Couldn\'t destroy the tweet because:')
		print(e.reason)
