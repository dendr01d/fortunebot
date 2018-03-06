from markov2 import *


chain = Graph()
chain.feedCorpus('singleFortune.txt')
chain.feedCorpus('EICorpus.txt')
chain.feedCorpus('handmadeCorpus.txt')
chain.feedCorpus('wikiCorpus.txt')


for i in range(0, 50):
	print(chain.generate())
