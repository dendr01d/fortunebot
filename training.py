from markov2 import *
import pickle

corpora = [
'singleFortune.txt',
'EICorpus.txt',
'handmadeCorpus.txt',
'wikiCorpus.txt']


print('What file do you want to work on?')
fileName = input('?>')

# check for filesave and try to load it
web = {}
chain = Graph()

try:
	dataFile = open(fileName, 'rb')
	web = pickle.load(dataFile)
	dataFile.close()
	print('File successfully opened. Loading into chain...')
	chain.load(web)

except IOError as e:
	print('Could not open \'{}\':'.format(fileName))
	print('I/O error ({}): {}'.format(e.errno, e.strerror))

	print('Creating new chain from scratch')
	for f in corpora:
		chain.feedCorpus(f)

cmd = input('Print the web?>')
if cmd[0] == 'y':
	chain.printWeb()
	print('That\'s it; that\'s the web')

# Okay so
# Ideally I want to keep the web from simply regurgitating examples from the corpora
# and to stop that from happening here I'd need to load all the examples and check
#	against them before I vote on them, since I don't know them all
# except I'd need to format all the examples the same way the bot would actually
#	spit them out, so maybe I'll try that later
# Maybe I need to think about breaking up the markov class's functionality and
#	offload formatting to something I can use more generically


cmd = 'dummy'

while cmd[0] != 'q':
	tweet = chain.generate()
	print(tweet)
	cmd = input('?>')

# if the output is good, feed it back into the system to strengthen
#	the connections that made it
	if cmd == 'yes':
		for i in range(0, 5):
			chain.addSnippet(tweet)	
	elif cmd[0] == 'y' or cmd[0] == 'g':
		chain.addSnippet(tweet)


# save the results

web = chain.export()

cmd = input('Save to \'{}\'?>'.format(fileName))
if cmd[0] == 'y':
	dataFile = open(fileName, 'wb')
	pickle.dump(web, dataFile)
	dataFile.close()
else:
	fileName = input('Where to, then?: ')
	dataFile = open(fileName, 'wb')
	pickle.dump(web, dataFile)
	dataFile.close()

