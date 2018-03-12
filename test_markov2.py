from markov2 import *


model = additiveMarkovModel()
model.feedCorpus('singleFortune.txt')
model.feedCorpus('EICorpus.txt')
model.feedCorpus('handmadeCorpus.txt')
model.feedCorpus('wikiCorpus.txt')


for i in range(0, 50):
	print(model.generate())
